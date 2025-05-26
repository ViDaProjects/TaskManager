# This Python file uses the following encoding: utf-8
import sys
import time
import copy
from dataclasses import fields
from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QHeaderView, QAbstractItemView
from PySide6.QtCore import QTimer
from threading import Lock

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from gui.ui_form import Ui_MainWindow
from src.data_classes import ShowProcessData, ShowSystemData
from gui.graph_page import GraphPage
from src.qthread_gatherer import ProcDataThread, MemDataThread
from gui.ProcessDialog import ProcessDialog
import src.data_classes

proc_thread = None
ram_thread = None
lock_PID = None
lock_gather_info = None

example_data = ShowSystemData(
    cpu_usage=48.5,
    mem_total=8192.0,
    mem_used=5120.0,
    mem_used_percent=62.5,
    swap_used=256.0,
    swap_total=2048.0,
    swap_used_percent=12.5,
    proc_count_total=138,
    thread_count_total=754,
    process=[
        ShowProcessData(name="systemd", pid="2108", thread_count_proc=10, prio=20, prio_type="Normal", cpu_usage=1.2),
        ShowProcessData(name="chrome", pid="2408", thread_count_proc=36, prio=10, prio_type="User", cpu_usage=12.8),
        ShowProcessData(name="python", pid="2208", thread_count_proc=8, prio=5, prio_type="User", cpu_usage=7.3),
        ShowProcessData(name="code", pid="2138", thread_count_proc=15, prio=0, prio_type="Normal", cpu_usage=3.9),
    ]
)

PROCESSES_PAGE_INDEX = 0
MEMORY_USE_PAGE_INDEX = 1
CPU_USE_PAGE_INDEX = 2
class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setMinimumSize(1000, 600)

        #Init configs
        self.dialog = None
        self.show_process_list = []
        self.all_system_data = None
        self.proc_ram_data = None

        #process page
        self.ui.process_table.setColumnCount(len(fields(ShowProcessData)))
        self.ui.process_table.setHorizontalHeaderLabels([
            "Name", "PID", "Threads", "Priority", "Priority type", "CPU usage"
        ])
        self.ui.process_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.change_current_stack_page(PROCESSES_PAGE_INDEX)
        self.ui.process_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.ui.process_table.setSelectionMode(QAbstractItemView.SingleSelection)

        #graphs pages
        self.cpu_graph = GraphPage("%")
        self.cpu_graph.add_line_sample("Active")
        self.memory_graph = GraphPage("%")
        self.memory_graph.add_line_sample("RAM")
        self.memory_graph.add_line_sample("Swap")
        self.ui.cpu_graph_frame.layout().addWidget(self.cpu_graph)
        self.ui.mem_graph_frame.layout().addWidget(self.memory_graph)

        #Timer
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_stack_pages)
        self.update_stack_pages()
        self.timer.start(3000) #3 seconds

        #Connects signals
        self.ui.processes_button.clicked.connect(lambda: self.change_current_stack_page(PROCESSES_PAGE_INDEX))
        self.ui.cpu_usage_button.clicked.connect(lambda: self.change_current_stack_page(CPU_USE_PAGE_INDEX))
        self.ui.memory_usage_button.clicked.connect(lambda: self.change_current_stack_page(MEMORY_USE_PAGE_INDEX))
        self.ui.process_table.cellDoubleClicked.connect(self.open_process_info)

    def open_process_info(self, row):
        if 0 <= row < len(self.show_process_list):
            process = self.show_process_list[row]
            with lock_PID:
                src.data_classes.PID = process[1] #Get current PID value

            time.sleep(0.5) #Time to wait data
            self.dialog = ProcessDialog(self.all_system_data, self.proc_ram_data, self)
            self.dialog.finished.connect(lambda _: setattr(self, "dialog", None))
            self.dialog.exec()

    def change_current_stack_page(self, new_page_index: int):
        self.ui.stacked_pages.setCurrentIndex(new_page_index)

    def fill_process_table(self, processes: list[ShowProcessData]):
        if processes is None:
            print("No process to show")
            return

        table = self.ui.process_table
        self.show_process_list = processes
        table.setRowCount(len(self.show_process_list))

        for row, proc in enumerate(self.show_process_list):
            table.setItem(row, 0, QTableWidgetItem(proc.name))
            table.setItem(row, 1, QTableWidgetItem(proc.pid))
            table.setItem(row, 2, QTableWidgetItem(f"{proc.thread_count_proc:.0f}"))
            table.setItem(row, 3, QTableWidgetItem(f"{proc.prio:.0f}"))
            table.setItem(row, 4, QTableWidgetItem(proc.prio_type))
            table.setItem(row, 5, QTableWidgetItem(f"{proc.cpu_usage:.0f}"))

        table.resizeRowsToContents()

    def update_stack_pages(self):
        with lock_gather_info:
            self.all_system_data = copy.deepcopy(src.data_classes.SHOW_PROC_DATA)
            self.proc_ram_data = copy.deepcopy(src.data_classes.SHOW_PROC_DATA)
            #COPY PROC_RAM_DATA -----------------------

        if not isinstance(self.all_system_data, ShowSystemData):
            print("System data is not valid")
            return

        #Update labels
        self.ui.total_proc_label.setText(f"{self.all_system_data.proc_count_total:.0f}")
        self.ui.total_threads_label.setText(f"{self.all_system_data.thread_count_total:.0f}")
        self.ui.total_ram_label.setText(f"{self.all_system_data.mem_used:.0f}/{self.all_system_data.mem_total:.0f} MB")
        self.ui.total_swap_label.setText(f"{self.all_system_data.swap_used:.0f}/{self.all_system_data.swap_total:.0f} MB")

        #Update graphs
        self.cpu_graph.update_graph([self.all_system_data.cpu_usage])
        self.memory_graph.update_graph([self.all_system_data.mem_used_percent, self.all_system_data.swap_used_percent])

        #Update processes table
        self.fill_process_table(self.all_system_data.process)

        #Update dialog, if its open
        if self.dialog is not None:
            self.dialog.update_data(self.all_system_data, self.proc_ram_data)

    def closeEvent(self, event):
        global proc_thread, ram_thread
        self.timer.stop()
        proc_thread.stop()
        ram_thread.stop()

        proc_thread.wait()
        ram_thread.wait()
        super().closeEvent(event)


def main():
    global proc_thread, ram_thread, lock_PID
    lock_gather_info = Lock()
    lock_PID = Lock()

    proc_thread = ProcDataThread(lock_gather_info, lock_PID)
    ram_thread = MemDataThread(lock_gather_info, lock_PID)

    proc_thread.start()
    ram_thread.start()

    time.sleep(0.5)
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
