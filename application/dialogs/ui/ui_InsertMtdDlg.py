# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\WPy64-3740\SEBASTES\application\dialogs\ui\InsertMtdDlg.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_insertMtdDlg(object):
    def setupUi(self, insertMtdDlg):
        insertMtdDlg.setObjectName("insertMtdDlg")
        insertMtdDlg.resize(564, 227)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(insertMtdDlg)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.habitatLabel = QtWidgets.QLabel(insertMtdDlg)
        self.habitatLabel.setObjectName("habitatLabel")
        self.verticalLayout.addWidget(self.habitatLabel)
        self.metadataEdit = QtWidgets.QLineEdit(insertMtdDlg)
        self.metadataEdit.setObjectName("metadataEdit")
        self.verticalLayout.addWidget(self.metadataEdit)
        self.label = QtWidgets.QLabel(insertMtdDlg)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.metadataTypeEdit = QtWidgets.QLineEdit(insertMtdDlg)
        self.metadataTypeEdit.setObjectName("metadataTypeEdit")
        self.verticalLayout.addWidget(self.metadataTypeEdit)
        self.label_4 = QtWidgets.QLabel(insertMtdDlg)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.categoryBox = QtWidgets.QComboBox(insertMtdDlg)
        self.categoryBox.setObjectName("categoryBox")
        self.verticalLayout.addWidget(self.categoryBox)
        self.label_3 = QtWidgets.QLabel(insertMtdDlg)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.orderSpinBox = QtWidgets.QSpinBox(insertMtdDlg)
        self.orderSpinBox.setMinimum(1)
        self.orderSpinBox.setObjectName("orderSpinBox")
        self.verticalLayout.addWidget(self.orderSpinBox)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(-1, -1, 0, -1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(insertMtdDlg)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.descEdit = QtWidgets.QTextEdit(insertMtdDlg)
        self.descEdit.setObjectName("descEdit")
        self.verticalLayout_2.addWidget(self.descEdit)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.cancelBtn = QtWidgets.QPushButton(insertMtdDlg)
        self.cancelBtn.setObjectName("cancelBtn")
        self.horizontalLayout_3.addWidget(self.cancelBtn)
        self.saveBtn = QtWidgets.QPushButton(insertMtdDlg)
        self.saveBtn.setObjectName("saveBtn")
        self.horizontalLayout_3.addWidget(self.saveBtn)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.retranslateUi(insertMtdDlg)
        QtCore.QMetaObject.connectSlotsByName(insertMtdDlg)

    def retranslateUi(self, insertMtdDlg):
        _translate = QtCore.QCoreApplication.translate
        insertMtdDlg.setWindowTitle(_translate("insertMtdDlg", "Insert metadata information"))
        self.habitatLabel.setText(_translate("insertMtdDlg", "Metadata tag"))
        self.label.setText(_translate("insertMtdDlg", "Metadata Type"))
        self.label_4.setText(_translate("insertMtdDlg", "Metadata gui element"))
        self.label_3.setText(_translate("insertMtdDlg", "GUI order"))
        self.label_2.setText(_translate("insertMtdDlg", "Description"))
        self.cancelBtn.setText(_translate("insertMtdDlg", "Cancel"))
        self.saveBtn.setText(_translate("insertMtdDlg", "Save"))
