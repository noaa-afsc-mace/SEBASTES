# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\SEBASTES\SEBASTES_Python-3.7\applications\SEBASTES\application\dialogs\ui\EditSpeciesDlg.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_editSpeciesDlg(object):
    def setupUi(self, editSpeciesDlg):
        editSpeciesDlg.setObjectName("editSpeciesDlg")
        editSpeciesDlg.resize(636, 233)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(editSpeciesDlg)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_5 = QtWidgets.QLabel(editSpeciesDlg)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_4.addWidget(self.label_5)
        self.startFrameEdit = QtWidgets.QLineEdit(editSpeciesDlg)
        self.startFrameEdit.setObjectName("startFrameEdit")
        self.verticalLayout_4.addWidget(self.startFrameEdit)
        self.horizontalLayout_4.addLayout(self.verticalLayout_4)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_6 = QtWidgets.QLabel(editSpeciesDlg)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_6.addWidget(self.label_6)
        self.endFrameEdit = QtWidgets.QLineEdit(editSpeciesDlg)
        self.endFrameEdit.setObjectName("endFrameEdit")
        self.verticalLayout_6.addWidget(self.endFrameEdit)
        self.horizontalLayout_4.addLayout(self.verticalLayout_6)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(editSpeciesDlg)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.fromSpeciesBox = QtWidgets.QComboBox(editSpeciesDlg)
        self.fromSpeciesBox.setObjectName("fromSpeciesBox")
        self.verticalLayout.addWidget(self.fromSpeciesBox)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(editSpeciesDlg)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.toSpeciesBox = QtWidgets.QComboBox(editSpeciesDlg)
        self.toSpeciesBox.setObjectName("toSpeciesBox")
        self.verticalLayout_2.addWidget(self.toSpeciesBox)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(editSpeciesDlg)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.targetCountLabel = QtWidgets.QLabel(editSpeciesDlg)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.targetCountLabel.setFont(font)
        self.targetCountLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.targetCountLabel.setText("")
        self.targetCountLabel.setObjectName("targetCountLabel")
        self.horizontalLayout_3.addWidget(self.targetCountLabel)
        self.label_4 = QtWidgets.QLabel(editSpeciesDlg)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.spinBox = QtWidgets.QSpinBox(editSpeciesDlg)
        self.spinBox.setObjectName("spinBox")
        self.horizontalLayout_3.addWidget(self.spinBox)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.changeBtn = QtWidgets.QPushButton(editSpeciesDlg)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.changeBtn.setFont(font)
        self.changeBtn.setObjectName("changeBtn")
        self.horizontalLayout_2.addWidget(self.changeBtn)
        self.nextBtn = QtWidgets.QPushButton(editSpeciesDlg)
        self.nextBtn.setObjectName("nextBtn")
        self.horizontalLayout_2.addWidget(self.nextBtn)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.doneBtn = QtWidgets.QPushButton(editSpeciesDlg)
        self.doneBtn.setObjectName("doneBtn")
        self.horizontalLayout_2.addWidget(self.doneBtn)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.retranslateUi(editSpeciesDlg)
        QtCore.QMetaObject.connectSlotsByName(editSpeciesDlg)

    def retranslateUi(self, editSpeciesDlg):
        _translate = QtCore.QCoreApplication.translate
        editSpeciesDlg.setWindowTitle(_translate("editSpeciesDlg", "Edit Species"))
        self.label_5.setText(_translate("editSpeciesDlg", "Start Frame"))
        self.label_6.setText(_translate("editSpeciesDlg", "End Frame"))
        self.label.setText(_translate("editSpeciesDlg", "Species to find"))
        self.label_2.setText(_translate("editSpeciesDlg", "Change to species"))
        self.label_3.setText(_translate("editSpeciesDlg", "Target count:"))
        self.label_4.setText(_translate("editSpeciesDlg", "Zoom level:"))
        self.changeBtn.setText(_translate("editSpeciesDlg", "Change"))
        self.nextBtn.setText(_translate("editSpeciesDlg", "Skip"))
        self.doneBtn.setText(_translate("editSpeciesDlg", "Done"))