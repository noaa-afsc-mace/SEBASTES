# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\WPy64-3740\SEBASTES\application\dialogs\ui\commentDlg.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_commentDlg(object):
    def setupUi(self, commentDlg):
        commentDlg.setObjectName("commentDlg")
        commentDlg.resize(400, 300)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(commentDlg)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setContentsMargins(-1, 10, -1, -1)
        self.gridLayout.setObjectName("gridLayout")
        self.classLabel = QtWidgets.QLabel(commentDlg)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.classLabel.setFont(font)
        self.classLabel.setObjectName("classLabel")
        self.gridLayout.addWidget(self.classLabel, 0, 0, 1, 1)
        self.tClassLabel = QtWidgets.QLabel(commentDlg)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tClassLabel.setFont(font)
        self.tClassLabel.setText("")
        self.tClassLabel.setObjectName("tClassLabel")
        self.gridLayout.addWidget(self.tClassLabel, 0, 1, 1, 1)
        self.targetLabel = QtWidgets.QLabel(commentDlg)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.targetLabel.setFont(font)
        self.targetLabel.setObjectName("targetLabel")
        self.gridLayout.addWidget(self.targetLabel, 1, 0, 1, 1)
        self.tNumLabel = QtWidgets.QLabel(commentDlg)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tNumLabel.setFont(font)
        self.tNumLabel.setText("")
        self.tNumLabel.setObjectName("tNumLabel")
        self.gridLayout.addWidget(self.tNumLabel, 1, 1, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.commentBox = QtWidgets.QPlainTextEdit(commentDlg)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.commentBox.setFont(font)
        self.commentBox.setObjectName("commentBox")
        self.verticalLayout.addWidget(self.commentBox)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.saveAndExitBtn = QtWidgets.QPushButton(commentDlg)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.saveAndExitBtn.setFont(font)
        self.saveAndExitBtn.setObjectName("saveAndExitBtn")
        self.verticalLayout_2.addWidget(self.saveAndExitBtn)

        self.retranslateUi(commentDlg)
        QtCore.QMetaObject.connectSlotsByName(commentDlg)

    def retranslateUi(self, commentDlg):
        _translate = QtCore.QCoreApplication.translate
        commentDlg.setWindowTitle(_translate("commentDlg", "Insert Comment"))
        self.classLabel.setText(_translate("commentDlg", "Active Target Class"))
        self.targetLabel.setText(_translate("commentDlg", "Active Target number"))
        self.saveAndExitBtn.setText(_translate("commentDlg", "Save Comment"))
