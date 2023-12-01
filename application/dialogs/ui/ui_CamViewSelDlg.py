# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\SEBASTES\SEBASTES_Python-3.7\applications\SEBASTES\application\dialogs\ui\CamViewSelDlg.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_camViewSelDlg(object):
    def setupUi(self, camViewSelDlg):
        camViewSelDlg.setObjectName("camViewSelDlg")
        camViewSelDlg.resize(400, 118)
        self.verticalLayout = QtWidgets.QVBoxLayout(camViewSelDlg)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(camViewSelDlg)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.groupBox = QtWidgets.QGroupBox(camViewSelDlg)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.leftRadio = QtWidgets.QRadioButton(self.groupBox)
        self.leftRadio.setObjectName("leftRadio")
        self.horizontalLayout.addWidget(self.leftRadio)
        self.rightRadio = QtWidgets.QRadioButton(self.groupBox)
        self.rightRadio.setObjectName("rightRadio")
        self.horizontalLayout.addWidget(self.rightRadio)
        self.verticalLayout.addWidget(self.groupBox)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.cancelBtn = QtWidgets.QPushButton(camViewSelDlg)
        self.cancelBtn.setObjectName("cancelBtn")
        self.horizontalLayout_2.addWidget(self.cancelBtn)
        self.okBtn = QtWidgets.QPushButton(camViewSelDlg)
        self.okBtn.setObjectName("okBtn")
        self.horizontalLayout_2.addWidget(self.okBtn)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(camViewSelDlg)
        QtCore.QMetaObject.connectSlotsByName(camViewSelDlg)

    def retranslateUi(self, camViewSelDlg):
        _translate = QtCore.QCoreApplication.translate
        camViewSelDlg.setWindowTitle(_translate("camViewSelDlg", "Mono view camera selection"))
        self.label.setText(_translate("camViewSelDlg", "Select Camera to View:"))
        self.groupBox.setTitle(_translate("camViewSelDlg", "Cameras"))
        self.leftRadio.setText(_translate("camViewSelDlg", "Left"))
        self.rightRadio.setText(_translate("camViewSelDlg", "Right"))
        self.cancelBtn.setText(_translate("camViewSelDlg", "Cancel"))
        self.okBtn.setText(_translate("camViewSelDlg", "OK"))
