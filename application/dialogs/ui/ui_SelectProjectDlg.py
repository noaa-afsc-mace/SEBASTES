# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\SEBASTES\SEBASTES_development\SEBASTES\application\dialogs\ui\SelectProjectDlg.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_selectProjectDlg(object):
    def setupUi(self, selectProjectDlg):
        selectProjectDlg.setObjectName("selectProjectDlg")
        selectProjectDlg.resize(516, 189)
        self.verticalLayout = QtWidgets.QVBoxLayout(selectProjectDlg)
        self.verticalLayout.setObjectName("verticalLayout")
        self.projectView = QtWidgets.QTableView(selectProjectDlg)
        self.projectView.setObjectName("projectView")
        self.verticalLayout.addWidget(self.projectView)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.createNewProjBtn = QtWidgets.QPushButton(selectProjectDlg)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.createNewProjBtn.sizePolicy().hasHeightForWidth())
        self.createNewProjBtn.setSizePolicy(sizePolicy)
        self.createNewProjBtn.setObjectName("createNewProjBtn")
        self.horizontalLayout_2.addWidget(self.createNewProjBtn)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.cancelBtn = QtWidgets.QPushButton(selectProjectDlg)
        self.cancelBtn.setObjectName("cancelBtn")
        self.horizontalLayout_2.addWidget(self.cancelBtn)
        self.okBtn = QtWidgets.QPushButton(selectProjectDlg)
        self.okBtn.setObjectName("okBtn")
        self.horizontalLayout_2.addWidget(self.okBtn)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(selectProjectDlg)
        QtCore.QMetaObject.connectSlotsByName(selectProjectDlg)

    def retranslateUi(self, selectProjectDlg):
        _translate = QtCore.QCoreApplication.translate
        selectProjectDlg.setWindowTitle(_translate("selectProjectDlg", "Select a project"))
        self.createNewProjBtn.setText(_translate("selectProjectDlg", "Create Project"))
        self.cancelBtn.setText(_translate("selectProjectDlg", "Cancel"))
        self.okBtn.setText(_translate("selectProjectDlg", "OK"))
