# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\SEBASTES\SEBASTES_Python-3.7\applications\SEBASTES\application\dialogs\ui\AnnotatorDlg.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_annotatorDlg(object):
    def setupUi(self, annotatorDlg):
        annotatorDlg.setObjectName("annotatorDlg")
        annotatorDlg.resize(264, 111)
        self.verticalLayout = QtWidgets.QVBoxLayout(annotatorDlg)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(annotatorDlg)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.annotatorEdit = QtWidgets.QLineEdit(annotatorDlg)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.annotatorEdit.setFont(font)
        self.annotatorEdit.setObjectName("annotatorEdit")
        self.verticalLayout.addWidget(self.annotatorEdit)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.cancelBtn = QtWidgets.QPushButton(annotatorDlg)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.cancelBtn.setFont(font)
        self.cancelBtn.setObjectName("cancelBtn")
        self.horizontalLayout.addWidget(self.cancelBtn)
        self.okBtn = QtWidgets.QPushButton(annotatorDlg)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.okBtn.setFont(font)
        self.okBtn.setObjectName("okBtn")
        self.horizontalLayout.addWidget(self.okBtn)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(annotatorDlg)
        QtCore.QMetaObject.connectSlotsByName(annotatorDlg)

    def retranslateUi(self, annotatorDlg):
        _translate = QtCore.QCoreApplication.translate
        annotatorDlg.setWindowTitle(_translate("annotatorDlg", "Tell me about yourself..."))
        self.label.setText(_translate("annotatorDlg", "Your initials please"))
        self.cancelBtn.setText(_translate("annotatorDlg", "Cancel"))
        self.okBtn.setText(_translate("annotatorDlg", "OK"))
