# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\SEBASTES\SEBASTES_Python-3.7\applications\SEBASTES\application\dialogs\ui\InsertSpcDlg.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_insertSpcDlg(object):
    def setupUi(self, insertSpcDlg):
        insertSpcDlg.setObjectName("insertSpcDlg")
        insertSpcDlg.resize(538, 294)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(insertSpcDlg)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(insertSpcDlg)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.speciesEdit = QtWidgets.QLineEdit(insertSpcDlg)
        self.speciesEdit.setObjectName("speciesEdit")
        self.verticalLayout.addWidget(self.speciesEdit)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(insertSpcDlg)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.btnColLabel = QtWidgets.QLabel(insertSpcDlg)
        self.btnColLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.btnColLabel.setText("")
        self.btnColLabel.setObjectName("btnColLabel")
        self.horizontalLayout_3.addWidget(self.btnColLabel)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.setColorBtn = QtWidgets.QPushButton(insertSpcDlg)
        self.setColorBtn.setObjectName("setColorBtn")
        self.verticalLayout.addWidget(self.setColorBtn)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(-1, -1, 0, 6)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(insertSpcDlg)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.sortEdit = QtWidgets.QLineEdit(insertSpcDlg)
        self.sortEdit.setObjectName("sortEdit")
        self.horizontalLayout_4.addWidget(self.sortEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(-1, -1, 0, -1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(insertSpcDlg)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.descEdit = QtWidgets.QTextEdit(insertSpcDlg)
        self.descEdit.setObjectName("descEdit")
        self.verticalLayout_2.addWidget(self.descEdit)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.cancelBtn = QtWidgets.QPushButton(insertSpcDlg)
        self.cancelBtn.setObjectName("cancelBtn")
        self.horizontalLayout_2.addWidget(self.cancelBtn)
        self.saveBtn = QtWidgets.QPushButton(insertSpcDlg)
        self.saveBtn.setObjectName("saveBtn")
        self.horizontalLayout_2.addWidget(self.saveBtn)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.retranslateUi(insertSpcDlg)
        QtCore.QMetaObject.connectSlotsByName(insertSpcDlg)

    def retranslateUi(self, insertSpcDlg):
        _translate = QtCore.QCoreApplication.translate
        insertSpcDlg.setWindowTitle(_translate("insertSpcDlg", "Insert species group"))
        self.label.setText(_translate("insertSpcDlg", "Species Group"))
        self.label_3.setText(_translate("insertSpcDlg", "Button color"))
        self.setColorBtn.setText(_translate("insertSpcDlg", "Set Color"))
        self.label_4.setText(_translate("insertSpcDlg", "Button  Order"))
        self.label_2.setText(_translate("insertSpcDlg", "Description"))
        self.cancelBtn.setText(_translate("insertSpcDlg", "Cancel"))
        self.saveBtn.setText(_translate("insertSpcDlg", "Save"))
