# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\WPy64-3740\SEBASTES\application\dialogs\ui\TargetLFViewDlg.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_targetLFViewDlg(object):
    def setupUi(self, targetLFViewDlg):
        targetLFViewDlg.setObjectName("targetLFViewDlg")
        targetLFViewDlg.resize(645, 351)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(targetLFViewDlg)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.plotWindow = mplwidget(targetLFViewDlg)
        self.plotWindow.setObjectName("plotWindow")
        self.verticalLayout.addWidget(self.plotWindow)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.frame = QtWidgets.QFrame(targetLFViewDlg)
        self.frame.setMaximumSize(QtCore.QSize(16777215, 60))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.exitBtn = QtWidgets.QPushButton(self.frame)
        self.exitBtn.setObjectName("exitBtn")
        self.horizontalLayout.addWidget(self.exitBtn)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addWidget(self.frame)

        self.retranslateUi(targetLFViewDlg)
        QtCore.QMetaObject.connectSlotsByName(targetLFViewDlg)

    def retranslateUi(self, targetLFViewDlg):
        _translate = QtCore.QCoreApplication.translate
        targetLFViewDlg.setWindowTitle(_translate("targetLFViewDlg", "Dialog"))
        self.exitBtn.setText(_translate("targetLFViewDlg", "Exit"))
from mplwidget import mplwidget
