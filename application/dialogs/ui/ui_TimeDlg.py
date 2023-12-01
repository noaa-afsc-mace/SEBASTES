# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\WPy64-3740\SEBASTES\application\dialogs\ui\TimeDlg.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_timeDlg(object):
    def setupUi(self, timeDlg):
        timeDlg.setObjectName("timeDlg")
        timeDlg.resize(274, 216)
        self.timeEdit = QtWidgets.QTimeEdit(timeDlg)
        self.timeEdit.setGeometry(QtCore.QRect(20, 100, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.timeEdit.setFont(font)
        self.timeEdit.setTime(QtCore.QTime(0, 0, 0))
        self.timeEdit.setObjectName("timeEdit")
        self.dateEdit = QtWidgets.QDateEdit(timeDlg)
        self.dateEdit.setGeometry(QtCore.QRect(20, 40, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.dateEdit.setFont(font)
        self.dateEdit.setObjectName("dateEdit")
        self.okBtn = QtWidgets.QPushButton(timeDlg)
        self.okBtn.setGeometry(QtCore.QRect(150, 160, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.okBtn.setFont(font)
        self.okBtn.setObjectName("okBtn")
        self.cancelBtn = QtWidgets.QPushButton(timeDlg)
        self.cancelBtn.setGeometry(QtCore.QRect(20, 160, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.cancelBtn.setFont(font)
        self.cancelBtn.setObjectName("cancelBtn")
        self.label = QtWidgets.QLabel(timeDlg)
        self.label.setGeometry(QtCore.QRect(30, 10, 181, 16))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.retranslateUi(timeDlg)
        QtCore.QMetaObject.connectSlotsByName(timeDlg)

    def retranslateUi(self, timeDlg):
        _translate = QtCore.QCoreApplication.translate
        timeDlg.setWindowTitle(_translate("timeDlg", "Dialog"))
        self.timeEdit.setDisplayFormat(_translate("timeDlg", "hh:mm:ss"))
        self.okBtn.setText(_translate("timeDlg", "OK"))
        self.cancelBtn.setText(_translate("timeDlg", "Cancel"))
        self.label.setText(_translate("timeDlg", "Enter a date/ time..."))
