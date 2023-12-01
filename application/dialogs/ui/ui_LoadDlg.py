# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\WPy64-3740\SEBASTES\application\dialogs\ui\LoadDlg.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_loadDlg(object):
    def setupUi(self, loadDlg):
        loadDlg.setObjectName("loadDlg")
        loadDlg.resize(291, 300)
        self.verticalLayout = QtWidgets.QVBoxLayout(loadDlg)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(loadDlg)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.tableView = QtWidgets.QTableView(loadDlg)
        self.tableView.setObjectName("tableView")
        self.verticalLayout.addWidget(self.tableView)
        self.frame = QtWidgets.QFrame(loadDlg)
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

        self.retranslateUi(loadDlg)
        QtCore.QMetaObject.connectSlotsByName(loadDlg)

    def retranslateUi(self, loadDlg):
        _translate = QtCore.QCoreApplication.translate
        loadDlg.setWindowTitle(_translate("loadDlg", "Load Deployment"))
        self.label.setText(_translate("loadDlg", "Existing Deployments"))
        self.cancelBtn.setText(_translate("loadDlg", "Cancel"))
        self.okBtn.setText(_translate("loadDlg", "OK"))
