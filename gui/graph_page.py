# This Python file uses the following encoding: utf-8

# if __name__ == "__main__":
#     pass
from PySide6.QtCharts import QChart, QChartView, QLineSeries, QValueAxis
from PySide6.QtWidgets import QWidget, QVBoxLayout, QGraphicsSimpleTextItem
from PySide6.QtGui import QPainter
from PySide6.QtCore import QPointF

class GraphPage(QWidget):
    def __init__(self, y_label):
        super().__init__()
        self.series = []
        self.label_items = []
        self.data_points = []

        self.chart = QChart()
        self.chart.createDefaultAxes()

        self.axisX = QValueAxis()
        self.axisX.setLabelFormat("%d")
        self.axisX.setTitleText("Time")
        self.chart.setAxisX(self.axisX)

        self.axisY = QValueAxis()
        self.axisY.setTitleText(y_label)
        self.chart.setAxisY(self.axisY)

        self.chart.legend().setVisible(True)

        self.view = QChartView(self.chart)
        self.view.setRenderHint(QPainter.Antialiasing)

        layout = QVBoxLayout()
        layout.addWidget(self.view)
        self.setLayout(layout)

        self.max_points = 20

    def add_line_sample(self, name):
        serie = QLineSeries()
        serie.setName(name)
        serie.setPointsVisible(True)
        self.chart.addSeries(serie)
        self.chart.setAxisX(self.axisX, serie)
        self.chart.setAxisY(self.axisY, serie)
        self.series.append(serie)

        label = QGraphicsSimpleTextItem()
        self.chart.scene().addItem(label)
        self.label_items.append(label)
        self.data_points.append([])

    def update_graph(self, values):
        for i, val in enumerate(values):
            self.data_points[i].append(val)
            if len(self.data_points[i]) > self.max_points:
                self.data_points[i].pop(0)

        for i, serie in enumerate(self.series):
            serie.clear()
            for x, y in enumerate(self.data_points[i]):
                serie.append(x, y)

        self.axisX.setRange(0, self.max_points)
        max_y = max(max(points) if points else 0 for points in self.data_points)
        self.axisY.setRange(0, max(100, max_y))

        for i, points in enumerate(self.data_points):
            if points:
                last_x = len(points) - 1
                last_y = points[-1]
                self.label_items[i].setText(f"{last_y:.1f}")
                pos = self.chart.mapToPosition(QPointF(last_x, last_y), self.series[i])
                self.label_items[i].setPos(pos.x() + 5, pos.y() - 20)
