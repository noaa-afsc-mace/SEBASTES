# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\WPy64-3740\SEBASTES\application\dialogs\ui\TargetCommentDlg.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_targetCommentDlg(object):
    def setupUi(self, targetCommentDlg):
        targetCommentDlg.setObjectName("targetCommentDlg")
        targetCommentDlg.resize(400, 300)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(targetCommentDlg)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setContentsMargins(-1, 10, -1, -1)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(targetCommentDlg)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.tClassLabel = QtWidgets.QLabel(targetCommentDlg)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tClassLabel.setFont(font)
        self.tClassLabel.setText("")
        self.tClassLabel.setObjectName("tClassLabel")
        self.gridLayout.addWidget(self.tClassLabel, 0, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(targetCommentDlg)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.tNumLabel = QtWidgets.QLabel(targetCommentDlg)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tNumLabel.setFont(font)
        self.tNumLabel.setText("")
        self.tNumLabel.setObjectName("tNumLabel")
        self.gridLayout.addWidget(self.tNumLabel, 1, 1, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.commentBox = QtWidgets.QPlainTextEdit(targetCommentDlg)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.commentBox.setFont(font)
        self.commentBox.setObjectName("commentBox")
        self.verticalLayout.addWidget(self.commentBox)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.saveAndExitBtn = QtWidgets.QPushButton(targetCommentDlg)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.saveAndExitBtn.setFont(font)
        self.saveAndExitBtn.setObjectName("saveAndExitBtn")
        self.verticalLayout_2.addWidget(self.saveAndExitBtn)

        self.retranslateUi(targetCommentDlg)
        QtCore.QMetaObject.connectSlotsByName(targetCommentDlg)

    def retranslateUi(self, targetCommentDlg):
        _translate = QtCore.QCoreApplication.translate
        targetCommentDlg.setWindowTitle(_translate("targetCommentDlg", "Insert Target Comment"))
        self.label.setText(_translate("targetCommentDlg", "Active Target Class"))
        self.label_3.setText(_translate("targetCommentDlg", "Active Target number"))
        self.saveAndExitBtn.setText(_translate("targetCommentDlg", "Save Comment"))
