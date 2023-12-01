# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\WPy64-3740\SEBASTES\application\dialogs\ui\TimestampExtractHelpDlg.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_timestampExtractHelpDlg(object):
    def setupUi(self, timestampExtractHelpDlg):
        timestampExtractHelpDlg.setObjectName("timestampExtractHelpDlg")
        timestampExtractHelpDlg.resize(400, 325)
        self.verticalLayout = QtWidgets.QVBoxLayout(timestampExtractHelpDlg)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(timestampExtractHelpDlg)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label_2 = QtWidgets.QLabel(timestampExtractHelpDlg)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.timestampFormat = QtWidgets.QLineEdit(timestampExtractHelpDlg)
        self.timestampFormat.setObjectName("timestampFormat")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.timestampFormat)
        self.label_3 = QtWidgets.QLabel(timestampExtractHelpDlg)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.timestampStartIndex = QtWidgets.QLineEdit(timestampExtractHelpDlg)
        self.timestampStartIndex.setObjectName("timestampStartIndex")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.timestampStartIndex)
        self.label_4 = QtWidgets.QLabel(timestampExtractHelpDlg)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.filenameEdit = QtWidgets.QLineEdit(timestampExtractHelpDlg)
        self.filenameEdit.setObjectName("filenameEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.filenameEdit)
        self.verticalLayout.addLayout(self.formLayout)
        self.extractBtn = QtWidgets.QPushButton(timestampExtractHelpDlg)
        self.extractBtn.setObjectName("extractBtn")
        self.verticalLayout.addWidget(self.extractBtn)
        self.resultLabel = QtWidgets.QLabel(timestampExtractHelpDlg)
        self.resultLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.resultLabel.setText("")
        self.resultLabel.setObjectName("resultLabel")
        self.verticalLayout.addWidget(self.resultLabel)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.okBtn = QtWidgets.QPushButton(timestampExtractHelpDlg)
        self.okBtn.setObjectName("okBtn")
        self.horizontalLayout.addWidget(self.okBtn)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(timestampExtractHelpDlg)
        QtCore.QMetaObject.connectSlotsByName(timestampExtractHelpDlg)

    def retranslateUi(self, timestampExtractHelpDlg):
        _translate = QtCore.QCoreApplication.translate
        timestampExtractHelpDlg.setWindowTitle(_translate("timestampExtractHelpDlg", "Help Dialog"))
        self.label.setText(_translate("timestampExtractHelpDlg", "To correcly label each frame with the appropriate timestamp, the time has to be known.  It can either be extracted from the image file name, or retrieved from teh image metadate using the EXIV library, which is standard for most image file types such as JPEG. If you want to extract the timestamp from teh name, this dialog can help figure out the format.  It uses Qt standard for designating days, months and times.  For example if the timestamp is 04.05.2020, the timestamp format would be \" dd.MM.yyyy\", and if the time was 13:47:10.234, the time format would be \"hh:mm:ss.zzz\".  To test timestamp extraction, paste an example of your image file name (with or without extension) and fill in the format string as well as the staring index  if the time is correctly extracted you will get positive feedback."))
        self.label_2.setText(_translate("timestampExtractHelpDlg", "Date format string"))
        self.label_3.setText(_translate("timestampExtractHelpDlg", "date index start"))
        self.label_4.setText(_translate("timestampExtractHelpDlg", "Filename"))
        self.extractBtn.setText(_translate("timestampExtractHelpDlg", "Extract"))
        self.okBtn.setText(_translate("timestampExtractHelpDlg", "OK"))
