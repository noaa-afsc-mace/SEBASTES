# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'CamSelDlg.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QComboBox, QDialog,
    QDialogButtonBox, QFormLayout, QLabel, QSizePolicy,
    QWidget)

class Ui_camSelDlg(object):
    def setupUi(self, camSelDlg):
        if not camSelDlg.objectName():
            camSelDlg.setObjectName(u"camSelDlg")
        camSelDlg.resize(437, 107)
        self.formLayout_2 = QFormLayout(camSelDlg)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setFieldGrowthPolicy(QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")

        self.formLayout_2.setLayout(0, QFormLayout.ItemRole.LabelRole, self.formLayout)

        self.label = QLabel(camSelDlg)
        self.label.setObjectName(u"label")

        self.formLayout_2.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label)

        self.leftBox = QComboBox(camSelDlg)
        self.leftBox.setObjectName(u"leftBox")

        self.formLayout_2.setWidget(1, QFormLayout.ItemRole.FieldRole, self.leftBox)

        self.label_2 = QLabel(camSelDlg)
        self.label_2.setObjectName(u"label_2")

        self.formLayout_2.setWidget(3, QFormLayout.ItemRole.LabelRole, self.label_2)

        self.rightBox = QComboBox(camSelDlg)
        self.rightBox.setObjectName(u"rightBox")

        self.formLayout_2.setWidget(3, QFormLayout.ItemRole.FieldRole, self.rightBox)

        self.buttonBox = QDialogButtonBox(camSelDlg)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.formLayout_2.setWidget(4, QFormLayout.ItemRole.FieldRole, self.buttonBox)


        self.retranslateUi(camSelDlg)

        QMetaObject.connectSlotsByName(camSelDlg)
    # setupUi

    def retranslateUi(self, camSelDlg):
        camSelDlg.setWindowTitle(QCoreApplication.translate("camSelDlg", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("camSelDlg", u"Left Display", None))
        self.label_2.setText(QCoreApplication.translate("camSelDlg", u"Right Display", None))
    # retranslateUi

