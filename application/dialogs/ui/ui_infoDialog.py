# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\WPy64-3740\SEBASTES\application\dialogs\ui\infoDialog.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_infoDialog(object):
    def setupUi(self, infoDialog):
        infoDialog.setObjectName("infoDialog")
        infoDialog.resize(400, 650)
        self.verticalLayout = QtWidgets.QVBoxLayout(infoDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.statusText = QtWidgets.QPlainTextEdit(infoDialog)
        self.statusText.setAcceptDrops(False)
        self.statusText.setUndoRedoEnabled(False)
        self.statusText.setReadOnly(True)
        self.statusText.setCenterOnScroll(False)
        self.statusText.setObjectName("statusText")
        self.verticalLayout.addWidget(self.statusText)
        self.frame = QtWidgets.QFrame(infoDialog)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.saveBtn = QtWidgets.QPushButton(self.frame)
        self.saveBtn.setObjectName("saveBtn")
        self.horizontalLayout.addWidget(self.saveBtn)
        self.verticalLayout.addWidget(self.frame)

        self.retranslateUi(infoDialog)
        QtCore.QMetaObject.connectSlotsByName(infoDialog)

    def retranslateUi(self, infoDialog):
        _translate = QtCore.QCoreApplication.translate
        infoDialog.setWindowTitle(_translate("infoDialog", "Information Dialog"))
        self.saveBtn.setText(_translate("infoDialog", "OK"))
