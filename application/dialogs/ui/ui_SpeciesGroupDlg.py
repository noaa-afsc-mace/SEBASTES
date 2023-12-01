# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\WPy64-3740\SEBASTES\application\dialogs\ui\SpeciesGroupDlg.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_speciesGroupDlg(object):
    def setupUi(self, speciesGroupDlg):
        speciesGroupDlg.setObjectName("speciesGroupDlg")
        speciesGroupDlg.resize(224, 199)
        self.verticalLayout = QtWidgets.QVBoxLayout(speciesGroupDlg)
        self.verticalLayout.setObjectName("verticalLayout")
        self.listWidget = QtWidgets.QListWidget(speciesGroupDlg)
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout.addWidget(self.listWidget)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.cancelBtn = QtWidgets.QPushButton(speciesGroupDlg)
        self.cancelBtn.setObjectName("cancelBtn")
        self.horizontalLayout_2.addWidget(self.cancelBtn)
        self.okBtn = QtWidgets.QPushButton(speciesGroupDlg)
        self.okBtn.setObjectName("okBtn")
        self.horizontalLayout_2.addWidget(self.okBtn)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(speciesGroupDlg)
        QtCore.QMetaObject.connectSlotsByName(speciesGroupDlg)

    def retranslateUi(self, speciesGroupDlg):
        _translate = QtCore.QCoreApplication.translate
        speciesGroupDlg.setWindowTitle(_translate("speciesGroupDlg", "Select a species group"))
        self.cancelBtn.setText(_translate("speciesGroupDlg", "Cancel"))
        self.okBtn.setText(_translate("speciesGroupDlg", "OK"))
