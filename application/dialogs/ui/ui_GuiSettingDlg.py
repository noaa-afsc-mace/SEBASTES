# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\SEBASTES\SEBASTES_Python-3.7\applications\SEBASTES\application\dialogs\ui\GuiSettingDlg.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_guiSettingDlg(object):
    def setupUi(self, guiSettingDlg):
        guiSettingDlg.setObjectName("guiSettingDlg")
        guiSettingDlg.resize(469, 398)
        self.verticalLayout = QtWidgets.QVBoxLayout(guiSettingDlg)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label_21 = QtWidgets.QLabel(guiSettingDlg)
        self.label_21.setObjectName("label_21")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_21)
        self.measureLineWidthBox = QtWidgets.QComboBox(guiSettingDlg)
        self.measureLineWidthBox.setObjectName("measureLineWidthBox")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.measureLineWidthBox)
        self.label_22 = QtWidgets.QLabel(guiSettingDlg)
        self.label_22.setObjectName("label_22")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_22)
        self.measureLineTailLengthBox = QtWidgets.QComboBox(guiSettingDlg)
        self.measureLineTailLengthBox.setObjectName("measureLineTailLengthBox")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.measureLineTailLengthBox)
        self.label_25 = QtWidgets.QLabel(guiSettingDlg)
        self.label_25.setObjectName("label_25")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_25)
        self.boxLineThicknessBox = QtWidgets.QComboBox(guiSettingDlg)
        self.boxLineThicknessBox.setObjectName("boxLineThicknessBox")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.boxLineThicknessBox)
        self.label_26 = QtWidgets.QLabel(guiSettingDlg)
        self.label_26.setObjectName("label_26")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_26)
        self.labelTextSizeBox = QtWidgets.QComboBox(guiSettingDlg)
        self.labelTextSizeBox.setObjectName("labelTextSizeBox")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.labelTextSizeBox)
        self.label = QtWidgets.QLabel(guiSettingDlg)
        self.label.setObjectName("label")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label)
        self.groupBox = QtWidgets.QGroupBox(guiSettingDlg)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.metaSelRetainRadio = QtWidgets.QRadioButton(self.groupBox)
        self.metaSelRetainRadio.setObjectName("metaSelRetainRadio")
        self.horizontalLayout_2.addWidget(self.metaSelRetainRadio)
        self.metaSelClearRadio = QtWidgets.QRadioButton(self.groupBox)
        self.metaSelClearRadio.setObjectName("metaSelClearRadio")
        self.horizontalLayout_2.addWidget(self.metaSelClearRadio)
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.groupBox)
        self.label_3 = QtWidgets.QLabel(guiSettingDlg)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.groupBox_2 = QtWidgets.QGroupBox(guiSettingDlg)
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.spcSelRetainRadio = QtWidgets.QRadioButton(self.groupBox_2)
        self.spcSelRetainRadio.setObjectName("spcSelRetainRadio")
        self.horizontalLayout_3.addWidget(self.spcSelRetainRadio)
        self.spcSelClearRadio = QtWidgets.QRadioButton(self.groupBox_2)
        self.spcSelClearRadio.setObjectName("spcSelClearRadio")
        self.horizontalLayout_3.addWidget(self.spcSelClearRadio)
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.groupBox_2)
        self.label_2 = QtWidgets.QLabel(guiSettingDlg)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.classLabelCheckBox = QtWidgets.QCheckBox(guiSettingDlg)
        self.classLabelCheckBox.setText("")
        self.classLabelCheckBox.setObjectName("classLabelCheckBox")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.classLabelCheckBox)
        self.label_24 = QtWidgets.QLabel(guiSettingDlg)
        self.label_24.setObjectName("label_24")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.label_24)
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.sceneColorLabel = QtWidgets.QLabel(guiSettingDlg)
        self.sceneColorLabel.setMinimumSize(QtCore.QSize(51, 0))
        self.sceneColorLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.sceneColorLabel.setText("")
        self.sceneColorLabel.setObjectName("sceneColorLabel")
        self.horizontalLayout_15.addWidget(self.sceneColorLabel)
        self.sceneColorBtn = QtWidgets.QPushButton(guiSettingDlg)
        self.sceneColorBtn.setObjectName("sceneColorBtn")
        self.horizontalLayout_15.addWidget(self.sceneColorBtn)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_15.addItem(spacerItem)
        self.formLayout.setLayout(8, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_15)
        self.label_23 = QtWidgets.QLabel(guiSettingDlg)
        self.label_23.setObjectName("label_23")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.LabelRole, self.label_23)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.targetColorLabel = QtWidgets.QLabel(guiSettingDlg)
        self.targetColorLabel.setMinimumSize(QtCore.QSize(51, 0))
        self.targetColorLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.targetColorLabel.setText("")
        self.targetColorLabel.setObjectName("targetColorLabel")
        self.horizontalLayout_14.addWidget(self.targetColorLabel)
        self.targetLineColorBtn = QtWidgets.QPushButton(guiSettingDlg)
        self.targetLineColorBtn.setObjectName("targetLineColorBtn")
        self.horizontalLayout_14.addWidget(self.targetLineColorBtn)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_14.addItem(spacerItem1)
        self.formLayout.setLayout(9, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_14)
        self.label_4 = QtWidgets.QLabel(guiSettingDlg)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.speedAdjLabel = QtWidgets.QLineEdit(guiSettingDlg)
        self.speedAdjLabel.setMaximumSize(QtCore.QSize(51, 16777215))
        self.speedAdjLabel.setObjectName("speedAdjLabel")
        self.horizontalLayout_4.addWidget(self.speedAdjLabel)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.formLayout.setLayout(7, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_4)
        self.verticalLayout.addLayout(self.formLayout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.cancelBtn = QtWidgets.QPushButton(guiSettingDlg)
        self.cancelBtn.setObjectName("cancelBtn")
        self.horizontalLayout.addWidget(self.cancelBtn)
        self.saveBtn = QtWidgets.QPushButton(guiSettingDlg)
        self.saveBtn.setObjectName("saveBtn")
        self.horizontalLayout.addWidget(self.saveBtn)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(guiSettingDlg)
        QtCore.QMetaObject.connectSlotsByName(guiSettingDlg)

    def retranslateUi(self, guiSettingDlg):
        _translate = QtCore.QCoreApplication.translate
        guiSettingDlg.setWindowTitle(_translate("guiSettingDlg", "GUI Settings"))
        self.label_21.setText(_translate("guiSettingDlg", "MeasureLineWidth"))
        self.label_22.setText(_translate("guiSettingDlg", "MeasureLineTailLength"))
        self.label_25.setText(_translate("guiSettingDlg", "BoxLineThickness"))
        self.label_26.setText(_translate("guiSettingDlg", "LabelTextSize"))
        self.label.setText(_translate("guiSettingDlg", "DefaultMetadataSelection"))
        self.metaSelRetainRadio.setText(_translate("guiSettingDlg", "Retain Selection"))
        self.metaSelClearRadio.setText(_translate("guiSettingDlg", "Clear Selection"))
        self.label_3.setText(_translate("guiSettingDlg", "RetainSpeciesSelection"))
        self.spcSelRetainRadio.setText(_translate("guiSettingDlg", "Retain Selection"))
        self.spcSelClearRadio.setText(_translate("guiSettingDlg", "Clear Selection"))
        self.label_2.setText(_translate("guiSettingDlg", "ShowClassOnLabel"))
        self.label_24.setText(_translate("guiSettingDlg", "SceneColor"))
        self.sceneColorBtn.setText(_translate("guiSettingDlg", "Select color"))
        self.label_23.setText(_translate("guiSettingDlg", "TargetLineColor"))
        self.targetLineColorBtn.setText(_translate("guiSettingDlg", "Select color"))
        self.label_4.setText(_translate("guiSettingDlg", "Playback scale"))
        self.cancelBtn.setText(_translate("guiSettingDlg", "Cancel"))
        self.saveBtn.setText(_translate("guiSettingDlg", "Save"))