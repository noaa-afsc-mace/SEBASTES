# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\SEBASTES\SEBASTES_development\SEBASTES\application\dialogs\ui\SetActiveProfilesDlg.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_setActiveProfilesDlg(object):
    def setupUi(self, setActiveProfilesDlg):
        setActiveProfilesDlg.setObjectName("setActiveProfilesDlg")
        setActiveProfilesDlg.resize(230, 196)
        self.verticalLayout = QtWidgets.QVBoxLayout(setActiveProfilesDlg)
        self.verticalLayout.setObjectName("verticalLayout")
        self.setProjectsBtn = QtWidgets.QPushButton(setActiveProfilesDlg)
        self.setProjectsBtn.setObjectName("setProjectsBtn")
        self.verticalLayout.addWidget(self.setProjectsBtn)
        self.setProfilesBtn = QtWidgets.QPushButton(setActiveProfilesDlg)
        self.setProfilesBtn.setObjectName("setProfilesBtn")
        self.verticalLayout.addWidget(self.setProfilesBtn)
        self.setSpcCollectionsBtn = QtWidgets.QPushButton(setActiveProfilesDlg)
        self.setSpcCollectionsBtn.setObjectName("setSpcCollectionsBtn")
        self.verticalLayout.addWidget(self.setSpcCollectionsBtn)
        self.setMetaGroupsBtn = QtWidgets.QPushButton(setActiveProfilesDlg)
        self.setMetaGroupsBtn.setObjectName("setMetaGroupsBtn")
        self.verticalLayout.addWidget(self.setMetaGroupsBtn)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.okBtn = QtWidgets.QPushButton(setActiveProfilesDlg)
        self.okBtn.setObjectName("okBtn")
        self.horizontalLayout.addWidget(self.okBtn)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(setActiveProfilesDlg)
        QtCore.QMetaObject.connectSlotsByName(setActiveProfilesDlg)

    def retranslateUi(self, setActiveProfilesDlg):
        _translate = QtCore.QCoreApplication.translate
        setActiveProfilesDlg.setWindowTitle(_translate("setActiveProfilesDlg", "Set Active Profiles"))
        self.setProjectsBtn.setText(_translate("setActiveProfilesDlg", "Set Active Projects"))
        self.setProfilesBtn.setText(_translate("setActiveProfilesDlg", "Set Active Profiles"))
        self.setSpcCollectionsBtn.setText(_translate("setActiveProfilesDlg", "Set Active Species Collections"))
        self.setMetaGroupsBtn.setText(_translate("setActiveProfilesDlg", "Set Active Metadata Groups"))
        self.okBtn.setText(_translate("setActiveProfilesDlg", "OK"))