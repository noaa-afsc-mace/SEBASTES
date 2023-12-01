# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\SEBASTES\SEBASTES_Python-3.7\applications\SEBASTES\application\dialogs\ui\DataviewDlg.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_dataviewDlg(object):
    def setupUi(self, dataviewDlg):
        dataviewDlg.setObjectName("dataviewDlg")
        dataviewDlg.setWindowModality(QtCore.Qt.NonModal)
        dataviewDlg.resize(354, 394)
        self.horizontalLayout = QtWidgets.QHBoxLayout(dataviewDlg)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tabWidget = QtWidgets.QTabWidget(dataviewDlg)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.tab)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.metadataTable = QtWidgets.QTableView(self.tab)
        self.metadataTable.setObjectName("metadataTable")
        self.horizontalLayout_2.addWidget(self.metadataTable)
        self.tabWidget.addTab(self.tab, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.tab_3)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.frameTable = QtWidgets.QTableView(self.tab_3)
        self.frameTable.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.frameTable.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.frameTable.setObjectName("frameTable")
        self.horizontalLayout_4.addWidget(self.frameTable)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.tab_2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.targetTable = QtWidgets.QTableView(self.tab_2)
        self.targetTable.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.targetTable.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.targetTable.setObjectName("targetTable")
        self.verticalLayout.addWidget(self.targetTable)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.filterBtn = QtWidgets.QPushButton(self.tab_2)
        self.filterBtn.setCheckable(True)
        self.filterBtn.setObjectName("filterBtn")
        self.horizontalLayout_3.addWidget(self.filterBtn)
        self.editBtn = QtWidgets.QPushButton(self.tab_2)
        self.editBtn.setObjectName("editBtn")
        self.horizontalLayout_3.addWidget(self.editBtn)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.tabWidget.addTab(self.tab_2, "")
        self.horizontalLayout.addWidget(self.tabWidget)

        self.retranslateUi(dataviewDlg)
        self.tabWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(dataviewDlg)

    def retranslateUi(self, dataviewDlg):
        _translate = QtCore.QCoreApplication.translate
        dataviewDlg.setWindowTitle(_translate("dataviewDlg", "Dialog"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("dataviewDlg", "Metadata"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("dataviewDlg", "Frames"))
        self.filterBtn.setText(_translate("dataviewDlg", "Filter by Species"))
        self.editBtn.setText(_translate("dataviewDlg", "Edit Species"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("dataviewDlg", "Targets"))
