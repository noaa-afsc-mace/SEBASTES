# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\WPy64-3740\SEBASTES\application\dialogs\ui\CalibrationDlg.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_calibrationDlg(object):
    def setupUi(self, calibrationDlg):
        calibrationDlg.setObjectName("calibrationDlg")
        calibrationDlg.resize(421, 213)
        self.gridLayout = QtWidgets.QGridLayout(calibrationDlg)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(calibrationDlg)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.calIDBox = QtWidgets.QLineEdit(calibrationDlg)
        self.calIDBox.setObjectName("calIDBox")
        self.gridLayout.addWidget(self.calIDBox, 0, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(calibrationDlg)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 1, 0, 1, 1)
        self.dateTimeBox = QtWidgets.QLineEdit(calibrationDlg)
        self.dateTimeBox.setObjectName("dateTimeBox")
        self.gridLayout.addWidget(self.dateTimeBox, 1, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(calibrationDlg)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.locationBox = QtWidgets.QLineEdit(calibrationDlg)
        self.locationBox.setObjectName("locationBox")
        self.gridLayout.addWidget(self.locationBox, 2, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(calibrationDlg)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)
        self.methodBox = QtWidgets.QComboBox(calibrationDlg)
        self.methodBox.setObjectName("methodBox")
        self.gridLayout.addWidget(self.methodBox, 3, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(calibrationDlg)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 4, 0, 1, 1)
        self.fileBox = QtWidgets.QLineEdit(calibrationDlg)
        self.fileBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.fileBox.setObjectName("fileBox")
        self.gridLayout.addWidget(self.fileBox, 4, 1, 1, 1)
        self.frame = QtWidgets.QFrame(calibrationDlg)
        self.frame.setMinimumSize(QtCore.QSize(0, 40))
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
        self.okBtn = QtWidgets.QPushButton(self.frame)
        self.okBtn.setObjectName("okBtn")
        self.horizontalLayout.addWidget(self.okBtn)
        self.gridLayout.addWidget(self.frame, 5, 0, 1, 3)
        self.browseBtn = QtWidgets.QToolButton(calibrationDlg)
        self.browseBtn.setObjectName("browseBtn")
        self.gridLayout.addWidget(self.browseBtn, 4, 2, 1, 1)

        self.retranslateUi(calibrationDlg)
        QtCore.QMetaObject.connectSlotsByName(calibrationDlg)

    def retranslateUi(self, calibrationDlg):
        _translate = QtCore.QCoreApplication.translate
        calibrationDlg.setWindowTitle(_translate("calibrationDlg", "Calibration"))
        self.label.setText(_translate("calibrationDlg", "Calibration_ID"))
        self.label_8.setText(_translate("calibrationDlg", "Date and Time"))
        self.label_2.setText(_translate("calibrationDlg", "Location"))
        self.label_3.setText(_translate("calibrationDlg", "Method"))
        self.label_4.setText(_translate("calibrationDlg", "File location"))
        self.cancelBtn.setText(_translate("calibrationDlg", "cancel"))
        self.okBtn.setText(_translate("calibrationDlg", "OK"))
        self.browseBtn.setText(_translate("calibrationDlg", "browse ..."))
