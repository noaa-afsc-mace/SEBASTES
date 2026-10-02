# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'AutoSettingsDlg.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFormLayout, QFrame,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QWidget)

class Ui_autoSettingsDlg(object):
    def setupUi(self, autoSettingsDlg):
        if not autoSettingsDlg.objectName():
            autoSettingsDlg.setObjectName(u"autoSettingsDlg")
        autoSettingsDlg.resize(400, 500)
        self.formLayout_2 = QFormLayout(autoSettingsDlg)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setFieldGrowthPolicy(QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")

        self.formLayout_2.setLayout(0, QFormLayout.ItemRole.LabelRole, self.formLayout)

        self.label1 = QLabel(autoSettingsDlg)
        self.label1.setObjectName(u"label1")

        self.formLayout_2.setWidget(2, QFormLayout.ItemRole.LabelRole, self.label1)

        self.lineEdit1 = QLineEdit(autoSettingsDlg)
        self.lineEdit1.setObjectName(u"lineEdit1")

        self.formLayout_2.setWidget(2, QFormLayout.ItemRole.FieldRole, self.lineEdit1)

        self.label2 = QLabel(autoSettingsDlg)
        self.label2.setObjectName(u"label2")

        self.formLayout_2.setWidget(3, QFormLayout.ItemRole.LabelRole, self.label2)

        self.lineEdit2 = QLineEdit(autoSettingsDlg)
        self.lineEdit2.setObjectName(u"lineEdit2")

        self.formLayout_2.setWidget(3, QFormLayout.ItemRole.FieldRole, self.lineEdit2)

        self.label3 = QLabel(autoSettingsDlg)
        self.label3.setObjectName(u"label3")

        self.formLayout_2.setWidget(4, QFormLayout.ItemRole.LabelRole, self.label3)

        self.lineEdit3 = QLineEdit(autoSettingsDlg)
        self.lineEdit3.setObjectName(u"lineEdit3")

        self.formLayout_2.setWidget(4, QFormLayout.ItemRole.FieldRole, self.lineEdit3)

        self.label4 = QLabel(autoSettingsDlg)
        self.label4.setObjectName(u"label4")

        self.formLayout_2.setWidget(5, QFormLayout.ItemRole.LabelRole, self.label4)

        self.lineEdit4 = QLineEdit(autoSettingsDlg)
        self.lineEdit4.setObjectName(u"lineEdit4")

        self.formLayout_2.setWidget(5, QFormLayout.ItemRole.FieldRole, self.lineEdit4)

        self.label5 = QLabel(autoSettingsDlg)
        self.label5.setObjectName(u"label5")

        self.formLayout_2.setWidget(6, QFormLayout.ItemRole.LabelRole, self.label5)

        self.lineEdit5 = QLineEdit(autoSettingsDlg)
        self.lineEdit5.setObjectName(u"lineEdit5")

        self.formLayout_2.setWidget(6, QFormLayout.ItemRole.FieldRole, self.lineEdit5)

        self.label6 = QLabel(autoSettingsDlg)
        self.label6.setObjectName(u"label6")

        self.formLayout_2.setWidget(7, QFormLayout.ItemRole.LabelRole, self.label6)

        self.lineEdit6 = QLineEdit(autoSettingsDlg)
        self.lineEdit6.setObjectName(u"lineEdit6")

        self.formLayout_2.setWidget(7, QFormLayout.ItemRole.FieldRole, self.lineEdit6)

        self.label7 = QLabel(autoSettingsDlg)
        self.label7.setObjectName(u"label7")

        self.formLayout_2.setWidget(8, QFormLayout.ItemRole.LabelRole, self.label7)

        self.lineEdit7 = QLineEdit(autoSettingsDlg)
        self.lineEdit7.setObjectName(u"lineEdit7")

        self.formLayout_2.setWidget(8, QFormLayout.ItemRole.FieldRole, self.lineEdit7)

        self.label8 = QLabel(autoSettingsDlg)
        self.label8.setObjectName(u"label8")

        self.formLayout_2.setWidget(9, QFormLayout.ItemRole.LabelRole, self.label8)

        self.lineEdit8 = QLineEdit(autoSettingsDlg)
        self.lineEdit8.setObjectName(u"lineEdit8")

        self.formLayout_2.setWidget(9, QFormLayout.ItemRole.FieldRole, self.lineEdit8)

        self.label9 = QLabel(autoSettingsDlg)
        self.label9.setObjectName(u"label9")

        self.formLayout_2.setWidget(10, QFormLayout.ItemRole.LabelRole, self.label9)

        self.lineEdit9 = QLineEdit(autoSettingsDlg)
        self.lineEdit9.setObjectName(u"lineEdit9")

        self.formLayout_2.setWidget(10, QFormLayout.ItemRole.FieldRole, self.lineEdit9)

        self.label10 = QLabel(autoSettingsDlg)
        self.label10.setObjectName(u"label10")

        self.formLayout_2.setWidget(11, QFormLayout.ItemRole.LabelRole, self.label10)

        self.lineEdit10 = QLineEdit(autoSettingsDlg)
        self.lineEdit10.setObjectName(u"lineEdit10")

        self.formLayout_2.setWidget(11, QFormLayout.ItemRole.FieldRole, self.lineEdit10)

        self.label11 = QLabel(autoSettingsDlg)
        self.label11.setObjectName(u"label11")

        self.formLayout_2.setWidget(12, QFormLayout.ItemRole.LabelRole, self.label11)

        self.lineEdit11 = QLineEdit(autoSettingsDlg)
        self.lineEdit11.setObjectName(u"lineEdit11")

        self.formLayout_2.setWidget(12, QFormLayout.ItemRole.FieldRole, self.lineEdit11)

        self.frame = QFrame(autoSettingsDlg)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 51))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.cancelBtn = QPushButton(self.frame)
        self.cancelBtn.setObjectName(u"cancelBtn")

        self.horizontalLayout.addWidget(self.cancelBtn)

        self.saveBtn = QPushButton(self.frame)
        self.saveBtn.setObjectName(u"saveBtn")

        self.horizontalLayout.addWidget(self.saveBtn)


        self.horizontalLayout_2.addLayout(self.horizontalLayout)


        self.formLayout_2.setWidget(16, QFormLayout.ItemRole.FieldRole, self.frame)

        self.label0 = QLabel(autoSettingsDlg)
        self.label0.setObjectName(u"label0")

        self.formLayout_2.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label0)

        self.lineEdit0 = QLineEdit(autoSettingsDlg)
        self.lineEdit0.setObjectName(u"lineEdit0")

        self.formLayout_2.setWidget(1, QFormLayout.ItemRole.FieldRole, self.lineEdit0)

        self.lineEdit12 = QLineEdit(autoSettingsDlg)
        self.lineEdit12.setObjectName(u"lineEdit12")

        self.formLayout_2.setWidget(13, QFormLayout.ItemRole.FieldRole, self.lineEdit12)

        self.label12 = QLabel(autoSettingsDlg)
        self.label12.setObjectName(u"label12")

        self.formLayout_2.setWidget(13, QFormLayout.ItemRole.LabelRole, self.label12)

        self.lineEdit13 = QLineEdit(autoSettingsDlg)
        self.lineEdit13.setObjectName(u"lineEdit13")

        self.formLayout_2.setWidget(14, QFormLayout.ItemRole.FieldRole, self.lineEdit13)

        self.label13 = QLabel(autoSettingsDlg)
        self.label13.setObjectName(u"label13")

        self.formLayout_2.setWidget(14, QFormLayout.ItemRole.LabelRole, self.label13)

        self.lineEdit14 = QLineEdit(autoSettingsDlg)
        self.lineEdit14.setObjectName(u"lineEdit14")

        self.formLayout_2.setWidget(15, QFormLayout.ItemRole.FieldRole, self.lineEdit14)

        self.label14 = QLabel(autoSettingsDlg)
        self.label14.setObjectName(u"label14")

        self.formLayout_2.setWidget(15, QFormLayout.ItemRole.LabelRole, self.label14)


        self.retranslateUi(autoSettingsDlg)

        QMetaObject.connectSlotsByName(autoSettingsDlg)
    # setupUi

    def retranslateUi(self, autoSettingsDlg):
        autoSettingsDlg.setWindowTitle(QCoreApplication.translate("autoSettingsDlg", u"Dialog", None))
        self.label1.setText("")
        self.label2.setText("")
        self.label3.setText("")
        self.label4.setText("")
        self.label5.setText("")
        self.label6.setText("")
        self.label7.setText("")
        self.label8.setText("")
        self.label9.setText("")
        self.label10.setText("")
        self.label11.setText("")
        self.cancelBtn.setText(QCoreApplication.translate("autoSettingsDlg", u"Cancel", None))
        self.saveBtn.setText(QCoreApplication.translate("autoSettingsDlg", u"Save", None))
        self.label0.setText("")
        self.label12.setText("")
        self.label13.setText("")
        self.label14.setText("")
    # retranslateUi

