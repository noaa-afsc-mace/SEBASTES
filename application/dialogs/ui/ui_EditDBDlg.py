# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\SEBASTES\SEBASTES_Python-3.7\applications\SEBASTES\application\dialogs\ui\EditDBDlg.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_editDBDlg(object):
    def setupUi(self, editDBDlg):
        editDBDlg.setObjectName("editDBDlg")
        editDBDlg.resize(1097, 391)
        self.verticalLayout = QtWidgets.QVBoxLayout(editDBDlg)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.groupBox = QtWidgets.QGroupBox(editDBDlg)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.appRadio = QtWidgets.QRadioButton(self.groupBox)
        self.appRadio.setObjectName("appRadio")
        self.horizontalLayout_4.addWidget(self.appRadio)
        self.locRadio = QtWidgets.QRadioButton(self.groupBox)
        self.locRadio.setObjectName("locRadio")
        self.horizontalLayout_4.addWidget(self.locRadio)
        self.horizontalLayout.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(editDBDlg)
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        self.updateBtn = QtWidgets.QPushButton(self.groupBox_2)
        self.updateBtn.setCheckable(True)
        self.updateBtn.setAutoExclusive(True)
        self.updateBtn.setObjectName("updateBtn")
        self.horizontalLayout_5.addWidget(self.updateBtn)
        self.deleteBtn = QtWidgets.QPushButton(self.groupBox_2)
        self.deleteBtn.setCheckable(True)
        self.deleteBtn.setAutoExclusive(True)
        self.deleteBtn.setObjectName("deleteBtn")
        self.horizontalLayout_5.addWidget(self.deleteBtn)
        self.horizontalLayout.addWidget(self.groupBox_2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.updateFrame = QtWidgets.QFrame(editDBDlg)
        self.updateFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.updateFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.updateFrame.setObjectName("updateFrame")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.updateFrame)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label = QtWidgets.QLabel(self.updateFrame)
        self.label.setObjectName("label")
        self.horizontalLayout_6.addWidget(self.label)
        self.updateTableBox = QtWidgets.QComboBox(self.updateFrame)
        self.updateTableBox.setObjectName("updateTableBox")
        self.horizontalLayout_6.addWidget(self.updateTableBox)
        self.label_2 = QtWidgets.QLabel(self.updateFrame)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_6.addWidget(self.label_2)
        self.updateFieldBox = QtWidgets.QComboBox(self.updateFrame)
        self.updateFieldBox.setObjectName("updateFieldBox")
        self.horizontalLayout_6.addWidget(self.updateFieldBox)
        self.label_3 = QtWidgets.QLabel(self.updateFrame)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_6.addWidget(self.label_3)
        self.updateValueEdit = QtWidgets.QLineEdit(self.updateFrame)
        self.updateValueEdit.setObjectName("updateValueEdit")
        self.horizontalLayout_6.addWidget(self.updateValueEdit)
        self.label_4 = QtWidgets.QLabel(self.updateFrame)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_6.addWidget(self.label_4)
        self.updateConditionFieldBox = QtWidgets.QComboBox(self.updateFrame)
        self.updateConditionFieldBox.setObjectName("updateConditionFieldBox")
        self.horizontalLayout_6.addWidget(self.updateConditionFieldBox)
        self.updateSignBox = QtWidgets.QComboBox(self.updateFrame)
        self.updateSignBox.setObjectName("updateSignBox")
        self.horizontalLayout_6.addWidget(self.updateSignBox)
        self.updateWhereValueEdit = QtWidgets.QLineEdit(self.updateFrame)
        self.updateWhereValueEdit.setObjectName("updateWhereValueEdit")
        self.horizontalLayout_6.addWidget(self.updateWhereValueEdit)
        self.updateWhereValueBox = QtWidgets.QComboBox(self.updateFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.updateWhereValueBox.sizePolicy().hasHeightForWidth())
        self.updateWhereValueBox.setSizePolicy(sizePolicy)
        self.updateWhereValueBox.setMinimumSize(QtCore.QSize(200, 0))
        self.updateWhereValueBox.setObjectName("updateWhereValueBox")
        self.horizontalLayout_6.addWidget(self.updateWhereValueBox)
        self.updateSQLBtn = QtWidgets.QPushButton(self.updateFrame)
        self.updateSQLBtn.setObjectName("updateSQLBtn")
        self.horizontalLayout_6.addWidget(self.updateSQLBtn)
        self.verticalLayout.addWidget(self.updateFrame)
        self.deleteFrame = QtWidgets.QFrame(editDBDlg)
        self.deleteFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.deleteFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.deleteFrame.setObjectName("deleteFrame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.deleteFrame)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_6 = QtWidgets.QLabel(self.deleteFrame)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_2.addWidget(self.label_6)
        self.deleteTableBox = QtWidgets.QComboBox(self.deleteFrame)
        self.deleteTableBox.setObjectName("deleteTableBox")
        self.horizontalLayout_2.addWidget(self.deleteTableBox)
        self.label_7 = QtWidgets.QLabel(self.deleteFrame)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_2.addWidget(self.label_7)
        self.deleteConditionFieldBox = QtWidgets.QComboBox(self.deleteFrame)
        self.deleteConditionFieldBox.setObjectName("deleteConditionFieldBox")
        self.horizontalLayout_2.addWidget(self.deleteConditionFieldBox)
        self.deleteSignBox = QtWidgets.QComboBox(self.deleteFrame)
        self.deleteSignBox.setObjectName("deleteSignBox")
        self.horizontalLayout_2.addWidget(self.deleteSignBox)
        self.deleteWhereValueEdit = QtWidgets.QLineEdit(self.deleteFrame)
        self.deleteWhereValueEdit.setObjectName("deleteWhereValueEdit")
        self.horizontalLayout_2.addWidget(self.deleteWhereValueEdit)
        self.deleteWhereValueBox = QtWidgets.QComboBox(self.deleteFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.deleteWhereValueBox.sizePolicy().hasHeightForWidth())
        self.deleteWhereValueBox.setSizePolicy(sizePolicy)
        self.deleteWhereValueBox.setMinimumSize(QtCore.QSize(200, 0))
        self.deleteWhereValueBox.setObjectName("deleteWhereValueBox")
        self.horizontalLayout_2.addWidget(self.deleteWhereValueBox)
        self.deleteSQLBtn = QtWidgets.QPushButton(self.deleteFrame)
        self.deleteSQLBtn.setObjectName("deleteSQLBtn")
        self.horizontalLayout_2.addWidget(self.deleteSQLBtn)
        self.verticalLayout.addWidget(self.deleteFrame)
        self.sqlCmdTable = QtWidgets.QPlainTextEdit(editDBDlg)
        self.sqlCmdTable.setReadOnly(True)
        self.sqlCmdTable.setObjectName("sqlCmdTable")
        self.verticalLayout.addWidget(self.sqlCmdTable)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.runBtn = QtWidgets.QPushButton(editDBDlg)
        self.runBtn.setObjectName("runBtn")
        self.horizontalLayout_3.addWidget(self.runBtn)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.okBtn = QtWidgets.QPushButton(editDBDlg)
        self.okBtn.setObjectName("okBtn")
        self.horizontalLayout_3.addWidget(self.okBtn)
        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.retranslateUi(editDBDlg)
        QtCore.QMetaObject.connectSlotsByName(editDBDlg)

    def retranslateUi(self, editDBDlg):
        _translate = QtCore.QCoreApplication.translate
        editDBDlg.setWindowTitle(_translate("editDBDlg", "Dialog"))
        self.groupBox.setTitle(_translate("editDBDlg", "Database"))
        self.appRadio.setText(_translate("editDBDlg", "Application"))
        self.locRadio.setText(_translate("editDBDlg", "Local"))
        self.groupBox_2.setTitle(_translate("editDBDlg", "Action"))
        self.updateBtn.setText(_translate("editDBDlg", "UPDATE"))
        self.deleteBtn.setText(_translate("editDBDlg", "DELETE"))
        self.label.setText(_translate("editDBDlg", "UPDATE"))
        self.label_2.setText(_translate("editDBDlg", "SET"))
        self.label_3.setText(_translate("editDBDlg", "="))
        self.label_4.setText(_translate("editDBDlg", "WHERE"))
        self.updateSQLBtn.setText(_translate("editDBDlg", "generate SQL"))
        self.label_6.setText(_translate("editDBDlg", "DELETE FROM"))
        self.label_7.setText(_translate("editDBDlg", "WHERE"))
        self.deleteSQLBtn.setText(_translate("editDBDlg", "generate SQL"))
        self.runBtn.setText(_translate("editDBDlg", "Run Action"))
        self.okBtn.setText(_translate("editDBDlg", "Done"))