# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\WPy64-3740\SEBASTES\application\dialogs\ui\OpSelDlg.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_opSelDlg(object):
    def setupUi(self, opSelDlg):
        opSelDlg.setObjectName("opSelDlg")
        opSelDlg.resize(437, 84)
        self.formLayout_2 = QtWidgets.QFormLayout(opSelDlg)
        self.formLayout_2.setFieldGrowthPolicy(QtWidgets.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_2.setObjectName("formLayout_2")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.formLayout_2.setLayout(0, QtWidgets.QFormLayout.LabelRole, self.formLayout)
        self.label = QtWidgets.QLabel(opSelDlg)
        self.label.setObjectName("label")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label)
        self.opBox = QtWidgets.QComboBox(opSelDlg)
        self.opBox.setObjectName("opBox")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.opBox)
        self.buttonBox = QtWidgets.QDialogButtonBox(opSelDlg)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.buttonBox)

        self.retranslateUi(opSelDlg)
        QtCore.QMetaObject.connectSlotsByName(opSelDlg)

    def retranslateUi(self, opSelDlg):
        _translate = QtCore.QCoreApplication.translate
        opSelDlg.setWindowTitle(_translate("opSelDlg", "Dialog"))
        self.label.setText(_translate("opSelDlg", "select operation"))
