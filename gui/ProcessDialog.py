# This Python file uses the following encoding: utf-8

from PySide6.QtWidgets import QDialog
from gui.ui_process_dialog import Ui_Dialog  # import gerado
from data_classes import ShowProcessData, ShowRamData
from gui.graph_page import GraphPage

#Fill process data with gathered data
class ProcessDialog(QDialog):
    def __init__(self, process: ShowProcessData, proc_ram: ShowRamData, parent=None):
        super().__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        #Create graph with ram data
        self.ram_graph = GraphPage("kB")
        self.ram_graph.add_line_sample("Virtual size")
        self.ram_graph.add_line_sample("Stack size")
        self.ram_graph.add_line_sample("Real size shared")
        self.ram_graph.add_line_sample("Real size NOT shared")
        self.ui.ram_graph_frame.layout().addWidget(self.ram_graph)

        self.update_data(process, proc_ram)

    def update_data(self, process: ShowProcessData, proc_ram: ShowRamData):
        if not isinstance(process, ShowProcessData) or not isinstance(proc_ram, ShowRamData):
            print("Invalid data to dialog page. Could not use it")
            return

        self.ui.name_label.setText(process.name)
        self.ui.pid_label.setText(f"{process.pid}")
        self.ui.threads_label.setText(f"{process.thread_count_proc:.2f}")
        self.ui.prio_label.setText(f"{process.prio:.2f}")
        self.ui.prio_tp_label.setText(f"{process.prio_type}")
        self.ui.cpu_label.setText(f"{process.cpu_usage:.2f}")
        self.ui.dirty_ram_label.setText(f"{proc_ram.dirty_percentage:.2f}")
        self.ui.swap_label.setText(f"{proc_ram.swap_percentage:.2f}")


