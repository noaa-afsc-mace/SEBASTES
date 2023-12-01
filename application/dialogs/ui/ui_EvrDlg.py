# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\WPy64-3740\SEBASTES\application\dialogs\ui\EvrDlg.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_EvrDlg(object):
    def setupUi(self, EvrDlg):
        EvrDlg.setObjectName("EvrDlg")
        EvrDlg.resize(239, 165)
        self.formLayout = QtWidgets.QFormLayout(EvrDlg)
        self.formLayout.setFieldGrowthPolicy(QtWidgets.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName("formLayout")
        self.regSize = QtWidgets.QLineEdit(EvrDlg)
        self.regSize.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.regSize.setObjectName("regSize")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.regSize)
        self.label = QtWidgets.QLabel(EvrDlg)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.label_2 = QtWidgets.QLabel(EvrDlg)
        self.label_2.setMinimumSize(QtCore.QSize(100, 0))
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.vertDens = QtWidgets.QLineEdit(EvrDlg)
        self.vertDens.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.vertDens.setObjectName("vertDens")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.vertDens)
        self.label_3 = QtWidgets.QLabel(EvrDlg)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.regHeight = QtWidgets.QLineEdit(EvrDlg)
        self.regHeight.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.regHeight.setObjectName("regHeight")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.regHeight)
        self.evlCheckBox = QtWidgets.QCheckBox(EvrDlg)
        self.evlCheckBox.setChecked(True)
        self.evlCheckBox.setObjectName("evlCheckBox")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.evlCheckBox)
        self.cancelBtn = QtWidgets.QPushButton(EvrDlg)
        self.cancelBtn.setObjectName("cancelBtn")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.cancelBtn)
        self.okBtn = QtWidgets.QPushButton(EvrDlg)
        self.okBtn.setObjectName("okBtn")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.okBtn)
        self.mergeCheckBox = QtWidgets.QCheckBox(EvrDlg)
        self.mergeCheckBox.setObjectName("mergeCheckBox")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.mergeCheckBox)

        self.retranslateUi(EvrDlg)
        QtCore.QMetaObject.connectSlotsByName(EvrDlg)

    def retranslateUi(self, EvrDlg):
        _translate = QtCore.QCoreApplication.translate
        EvrDlg.setWindowTitle(_translate("EvrDlg", "EchoView region file"))
        self.regSize.setText(_translate("EvrDlg", "200"))
        self.label.setText(_translate("EvrDlg", "Region Size in Frames"))
        self.label_2.setText(_translate("EvrDlg", "Vertex density in Frames"))
        self.vertDens.setText(_translate("EvrDlg", "20"))
        self.label_3.setText(_translate("EvrDlg", "Region Height in Meters"))
        self.regHeight.setText(_translate("EvrDlg", "20"))
        self.evlCheckBox.setText(_translate("EvrDlg", "Create evl File"))
        self.cancelBtn.setText(_translate("EvrDlg", "Cancel"))
        self.okBtn.setText(_translate("EvrDlg", "Proceed"))
        self.mergeCheckBox.setText(_translate("EvrDlg", "Merge Adjacent Regions"))
