# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\WPy64-3740\SEBASTES\application\dialogs\ui\ClassDlg.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_classDlg(object):
    def setupUi(self, classDlg):
        classDlg.setObjectName("classDlg")
        classDlg.resize(212, 298)
        self.verticalLayout = QtWidgets.QVBoxLayout(classDlg)
        self.verticalLayout.setObjectName("verticalLayout")
        self.listWidget = QtWidgets.QListWidget(classDlg)
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout.addWidget(self.listWidget)
        self.addBtn = QtWidgets.QPushButton(classDlg)
        self.addBtn.setObjectName("addBtn")
        self.verticalLayout.addWidget(self.addBtn)
        self.frame = QtWidgets.QFrame(classDlg)
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
        self.verticalLayout.addWidget(self.frame)

        self.retranslateUi(classDlg)
        QtCore.QMetaObject.connectSlotsByName(classDlg)

    def retranslateUi(self, classDlg):
        _translate = QtCore.QCoreApplication.translate
        classDlg.setWindowTitle(_translate("classDlg", "Select a class"))
        self.addBtn.setText(_translate("classDlg", "Add New Class"))
        self.cancelBtn.setText(_translate("classDlg", "Cancel"))
        self.okBtn.setText(_translate("classDlg", "OK"))
