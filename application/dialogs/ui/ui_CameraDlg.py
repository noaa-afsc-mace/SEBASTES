# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\WPy64-3740\SEBASTES\application\dialogs\ui\CameraDlg.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_cameraDlg(object):
    def setupUi(self, cameraDlg):
        cameraDlg.setObjectName("cameraDlg")
        cameraDlg.resize(400, 381)
        self.formLayout = QtWidgets.QFormLayout(cameraDlg)
        self.formLayout.setFieldGrowthPolicy(QtWidgets.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(cameraDlg)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.cameraGearBox = QtWidgets.QLineEdit(cameraDlg)
        self.cameraGearBox.setObjectName("cameraGearBox")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.cameraGearBox)
        self.label_8 = QtWidgets.QLabel(cameraDlg)
        self.label_8.setObjectName("label_8")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.lCameraDesc = QtWidgets.QPlainTextEdit(cameraDlg)
        self.lCameraDesc.setObjectName("lCameraDesc")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lCameraDesc)
        self.label_2 = QtWidgets.QLabel(cameraDlg)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.rCameraDesc = QtWidgets.QTextEdit(cameraDlg)
        self.rCameraDesc.setObjectName("rCameraDesc")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.rCameraDesc)
        self.frame = QtWidgets.QFrame(cameraDlg)
        self.frame.setMinimumSize(QtCore.QSize(0, 40))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.cancelBtn = QtWidgets.QPushButton(self.frame)
        self.cancelBtn.setObjectName("cancelBtn")
        self.horizontalLayout.addWidget(self.cancelBtn)
        self.okBtn = QtWidgets.QPushButton(self.frame)
        self.okBtn.setObjectName("okBtn")
        self.horizontalLayout.addWidget(self.okBtn)
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.frame)
        self.bsEdit = QtWidgets.QLineEdit(cameraDlg)
        self.bsEdit.setObjectName("bsEdit")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.bsEdit)
        self.label_3 = QtWidgets.QLabel(cameraDlg)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.descEdit = QtWidgets.QTextEdit(cameraDlg)
        self.descEdit.setObjectName("descEdit")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.descEdit)
        self.label_4 = QtWidgets.QLabel(cameraDlg)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_4)

        self.retranslateUi(cameraDlg)
        QtCore.QMetaObject.connectSlotsByName(cameraDlg)

    def retranslateUi(self, cameraDlg):
        _translate = QtCore.QCoreApplication.translate
        cameraDlg.setWindowTitle(_translate("cameraDlg", "Camera Gear"))
        self.label.setText(_translate("cameraDlg", "Camera Gear"))
        self.label_8.setText(_translate("cameraDlg", "Left Camera"))
        self.label_2.setText(_translate("cameraDlg", "Right Camera"))
        self.cancelBtn.setText(_translate("cameraDlg", "cancel"))
        self.okBtn.setText(_translate("cameraDlg", "OK"))
        self.label_3.setText(_translate("cameraDlg", "Baseline \n"
"separation"))
        self.label_4.setText(_translate("cameraDlg", "Description"))
