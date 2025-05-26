# This Python file uses the following encoding: utf-8
import sys
from dataclasses import fields
from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QHeaderView, QAbstractItemView
from PySide6.QtCore import QTimer

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from gui.ui_form import Ui_MainWindow
from src.data_classes import ShowProcessData, ShowSystemData
from gui.graph_page import GraphPage

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
        ShowProcessData(name="systemd", thread_count_proc=10, prio=20, prio_type="Normal", cpu_usage=1.2),
        ShowProcessData(name="chrome", thread_count_proc=36, prio=10, prio_type="User", cpu_usage=12.8),
        ShowProcessData(name="python", thread_count_proc=8, prio=5, prio_type="User", cpu_usage=7.3),
        ShowProcessData(name="code", thread_count_proc=15, prio=0, prio_type="Normal", cpu_usage=3.9),
    ]
)

PROCESSES_PAGE_INDEX = 0
MEMORY_USE_PAGE_INDEX = 1
CPU_USE_PAGE_INDEX = 2
i = 0
class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setMinimumSize(1000, 600)

        #Init configs
        #process page
        self.ui.process_table.setColumnCount(len(fields(ShowProcessData)))
        self.ui.process_table.setHorizontalHeaderLabels([
            "Name", "Threads", "Priority", "Priority type", "CPU usage"
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
        #Alterar quando receber sinal de dados prontos
        self.timer.timeout.connect(lambda: self.update_stack_pages(example_data))

        #Fill pages, then start timer
        self.update_stack_pages(example_data)
        self.timer.start(5000) #5 seconds

        #Connects signals
        self.ui.processes_button.clicked.connect(lambda: self.change_current_stack_page(PROCESSES_PAGE_INDEX))
        self.ui.cpu_usage_button.clicked.connect(lambda: self.change_current_stack_page(CPU_USE_PAGE_INDEX))
        self.ui.memory_usage_button.clicked.connect(lambda: self.change_current_stack_page(MEMORY_USE_PAGE_INDEX))

    def change_current_stack_page(self, new_page_index: int):
        self.ui.stacked_pages.setCurrentIndex(new_page_index)

    def fill_process_table(self, processes: list[ShowProcessData]):
        table = self.ui.process_table
        table.setRowCount(len(processes))

        for row, proc in enumerate(processes):
            table.setItem(row, 0, QTableWidgetItem(proc.name))
            table.setItem(row, 1, QTableWidgetItem(f"{proc.thread_count_proc:.0f}"))
            table.setItem(row, 2, QTableWidgetItem(f"{proc.prio:.0f}"))
            table.setItem(row, 3, QTableWidgetItem(proc.prio_type))
            table.setItem(row, 4, QTableWidgetItem(f"{proc.cpu_usage:.0f}"))

        table.resizeRowsToContents()

    #Fazer lock antes de alterar
    def update_stack_pages(self, data: ShowSystemData):
        if not isinstance(data, ShowSystemData):
            print("System data is not valid")
            return

        print("update data")

        #Atualizar labels: total proc, total threads, mem usada, swap usado
        self.ui.total_proc_label.setText(f"{data.proc_count_total:.0f}")
        self.ui.total_threads_label.setText(f"{data.thread_count_total:.0f}")
        self.ui.total_ram_label.setText(f"{data.mem_used:.0f}/{data.mem_total:.0f} MB")
        self.ui.total_swap_label.setText(f"{data.swap_used:.0f}/{data.swap_total:.0f} MB")
        self.cpu_graph.update_graph([data.cpu_usage])
        self.memory_graph.update_graph([data.mem_used_percent, data.swap_used_percent])

        #Incrementa dados
        for i in range(len(data.process)):
            data.process[i].cpu_usage += 10
        self.fill_process_table(data.process)

        #if dialog is not none, atualiza dialog?

    def closeEvent(self, event):
        self.timer.stop()
        super().closeEvent(event)


def main():
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
