# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\WPy64-3740\SEBASTES\application\dialogs\ui\CloseupDlg.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_closeupDlg(object):
    def setupUi(self, closeupDlg):
        closeupDlg.setObjectName("closeupDlg")
        closeupDlg.resize(275, 275)
        closeupDlg.setModal(False)
        self.imgLabel = QtWidgets.QLabel(closeupDlg)
        self.imgLabel.setGeometry(QtCore.QRect(10, 10, 256, 256))
        self.imgLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.imgLabel.setText("")
        self.imgLabel.setObjectName("imgLabel")

        self.retranslateUi(closeupDlg)
        QtCore.QMetaObject.connectSlotsByName(closeupDlg)

    def retranslateUi(self, closeupDlg):
        _translate = QtCore.QCoreApplication.translate
        closeupDlg.setWindowTitle(_translate("closeupDlg", "CloseupView"))
