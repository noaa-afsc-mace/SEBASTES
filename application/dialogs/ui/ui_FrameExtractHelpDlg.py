# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\WPy64-3740\SEBASTES\application\dialogs\ui\FrameExtractHelpDlg.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_frameExtractHelpDlg(object):
    def setupUi(self, frameExtractHelpDlg):
        frameExtractHelpDlg.setObjectName("frameExtractHelpDlg")
        frameExtractHelpDlg.resize(400, 238)
        self.verticalLayout = QtWidgets.QVBoxLayout(frameExtractHelpDlg)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(frameExtractHelpDlg)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.filenameEdit = QtWidgets.QLineEdit(frameExtractHelpDlg)
        self.filenameEdit.setObjectName("filenameEdit")
        self.verticalLayout.addWidget(self.filenameEdit)
        self.label_2 = QtWidgets.QLabel(frameExtractHelpDlg)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.startInd = QtWidgets.QLineEdit(frameExtractHelpDlg)
        self.startInd.setObjectName("startInd")
        self.horizontalLayout.addWidget(self.startInd)
        self.label_3 = QtWidgets.QLabel(frameExtractHelpDlg)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.endInd = QtWidgets.QLineEdit(frameExtractHelpDlg)
        self.endInd.setObjectName("endInd")
        self.horizontalLayout.addWidget(self.endInd)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.extractBtn = QtWidgets.QPushButton(frameExtractHelpDlg)
        self.extractBtn.setObjectName("extractBtn")
        self.verticalLayout.addWidget(self.extractBtn)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_4 = QtWidgets.QLabel(frameExtractHelpDlg)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        self.resultLabel = QtWidgets.QLabel(frameExtractHelpDlg)
        self.resultLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.resultLabel.setText("")
        self.resultLabel.setObjectName("resultLabel")
        self.horizontalLayout_2.addWidget(self.resultLabel)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.okBtn = QtWidgets.QPushButton(frameExtractHelpDlg)
        self.okBtn.setObjectName("okBtn")
        self.horizontalLayout_3.addWidget(self.okBtn)
        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.retranslateUi(frameExtractHelpDlg)
        QtCore.QMetaObject.connectSlotsByName(frameExtractHelpDlg)

    def retranslateUi(self, frameExtractHelpDlg):
        _translate = QtCore.QCoreApplication.translate
        frameExtractHelpDlg.setWindowTitle(_translate("frameExtractHelpDlg", "Help Dialog"))
        self.label.setText(_translate("frameExtractHelpDlg", "Frame numbers are extracted from the image file name.  Fo rthis to work they have to be in the same location for each file.  This window helps with setting the indices for the frame number within the name. Please copy and paste the full image name (with or wihtout extension) into the box below."))
        self.label_2.setText(_translate("frameExtractHelpDlg", "Now put the starting and ending values (inclusive) into the two boxes below."))
        self.label_3.setText(_translate("frameExtractHelpDlg", "to"))
        self.extractBtn.setText(_translate("frameExtractHelpDlg", "Extract frame number"))
        self.label_4.setText(_translate("frameExtractHelpDlg", "Result"))
        self.okBtn.setText(_translate("frameExtractHelpDlg", "OK"))
