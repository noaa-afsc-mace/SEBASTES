# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\SEBASTES\SEBASTES_development\SEBASTES\application\dialogs\ui\ProfileSetupDlg.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_profileSetupDlg(object):
    def setupUi(self, profileSetupDlg):
        profileSetupDlg.setObjectName("profileSetupDlg")
        profileSetupDlg.resize(649, 652)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(profileSetupDlg)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tabWidget = QtWidgets.QTabWidget(profileSetupDlg)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.newProfileBtn = QtWidgets.QPushButton(self.tab)
        self.newProfileBtn.setObjectName("newProfileBtn")
        self.horizontalLayout_2.addWidget(self.newProfileBtn)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.label_28 = QtWidgets.QLabel(self.tab)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_28.setFont(font)
        self.label_28.setObjectName("label_28")
        self.horizontalLayout_2.addWidget(self.label_28)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.selectProfileBtn = QtWidgets.QPushButton(self.tab)
        self.selectProfileBtn.setObjectName("selectProfileBtn")
        self.horizontalLayout_2.addWidget(self.selectProfileBtn)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.profileFrame = QtWidgets.QFrame(self.tab)
        self.profileFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.profileFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.profileFrame.setObjectName("profileFrame")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.profileFrame)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.timestampFormatEdit = QtWidgets.QLineEdit(self.profileFrame)
        self.timestampFormatEdit.setObjectName("timestampFormatEdit")
        self.horizontalLayout_19.addWidget(self.timestampFormatEdit)
        self.timestampFormatBtn = QtWidgets.QPushButton(self.profileFrame)
        self.timestampFormatBtn.setMaximumSize(QtCore.QSize(31, 16777215))
        self.timestampFormatBtn.setObjectName("timestampFormatBtn")
        self.horizontalLayout_19.addWidget(self.timestampFormatBtn)
        self.gridLayout.addLayout(self.horizontalLayout_19, 7, 2, 1, 1)
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.rightCamPathEdit = QtWidgets.QLineEdit(self.profileFrame)
        self.rightCamPathEdit.setObjectName("rightCamPathEdit")
        self.horizontalLayout_17.addWidget(self.rightCamPathEdit)
        self.gridLayout.addLayout(self.horizontalLayout_17, 3, 2, 1, 1)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.rotateLeftBox = QtWidgets.QComboBox(self.profileFrame)
        self.rotateLeftBox.setObjectName("rotateLeftBox")
        self.horizontalLayout_6.addWidget(self.rotateLeftBox)
        self.label_12 = QtWidgets.QLabel(self.profileFrame)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_6.addWidget(self.label_12)
        self.gridLayout.addLayout(self.horizontalLayout_6, 10, 2, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.profileFrame)
        self.label_13.setObjectName("label_13")
        self.gridLayout.addWidget(self.label_13, 11, 0, 1, 1)
        self.label_30 = QtWidgets.QLabel(self.profileFrame)
        self.label_30.setObjectName("label_30")
        self.gridLayout.addWidget(self.label_30, 8, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.profileFrame)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.rotateRightBox = QtWidgets.QComboBox(self.profileFrame)
        self.rotateRightBox.setObjectName("rotateRightBox")
        self.horizontalLayout_7.addWidget(self.rotateRightBox)
        self.label_14 = QtWidgets.QLabel(self.profileFrame)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_7.addWidget(self.label_14)
        self.gridLayout.addLayout(self.horizontalLayout_7, 11, 2, 1, 1)
        self.timestampStartEdit = QtWidgets.QLineEdit(self.profileFrame)
        self.timestampStartEdit.setObjectName("timestampStartEdit")
        self.gridLayout.addWidget(self.timestampStartEdit, 8, 2, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.profileFrame)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.profileFrame)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 6, 0, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.profileFrame)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 9, 0, 1, 1)
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.calFilePathEdit = QtWidgets.QLineEdit(self.profileFrame)
        self.calFilePathEdit.setObjectName("calFilePathEdit")
        self.horizontalLayout_18.addWidget(self.calFilePathEdit)
        self.gridLayout.addLayout(self.horizontalLayout_18, 4, 2, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.profileFrame)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 4, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.profileFrame)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 7, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.profileFrame)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)
        self.profileDescriptionEdit = QtWidgets.QLineEdit(self.profileFrame)
        self.profileDescriptionEdit.setObjectName("profileDescriptionEdit")
        self.gridLayout.addWidget(self.profileDescriptionEdit, 1, 2, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.profileFrame)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 5, 0, 1, 1)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.leftCamPathEdit = QtWidgets.QLineEdit(self.profileFrame)
        self.leftCamPathEdit.setObjectName("leftCamPathEdit")
        self.horizontalLayout_10.addWidget(self.leftCamPathEdit)
        self.gridLayout.addLayout(self.horizontalLayout_10, 2, 2, 1, 1)
        self.timestampTypeBox = QtWidgets.QComboBox(self.profileFrame)
        self.timestampTypeBox.setObjectName("timestampTypeBox")
        self.gridLayout.addWidget(self.timestampTypeBox, 6, 2, 1, 1)
        self.profileNameEdit = QtWidgets.QLineEdit(self.profileFrame)
        self.profileNameEdit.setObjectName("profileNameEdit")
        self.gridLayout.addWidget(self.profileNameEdit, 0, 2, 1, 1)
        self.label = QtWidgets.QLabel(self.profileFrame)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.profileFrame)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 10, 0, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.stFrameIndEdit = QtWidgets.QLineEdit(self.profileFrame)
        self.stFrameIndEdit.setObjectName("stFrameIndEdit")
        self.horizontalLayout_4.addWidget(self.stFrameIndEdit)
        self.label_8 = QtWidgets.QLabel(self.profileFrame)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_4.addWidget(self.label_8)
        self.endFrameIndEdit = QtWidgets.QLineEdit(self.profileFrame)
        self.endFrameIndEdit.setObjectName("endFrameIndEdit")
        self.horizontalLayout_4.addWidget(self.endFrameIndEdit)
        self.frameIndHelpBtn = QtWidgets.QPushButton(self.profileFrame)
        self.frameIndHelpBtn.setMaximumSize(QtCore.QSize(31, 16777215))
        self.frameIndHelpBtn.setObjectName("frameIndHelpBtn")
        self.horizontalLayout_4.addWidget(self.frameIndHelpBtn)
        self.gridLayout.addLayout(self.horizontalLayout_4, 5, 2, 1, 1)
        self.metadataInfoBox = QtWidgets.QGroupBox(self.profileFrame)
        self.metadataInfoBox.setTitle("")
        self.metadataInfoBox.setObjectName("metadataInfoBox")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.metadataInfoBox)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.metadataYesBtn = QtWidgets.QRadioButton(self.metadataInfoBox)
        self.metadataYesBtn.setObjectName("metadataYesBtn")
        self.horizontalLayout_5.addWidget(self.metadataYesBtn)
        self.metadataNoBtn = QtWidgets.QRadioButton(self.metadataInfoBox)
        self.metadataNoBtn.setObjectName("metadataNoBtn")
        self.horizontalLayout_5.addWidget(self.metadataNoBtn)
        self.gridLayout.addWidget(self.metadataInfoBox, 9, 2, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.profileFrame)
        self.label_15.setObjectName("label_15")
        self.gridLayout.addWidget(self.label_15, 12, 0, 1, 1)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.subsampleMaskEdit = QtWidgets.QLineEdit(self.profileFrame)
        self.subsampleMaskEdit.setObjectName("subsampleMaskEdit")
        self.horizontalLayout_12.addWidget(self.subsampleMaskEdit)
        self.subsampleMaskBtn = QtWidgets.QPushButton(self.profileFrame)
        self.subsampleMaskBtn.setMaximumSize(QtCore.QSize(31, 16777215))
        self.subsampleMaskBtn.setObjectName("subsampleMaskBtn")
        self.horizontalLayout_12.addWidget(self.subsampleMaskBtn)
        self.gridLayout.addLayout(self.horizontalLayout_12, 12, 2, 1, 1)
        self.verticalLayout_11.addLayout(self.gridLayout)
        self.verticalLayout.addWidget(self.profileFrame)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.tab_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.newSpcCollectionBtn = QtWidgets.QPushButton(self.tab_2)
        self.newSpcCollectionBtn.setObjectName("newSpcCollectionBtn")
        self.horizontalLayout_3.addWidget(self.newSpcCollectionBtn)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.label_18 = QtWidgets.QLabel(self.tab_2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_18.setFont(font)
        self.label_18.setAlignment(QtCore.Qt.AlignCenter)
        self.label_18.setObjectName("label_18")
        self.horizontalLayout_3.addWidget(self.label_18)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.selectSpcCollectionBtn = QtWidgets.QPushButton(self.tab_2)
        self.selectSpcCollectionBtn.setObjectName("selectSpcCollectionBtn")
        self.horizontalLayout_3.addWidget(self.selectSpcCollectionBtn)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.speciesFrame = QtWidgets.QFrame(self.tab_2)
        self.speciesFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.speciesFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.speciesFrame.setObjectName("speciesFrame")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.speciesFrame)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.formLayout_3 = QtWidgets.QFormLayout()
        self.formLayout_3.setContentsMargins(-1, -1, -1, 10)
        self.formLayout_3.setObjectName("formLayout_3")
        self.label_17 = QtWidgets.QLabel(self.speciesFrame)
        self.label_17.setObjectName("label_17")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_17)
        self.label_27 = QtWidgets.QLabel(self.speciesFrame)
        self.label_27.setObjectName("label_27")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_27)
        self.spcCollectionNameEdit = QtWidgets.QLineEdit(self.speciesFrame)
        self.spcCollectionNameEdit.setObjectName("spcCollectionNameEdit")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.spcCollectionNameEdit)
        self.spcCollectionDescEdit = QtWidgets.QTextEdit(self.speciesFrame)
        self.spcCollectionDescEdit.setObjectName("spcCollectionDescEdit")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.spcCollectionDescEdit)
        self.verticalLayout_5.addLayout(self.formLayout_3)
        self.speciesView = QtWidgets.QTableView(self.speciesFrame)
        self.speciesView.setMinimumSize(QtCore.QSize(0, 351))
        self.speciesView.setObjectName("speciesView")
        self.verticalLayout_5.addWidget(self.speciesView)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem4)
        self.speciesInsertBtn = QtWidgets.QPushButton(self.speciesFrame)
        self.speciesInsertBtn.setObjectName("speciesInsertBtn")
        self.horizontalLayout_8.addWidget(self.speciesInsertBtn)
        self.speciesEditBtn = QtWidgets.QPushButton(self.speciesFrame)
        self.speciesEditBtn.setObjectName("speciesEditBtn")
        self.horizontalLayout_8.addWidget(self.speciesEditBtn)
        self.speciesDeleteBtn = QtWidgets.QPushButton(self.speciesFrame)
        self.speciesDeleteBtn.setObjectName("speciesDeleteBtn")
        self.horizontalLayout_8.addWidget(self.speciesDeleteBtn)
        self.verticalLayout_5.addLayout(self.horizontalLayout_8)
        self.verticalLayout_3.addWidget(self.speciesFrame)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.tab_3)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.newMetadataGroupBtn = QtWidgets.QPushButton(self.tab_3)
        self.newMetadataGroupBtn.setObjectName("newMetadataGroupBtn")
        self.horizontalLayout_9.addWidget(self.newMetadataGroupBtn)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem5)
        self.label_20 = QtWidgets.QLabel(self.tab_3)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_20.setFont(font)
        self.label_20.setAlignment(QtCore.Qt.AlignCenter)
        self.label_20.setObjectName("label_20")
        self.horizontalLayout_9.addWidget(self.label_20)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem6)
        self.selectMetadataGroupBtn = QtWidgets.QPushButton(self.tab_3)
        self.selectMetadataGroupBtn.setObjectName("selectMetadataGroupBtn")
        self.horizontalLayout_9.addWidget(self.selectMetadataGroupBtn)
        self.verticalLayout_4.addLayout(self.horizontalLayout_9)
        self.metadataFrame = QtWidgets.QFrame(self.tab_3)
        self.metadataFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.metadataFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.metadataFrame.setObjectName("metadataFrame")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.metadataFrame)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.formLayout_4 = QtWidgets.QFormLayout()
        self.formLayout_4.setContentsMargins(-1, -1, -1, 10)
        self.formLayout_4.setObjectName("formLayout_4")
        self.label_19 = QtWidgets.QLabel(self.metadataFrame)
        self.label_19.setObjectName("label_19")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_19)
        self.label_29 = QtWidgets.QLabel(self.metadataFrame)
        self.label_29.setObjectName("label_29")
        self.formLayout_4.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_29)
        self.metadataGroupEdit = QtWidgets.QLineEdit(self.metadataFrame)
        self.metadataGroupEdit.setObjectName("metadataGroupEdit")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.metadataGroupEdit)
        self.metadataGroupDescEdit = QtWidgets.QTextEdit(self.metadataFrame)
        self.metadataGroupDescEdit.setObjectName("metadataGroupDescEdit")
        self.formLayout_4.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.metadataGroupDescEdit)
        self.verticalLayout_10.addLayout(self.formLayout_4)
        self.metadataView = QtWidgets.QTableView(self.metadataFrame)
        self.metadataView.setMinimumSize(QtCore.QSize(0, 351))
        self.metadataView.setObjectName("metadataView")
        self.verticalLayout_10.addWidget(self.metadataView)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem7)
        self.metadataInsertBtn = QtWidgets.QPushButton(self.metadataFrame)
        self.metadataInsertBtn.setObjectName("metadataInsertBtn")
        self.horizontalLayout_11.addWidget(self.metadataInsertBtn)
        self.metadataEditBtn = QtWidgets.QPushButton(self.metadataFrame)
        self.metadataEditBtn.setObjectName("metadataEditBtn")
        self.horizontalLayout_11.addWidget(self.metadataEditBtn)
        self.metadataDeleteBtn = QtWidgets.QPushButton(self.metadataFrame)
        self.metadataDeleteBtn.setObjectName("metadataDeleteBtn")
        self.horizontalLayout_11.addWidget(self.metadataDeleteBtn)
        self.verticalLayout_10.addLayout(self.horizontalLayout_11)
        self.verticalLayout_4.addWidget(self.metadataFrame)
        self.tabWidget.addTab(self.tab_3, "")
        self.verticalLayout_2.addWidget(self.tabWidget)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.reloadBtn = QtWidgets.QPushButton(profileSetupDlg)
        self.reloadBtn.setObjectName("reloadBtn")
        self.horizontalLayout.addWidget(self.reloadBtn)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem8)
        self.cancelBtn = QtWidgets.QPushButton(profileSetupDlg)
        self.cancelBtn.setObjectName("cancelBtn")
        self.horizontalLayout.addWidget(self.cancelBtn)
        self.saveBtn = QtWidgets.QPushButton(profileSetupDlg)
        self.saveBtn.setObjectName("saveBtn")
        self.horizontalLayout.addWidget(self.saveBtn)
        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.retranslateUi(profileSetupDlg)
        self.tabWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(profileSetupDlg)
        profileSetupDlg.setTabOrder(self.tabWidget, self.newProfileBtn)
        profileSetupDlg.setTabOrder(self.newProfileBtn, self.selectProfileBtn)
        profileSetupDlg.setTabOrder(self.selectProfileBtn, self.profileNameEdit)
        profileSetupDlg.setTabOrder(self.profileNameEdit, self.profileDescriptionEdit)
        profileSetupDlg.setTabOrder(self.profileDescriptionEdit, self.leftCamPathEdit)
        profileSetupDlg.setTabOrder(self.leftCamPathEdit, self.rightCamPathEdit)
        profileSetupDlg.setTabOrder(self.rightCamPathEdit, self.calFilePathEdit)
        profileSetupDlg.setTabOrder(self.calFilePathEdit, self.stFrameIndEdit)
        profileSetupDlg.setTabOrder(self.stFrameIndEdit, self.endFrameIndEdit)
        profileSetupDlg.setTabOrder(self.endFrameIndEdit, self.timestampTypeBox)
        profileSetupDlg.setTabOrder(self.timestampTypeBox, self.timestampFormatEdit)
        profileSetupDlg.setTabOrder(self.timestampFormatEdit, self.timestampStartEdit)
        profileSetupDlg.setTabOrder(self.timestampStartEdit, self.metadataYesBtn)
        profileSetupDlg.setTabOrder(self.metadataYesBtn, self.metadataNoBtn)
        profileSetupDlg.setTabOrder(self.metadataNoBtn, self.rotateLeftBox)
        profileSetupDlg.setTabOrder(self.rotateLeftBox, self.rotateRightBox)
        profileSetupDlg.setTabOrder(self.rotateRightBox, self.timestampFormatBtn)
        profileSetupDlg.setTabOrder(self.timestampFormatBtn, self.newSpcCollectionBtn)
        profileSetupDlg.setTabOrder(self.newSpcCollectionBtn, self.selectSpcCollectionBtn)
        profileSetupDlg.setTabOrder(self.selectSpcCollectionBtn, self.frameIndHelpBtn)
        profileSetupDlg.setTabOrder(self.frameIndHelpBtn, self.spcCollectionNameEdit)
        profileSetupDlg.setTabOrder(self.spcCollectionNameEdit, self.spcCollectionDescEdit)
        profileSetupDlg.setTabOrder(self.spcCollectionDescEdit, self.speciesView)
        profileSetupDlg.setTabOrder(self.speciesView, self.speciesInsertBtn)
        profileSetupDlg.setTabOrder(self.speciesInsertBtn, self.speciesEditBtn)
        profileSetupDlg.setTabOrder(self.speciesEditBtn, self.speciesDeleteBtn)
        profileSetupDlg.setTabOrder(self.speciesDeleteBtn, self.newMetadataGroupBtn)
        profileSetupDlg.setTabOrder(self.newMetadataGroupBtn, self.selectMetadataGroupBtn)
        profileSetupDlg.setTabOrder(self.selectMetadataGroupBtn, self.metadataGroupEdit)
        profileSetupDlg.setTabOrder(self.metadataGroupEdit, self.metadataGroupDescEdit)
        profileSetupDlg.setTabOrder(self.metadataGroupDescEdit, self.metadataView)
        profileSetupDlg.setTabOrder(self.metadataView, self.metadataInsertBtn)
        profileSetupDlg.setTabOrder(self.metadataInsertBtn, self.metadataEditBtn)
        profileSetupDlg.setTabOrder(self.metadataEditBtn, self.metadataDeleteBtn)
        profileSetupDlg.setTabOrder(self.metadataDeleteBtn, self.cancelBtn)
        profileSetupDlg.setTabOrder(self.cancelBtn, self.saveBtn)

    def retranslateUi(self, profileSetupDlg):
        _translate = QtCore.QCoreApplication.translate
        profileSetupDlg.setWindowTitle(_translate("profileSetupDlg", "Setup profiles"))
        self.newProfileBtn.setText(_translate("profileSetupDlg", "Create New Profile"))
        self.label_28.setText(_translate("profileSetupDlg", "or"))
        self.selectProfileBtn.setText(_translate("profileSetupDlg", "Select Existing Profile"))
        self.timestampFormatBtn.setText(_translate("profileSetupDlg", "?"))
        self.label_12.setText(_translate("profileSetupDlg", "degrees"))
        self.label_13.setText(_translate("profileSetupDlg", "RotateRightImage"))
        self.label_30.setText(_translate("profileSetupDlg", "ImageTimestampStart"))
        self.label_2.setText(_translate("profileSetupDlg", "Profile description"))
        self.label_14.setText(_translate("profileSetupDlg", "degrees"))
        self.label_4.setText(_translate("profileSetupDlg", "RightCameraImagePath"))
        self.label_6.setText(_translate("profileSetupDlg", "ImageTimestampType"))
        self.label_10.setText(_translate("profileSetupDlg", "CollectMetadata"))
        self.label_9.setText(_translate("profileSetupDlg", "CalibrationFileName"))
        self.label_7.setText(_translate("profileSetupDlg", "ImageTimestampFormat"))
        self.label_3.setText(_translate("profileSetupDlg", "Profile name"))
        self.label_5.setText(_translate("profileSetupDlg", "FrameNumberIndices"))
        self.label.setText(_translate("profileSetupDlg", "LeftCameraImagePath"))
        self.label_11.setText(_translate("profileSetupDlg", "RotateLeftImage"))
        self.label_8.setText(_translate("profileSetupDlg", "to"))
        self.frameIndHelpBtn.setText(_translate("profileSetupDlg", "?"))
        self.metadataYesBtn.setText(_translate("profileSetupDlg", "Yes"))
        self.metadataNoBtn.setText(_translate("profileSetupDlg", "No"))
        self.label_15.setText(_translate("profileSetupDlg", "SubsampleMask"))
        self.subsampleMaskBtn.setText(_translate("profileSetupDlg", "?"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("profileSetupDlg", "Profiles"))
        self.newSpcCollectionBtn.setText(_translate("profileSetupDlg", "Create new \n"
" Species Collection"))
        self.label_18.setText(_translate("profileSetupDlg", "or"))
        self.selectSpcCollectionBtn.setText(_translate("profileSetupDlg", "Select Existing\n"
" Species Collection"))
        self.label_17.setText(_translate("profileSetupDlg", "Species Collection Name"))
        self.label_27.setText(_translate("profileSetupDlg", "Species Collection Description"))
        self.speciesInsertBtn.setText(_translate("profileSetupDlg", "Insert"))
        self.speciesEditBtn.setText(_translate("profileSetupDlg", "Edit"))
        self.speciesDeleteBtn.setText(_translate("profileSetupDlg", "Delete"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("profileSetupDlg", "Species Collections"))
        self.newMetadataGroupBtn.setText(_translate("profileSetupDlg", "Create new \n"
" Metadata Group"))
        self.label_20.setText(_translate("profileSetupDlg", "or"))
        self.selectMetadataGroupBtn.setText(_translate("profileSetupDlg", "Select Existing \n"
"Metadata Group"))
        self.label_19.setText(_translate("profileSetupDlg", "Metadata Group"))
        self.label_29.setText(_translate("profileSetupDlg", " Description"))
        self.metadataInsertBtn.setText(_translate("profileSetupDlg", "Insert"))
        self.metadataEditBtn.setText(_translate("profileSetupDlg", "Edit"))
        self.metadataDeleteBtn.setText(_translate("profileSetupDlg", "Delete"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("profileSetupDlg", "Metadata Groups"))
        self.reloadBtn.setText(_translate("profileSetupDlg", "Reload deployment with new profile"))
        self.cancelBtn.setText(_translate("profileSetupDlg", "Cancel"))
        self.saveBtn.setText(_translate("profileSetupDlg", "Save changes"))
