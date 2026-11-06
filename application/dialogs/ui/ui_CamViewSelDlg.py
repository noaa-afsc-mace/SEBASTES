# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'CamViewSelDlg.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QGroupBox, QHBoxLayout,
    QLabel, QPushButton, QRadioButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_camViewSelDlg(object):
    def setupUi(self, camViewSelDlg):
        if not camViewSelDlg.objectName():
            camViewSelDlg.setObjectName(u"camViewSelDlg")
        camViewSelDlg.resize(400, 118)
        self.verticalLayout = QVBoxLayout(camViewSelDlg)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(camViewSelDlg)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.groupBox = QGroupBox(camViewSelDlg)
        self.groupBox.setObjectName(u"groupBox")
        self.horizontalLayout = QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.leftRadio = QRadioButton(self.groupBox)
        self.leftRadio.setObjectName(u"leftRadio")

        self.horizontalLayout.addWidget(self.leftRadio)

        self.rightRadio = QRadioButton(self.groupBox)
        self.rightRadio.setObjectName(u"rightRadio")

        self.horizontalLayout.addWidget(self.rightRadio)


        self.verticalLayout.addWidget(self.groupBox)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.cancelBtn = QPushButton(camViewSelDlg)
        self.cancelBtn.setObjectName(u"cancelBtn")

        self.horizontalLayout_2.addWidget(self.cancelBtn)

        self.okBtn = QPushButton(camViewSelDlg)
        self.okBtn.setObjectName(u"okBtn")

        self.horizontalLayout_2.addWidget(self.okBtn)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.retranslateUi(camViewSelDlg)

        QMetaObject.connectSlotsByName(camViewSelDlg)
    # setupUi

    def retranslateUi(self, camViewSelDlg):
        camViewSelDlg.setWindowTitle(QCoreApplication.translate("camViewSelDlg", u"Mono view camera selection", None))
        self.label.setText(QCoreApplication.translate("camViewSelDlg", u"Select Camera to View:", None))
        self.groupBox.setTitle(QCoreApplication.translate("camViewSelDlg", u"Cameras", None))
        self.leftRadio.setText(QCoreApplication.translate("camViewSelDlg", u"Left", None))
        self.rightRadio.setText(QCoreApplication.translate("camViewSelDlg", u"Right", None))
        self.cancelBtn.setText(QCoreApplication.translate("camViewSelDlg", u"Cancel", None))
        self.okBtn.setText(QCoreApplication.translate("camViewSelDlg", u"OK", None))
    # retranslateUi

