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
        icon3 = QIcon()
        icon3.addFile(u"icons/align-center.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_4.setIcon(icon3)
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

        self.verticalLayout_4.addWidget(self.stacked_pages)


        self.verticalLayout_3.addWidget(self.frame_7)


        self.horizontalLayout.addWidget(self.frame_2)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.pushButton_4.setDefault(False)
        self.stacked_pages.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_7.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"TASK MANAGER", None))
        self.processes_button.setText(QCoreApplication.translate("MainWindow", u"Processes", None))
        self.cpu_usage_button.setText(QCoreApplication.translate("MainWindow", u"CPU usage", None))
        self.memory_usage_button.setText(QCoreApplication.translate("MainWindow", u"Memory usage", None))
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
    # retranslateUi

