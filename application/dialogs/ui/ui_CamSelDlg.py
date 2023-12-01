# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\WPy64-3740\SEBASTES\application\dialogs\ui\CamSelDlg.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_camSelDlg(object):
    def setupUi(self, camSelDlg):
        camSelDlg.setObjectName("camSelDlg")
        camSelDlg.resize(437, 107)
        self.formLayout_2 = QtWidgets.QFormLayout(camSelDlg)
        self.formLayout_2.setFieldGrowthPolicy(QtWidgets.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_2.setObjectName("formLayout_2")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.formLayout_2.setLayout(0, QtWidgets.QFormLayout.LabelRole, self.formLayout)
        self.label = QtWidgets.QLabel(camSelDlg)
        self.label.setObjectName("label")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label)
        self.leftBox = QtWidgets.QComboBox(camSelDlg)
        self.leftBox.setObjectName("leftBox")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.leftBox)
        self.label_2 = QtWidgets.QLabel(camSelDlg)
        self.label_2.setObjectName("label_2")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.rightBox = QtWidgets.QComboBox(camSelDlg)
        self.rightBox.setObjectName("rightBox")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.rightBox)
        self.buttonBox = QtWidgets.QDialogButtonBox(camSelDlg)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.buttonBox)

        self.retranslateUi(camSelDlg)
        QtCore.QMetaObject.connectSlotsByName(camSelDlg)

    def retranslateUi(self, camSelDlg):
        _translate = QtCore.QCoreApplication.translate
        camSelDlg.setWindowTitle(_translate("camSelDlg", "Dialog"))
        self.label.setText(_translate("camSelDlg", "Left Display"))
        self.label_2.setText(_translate("camSelDlg", "Right Display"))
