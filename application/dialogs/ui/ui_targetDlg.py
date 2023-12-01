# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\WPy64-3740\SEBASTES\application\dialogs\ui\targetDlg.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_targetDlg(object):
    def setupUi(self, targetDlg):
        targetDlg.setObjectName("targetDlg")
        targetDlg.resize(300, 217)
        self.formLayout = QtWidgets.QFormLayout(targetDlg)
        self.formLayout.setFieldGrowthPolicy(QtWidgets.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(targetDlg)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.targetLabel = QtWidgets.QLabel(targetDlg)
        self.targetLabel.setMinimumSize(QtCore.QSize(0, 23))
        self.targetLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.targetLabel.setText("")
        self.targetLabel.setObjectName("targetLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.targetLabel)
        self.label_3 = QtWidgets.QLabel(targetDlg)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.classBox = QtWidgets.QComboBox(targetDlg)
        self.classBox.setMinimumSize(QtCore.QSize(0, 23))
        self.classBox.setObjectName("classBox")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.classBox)
        self.frame = QtWidgets.QFrame(targetDlg)
        self.frame.setMinimumSize(QtCore.QSize(0, 50))
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
        self.saveBtn = QtWidgets.QPushButton(self.frame)
        self.saveBtn.setObjectName("saveBtn")
        self.horizontalLayout.addWidget(self.saveBtn)
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.SpanningRole, self.frame)
        self.label_2 = QtWidgets.QLabel(targetDlg)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.measureLabel = QtWidgets.QLabel(targetDlg)
        self.measureLabel.setMinimumSize(QtCore.QSize(0, 23))
        self.measureLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.measureLabel.setText("")
        self.measureLabel.setObjectName("measureLabel")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.measureLabel)
        self.label_4 = QtWidgets.QLabel(targetDlg)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.rangeLabel = QtWidgets.QLabel(targetDlg)
        self.rangeLabel.setMinimumSize(QtCore.QSize(0, 23))
        self.rangeLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.rangeLabel.setText("")
        self.rangeLabel.setObjectName("rangeLabel")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.rangeLabel)
        self.measureBtn = QtWidgets.QPushButton(targetDlg)
        self.measureBtn.setMinimumSize(QtCore.QSize(0, 28))
        self.measureBtn.setObjectName("measureBtn")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.measureBtn)

        self.retranslateUi(targetDlg)
        QtCore.QMetaObject.connectSlotsByName(targetDlg)

    def retranslateUi(self, targetDlg):
        _translate = QtCore.QCoreApplication.translate
        targetDlg.setWindowTitle(_translate("targetDlg", "Target Actions"))
        self.label.setText(_translate("targetDlg", "Target ID"))
        self.label_3.setText(_translate("targetDlg", "Class"))
        self.cancelBtn.setText(_translate("targetDlg", "Cancel"))
        self.saveBtn.setText(_translate("targetDlg", "Save"))
        self.label_2.setText(_translate("targetDlg", "Length"))
        self.label_4.setText(_translate("targetDlg", "Range"))
        self.measureBtn.setText(_translate("targetDlg", "Measure"))
