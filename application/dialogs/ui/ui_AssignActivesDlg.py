# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\SEBASTES\SEBASTES_Python-3.7\applications\SEBASTES\application\dialogs\ui\AssignActivesDlg.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_assignActivesDlg(object):
    def setupUi(self, assignActivesDlg):
        assignActivesDlg.setObjectName("assignActivesDlg")
        assignActivesDlg.resize(354, 378)
        self.verticalLayout = QtWidgets.QVBoxLayout(assignActivesDlg)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setContentsMargins(-1, -1, -1, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label1 = QtWidgets.QLabel(assignActivesDlg)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label1.setFont(font)
        self.label1.setObjectName("label1")
        self.verticalLayout_5.addWidget(self.label1)
        self.inactiveView = QtWidgets.QTableView(assignActivesDlg)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.inactiveView.setFont(font)
        self.inactiveView.setObjectName("inactiveView")
        self.verticalLayout_5.addWidget(self.inactiveView)
        self.horizontalLayout.addLayout(self.verticalLayout_5)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setContentsMargins(-1, -1, 0, -1)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.addBtn = QtWidgets.QPushButton(assignActivesDlg)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.addBtn.setFont(font)
        self.addBtn.setObjectName("addBtn")
        self.verticalLayout_6.addWidget(self.addBtn)
        self.remBtn = QtWidgets.QPushButton(assignActivesDlg)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.remBtn.setFont(font)
        self.remBtn.setObjectName("remBtn")
        self.verticalLayout_6.addWidget(self.remBtn)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem)
        self.horizontalLayout.addLayout(self.verticalLayout_6)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setContentsMargins(-1, -1, 0, -1)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label2 = QtWidgets.QLabel(assignActivesDlg)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label2.setFont(font)
        self.label2.setObjectName("label2")
        self.verticalLayout_7.addWidget(self.label2)
        self.activeView = QtWidgets.QTableView(assignActivesDlg)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.activeView.setFont(font)
        self.activeView.setObjectName("activeView")
        self.verticalLayout_7.addWidget(self.activeView)
        self.horizontalLayout.addLayout(self.verticalLayout_7)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.okBtn = QtWidgets.QPushButton(assignActivesDlg)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.okBtn.setFont(font)
        self.okBtn.setObjectName("okBtn")
        self.horizontalLayout_4.addWidget(self.okBtn)
        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.retranslateUi(assignActivesDlg)
        QtCore.QMetaObject.connectSlotsByName(assignActivesDlg)

    def retranslateUi(self, assignActivesDlg):
        _translate = QtCore.QCoreApplication.translate
        assignActivesDlg.setWindowTitle(_translate("assignActivesDlg", "Assign Species"))
        self.label1.setText(_translate("assignActivesDlg", "Inactive"))
        self.addBtn.setText(_translate("assignActivesDlg", "Add"))
        self.remBtn.setText(_translate("assignActivesDlg", "Remove"))
        self.label2.setText(_translate("assignActivesDlg", "Active"))
        self.okBtn.setText(_translate("assignActivesDlg", "Done"))
