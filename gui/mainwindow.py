# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QHeaderView

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from gui.ui_form import Ui_MainWindow
from src.data_classes import ProcessData

# Exemplo de processos fictícios
process_list = [
    ProcessData(name="systemd", thread_count_proc=10, prio=20, cpu_runtime=123.45, cpu_active_time=87.65),
    ProcessData(name="chrome", thread_count_proc=25, prio=15, cpu_runtime=523.12, cpu_active_time=400.75),
    ProcessData(name="python", thread_count_proc=8, prio=5, cpu_runtime=220.55, cpu_active_time=180.32),
    ProcessData(name="code", thread_count_proc=12, prio=10, cpu_runtime=300.12, cpu_active_time=250.91),
]

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
        self.ui.process_table.setColumnCount(5)
        self.ui.process_table.setHorizontalHeaderLabels([
            "Name", "Threads", "Priority", "CPU Runtime", "CPU Active Time"
        ])
        self.ui.process_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.change_current_stack_page(PROCESSES_PAGE_INDEX)

        #Connects signals
        self.ui.processes_button.clicked.connect(lambda: self.change_current_stack_page(PROCESSES_PAGE_INDEX, process_list))
        self.ui.cpu_usage_button.clicked.connect(lambda: self.change_current_stack_page(CPU_USE_PAGE_INDEX))
        self.ui.memory_usage_button.clicked.connect(lambda: self.change_current_stack_page(MEMORY_USE_PAGE_INDEX))

    def change_current_stack_page(self, new_page_index: int, processes: list[ProcessData] = None):
        if new_page_index == PROCESSES_PAGE_INDEX and processes is not None:
            self.fill_process_table(processes)
        self.ui.stacked_pages.setCurrentIndex(new_page_index)

    def fill_process_table(self, processes: list[ProcessData]):
        table = self.ui.process_table
        table.setRowCount(len(processes))

        for row, proc in enumerate(processes):
            table.setItem(row, 0, QTableWidgetItem(proc.name))
            table.setItem(row, 1, QTableWidgetItem(f"{proc.thread_count_proc:.0f}"))
            table.setItem(row, 2, QTableWidgetItem(f"{proc.prio:.0f}"))
            table.setItem(row, 3, QTableWidgetItem(f"{proc.cpu_runtime:.2f}"))
            table.setItem(row, 4, QTableWidgetItem(f"{proc.cpu_active_time:.2f}"))

        table.resizeRowsToContents()

def main():
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
