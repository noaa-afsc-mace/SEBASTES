# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'CalibrationDlg.ui'
##
## Created by: Qt User Interface Compiler version 6.11.1
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QFrame,
    QGridLayout, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSpacerItem, QToolButton,
    QWidget)

class Ui_calibrationDlg(object):
    def setupUi(self, calibrationDlg):
        if not calibrationDlg.objectName():
            calibrationDlg.setObjectName(u"calibrationDlg")
        calibrationDlg.resize(421, 213)
        self.gridLayout = QGridLayout(calibrationDlg)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(calibrationDlg)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.calIDBox = QLineEdit(calibrationDlg)
        self.calIDBox.setObjectName(u"calIDBox")

        self.gridLayout.addWidget(self.calIDBox, 0, 1, 1, 1)

        self.label_8 = QLabel(calibrationDlg)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout.addWidget(self.label_8, 1, 0, 1, 1)

        self.dateTimeBox = QLineEdit(calibrationDlg)
        self.dateTimeBox.setObjectName(u"dateTimeBox")

        self.gridLayout.addWidget(self.dateTimeBox, 1, 1, 1, 1)

        self.label_2 = QLabel(calibrationDlg)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)

        self.locationBox = QLineEdit(calibrationDlg)
        self.locationBox.setObjectName(u"locationBox")

        self.gridLayout.addWidget(self.locationBox, 2, 1, 1, 1)

        self.label_3 = QLabel(calibrationDlg)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)

        self.methodBox = QComboBox(calibrationDlg)
        self.methodBox.setObjectName(u"methodBox")

        self.gridLayout.addWidget(self.methodBox, 3, 1, 1, 1)

        self.label_4 = QLabel(calibrationDlg)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 4, 0, 1, 1)

        self.fileBox = QLineEdit(calibrationDlg)
        self.fileBox.setObjectName(u"fileBox")
        self.fileBox.setLayoutDirection(Qt.LeftToRight)

        self.gridLayout.addWidget(self.fileBox, 4, 1, 1, 1)

        self.frame = QFrame(calibrationDlg)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 40))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.cancelBtn = QPushButton(self.frame)
        self.cancelBtn.setObjectName(u"cancelBtn")

        self.horizontalLayout.addWidget(self.cancelBtn)

        self.okBtn = QPushButton(self.frame)
        self.okBtn.setObjectName(u"okBtn")

        self.horizontalLayout.addWidget(self.okBtn)


        self.gridLayout.addWidget(self.frame, 5, 0, 1, 3)

        self.browseBtn = QToolButton(calibrationDlg)
        self.browseBtn.setObjectName(u"browseBtn")

        self.gridLayout.addWidget(self.browseBtn, 4, 2, 1, 1)


        self.retranslateUi(calibrationDlg)

        QMetaObject.connectSlotsByName(calibrationDlg)
    # setupUi

    def retranslateUi(self, calibrationDlg):
        calibrationDlg.setWindowTitle(QCoreApplication.translate("calibrationDlg", u"Calibration", None))
        self.label.setText(QCoreApplication.translate("calibrationDlg", u"Calibration_ID", None))
        self.label_8.setText(QCoreApplication.translate("calibrationDlg", u"Date and Time", None))
        self.label_2.setText(QCoreApplication.translate("calibrationDlg", u"Location", None))
        self.label_3.setText(QCoreApplication.translate("calibrationDlg", u"Method", None))
        self.label_4.setText(QCoreApplication.translate("calibrationDlg", u"File location", None))
        self.cancelBtn.setText(QCoreApplication.translate("calibrationDlg", u"cancel", None))
        self.okBtn.setText(QCoreApplication.translate("calibrationDlg", u"OK", None))
        self.browseBtn.setText(QCoreApplication.translate("calibrationDlg", u"browse ...", None))
    # retranslateUi

