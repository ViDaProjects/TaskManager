# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QHeaderView, QVBoxLayout
from PySide6.QtCore import QTimer

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from gui.ui_form import Ui_MainWindow
from src.data_classes import ProcessData, SystemData
from gui.graph_page import GraphPage

# Exemplo de processos fictícios
process_list = [
    ProcessData(name="systemd", thread_count_proc=10, prio=20, cpu_runtime=123.45, cpu_active_time=87.65),
    ProcessData(name="chrome", thread_count_proc=25, prio=15, cpu_runtime=523.12, cpu_active_time=400.75),
    ProcessData(name="python", thread_count_proc=8, prio=5, cpu_runtime=220.55, cpu_active_time=180.32),
    ProcessData(name="code", thread_count_proc=12, prio=10, cpu_runtime=300.12, cpu_active_time=250.91),
]

# Dados gerais do sistema (valores aleatórios)
fake_system_data = SystemData(
    cpu_runtime=10000.0,
    cpu_active_time=8500.0,
    mem_total=16000.0,
    mem_unused=6000.0,
    mem_available=8000.0,
    swap_total=2000.0,
    swap_free=1500.0,
    proc_count=150,
    thread_count_total=1200,
    process=process_list
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
        self.ui.process_table.setColumnCount(5)
        self.ui.process_table.setHorizontalHeaderLabels([
            "Name", "Threads", "Priority", "CPU Runtime", "CPU Active Time"
        ])
        self.ui.process_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.change_current_stack_page(PROCESSES_PAGE_INDEX)

        #graphs pages
        self.cpu_graph = GraphPage("% Active")
        self.memory_graph = GraphPage("MB used")
        self.ui.cpu_graph_frame.layout().addWidget(self.cpu_graph)
        self.ui.mem_graph_frame.layout().addWidget(self.memory_graph)


        #Timer
        self.timer = QTimer()
        self.timer.timeout.connect(lambda: self.update_stack_pages(fake_system_data))

        #Fill pages, then start timer
        self.update_stack_pages(fake_system_data)
        self.timer.start(5000) #5 seconds

        #Connects signals
        self.ui.processes_button.clicked.connect(lambda: self.change_current_stack_page(PROCESSES_PAGE_INDEX))
        self.ui.cpu_usage_button.clicked.connect(lambda: self.change_current_stack_page(CPU_USE_PAGE_INDEX))
        self.ui.memory_usage_button.clicked.connect(lambda: self.change_current_stack_page(MEMORY_USE_PAGE_INDEX))

    def change_current_stack_page(self, new_page_index: int):
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

    def update_stack_pages(self, data: SystemData):
        if not isinstance(data, SystemData):
            print("System data is not valid")
            return

        print("update data")
        cpu_percent = (data.cpu_active_time / data.cpu_runtime * 100) if data.cpu_runtime else 0
        mem_used = data.mem_total - data.mem_available

        self.cpu_graph.update_graph(cpu_percent)
        self.memory_graph.update_graph(mem_used)
        #Incrementa dados
        for i in range(len(data.process)):
            data.process[i].cpu_active_time += 10
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
