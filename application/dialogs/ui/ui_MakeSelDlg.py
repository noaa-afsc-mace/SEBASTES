# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\WPy64-3740\SEBASTES\application\dialogs\ui\MakeSelDlg.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_makeSelDlg(object):
    def setupUi(self, makeSelDlg):
        makeSelDlg.setObjectName("makeSelDlg")
        makeSelDlg.resize(400, 252)
        self.verticalLayout = QtWidgets.QVBoxLayout(makeSelDlg)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(makeSelDlg)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.dataView = QtWidgets.QTableView(makeSelDlg)
        self.dataView.setObjectName("dataView")
        self.verticalLayout.addWidget(self.dataView)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.cancelBtn = QtWidgets.QPushButton(makeSelDlg)
        self.cancelBtn.setObjectName("cancelBtn")
        self.horizontalLayout.addWidget(self.cancelBtn)
        self.selectBtn = QtWidgets.QPushButton(makeSelDlg)
        self.selectBtn.setObjectName("selectBtn")
        self.horizontalLayout.addWidget(self.selectBtn)
        self.newBtn = QtWidgets.QPushButton(makeSelDlg)
        self.newBtn.setObjectName("newBtn")
        self.horizontalLayout.addWidget(self.newBtn)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(makeSelDlg)
        QtCore.QMetaObject.connectSlotsByName(makeSelDlg)

    def retranslateUi(self, makeSelDlg):
        _translate = QtCore.QCoreApplication.translate
        makeSelDlg.setWindowTitle(_translate("makeSelDlg", "Make a selection"))
        self.label.setText(_translate("makeSelDlg", "Profiles"))
        self.cancelBtn.setText(_translate("makeSelDlg", "Cancel"))
        self.selectBtn.setText(_translate("makeSelDlg", "Select"))
        self.newBtn.setText(_translate("makeSelDlg", "New"))
