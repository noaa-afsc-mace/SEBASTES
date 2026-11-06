# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'KrillDlg.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QDialog, QGroupBox,
    QHBoxLayout, QPushButton, QRadioButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_krillDlg(object):
    def setupUi(self, krillDlg):
        if not krillDlg.objectName():
            krillDlg.setObjectName(u"krillDlg")
        krillDlg.resize(277, 285)
        self.verticalLayout = QVBoxLayout(krillDlg)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.groupBox = QGroupBox(krillDlg)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.radioButton1_1 = QRadioButton(self.groupBox)
        self.radioButton1_1.setObjectName(u"radioButton1_1")

        self.verticalLayout_2.addWidget(self.radioButton1_1)

        self.radioButton1_2 = QRadioButton(self.groupBox)
        self.radioButton1_2.setObjectName(u"radioButton1_2")

        self.verticalLayout_2.addWidget(self.radioButton1_2)

        self.radioButton1_3 = QRadioButton(self.groupBox)
        self.radioButton1_3.setObjectName(u"radioButton1_3")

        self.verticalLayout_2.addWidget(self.radioButton1_3)

        self.radioButton1_4 = QRadioButton(self.groupBox)
        self.radioButton1_4.setObjectName(u"radioButton1_4")

        self.verticalLayout_2.addWidget(self.radioButton1_4)

        self.radioButton1_5 = QRadioButton(self.groupBox)
        self.radioButton1_5.setObjectName(u"radioButton1_5")

        self.verticalLayout_2.addWidget(self.radioButton1_5)


        self.horizontalLayout.addWidget(self.groupBox)

        self.groupBox2_4 = QGroupBox(krillDlg)
        self.groupBox2_4.setObjectName(u"groupBox2_4")
        self.verticalLayout_3 = QVBoxLayout(self.groupBox2_4)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.radioButton2_1 = QRadioButton(self.groupBox2_4)
        self.radioButton2_1.setObjectName(u"radioButton2_1")

        self.verticalLayout_3.addWidget(self.radioButton2_1)

        self.radioButton2_2 = QRadioButton(self.groupBox2_4)
        self.radioButton2_2.setObjectName(u"radioButton2_2")

        self.verticalLayout_3.addWidget(self.radioButton2_2)

        self.radioButton2_3 = QRadioButton(self.groupBox2_4)
        self.radioButton2_3.setObjectName(u"radioButton2_3")

        self.verticalLayout_3.addWidget(self.radioButton2_3)

        self.radioButton2_4 = QRadioButton(self.groupBox2_4)
        self.radioButton2_4.setObjectName(u"radioButton2_4")

        self.verticalLayout_3.addWidget(self.radioButton2_4)

        self.radioButton2_5 = QRadioButton(self.groupBox2_4)
        self.radioButton2_5.setObjectName(u"radioButton2_5")

        self.verticalLayout_3.addWidget(self.radioButton2_5)


        self.horizontalLayout.addWidget(self.groupBox2_4)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.checkBox = QCheckBox(krillDlg)
        self.checkBox.setObjectName(u"checkBox")

        self.verticalLayout.addWidget(self.checkBox)

        self.pushButton = QPushButton(krillDlg)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout.addWidget(self.pushButton)


        self.retranslateUi(krillDlg)

        QMetaObject.connectSlotsByName(krillDlg)
    # setupUi

    def retranslateUi(self, krillDlg):
        krillDlg.setWindowTitle(QCoreApplication.translate("krillDlg", u"Dialog", None))
        self.groupBox.setTitle(QCoreApplication.translate("krillDlg", u"Roll", None))
        self.radioButton1_1.setText(QCoreApplication.translate("krillDlg", u"RadioButton", None))
        self.radioButton1_2.setText(QCoreApplication.translate("krillDlg", u"RadioButton", None))
        self.radioButton1_3.setText(QCoreApplication.translate("krillDlg", u"RadioButton", None))
        self.radioButton1_4.setText(QCoreApplication.translate("krillDlg", u"RadioButton", None))
        self.radioButton1_5.setText(QCoreApplication.translate("krillDlg", u"RadioButton", None))
        self.groupBox2_4.setTitle(QCoreApplication.translate("krillDlg", u"Curvature", None))
        self.radioButton2_1.setText(QCoreApplication.translate("krillDlg", u"RadioButton", None))
        self.radioButton2_2.setText(QCoreApplication.translate("krillDlg", u"RadioButton", None))
        self.radioButton2_3.setText(QCoreApplication.translate("krillDlg", u"RadioButton", None))
        self.radioButton2_4.setText(QCoreApplication.translate("krillDlg", u"RadioButton", None))
        self.radioButton2_5.setText(QCoreApplication.translate("krillDlg", u"RadioButton", None))
        self.checkBox.setText(QCoreApplication.translate("krillDlg", u"Use for length", None))
        self.pushButton.setText(QCoreApplication.translate("krillDlg", u"Done", None))
    # retranslateUi

