# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'OpSelDlg.ui'
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

class Ui_opSelDlg(object):
    def setupUi(self, opSelDlg):
        if not opSelDlg.objectName():
            opSelDlg.setObjectName(u"opSelDlg")
        opSelDlg.resize(437, 84)
        self.formLayout_2 = QFormLayout(opSelDlg)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setFieldGrowthPolicy(QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")

        self.formLayout_2.setLayout(0, QFormLayout.ItemRole.LabelRole, self.formLayout)

        self.label = QLabel(opSelDlg)
        self.label.setObjectName(u"label")

        self.formLayout_2.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label)

        self.opBox = QComboBox(opSelDlg)
        self.opBox.setObjectName(u"opBox")

        self.formLayout_2.setWidget(1, QFormLayout.ItemRole.FieldRole, self.opBox)

        self.buttonBox = QDialogButtonBox(opSelDlg)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.formLayout_2.setWidget(3, QFormLayout.ItemRole.FieldRole, self.buttonBox)


        self.retranslateUi(opSelDlg)

        QMetaObject.connectSlotsByName(opSelDlg)
    # setupUi

    def retranslateUi(self, opSelDlg):
        opSelDlg.setWindowTitle(QCoreApplication.translate("opSelDlg", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("opSelDlg", u"select operation", None))
    # retranslateUi

