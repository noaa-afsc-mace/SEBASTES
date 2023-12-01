# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\WPy64-3740\SEBASTES\application\dialogs\ui\SubsampleMaskHelpDlg.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_subsampleMaskHelpDlg(object):
    def setupUi(self, subsampleMaskHelpDlg):
        subsampleMaskHelpDlg.setObjectName("subsampleMaskHelpDlg")
        subsampleMaskHelpDlg.resize(400, 191)
        self.verticalLayout = QtWidgets.QVBoxLayout(subsampleMaskHelpDlg)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(subsampleMaskHelpDlg)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.okBtn = QtWidgets.QPushButton(subsampleMaskHelpDlg)
        self.okBtn.setObjectName("okBtn")
        self.horizontalLayout.addWidget(self.okBtn)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(subsampleMaskHelpDlg)
        QtCore.QMetaObject.connectSlotsByName(subsampleMaskHelpDlg)

    def retranslateUi(self, subsampleMaskHelpDlg):
        _translate = QtCore.QCoreApplication.translate
        subsampleMaskHelpDlg.setWindowTitle(_translate("subsampleMaskHelpDlg", "Subsample Mask Help"))
        self.label.setText(_translate("subsampleMaskHelpDlg", "The Subsample Mask provides an opportunity for a graphical region of interest (ROI) to be drawn on an image to constrain the are where analysis takes place.  it is specified in pixel coordinates.  Four comma separated values are required, indicating the origin x, origin y, rectangle width and rectangle height.  For example, a value of 10,10,100,100 will mask out all areas of the image except a rectangle that starts at pixel x,y position 10,10 (from top left) and that extends 100 pixels in width and height."))
        self.okBtn.setText(_translate("subsampleMaskHelpDlg", "OK"))
