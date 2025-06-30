from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout, QHBoxLayout, QFrame, QGroupBox
from PySide6.QtGui import QColor, QPalette
from PySide6.QtCore import Qt
from typing import List, Optional
from src.data_classes import ShowDiscInfo, ShowPartitionInfo

class PartitionGraph(QWidget):
    MIN_RATIO = 0.01

    def __init__(self, parent=None):
        super().__init__(parent)
        self.current_discs: Optional[List[ShowDiscInfo]] = None
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.setMinimumHeight(200)

        self.message_label = QLabel("No disk data yet")
        self.message_label.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.message_label)

    def update_graph(self, discs: List[ShowDiscInfo]):
        if discs is None or self.current_discs == discs:
            return

        self.current_discs = discs

        while self.layout.count():
            child = self.layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()

        if not discs:
            self.layout.addWidget(QLabel("No partition data available"))
            return

        for disc in discs:
            group = QGroupBox(f"{disc.model} (Vendor: {disc.vendor})")
            group_layout = QVBoxLayout()
            group.setLayout(group_layout)

            info_label = QLabel(
                f"<b>Read:</b> {disc.read_speed:.1f} MB/s  |  "
                f"<b>Write:</b> {disc.write_speed:.1f} MB/s<br>"
                f"<b>Read Wait:</b> {disc.time_waiting_read:.1f} ms  |  "
                f"<b>Write Wait:</b> {disc.time_waiting_write:.1f} ms"
            )
            group_layout.addWidget(info_label)

            bar_layout = QHBoxLayout()
            total_size = sum(p.size for p in disc.partitions if p.size > 0)

            for part in disc.partitions:
                width_ratio = part.size / total_size if total_size else 0
                if width_ratio < self.MIN_RATIO:
                    continue
                part_widget = self.make_partition_widget(part)
                bar_layout.addWidget(part_widget, stretch=int(width_ratio * 100))

            group_layout.addLayout(bar_layout)
            self.layout.addWidget(group)

    def make_partition_widget(self, part: ShowPartitionInfo):
        frame = QFrame()
        frame.setFrameShape(QFrame.Panel)
        frame.setLineWidth(2)
        frame.setMinimumHeight(60)

        color = QColor.fromHsv(hash(part.name) % 360, 180, 240)
        palette = frame.palette()
        palette.setColor(QPalette.Window, color)
        frame.setAutoFillBackground(True)
        frame.setPalette(palette)
        frame.setMouseTracking(True)

        layout = QVBoxLayout()
        label = QLabel()
        label.setAlignment(Qt.AlignCenter)
        label.setText(
            f"<b>{part.name}</b><br>{part.used:.0f} GB / {part.size:.0f} GB<br>{part.used_percentage:.1f}% used"
        )
        label.setStyleSheet("color: black; font-weight: bold;")
        layout.addWidget(label)
        frame.setLayout(layout)

        tooltip = (
            f"<b>{part.name}</b><br>"
            f"Mounted at: {part.mount_point}<br>"
            f"Size: {part.size:.0f} MB<br>"
            f"Used: {part.used:.0f} MB ({part.used_percentage:.1f}%)"
        )
        frame.setToolTip(tooltip)

        return frame
