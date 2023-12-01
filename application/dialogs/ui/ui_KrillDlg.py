# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\WPy64-3740\SEBASTES\application\dialogs\ui\KrillDlg.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_krillDlg(object):
    def setupUi(self, krillDlg):
        krillDlg.setObjectName("krillDlg")
        krillDlg.resize(277, 285)
        self.verticalLayout = QtWidgets.QVBoxLayout(krillDlg)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.groupBox = QtWidgets.QGroupBox(krillDlg)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.radioButton1_1 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton1_1.setObjectName("radioButton1_1")
        self.verticalLayout_2.addWidget(self.radioButton1_1)
        self.radioButton1_2 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton1_2.setObjectName("radioButton1_2")
        self.verticalLayout_2.addWidget(self.radioButton1_2)
        self.radioButton1_3 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton1_3.setObjectName("radioButton1_3")
        self.verticalLayout_2.addWidget(self.radioButton1_3)
        self.radioButton1_4 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton1_4.setObjectName("radioButton1_4")
        self.verticalLayout_2.addWidget(self.radioButton1_4)
        self.radioButton1_5 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton1_5.setObjectName("radioButton1_5")
        self.verticalLayout_2.addWidget(self.radioButton1_5)
        self.horizontalLayout.addWidget(self.groupBox)
        self.groupBox2_4 = QtWidgets.QGroupBox(krillDlg)
        self.groupBox2_4.setObjectName("groupBox2_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox2_4)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.radioButton2_1 = QtWidgets.QRadioButton(self.groupBox2_4)
        self.radioButton2_1.setObjectName("radioButton2_1")
        self.verticalLayout_3.addWidget(self.radioButton2_1)
        self.radioButton2_2 = QtWidgets.QRadioButton(self.groupBox2_4)
        self.radioButton2_2.setObjectName("radioButton2_2")
        self.verticalLayout_3.addWidget(self.radioButton2_2)
        self.radioButton2_3 = QtWidgets.QRadioButton(self.groupBox2_4)
        self.radioButton2_3.setObjectName("radioButton2_3")
        self.verticalLayout_3.addWidget(self.radioButton2_3)
        self.radioButton2_4 = QtWidgets.QRadioButton(self.groupBox2_4)
        self.radioButton2_4.setObjectName("radioButton2_4")
        self.verticalLayout_3.addWidget(self.radioButton2_4)
        self.radioButton2_5 = QtWidgets.QRadioButton(self.groupBox2_4)
        self.radioButton2_5.setObjectName("radioButton2_5")
        self.verticalLayout_3.addWidget(self.radioButton2_5)
        self.horizontalLayout.addWidget(self.groupBox2_4)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.checkBox = QtWidgets.QCheckBox(krillDlg)
        self.checkBox.setObjectName("checkBox")
        self.verticalLayout.addWidget(self.checkBox)
        self.pushButton = QtWidgets.QPushButton(krillDlg)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)

        self.retranslateUi(krillDlg)
        QtCore.QMetaObject.connectSlotsByName(krillDlg)

    def retranslateUi(self, krillDlg):
        _translate = QtCore.QCoreApplication.translate
        krillDlg.setWindowTitle(_translate("krillDlg", "Dialog"))
        self.groupBox.setTitle(_translate("krillDlg", "Roll"))
        self.radioButton1_1.setText(_translate("krillDlg", "RadioButton"))
        self.radioButton1_2.setText(_translate("krillDlg", "RadioButton"))
        self.radioButton1_3.setText(_translate("krillDlg", "RadioButton"))
        self.radioButton1_4.setText(_translate("krillDlg", "RadioButton"))
        self.radioButton1_5.setText(_translate("krillDlg", "RadioButton"))
        self.groupBox2_4.setTitle(_translate("krillDlg", "Curvature"))
        self.radioButton2_1.setText(_translate("krillDlg", "RadioButton"))
        self.radioButton2_2.setText(_translate("krillDlg", "RadioButton"))
        self.radioButton2_3.setText(_translate("krillDlg", "RadioButton"))
        self.radioButton2_4.setText(_translate("krillDlg", "RadioButton"))
        self.radioButton2_5.setText(_translate("krillDlg", "RadioButton"))
        self.checkBox.setText(_translate("krillDlg", "Use for length"))
        self.pushButton.setText(_translate("krillDlg", "Done"))
