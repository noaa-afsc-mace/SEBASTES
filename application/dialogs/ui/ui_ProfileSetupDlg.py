# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ProfileSetupDlg.ui'
##
## Created by: Qt User Interface Compiler version 6.11.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QFormLayout,
    QFrame, QGridLayout, QGroupBox, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QPushButton,
    QRadioButton, QSizePolicy, QSpacerItem, QTabWidget,
    QTableView, QTextEdit, QVBoxLayout, QWidget)

class Ui_profileSetupDlg(object):
    def setupUi(self, profileSetupDlg):
        if not profileSetupDlg.objectName():
            profileSetupDlg.setObjectName(u"profileSetupDlg")
        profileSetupDlg.resize(649, 728)
        self.verticalLayout_2 = QVBoxLayout(profileSetupDlg)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.tabWidget = QTabWidget(profileSetupDlg)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout = QVBoxLayout(self.tab)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.newProfileBtn = QPushButton(self.tab)
        self.newProfileBtn.setObjectName(u"newProfileBtn")

        self.horizontalLayout_2.addWidget(self.newProfileBtn)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_8)

        self.label_28 = QLabel(self.tab)
        self.label_28.setObjectName(u"label_28")
        font = QFont()
        font.setBold(True)
        self.label_28.setFont(font)

        self.horizontalLayout_2.addWidget(self.label_28)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_9)

        self.selectProfileBtn = QPushButton(self.tab)
        self.selectProfileBtn.setObjectName(u"selectProfileBtn")

        self.horizontalLayout_2.addWidget(self.selectProfileBtn)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.profileFrame = QFrame(self.tab)
        self.profileFrame.setObjectName(u"profileFrame")
        self.profileFrame.setFrameShape(QFrame.StyledPanel)
        self.profileFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.profileFrame)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(self.profileFrame)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)

        self.label_7 = QLabel(self.profileFrame)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout.addWidget(self.label_7, 7, 0, 1, 1)

        self.timestampStartEdit = QLineEdit(self.profileFrame)
        self.timestampStartEdit.setObjectName(u"timestampStartEdit")

        self.gridLayout.addWidget(self.timestampStartEdit, 8, 2, 1, 1)

        self.profileDescriptionEdit = QLineEdit(self.profileFrame)
        self.profileDescriptionEdit.setObjectName(u"profileDescriptionEdit")

        self.gridLayout.addWidget(self.profileDescriptionEdit, 1, 2, 1, 1)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.rightCamPathEdit = QLineEdit(self.profileFrame)
        self.rightCamPathEdit.setObjectName(u"rightCamPathEdit")

        self.horizontalLayout_17.addWidget(self.rightCamPathEdit)


        self.gridLayout.addLayout(self.horizontalLayout_17, 3, 2, 1, 1)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.leftCamPathEdit = QLineEdit(self.profileFrame)
        self.leftCamPathEdit.setObjectName(u"leftCamPathEdit")

        self.horizontalLayout_10.addWidget(self.leftCamPathEdit)


        self.gridLayout.addLayout(self.horizontalLayout_10, 2, 2, 1, 1)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.rotateLeftBox = QComboBox(self.profileFrame)
        self.rotateLeftBox.setObjectName(u"rotateLeftBox")

        self.horizontalLayout_6.addWidget(self.rotateLeftBox)

        self.label_12 = QLabel(self.profileFrame)
        self.label_12.setObjectName(u"label_12")

        self.horizontalLayout_6.addWidget(self.label_12)


        self.gridLayout.addLayout(self.horizontalLayout_6, 11, 2, 1, 1)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.subsampleMaskEdit = QLineEdit(self.profileFrame)
        self.subsampleMaskEdit.setObjectName(u"subsampleMaskEdit")

        self.horizontalLayout_12.addWidget(self.subsampleMaskEdit)

        self.subsampleMaskBtn = QPushButton(self.profileFrame)
        self.subsampleMaskBtn.setObjectName(u"subsampleMaskBtn")
        self.subsampleMaskBtn.setMaximumSize(QSize(31, 16777215))

        self.horizontalLayout_12.addWidget(self.subsampleMaskBtn)


        self.gridLayout.addLayout(self.horizontalLayout_12, 13, 2, 1, 1)

        self.label_5 = QLabel(self.profileFrame)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 5, 0, 1, 1)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.timestampFormatEdit = QLineEdit(self.profileFrame)
        self.timestampFormatEdit.setObjectName(u"timestampFormatEdit")

        self.horizontalLayout_19.addWidget(self.timestampFormatEdit)

        self.timestampFormatBtn = QPushButton(self.profileFrame)
        self.timestampFormatBtn.setObjectName(u"timestampFormatBtn")
        self.timestampFormatBtn.setMaximumSize(QSize(31, 16777215))

        self.horizontalLayout_19.addWidget(self.timestampFormatBtn)


        self.gridLayout.addLayout(self.horizontalLayout_19, 7, 2, 1, 1)

        self.timestampTypeBox = QComboBox(self.profileFrame)
        self.timestampTypeBox.setObjectName(u"timestampTypeBox")

        self.gridLayout.addWidget(self.timestampTypeBox, 6, 2, 1, 1)

        self.label_13 = QLabel(self.profileFrame)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout.addWidget(self.label_13, 12, 0, 1, 1)

        self.label_9 = QLabel(self.profileFrame)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout.addWidget(self.label_9, 4, 0, 1, 1)

        self.label_4 = QLabel(self.profileFrame)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)

        self.metadataInfoBox = QGroupBox(self.profileFrame)
        self.metadataInfoBox.setObjectName(u"metadataInfoBox")
        self.horizontalLayout_5 = QHBoxLayout(self.metadataInfoBox)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.metadataYesBtn = QRadioButton(self.metadataInfoBox)
        self.metadataYesBtn.setObjectName(u"metadataYesBtn")

        self.horizontalLayout_5.addWidget(self.metadataYesBtn)

        self.metadataNoBtn = QRadioButton(self.metadataInfoBox)
        self.metadataNoBtn.setObjectName(u"metadataNoBtn")

        self.horizontalLayout_5.addWidget(self.metadataNoBtn)


        self.gridLayout.addWidget(self.metadataInfoBox, 10, 2, 1, 1)

        self.label_15 = QLabel(self.profileFrame)
        self.label_15.setObjectName(u"label_15")

        self.gridLayout.addWidget(self.label_15, 13, 0, 1, 1)

        self.label_30 = QLabel(self.profileFrame)
        self.label_30.setObjectName(u"label_30")

        self.gridLayout.addWidget(self.label_30, 8, 0, 1, 1)

        self.label_2 = QLabel(self.profileFrame)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.profileNameEdit = QLineEdit(self.profileFrame)
        self.profileNameEdit.setObjectName(u"profileNameEdit")

        self.gridLayout.addWidget(self.profileNameEdit, 0, 2, 1, 1)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.stFrameIndEdit = QLineEdit(self.profileFrame)
        self.stFrameIndEdit.setObjectName(u"stFrameIndEdit")

        self.horizontalLayout_4.addWidget(self.stFrameIndEdit)

        self.label_8 = QLabel(self.profileFrame)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_4.addWidget(self.label_8)

        self.endFrameIndEdit = QLineEdit(self.profileFrame)
        self.endFrameIndEdit.setObjectName(u"endFrameIndEdit")

        self.horizontalLayout_4.addWidget(self.endFrameIndEdit)

        self.frameIndHelpBtn = QPushButton(self.profileFrame)
        self.frameIndHelpBtn.setObjectName(u"frameIndHelpBtn")
        self.frameIndHelpBtn.setMaximumSize(QSize(31, 16777215))

        self.horizontalLayout_4.addWidget(self.frameIndHelpBtn)


        self.gridLayout.addLayout(self.horizontalLayout_4, 5, 2, 1, 1)

        self.label_3 = QLabel(self.profileFrame)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)

        self.label_10 = QLabel(self.profileFrame)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout.addWidget(self.label_10, 10, 0, 1, 1)

        self.label_11 = QLabel(self.profileFrame)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout.addWidget(self.label_11, 11, 0, 1, 1)

        self.label_6 = QLabel(self.profileFrame)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 6, 0, 1, 1)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.rotateRightBox = QComboBox(self.profileFrame)
        self.rotateRightBox.setObjectName(u"rotateRightBox")

        self.horizontalLayout_7.addWidget(self.rotateRightBox)

        self.label_14 = QLabel(self.profileFrame)
        self.label_14.setObjectName(u"label_14")

        self.horizontalLayout_7.addWidget(self.label_14)


        self.gridLayout.addLayout(self.horizontalLayout_7, 12, 2, 1, 1)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.calFilePathEdit = QLineEdit(self.profileFrame)
        self.calFilePathEdit.setObjectName(u"calFilePathEdit")

        self.horizontalLayout_18.addWidget(self.calFilePathEdit)


        self.gridLayout.addLayout(self.horizontalLayout_18, 4, 2, 1, 1)

        self.label_16 = QLabel(self.profileFrame)
        self.label_16.setObjectName(u"label_16")

        self.gridLayout.addWidget(self.label_16, 9, 0, 1, 1)

        self.imageTypeEdit = QLineEdit(self.profileFrame)
        self.imageTypeEdit.setObjectName(u"imageTypeEdit")

        self.gridLayout.addWidget(self.imageTypeEdit, 9, 2, 1, 1)


        self.verticalLayout_11.addLayout(self.gridLayout)


        self.verticalLayout.addWidget(self.profileFrame)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_3 = QVBoxLayout(self.tab_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.newSpcCollectionBtn = QPushButton(self.tab_2)
        self.newSpcCollectionBtn.setObjectName(u"newSpcCollectionBtn")

        self.horizontalLayout_3.addWidget(self.newSpcCollectionBtn)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_10)

        self.label_18 = QLabel(self.tab_2)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setFont(font)
        self.label_18.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_18)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_11)

        self.selectSpcCollectionBtn = QPushButton(self.tab_2)
        self.selectSpcCollectionBtn.setObjectName(u"selectSpcCollectionBtn")

        self.horizontalLayout_3.addWidget(self.selectSpcCollectionBtn)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.speciesFrame = QFrame(self.tab_2)
        self.speciesFrame.setObjectName(u"speciesFrame")
        self.speciesFrame.setFrameShape(QFrame.StyledPanel)
        self.speciesFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.speciesFrame)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.formLayout_3 = QFormLayout()
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.formLayout_3.setContentsMargins(-1, -1, -1, 10)
        self.label_17 = QLabel(self.speciesFrame)
        self.label_17.setObjectName(u"label_17")

        self.formLayout_3.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_17)

        self.label_27 = QLabel(self.speciesFrame)
        self.label_27.setObjectName(u"label_27")

        self.formLayout_3.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_27)

        self.spcCollectionNameEdit = QLineEdit(self.speciesFrame)
        self.spcCollectionNameEdit.setObjectName(u"spcCollectionNameEdit")

        self.formLayout_3.setWidget(0, QFormLayout.ItemRole.FieldRole, self.spcCollectionNameEdit)

        self.spcCollectionDescEdit = QTextEdit(self.speciesFrame)
        self.spcCollectionDescEdit.setObjectName(u"spcCollectionDescEdit")

        self.formLayout_3.setWidget(1, QFormLayout.ItemRole.FieldRole, self.spcCollectionDescEdit)


        self.verticalLayout_5.addLayout(self.formLayout_3)

        self.speciesView = QTableView(self.speciesFrame)
        self.speciesView.setObjectName(u"speciesView")
        self.speciesView.setMinimumSize(QSize(0, 351))

        self.verticalLayout_5.addWidget(self.speciesView)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(-1, -1, -1, 0)
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_2)

        self.speciesInsertBtn = QPushButton(self.speciesFrame)
        self.speciesInsertBtn.setObjectName(u"speciesInsertBtn")

        self.horizontalLayout_8.addWidget(self.speciesInsertBtn)

        self.speciesEditBtn = QPushButton(self.speciesFrame)
        self.speciesEditBtn.setObjectName(u"speciesEditBtn")

        self.horizontalLayout_8.addWidget(self.speciesEditBtn)

        self.speciesDeleteBtn = QPushButton(self.speciesFrame)
        self.speciesDeleteBtn.setObjectName(u"speciesDeleteBtn")

        self.horizontalLayout_8.addWidget(self.speciesDeleteBtn)


        self.verticalLayout_5.addLayout(self.horizontalLayout_8)


        self.verticalLayout_3.addWidget(self.speciesFrame)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.verticalLayout_4 = QVBoxLayout(self.tab_3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.newMetadataGroupBtn = QPushButton(self.tab_3)
        self.newMetadataGroupBtn.setObjectName(u"newMetadataGroupBtn")

        self.horizontalLayout_9.addWidget(self.newMetadataGroupBtn)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_12)

        self.label_20 = QLabel(self.tab_3)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setFont(font)
        self.label_20.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_9.addWidget(self.label_20)

        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_13)

        self.selectMetadataGroupBtn = QPushButton(self.tab_3)
        self.selectMetadataGroupBtn.setObjectName(u"selectMetadataGroupBtn")

        self.horizontalLayout_9.addWidget(self.selectMetadataGroupBtn)


        self.verticalLayout_4.addLayout(self.horizontalLayout_9)

        self.metadataFrame = QFrame(self.tab_3)
        self.metadataFrame.setObjectName(u"metadataFrame")
        self.metadataFrame.setFrameShape(QFrame.StyledPanel)
        self.metadataFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.metadataFrame)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.formLayout_4 = QFormLayout()
        self.formLayout_4.setObjectName(u"formLayout_4")
        self.formLayout_4.setContentsMargins(-1, -1, -1, 10)
        self.label_19 = QLabel(self.metadataFrame)
        self.label_19.setObjectName(u"label_19")

        self.formLayout_4.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_19)

        self.label_29 = QLabel(self.metadataFrame)
        self.label_29.setObjectName(u"label_29")

        self.formLayout_4.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_29)

        self.metadataGroupEdit = QLineEdit(self.metadataFrame)
        self.metadataGroupEdit.setObjectName(u"metadataGroupEdit")

        self.formLayout_4.setWidget(0, QFormLayout.ItemRole.FieldRole, self.metadataGroupEdit)

        self.metadataGroupDescEdit = QTextEdit(self.metadataFrame)
        self.metadataGroupDescEdit.setObjectName(u"metadataGroupDescEdit")

        self.formLayout_4.setWidget(1, QFormLayout.ItemRole.FieldRole, self.metadataGroupDescEdit)


        self.verticalLayout_10.addLayout(self.formLayout_4)

        self.metadataView = QTableView(self.metadataFrame)
        self.metadataView.setObjectName(u"metadataView")
        self.metadataView.setMinimumSize(QSize(0, 351))

        self.verticalLayout_10.addWidget(self.metadataView)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(-1, -1, -1, 0)
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_3)

        self.metadataInsertBtn = QPushButton(self.metadataFrame)
        self.metadataInsertBtn.setObjectName(u"metadataInsertBtn")

        self.horizontalLayout_11.addWidget(self.metadataInsertBtn)

        self.metadataEditBtn = QPushButton(self.metadataFrame)
        self.metadataEditBtn.setObjectName(u"metadataEditBtn")

        self.horizontalLayout_11.addWidget(self.metadataEditBtn)

        self.metadataDeleteBtn = QPushButton(self.metadataFrame)
        self.metadataDeleteBtn.setObjectName(u"metadataDeleteBtn")

        self.horizontalLayout_11.addWidget(self.metadataDeleteBtn)


        self.verticalLayout_10.addLayout(self.horizontalLayout_11)


        self.verticalLayout_4.addWidget(self.metadataFrame)

        self.tabWidget.addTab(self.tab_3, "")

        self.verticalLayout_2.addWidget(self.tabWidget)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, -1, -1, 0)
        self.reloadBtn = QPushButton(profileSetupDlg)
        self.reloadBtn.setObjectName(u"reloadBtn")

        self.horizontalLayout.addWidget(self.reloadBtn)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.cancelBtn = QPushButton(profileSetupDlg)
        self.cancelBtn.setObjectName(u"cancelBtn")

        self.horizontalLayout.addWidget(self.cancelBtn)

        self.saveBtn = QPushButton(profileSetupDlg)
        self.saveBtn.setObjectName(u"saveBtn")

        self.horizontalLayout.addWidget(self.saveBtn)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        QWidget.setTabOrder(self.tabWidget, self.newProfileBtn)
        QWidget.setTabOrder(self.newProfileBtn, self.selectProfileBtn)
        QWidget.setTabOrder(self.selectProfileBtn, self.profileNameEdit)
        QWidget.setTabOrder(self.profileNameEdit, self.profileDescriptionEdit)
        QWidget.setTabOrder(self.profileDescriptionEdit, self.leftCamPathEdit)
        QWidget.setTabOrder(self.leftCamPathEdit, self.rightCamPathEdit)
        QWidget.setTabOrder(self.rightCamPathEdit, self.calFilePathEdit)
        QWidget.setTabOrder(self.calFilePathEdit, self.stFrameIndEdit)
        QWidget.setTabOrder(self.stFrameIndEdit, self.endFrameIndEdit)
        QWidget.setTabOrder(self.endFrameIndEdit, self.timestampTypeBox)
        QWidget.setTabOrder(self.timestampTypeBox, self.timestampFormatEdit)
        QWidget.setTabOrder(self.timestampFormatEdit, self.timestampStartEdit)
        QWidget.setTabOrder(self.timestampStartEdit, self.metadataYesBtn)
        QWidget.setTabOrder(self.metadataYesBtn, self.metadataNoBtn)
        QWidget.setTabOrder(self.metadataNoBtn, self.rotateLeftBox)
        QWidget.setTabOrder(self.rotateLeftBox, self.rotateRightBox)
        QWidget.setTabOrder(self.rotateRightBox, self.timestampFormatBtn)
        QWidget.setTabOrder(self.timestampFormatBtn, self.newSpcCollectionBtn)
        QWidget.setTabOrder(self.newSpcCollectionBtn, self.selectSpcCollectionBtn)
        QWidget.setTabOrder(self.selectSpcCollectionBtn, self.frameIndHelpBtn)
        QWidget.setTabOrder(self.frameIndHelpBtn, self.spcCollectionNameEdit)
        QWidget.setTabOrder(self.spcCollectionNameEdit, self.spcCollectionDescEdit)
        QWidget.setTabOrder(self.spcCollectionDescEdit, self.speciesView)
        QWidget.setTabOrder(self.speciesView, self.speciesInsertBtn)
        QWidget.setTabOrder(self.speciesInsertBtn, self.speciesEditBtn)
        QWidget.setTabOrder(self.speciesEditBtn, self.speciesDeleteBtn)
        QWidget.setTabOrder(self.speciesDeleteBtn, self.newMetadataGroupBtn)
        QWidget.setTabOrder(self.newMetadataGroupBtn, self.selectMetadataGroupBtn)
        QWidget.setTabOrder(self.selectMetadataGroupBtn, self.metadataGroupEdit)
        QWidget.setTabOrder(self.metadataGroupEdit, self.metadataGroupDescEdit)
        QWidget.setTabOrder(self.metadataGroupDescEdit, self.metadataView)
        QWidget.setTabOrder(self.metadataView, self.metadataInsertBtn)
        QWidget.setTabOrder(self.metadataInsertBtn, self.metadataEditBtn)
        QWidget.setTabOrder(self.metadataEditBtn, self.metadataDeleteBtn)
        QWidget.setTabOrder(self.metadataDeleteBtn, self.cancelBtn)
        QWidget.setTabOrder(self.cancelBtn, self.saveBtn)

        self.retranslateUi(profileSetupDlg)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(profileSetupDlg)
    # setupUi

    def retranslateUi(self, profileSetupDlg):
        profileSetupDlg.setWindowTitle(QCoreApplication.translate("profileSetupDlg", u"Setup profiles", None))
        self.newProfileBtn.setText(QCoreApplication.translate("profileSetupDlg", u"Create New Profile", None))
        self.label_28.setText(QCoreApplication.translate("profileSetupDlg", u"or", None))
        self.selectProfileBtn.setText(QCoreApplication.translate("profileSetupDlg", u"Select Existing Profile", None))
        self.label.setText(QCoreApplication.translate("profileSetupDlg", u"LeftCameraImagePath", None))
        self.label_7.setText(QCoreApplication.translate("profileSetupDlg", u"ImageTimestampFormat", None))
        self.label_12.setText(QCoreApplication.translate("profileSetupDlg", u"degrees", None))
        self.subsampleMaskBtn.setText(QCoreApplication.translate("profileSetupDlg", u"?", None))
        self.label_5.setText(QCoreApplication.translate("profileSetupDlg", u"FrameNumberIndices", None))
        self.timestampFormatBtn.setText(QCoreApplication.translate("profileSetupDlg", u"?", None))
        self.label_13.setText(QCoreApplication.translate("profileSetupDlg", u"RotateRightImage", None))
        self.label_9.setText(QCoreApplication.translate("profileSetupDlg", u"CalibrationFileName", None))
        self.label_4.setText(QCoreApplication.translate("profileSetupDlg", u"RightCameraImagePath", None))
        self.metadataInfoBox.setTitle("")
        self.metadataYesBtn.setText(QCoreApplication.translate("profileSetupDlg", u"Yes", None))
        self.metadataNoBtn.setText(QCoreApplication.translate("profileSetupDlg", u"No", None))
        self.label_15.setText(QCoreApplication.translate("profileSetupDlg", u"SubsampleMask", None))
        self.label_30.setText(QCoreApplication.translate("profileSetupDlg", u"ImageTimestampStart", None))
        self.label_2.setText(QCoreApplication.translate("profileSetupDlg", u"Profile description", None))
        self.label_8.setText(QCoreApplication.translate("profileSetupDlg", u"to", None))
        self.frameIndHelpBtn.setText(QCoreApplication.translate("profileSetupDlg", u"?", None))
        self.label_3.setText(QCoreApplication.translate("profileSetupDlg", u"Profile name", None))
        self.label_10.setText(QCoreApplication.translate("profileSetupDlg", u"CollectMetadata", None))
        self.label_11.setText(QCoreApplication.translate("profileSetupDlg", u"RotateLeftImage", None))
        self.label_6.setText(QCoreApplication.translate("profileSetupDlg", u"ImageTimestampType", None))
        self.label_14.setText(QCoreApplication.translate("profileSetupDlg", u"degrees", None))
        self.label_16.setText(QCoreApplication.translate("profileSetupDlg", u"ImageFileType", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("profileSetupDlg", u"Profiles", None))
        self.newSpcCollectionBtn.setText(QCoreApplication.translate("profileSetupDlg", u"Create new \n"
" Species Collection", None))
        self.label_18.setText(QCoreApplication.translate("profileSetupDlg", u"or", None))
        self.selectSpcCollectionBtn.setText(QCoreApplication.translate("profileSetupDlg", u"Select Existing\n"
" Species Collection", None))
        self.label_17.setText(QCoreApplication.translate("profileSetupDlg", u"Species Collection Name", None))
        self.label_27.setText(QCoreApplication.translate("profileSetupDlg", u"Species Collection Description", None))
        self.speciesInsertBtn.setText(QCoreApplication.translate("profileSetupDlg", u"Insert", None))
        self.speciesEditBtn.setText(QCoreApplication.translate("profileSetupDlg", u"Edit", None))
        self.speciesDeleteBtn.setText(QCoreApplication.translate("profileSetupDlg", u"Delete", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("profileSetupDlg", u"Species Collections", None))
        self.newMetadataGroupBtn.setText(QCoreApplication.translate("profileSetupDlg", u"Create new \n"
" Metadata Group", None))
        self.label_20.setText(QCoreApplication.translate("profileSetupDlg", u"or", None))
        self.selectMetadataGroupBtn.setText(QCoreApplication.translate("profileSetupDlg", u"Select Existing \n"
"Metadata Group", None))
        self.label_19.setText(QCoreApplication.translate("profileSetupDlg", u"Metadata Group", None))
        self.label_29.setText(QCoreApplication.translate("profileSetupDlg", u" Description", None))
        self.metadataInsertBtn.setText(QCoreApplication.translate("profileSetupDlg", u"Insert", None))
        self.metadataEditBtn.setText(QCoreApplication.translate("profileSetupDlg", u"Edit", None))
        self.metadataDeleteBtn.setText(QCoreApplication.translate("profileSetupDlg", u"Delete", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("profileSetupDlg", u"Metadata Groups", None))
        self.reloadBtn.setText(QCoreApplication.translate("profileSetupDlg", u"Reload deployment with new profile", None))
        self.cancelBtn.setText(QCoreApplication.translate("profileSetupDlg", u"Cancel", None))
        self.saveBtn.setText(QCoreApplication.translate("profileSetupDlg", u"Save changes", None))
    # retranslateUi

