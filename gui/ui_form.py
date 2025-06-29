# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QFrame, QHBoxLayout,
    QHeaderView, QLabel, QMainWindow, QPushButton,
    QSizePolicy, QSpacerItem, QStackedWidget, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1000, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.side_menu_frame = QFrame(self.centralwidget)
        self.side_menu_frame.setObjectName(u"side_menu_frame")
        self.side_menu_frame.setFrameShape(QFrame.Shape.NoFrame)
        self.side_menu_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.side_menu_frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_3 = QFrame(self.side_menu_frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_7 = QLabel(self.frame_3)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(50, 50))
        self.label_7.setMaximumSize(QSize(100, 100))
        self.label_7.setPixmap(QPixmap(u"icons/pie-chart.svg"))
        self.label_7.setScaledContents(True)
        self.label_7.setWordWrap(False)

        self.horizontalLayout_5.addWidget(self.label_7)

        self.label = QLabel(self.frame_3)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(14)
        self.label.setFont(font)

        self.horizontalLayout_5.addWidget(self.label, 0, Qt.AlignmentFlag.AlignHCenter)


        self.verticalLayout.addWidget(self.frame_3)

        self.menu_options_frame = QFrame(self.side_menu_frame)
        self.menu_options_frame.setObjectName(u"menu_options_frame")
        self.menu_options_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.menu_options_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.menu_options_frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_8 = QLabel(self.menu_options_frame)
        self.label_8.setObjectName(u"label_8")

        self.verticalLayout_2.addWidget(self.label_8, 0, Qt.AlignmentFlag.AlignHCenter)

        self.processes_button = QPushButton(self.menu_options_frame)
        self.processes_button.setObjectName(u"processes_button")
        self.processes_button.setMouseTracking(False)
        self.processes_button.setTabletTracking(False)
        icon = QIcon()
        icon.addFile(u"icons/activity.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.processes_button.setIcon(icon)
        self.processes_button.setIconSize(QSize(20, 20))
        self.processes_button.setFlat(False)

        self.verticalLayout_2.addWidget(self.processes_button)

        self.cpu_usage_button = QPushButton(self.menu_options_frame)
        self.cpu_usage_button.setObjectName(u"cpu_usage_button")
        icon1 = QIcon()
        icon1.addFile(u"icons/cpu.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.cpu_usage_button.setIcon(icon1)
        self.cpu_usage_button.setIconSize(QSize(20, 20))
        self.cpu_usage_button.setFlat(False)

        self.verticalLayout_2.addWidget(self.cpu_usage_button)

        self.memory_usage_button = QPushButton(self.menu_options_frame)
        self.memory_usage_button.setObjectName(u"memory_usage_button")
        icon2 = QIcon()
        icon2.addFile(u"icons/hard-drive.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.memory_usage_button.setIcon(icon2)
        self.memory_usage_button.setIconSize(QSize(20, 20))
        self.memory_usage_button.setFlat(False)

        self.verticalLayout_2.addWidget(self.memory_usage_button)

        self.line_3 = QFrame(self.menu_options_frame)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.Shape.HLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_2.addWidget(self.line_3)

        self.label_12 = QLabel(self.menu_options_frame)
        self.label_12.setObjectName(u"label_12")

        self.verticalLayout_2.addWidget(self.label_12, 0, Qt.AlignmentFlag.AlignHCenter)

        self.partitions_button = QPushButton(self.menu_options_frame)
        self.partitions_button.setObjectName(u"partitions_button")
        icon3 = QIcon()
        icon3.addFile(u"icons/grid.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.partitions_button.setIcon(icon3)

        self.verticalLayout_2.addWidget(self.partitions_button)

        self.file_explorer_button = QPushButton(self.menu_options_frame)
        self.file_explorer_button.setObjectName(u"file_explorer_button")
        icon4 = QIcon()
        icon4.addFile(u"icons/archive.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.file_explorer_button.setIcon(icon4)

        self.verticalLayout_2.addWidget(self.file_explorer_button)

        self.usage_per_process_button = QPushButton(self.menu_options_frame)
        self.usage_per_process_button.setObjectName(u"usage_per_process_button")
        icon5 = QIcon()
        icon5.addFile(u"icons/sliders.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.usage_per_process_button.setIcon(icon5)

        self.verticalLayout_2.addWidget(self.usage_per_process_button)

        self.verticalSpacer = QSpacerItem(20, 349, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.verticalLayout.addWidget(self.menu_options_frame)


        self.horizontalLayout.addWidget(self.side_menu_frame)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame_6 = QFrame(self.frame_2)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_8 = QFrame(self.frame_6)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setMinimumSize(QSize(77, 44))
        self.frame_8.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_8.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, -1, 0, -1)
        self.pushButton_4 = QPushButton(self.frame_8)
        self.pushButton_4.setObjectName(u"pushButton_4")
        icon6 = QIcon()
        icon6.addFile(u"icons/menu.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_4.setIcon(icon6)
        self.pushButton_4.setIconSize(QSize(20, 20))
        self.pushButton_4.setFlat(True)

        self.horizontalLayout_3.addWidget(self.pushButton_4)

        self.label_2 = QLabel(self.frame_8)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_3.addWidget(self.label_2)


        self.horizontalLayout_2.addWidget(self.frame_8)

        self.frame_9 = QFrame(self.frame_6)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_9.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, -1, 0, -1)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)

        self.label_3 = QLabel(self.frame_9)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_4.addWidget(self.label_3, 0, Qt.AlignmentFlag.AlignHCenter)

        self.horizontalSpacer_4 = QSpacerItem(114, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_4)


        self.horizontalLayout_2.addWidget(self.frame_9)

        self.frame_5 = QFrame(self.frame_6)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(77, 44))
        self.frame_5.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_2.addWidget(self.frame_5)


        self.verticalLayout_3.addWidget(self.frame_6)

        self.frame_7 = QFrame(self.frame_2)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_7)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.stacked_pages = QStackedWidget(self.frame_7)
        self.stacked_pages.setObjectName(u"stacked_pages")
        self.process_page = QWidget()
        self.process_page.setObjectName(u"process_page")
        self.verticalLayout_5 = QVBoxLayout(self.process_page)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.frame_10 = QFrame(self.process_page)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_10.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.frame_10)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_6.addWidget(self.label_4, 0, Qt.AlignmentFlag.AlignHCenter)


        self.verticalLayout_5.addWidget(self.frame_10, 0, Qt.AlignmentFlag.AlignTop)

        self.frame_11 = QFrame(self.process_page)
        self.frame_11.setObjectName(u"frame_11")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_11.sizePolicy().hasHeightForWidth())
        self.frame_11.setSizePolicy(sizePolicy)
        self.frame_11.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_11)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.process_table = QTableWidget(self.frame_11)
        self.process_table.setObjectName(u"process_table")
        self.process_table.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.process_table.setGridStyle(Qt.PenStyle.DashLine)

        self.verticalLayout_6.addWidget(self.process_table)

        self.labels_frame = QFrame(self.frame_11)
        self.labels_frame.setObjectName(u"labels_frame")
        self.labels_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.labels_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.labels_frame)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_9 = QLabel(self.labels_frame)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_9.addWidget(self.label_9)

        self.total_proc_label = QLabel(self.labels_frame)
        self.total_proc_label.setObjectName(u"total_proc_label")

        self.horizontalLayout_9.addWidget(self.total_proc_label)

        self.line = QFrame(self.labels_frame)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.VLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_9.addWidget(self.line)

        self.label_11 = QLabel(self.labels_frame)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_9.addWidget(self.label_11, 0, Qt.AlignmentFlag.AlignRight)

        self.total_threads_label = QLabel(self.labels_frame)
        self.total_threads_label.setObjectName(u"total_threads_label")

        self.horizontalLayout_9.addWidget(self.total_threads_label, 0, Qt.AlignmentFlag.AlignRight)


        self.verticalLayout_6.addWidget(self.labels_frame)


        self.verticalLayout_5.addWidget(self.frame_11)

        self.stacked_pages.addWidget(self.process_page)
        self.memory_use_page = QWidget()
        self.memory_use_page.setObjectName(u"memory_use_page")
        self.verticalLayout_11 = QVBoxLayout(self.memory_use_page)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.frame_15 = QFrame(self.memory_use_page)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_15.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_15)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.label_6 = QLabel(self.frame_15)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_12.addWidget(self.label_6, 0, Qt.AlignmentFlag.AlignHCenter)


        self.verticalLayout_11.addWidget(self.frame_15)

        self.mem_graph_frame = QFrame(self.memory_use_page)
        self.mem_graph_frame.setObjectName(u"mem_graph_frame")
        sizePolicy.setHeightForWidth(self.mem_graph_frame.sizePolicy().hasHeightForWidth())
        self.mem_graph_frame.setSizePolicy(sizePolicy)
        self.mem_graph_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.mem_graph_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.mem_graph_frame)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_11.addWidget(self.mem_graph_frame)

        self.frame = QFrame(self.memory_use_page)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_13 = QLabel(self.frame)
        self.label_13.setObjectName(u"label_13")

        self.horizontalLayout_7.addWidget(self.label_13, 0, Qt.AlignmentFlag.AlignLeft)

        self.total_ram_label = QLabel(self.frame)
        self.total_ram_label.setObjectName(u"total_ram_label")

        self.horizontalLayout_7.addWidget(self.total_ram_label)

        self.line_2 = QFrame(self.frame)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.VLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_7.addWidget(self.line_2)

        self.label_10 = QLabel(self.frame)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_7.addWidget(self.label_10, 0, Qt.AlignmentFlag.AlignRight)

        self.total_swap_label = QLabel(self.frame)
        self.total_swap_label.setObjectName(u"total_swap_label")

        self.horizontalLayout_7.addWidget(self.total_swap_label, 0, Qt.AlignmentFlag.AlignRight)


        self.verticalLayout_11.addWidget(self.frame)

        self.stacked_pages.addWidget(self.memory_use_page)
        self.cpu_use_page = QWidget()
        self.cpu_use_page.setObjectName(u"cpu_use_page")
        self.verticalLayout_8 = QVBoxLayout(self.cpu_use_page)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.frame_13 = QFrame(self.cpu_use_page)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_13.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_13)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.frame_13)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_9.addWidget(self.label_5, 0, Qt.AlignmentFlag.AlignHCenter)


        self.verticalLayout_8.addWidget(self.frame_13)

        self.cpu_graph_frame = QFrame(self.cpu_use_page)
        self.cpu_graph_frame.setObjectName(u"cpu_graph_frame")
        sizePolicy.setHeightForWidth(self.cpu_graph_frame.sizePolicy().hasHeightForWidth())
        self.cpu_graph_frame.setSizePolicy(sizePolicy)
        self.cpu_graph_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.cpu_graph_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.cpu_graph_frame)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_8.addWidget(self.cpu_graph_frame)

        self.stacked_pages.addWidget(self.cpu_use_page)
        self.partitions_page = QWidget()
        self.partitions_page.setObjectName(u"partitions_page")
        self.verticalLayout_13 = QVBoxLayout(self.partitions_page)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.frame_4 = QFrame(self.partitions_page)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.frame_4)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.label_14 = QLabel(self.frame_4)
        self.label_14.setObjectName(u"label_14")

        self.verticalLayout_19.addWidget(self.label_14, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)


        self.verticalLayout_13.addWidget(self.frame_4, 0, Qt.AlignmentFlag.AlignTop)

        self.partitions_frame_organizer = QFrame(self.partitions_page)
        self.partitions_frame_organizer.setObjectName(u"partitions_frame_organizer")
        self.partitions_frame_organizer.setFrameShape(QFrame.Shape.NoFrame)
        self.partitions_frame_organizer.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.partitions_frame_organizer)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.partitions_frame = QFrame(self.partitions_frame_organizer)
        self.partitions_frame.setObjectName(u"partitions_frame")
        self.partitions_frame.setFrameShape(QFrame.Shape.NoFrame)
        self.partitions_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_20 = QVBoxLayout(self.partitions_frame)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_18.addWidget(self.partitions_frame)

        self.spacer_frame = QFrame(self.partitions_frame_organizer)
        self.spacer_frame.setObjectName(u"spacer_frame")
        self.spacer_frame.setFrameShape(QFrame.Shape.NoFrame)
        self.verticalLayout_21 = QVBoxLayout(self.spacer_frame)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_21.addItem(self.verticalSpacer_2)


        self.verticalLayout_18.addWidget(self.spacer_frame)


        self.verticalLayout_13.addWidget(self.partitions_frame_organizer)

        self.stacked_pages.addWidget(self.partitions_page)
        self.file_explorer_page = QWidget()
        self.file_explorer_page.setObjectName(u"file_explorer_page")
        self.verticalLayout_14 = QVBoxLayout(self.file_explorer_page)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.frame_12 = QFrame(self.file_explorer_page)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_12.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.label_15 = QLabel(self.frame_12)
        self.label_15.setObjectName(u"label_15")

        self.horizontalLayout_10.addWidget(self.label_15, 0, Qt.AlignmentFlag.AlignHCenter)


        self.verticalLayout_14.addWidget(self.frame_12, 0, Qt.AlignmentFlag.AlignTop)

        self.frame_14 = QFrame(self.file_explorer_page)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_14)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.file_explorer_frame = QFrame(self.frame_14)
        self.file_explorer_frame.setObjectName(u"file_explorer_frame")
        self.file_explorer_frame.setFrameShape(QFrame.Shape.NoFrame)
        self.file_explorer_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_22 = QVBoxLayout(self.file_explorer_frame)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.label_18 = QLabel(self.file_explorer_frame)
        self.label_18.setObjectName(u"label_18")

        self.verticalLayout_22.addWidget(self.label_18)


        self.verticalLayout_17.addWidget(self.file_explorer_frame)

        self.file_spacer_frame = QFrame(self.frame_14)
        self.file_spacer_frame.setObjectName(u"file_spacer_frame")
        self.file_spacer_frame.setFrameShape(QFrame.Shape.NoFrame)
        self.file_spacer_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_23 = QVBoxLayout(self.file_spacer_frame)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_3 = QSpacerItem(20, 405, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_23.addItem(self.verticalSpacer_3)


        self.verticalLayout_17.addWidget(self.file_spacer_frame)


        self.verticalLayout_14.addWidget(self.frame_14)

        self.stacked_pages.addWidget(self.file_explorer_page)
        self.usage_per_process_page = QWidget()
        self.usage_per_process_page.setObjectName(u"usage_per_process_page")
        self.verticalLayout_15 = QVBoxLayout(self.usage_per_process_page)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.frame_16 = QFrame(self.usage_per_process_page)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_16.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_16)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.label_16 = QLabel(self.frame_16)
        self.label_16.setObjectName(u"label_16")

        self.horizontalLayout_11.addWidget(self.label_16, 0, Qt.AlignmentFlag.AlignHCenter)


        self.verticalLayout_15.addWidget(self.frame_16, 0, Qt.AlignmentFlag.AlignTop)

        self.frame_17 = QFrame(self.usage_per_process_page)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame_17)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.usage_per_proc_table = QTableWidget(self.frame_17)
        self.usage_per_proc_table.setObjectName(u"usage_per_proc_table")
        self.usage_per_proc_table.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.usage_per_proc_table.setGridStyle(Qt.PenStyle.DashLine)

        self.verticalLayout_16.addWidget(self.usage_per_proc_table)


        self.verticalLayout_15.addWidget(self.frame_17)

        self.stacked_pages.addWidget(self.usage_per_process_page)

        self.verticalLayout_4.addWidget(self.stacked_pages)


        self.verticalLayout_3.addWidget(self.frame_7)


        self.horizontalLayout.addWidget(self.frame_2)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.pushButton_4.setDefault(False)
        self.stacked_pages.setCurrentIndex(4)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_7.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"TASK MANAGER", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"System Monitor", None))
        self.processes_button.setText(QCoreApplication.translate("MainWindow", u"Processes", None))
        self.cpu_usage_button.setText(QCoreApplication.translate("MainWindow", u"CPU usage", None))
        self.memory_usage_button.setText(QCoreApplication.translate("MainWindow", u"Memory usage", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"File System", None))
        self.partitions_button.setText(QCoreApplication.translate("MainWindow", u"Partitions", None))
        self.file_explorer_button.setText(QCoreApplication.translate("MainWindow", u"File explorer", None))
        self.usage_per_process_button.setText(QCoreApplication.translate("MainWindow", u"Usage per process", None))
        self.pushButton_4.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Menu", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"DASHBOARD", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Running processes", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Processes:", None))
        self.total_proc_label.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Threads:", None))
        self.total_threads_label.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Memory usage", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"RAM:", None))
        self.total_ram_label.setText(QCoreApplication.translate("MainWindow", u"0/0 MB", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Swap:", None))
        self.total_swap_label.setText(QCoreApplication.translate("MainWindow", u"0/0 MB", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"CPU usage", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Partitions", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"File manager", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Marca\u00e7\u00e3o", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Usage per process", None))
    # retranslateUi

