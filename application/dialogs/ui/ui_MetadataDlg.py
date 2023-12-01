# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\WPy64-3740\SEBASTES\application\dialogs\ui\MetadataDlg.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MetadataDlg(object):
    def setupUi(self, MetadataDlg):
        MetadataDlg.setObjectName("MetadataDlg")
        MetadataDlg.resize(631, 105)
        self.gridLayout_2 = QtWidgets.QGridLayout(MetadataDlg)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.metaLabel1 = QtWidgets.QLabel(MetadataDlg)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.metaLabel1.setFont(font)
        self.metaLabel1.setObjectName("metaLabel1")
        self.gridLayout.addWidget(self.metaLabel1, 0, 0, 1, 1)
        self.metaValue1 = QtWidgets.QLabel(MetadataDlg)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.metaValue1.setFont(font)
        self.metaValue1.setFrameShape(QtWidgets.QFrame.Panel)
        self.metaValue1.setText("")
        self.metaValue1.setObjectName("metaValue1")
        self.gridLayout.addWidget(self.metaValue1, 1, 0, 1, 1)
        self.metaLabel2 = QtWidgets.QLabel(MetadataDlg)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.metaLabel2.setFont(font)
        self.metaLabel2.setObjectName("metaLabel2")
        self.gridLayout.addWidget(self.metaLabel2, 0, 1, 1, 1)
        self.metaValue2 = QtWidgets.QLabel(MetadataDlg)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.metaValue2.setFont(font)
        self.metaValue2.setFrameShape(QtWidgets.QFrame.Panel)
        self.metaValue2.setText("")
        self.metaValue2.setObjectName("metaValue2")
        self.gridLayout.addWidget(self.metaValue2, 1, 1, 1, 1)
        self.metaLabel3 = QtWidgets.QLabel(MetadataDlg)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.metaLabel3.setFont(font)
        self.metaLabel3.setObjectName("metaLabel3")
        self.gridLayout.addWidget(self.metaLabel3, 0, 2, 1, 1)
        self.metaValue3 = QtWidgets.QLabel(MetadataDlg)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.metaValue3.setFont(font)
        self.metaValue3.setFrameShape(QtWidgets.QFrame.Panel)
        self.metaValue3.setText("")
        self.metaValue3.setObjectName("metaValue3")
        self.gridLayout.addWidget(self.metaValue3, 1, 2, 1, 1)
        self.metaLabel4 = QtWidgets.QLabel(MetadataDlg)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.metaLabel4.setFont(font)
        self.metaLabel4.setObjectName("metaLabel4")
        self.gridLayout.addWidget(self.metaLabel4, 0, 3, 1, 1)
        self.metaValue4 = QtWidgets.QLabel(MetadataDlg)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.metaValue4.setFont(font)
        self.metaValue4.setFrameShape(QtWidgets.QFrame.Panel)
        self.metaValue4.setText("")
        self.metaValue4.setObjectName("metaValue4")
        self.gridLayout.addWidget(self.metaValue4, 1, 3, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.retranslateUi(MetadataDlg)
        QtCore.QMetaObject.connectSlotsByName(MetadataDlg)

    def retranslateUi(self, MetadataDlg):
        _translate = QtCore.QCoreApplication.translate
        MetadataDlg.setWindowTitle(_translate("MetadataDlg", "Image Metadata"))
        self.metaLabel1.setText(_translate("MetadataDlg", "TextLabel"))
        self.metaLabel2.setText(_translate("MetadataDlg", "TextLabel"))
        self.metaLabel3.setText(_translate("MetadataDlg", "TextLabel"))
        self.metaLabel4.setText(_translate("MetadataDlg", "TextLabel"))
