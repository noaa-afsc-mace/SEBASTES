# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DefaultDlg.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFormLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QWidget)

class Ui_defaultDlg(object):
    def setupUi(self, defaultDlg):
        if not defaultDlg.objectName():
            defaultDlg.setObjectName(u"defaultDlg")
        defaultDlg.resize(586, 531)
        self.formLayoutWidget = QWidget(defaultDlg)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(9, 49, 571, 456))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setFieldGrowthPolicy(QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.label_x = QLabel(self.formLayoutWidget)
        self.label_x.setObjectName(u"label_x")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_x)

        self.label_y = QLabel(self.formLayoutWidget)
        self.label_y.setObjectName(u"label_y")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.label_y)

        self.label_1 = QLabel(self.formLayoutWidget)
        self.label_1.setObjectName(u"label_1")
        self.label_1.setMinimumSize(QSize(100, 0))
        font = QFont()
        font.setPointSize(10)
        self.label_1.setFont(font)

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.label_1)

        self.lineEdit_1 = QLineEdit(self.formLayoutWidget)
        self.lineEdit_1.setObjectName(u"lineEdit_1")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.lineEdit_1)

        self.label_2 = QLabel(self.formLayoutWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(100, 0))
        self.label_2.setFont(font)

        self.formLayout.setWidget(4, QFormLayout.ItemRole.LabelRole, self.label_2)

        self.lineEdit_2 = QLineEdit(self.formLayoutWidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.FieldRole, self.lineEdit_2)

        self.label_3 = QLabel(self.formLayoutWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(100, 0))
        self.label_3.setFont(font)

        self.formLayout.setWidget(5, QFormLayout.ItemRole.LabelRole, self.label_3)

        self.lineEdit_3 = QLineEdit(self.formLayoutWidget)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.formLayout.setWidget(5, QFormLayout.ItemRole.FieldRole, self.lineEdit_3)

        self.label_4 = QLabel(self.formLayoutWidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(100, 0))
        self.label_4.setFont(font)

        self.formLayout.setWidget(6, QFormLayout.ItemRole.LabelRole, self.label_4)

        self.lineEdit_4 = QLineEdit(self.formLayoutWidget)
        self.lineEdit_4.setObjectName(u"lineEdit_4")

        self.formLayout.setWidget(6, QFormLayout.ItemRole.FieldRole, self.lineEdit_4)

        self.label_5 = QLabel(self.formLayoutWidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(100, 0))
        self.label_5.setFont(font)

        self.formLayout.setWidget(7, QFormLayout.ItemRole.LabelRole, self.label_5)

        self.lineEdit_5 = QLineEdit(self.formLayoutWidget)
        self.lineEdit_5.setObjectName(u"lineEdit_5")

        self.formLayout.setWidget(7, QFormLayout.ItemRole.FieldRole, self.lineEdit_5)

        self.label_6 = QLabel(self.formLayoutWidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(100, 0))
        self.label_6.setFont(font)

        self.formLayout.setWidget(8, QFormLayout.ItemRole.LabelRole, self.label_6)

        self.lineEdit_6 = QLineEdit(self.formLayoutWidget)
        self.lineEdit_6.setObjectName(u"lineEdit_6")

        self.formLayout.setWidget(8, QFormLayout.ItemRole.FieldRole, self.lineEdit_6)

        self.label_7 = QLabel(self.formLayoutWidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(100, 0))
        self.label_7.setFont(font)

        self.formLayout.setWidget(9, QFormLayout.ItemRole.LabelRole, self.label_7)

        self.lineEdit_7 = QLineEdit(self.formLayoutWidget)
        self.lineEdit_7.setObjectName(u"lineEdit_7")

        self.formLayout.setWidget(9, QFormLayout.ItemRole.FieldRole, self.lineEdit_7)

        self.label_8 = QLabel(self.formLayoutWidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(100, 0))
        self.label_8.setFont(font)

        self.formLayout.setWidget(10, QFormLayout.ItemRole.LabelRole, self.label_8)

        self.lineEdit_8 = QLineEdit(self.formLayoutWidget)
        self.lineEdit_8.setObjectName(u"lineEdit_8")

        self.formLayout.setWidget(10, QFormLayout.ItemRole.FieldRole, self.lineEdit_8)

        self.label_9 = QLabel(self.formLayoutWidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMinimumSize(QSize(100, 0))
        self.label_9.setFont(font)

        self.formLayout.setWidget(11, QFormLayout.ItemRole.LabelRole, self.label_9)

        self.lineEdit_9 = QLineEdit(self.formLayoutWidget)
        self.lineEdit_9.setObjectName(u"lineEdit_9")

        self.formLayout.setWidget(11, QFormLayout.ItemRole.FieldRole, self.lineEdit_9)

        self.label_10 = QLabel(self.formLayoutWidget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMinimumSize(QSize(100, 0))
        self.label_10.setFont(font)

        self.formLayout.setWidget(12, QFormLayout.ItemRole.LabelRole, self.label_10)

        self.lineEdit_10 = QLineEdit(self.formLayoutWidget)
        self.lineEdit_10.setObjectName(u"lineEdit_10")

        self.formLayout.setWidget(12, QFormLayout.ItemRole.FieldRole, self.lineEdit_10)

        self.label_11 = QLabel(self.formLayoutWidget)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMinimumSize(QSize(100, 0))
        self.label_11.setFont(font)

        self.formLayout.setWidget(13, QFormLayout.ItemRole.LabelRole, self.label_11)

        self.lineEdit_11 = QLineEdit(self.formLayoutWidget)
        self.lineEdit_11.setObjectName(u"lineEdit_11")

        self.formLayout.setWidget(13, QFormLayout.ItemRole.FieldRole, self.lineEdit_11)

        self.label_12 = QLabel(self.formLayoutWidget)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMinimumSize(QSize(100, 0))
        self.label_12.setFont(font)

        self.formLayout.setWidget(14, QFormLayout.ItemRole.LabelRole, self.label_12)

        self.lineEdit_12 = QLineEdit(self.formLayoutWidget)
        self.lineEdit_12.setObjectName(u"lineEdit_12")

        self.formLayout.setWidget(14, QFormLayout.ItemRole.FieldRole, self.lineEdit_12)

        self.label_13 = QLabel(self.formLayoutWidget)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font)

        self.formLayout.setWidget(15, QFormLayout.ItemRole.LabelRole, self.label_13)

        self.lineEdit_13 = QLineEdit(self.formLayoutWidget)
        self.lineEdit_13.setObjectName(u"lineEdit_13")

        self.formLayout.setWidget(15, QFormLayout.ItemRole.FieldRole, self.lineEdit_13)

        self.label_14 = QLabel(self.formLayoutWidget)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font)

        self.formLayout.setWidget(16, QFormLayout.ItemRole.LabelRole, self.label_14)

        self.lineEdit_14 = QLineEdit(self.formLayoutWidget)
        self.lineEdit_14.setObjectName(u"lineEdit_14")

        self.formLayout.setWidget(16, QFormLayout.ItemRole.FieldRole, self.lineEdit_14)

        self.label_15 = QLabel(self.formLayoutWidget)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font)

        self.formLayout.setWidget(17, QFormLayout.ItemRole.LabelRole, self.label_15)

        self.lineEdit_15 = QLineEdit(self.formLayoutWidget)
        self.lineEdit_15.setObjectName(u"lineEdit_15")

        self.formLayout.setWidget(17, QFormLayout.ItemRole.FieldRole, self.lineEdit_15)

        self.label = QLabel(defaultDlg)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 201, 16))
        self.saveBtn = QPushButton(defaultDlg)
        self.saveBtn.setObjectName(u"saveBtn")
        self.saveBtn.setGeometry(QRect(500, 500, 75, 23))
        self.cancelBtn = QPushButton(defaultDlg)
        self.cancelBtn.setObjectName(u"cancelBtn")
        self.cancelBtn.setGeometry(QRect(400, 500, 75, 23))

        self.retranslateUi(defaultDlg)

        QMetaObject.connectSlotsByName(defaultDlg)
    # setupUi

    def retranslateUi(self, defaultDlg):
        defaultDlg.setWindowTitle(QCoreApplication.translate("defaultDlg", u"Defaults", None))
        self.label_x.setText(QCoreApplication.translate("defaultDlg", u"Parameters", None))
        self.label_y.setText(QCoreApplication.translate("defaultDlg", u"Values", None))
        self.label_1.setText("")
        self.label_2.setText("")
        self.label_3.setText("")
        self.label_4.setText("")
        self.label_5.setText("")
        self.label_6.setText("")
        self.label_7.setText("")
        self.label_8.setText("")
        self.label_9.setText("")
        self.label_10.setText("")
        self.label_11.setText("")
        self.label_12.setText("")
        self.label_13.setText("")
        self.label_14.setText("")
        self.label_15.setText("")
        self.label.setText(QCoreApplication.translate("defaultDlg", u"Application defaults", None))
        self.saveBtn.setText(QCoreApplication.translate("defaultDlg", u"Save", None))
        self.cancelBtn.setText(QCoreApplication.translate("defaultDlg", u"Cancel", None))
    # retranslateUi

