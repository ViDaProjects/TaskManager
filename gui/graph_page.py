# This Python file uses the following encoding: utf-8

# if __name__ == "__main__":
#     pass
from PySide6.QtCharts import QChart, QChartView, QLineSeries, QValueAxis
from PySide6.QtWidgets import QWidget, QVBoxLayout
from PySide6.QtGui import QPainter

class GraphPage(QWidget):
    def __init__(self, y_label):
        super().__init__()
        self.series = QLineSeries()

        self.chart = QChart()
        self.chart.addSeries(self.series)
        #self.chart.setTitle(title)
        self.chart.createDefaultAxes()

        self.axisX = QValueAxis()
        self.axisX.setLabelFormat("%d")
        self.axisX.setTitleText("Time")
        self.chart.setAxisX(self.axisX, self.series)

        self.axisY = QValueAxis()
        self.axisY.setTitleText(y_label)
        self.chart.setAxisY(self.axisY, self.series)

        self.view = QChartView(self.chart)
        self.view.setRenderHint(QPainter.Antialiasing)

        layout = QVBoxLayout()
        layout.addWidget(self.view)
        self.setLayout(layout)

        self.max_points = 20
        self.data_points = []

    def update_graph(self, value):
        self.data_points.append(value)
        if len(self.data_points) > self.max_points:
            self.data_points.pop(0)

        self.series.clear()
        for i, val in enumerate(self.data_points):
            self.series.append(i, val)

        self.axisX.setRange(0, self.max_points)
        self.axisY.setRange(0, max(100, max(self.data_points)))
