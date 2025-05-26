# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'process.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QFrame, QHBoxLayout, QLabel, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(506, 414)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.NoFrame)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(9, 9, 9, 9)
        self.frame_4 = QFrame(self.frame_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_4)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_8 = QLabel(self.frame_4)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout.addWidget(self.label_8)

        self.name_label = QLabel(self.frame_4)
        self.name_label.setObjectName(u"name_label")

        self.horizontalLayout.addWidget(self.name_label)

        self.line = QFrame(self.frame_4)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.VLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout.addWidget(self.line)

        self.label = QLabel(self.frame_4)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label, 0, Qt.AlignmentFlag.AlignRight)

        self.pid_label = QLabel(self.frame_4)
        self.pid_label.setObjectName(u"pid_label")

        self.horizontalLayout.addWidget(self.pid_label, 0, Qt.AlignmentFlag.AlignRight)


        self.verticalLayout_3.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.frame_2)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_9 = QLabel(self.frame_5)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_2.addWidget(self.label_9)

        self.prio_label = QLabel(self.frame_5)
        self.prio_label.setObjectName(u"prio_label")

        self.horizontalLayout_2.addWidget(self.prio_label)

        self.line_2 = QFrame(self.frame_5)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.VLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_2.addWidget(self.line_2)

        self.label_3 = QLabel(self.frame_5)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_2.addWidget(self.label_3, 0, Qt.AlignmentFlag.AlignRight)

        self.prio_tp_label = QLabel(self.frame_5)
        self.prio_tp_label.setObjectName(u"prio_tp_label")

        self.horizontalLayout_2.addWidget(self.prio_tp_label, 0, Qt.AlignmentFlag.AlignRight)


        self.verticalLayout_3.addWidget(self.frame_5)

        self.frame_6 = QFrame(self.frame_2)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_6.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_11 = QLabel(self.frame_6)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_3.addWidget(self.label_11)

        self.threads_label = QLabel(self.frame_6)
        self.threads_label.setObjectName(u"threads_label")

        self.horizontalLayout_3.addWidget(self.threads_label)

        self.line_3 = QFrame(self.frame_6)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.Shape.VLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_3.addWidget(self.line_3)

        self.label_5 = QLabel(self.frame_6)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_3.addWidget(self.label_5, 0, Qt.AlignmentFlag.AlignRight)

        self.cpu_label = QLabel(self.frame_6)
        self.cpu_label.setObjectName(u"cpu_label")

        self.horizontalLayout_3.addWidget(self.cpu_label, 0, Qt.AlignmentFlag.AlignRight)


        self.verticalLayout_3.addWidget(self.frame_6)


        self.verticalLayout_2.addWidget(self.frame_2)

        self.frame_7 = QFrame(self.frame)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.frame_7)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_4.addWidget(self.label_2)

        self.dirty_ram_label = QLabel(self.frame_7)
        self.dirty_ram_label.setObjectName(u"dirty_ram_label")

        self.horizontalLayout_4.addWidget(self.dirty_ram_label)

        self.line_4 = QFrame(self.frame_7)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.Shape.VLine)
        self.line_4.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_4.addWidget(self.line_4)

        self.label_7 = QLabel(self.frame_7)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_4.addWidget(self.label_7, 0, Qt.AlignmentFlag.AlignRight)

        self.swap_label = QLabel(self.frame_7)
        self.swap_label.setObjectName(u"swap_label")

        self.horizontalLayout_4.addWidget(self.swap_label, 0, Qt.AlignmentFlag.AlignRight)


        self.verticalLayout_2.addWidget(self.frame_7)

        self.ram_graph_frame = QFrame(self.frame)
        self.ram_graph_frame.setObjectName(u"ram_graph_frame")
        self.ram_graph_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.ram_graph_frame.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout_2.addWidget(self.ram_graph_frame)


        self.verticalLayout.addWidget(self.frame)

        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label_8.setText(QCoreApplication.translate("Dialog", u"Name:", None))
        self.name_label.setText(QCoreApplication.translate("Dialog", u"...", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"PID:", None))
        self.pid_label.setText(QCoreApplication.translate("Dialog", u"0", None))
        self.label_9.setText(QCoreApplication.translate("Dialog", u"Priority:", None))
        self.prio_label.setText(QCoreApplication.translate("Dialog", u"0", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Priority type:", None))
        self.prio_tp_label.setText(QCoreApplication.translate("Dialog", u"...", None))
        self.label_11.setText(QCoreApplication.translate("Dialog", u"Threads:", None))
        self.threads_label.setText(QCoreApplication.translate("Dialog", u"0", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"CPU usage:", None))
        self.cpu_label.setText(QCoreApplication.translate("Dialog", u"0", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Dirty RAM (%):", None))
        self.dirty_ram_label.setText(QCoreApplication.translate("Dialog", u"0", None))
        self.label_7.setText(QCoreApplication.translate("Dialog", u"Swap (%):", None))
        self.swap_label.setText(QCoreApplication.translate("Dialog", u"0", None))
    # retranslateUi

