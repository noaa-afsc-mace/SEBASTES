# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'GuiSettingDlg.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDialog,
    QFormLayout, QFrame, QGroupBox, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QRadioButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_guiSettingDlg(object):
    def setupUi(self, guiSettingDlg):
        if not guiSettingDlg.objectName():
            guiSettingDlg.setObjectName(u"guiSettingDlg")
        guiSettingDlg.resize(522, 441)
        self.verticalLayout = QVBoxLayout(guiSettingDlg)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label_21 = QLabel(guiSettingDlg)
        self.label_21.setObjectName(u"label_21")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_21)

        self.measureLineWidthBox = QComboBox(guiSettingDlg)
        self.measureLineWidthBox.setObjectName(u"measureLineWidthBox")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.measureLineWidthBox)

        self.label_22 = QLabel(guiSettingDlg)
        self.label_22.setObjectName(u"label_22")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_22)

        self.measureLineTailLengthBox = QComboBox(guiSettingDlg)
        self.measureLineTailLengthBox.setObjectName(u"measureLineTailLengthBox")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.measureLineTailLengthBox)

        self.label_25 = QLabel(guiSettingDlg)
        self.label_25.setObjectName(u"label_25")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.label_25)

        self.boxLineThicknessBox = QComboBox(guiSettingDlg)
        self.boxLineThicknessBox.setObjectName(u"boxLineThicknessBox")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.boxLineThicknessBox)

        self.label_26 = QLabel(guiSettingDlg)
        self.label_26.setObjectName(u"label_26")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.label_26)

        self.labelTextSizeBox = QComboBox(guiSettingDlg)
        self.labelTextSizeBox.setObjectName(u"labelTextSizeBox")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.labelTextSizeBox)

        self.label = QLabel(guiSettingDlg)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(5, QFormLayout.ItemRole.LabelRole, self.label)

        self.groupBox = QGroupBox(guiSettingDlg)
        self.groupBox.setObjectName(u"groupBox")
        self.horizontalLayout_2 = QHBoxLayout(self.groupBox)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.metaSelRetainRadio = QRadioButton(self.groupBox)
        self.metaSelRetainRadio.setObjectName(u"metaSelRetainRadio")

        self.horizontalLayout_2.addWidget(self.metaSelRetainRadio)

        self.metaSelClearRadio = QRadioButton(self.groupBox)
        self.metaSelClearRadio.setObjectName(u"metaSelClearRadio")

        self.horizontalLayout_2.addWidget(self.metaSelClearRadio)


        self.formLayout.setWidget(5, QFormLayout.ItemRole.FieldRole, self.groupBox)

        self.label_3 = QLabel(guiSettingDlg)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(7, QFormLayout.ItemRole.LabelRole, self.label_3)

        self.groupBox_2 = QGroupBox(guiSettingDlg)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.horizontalLayout_3 = QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.spcSelRetainRadio = QRadioButton(self.groupBox_2)
        self.spcSelRetainRadio.setObjectName(u"spcSelRetainRadio")

        self.horizontalLayout_3.addWidget(self.spcSelRetainRadio)

        self.spcSelClearRadio = QRadioButton(self.groupBox_2)
        self.spcSelClearRadio.setObjectName(u"spcSelClearRadio")

        self.horizontalLayout_3.addWidget(self.spcSelClearRadio)


        self.formLayout.setWidget(7, QFormLayout.ItemRole.FieldRole, self.groupBox_2)

        self.label_2 = QLabel(guiSettingDlg)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(8, QFormLayout.ItemRole.LabelRole, self.label_2)

        self.classLabelCheckBox = QCheckBox(guiSettingDlg)
        self.classLabelCheckBox.setObjectName(u"classLabelCheckBox")

        self.formLayout.setWidget(8, QFormLayout.ItemRole.FieldRole, self.classLabelCheckBox)

        self.label_24 = QLabel(guiSettingDlg)
        self.label_24.setObjectName(u"label_24")

        self.formLayout.setWidget(10, QFormLayout.ItemRole.LabelRole, self.label_24)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.sceneColorLabel = QLabel(guiSettingDlg)
        self.sceneColorLabel.setObjectName(u"sceneColorLabel")
        self.sceneColorLabel.setMinimumSize(QSize(51, 0))
        self.sceneColorLabel.setFrameShape(QFrame.Box)

        self.horizontalLayout_15.addWidget(self.sceneColorLabel)

        self.sceneColorBtn = QPushButton(guiSettingDlg)
        self.sceneColorBtn.setObjectName(u"sceneColorBtn")

        self.horizontalLayout_15.addWidget(self.sceneColorBtn)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_7)


        self.formLayout.setLayout(10, QFormLayout.ItemRole.FieldRole, self.horizontalLayout_15)

        self.label_23 = QLabel(guiSettingDlg)
        self.label_23.setObjectName(u"label_23")

        self.formLayout.setWidget(11, QFormLayout.ItemRole.LabelRole, self.label_23)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.targetColorLabel = QLabel(guiSettingDlg)
        self.targetColorLabel.setObjectName(u"targetColorLabel")
        self.targetColorLabel.setMinimumSize(QSize(51, 0))
        self.targetColorLabel.setFrameShape(QFrame.Box)

        self.horizontalLayout_14.addWidget(self.targetColorLabel)

        self.targetLineColorBtn = QPushButton(guiSettingDlg)
        self.targetLineColorBtn.setObjectName(u"targetLineColorBtn")

        self.horizontalLayout_14.addWidget(self.targetLineColorBtn)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_6)


        self.formLayout.setLayout(11, QFormLayout.ItemRole.FieldRole, self.horizontalLayout_14)

        self.label_4 = QLabel(guiSettingDlg)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(9, QFormLayout.ItemRole.LabelRole, self.label_4)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.speedAdjLabel = QLineEdit(guiSettingDlg)
        self.speedAdjLabel.setObjectName(u"speedAdjLabel")
        self.speedAdjLabel.setMaximumSize(QSize(51, 16777215))

        self.horizontalLayout_4.addWidget(self.speedAdjLabel)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)


        self.formLayout.setLayout(9, QFormLayout.ItemRole.FieldRole, self.horizontalLayout_4)

        self.label_5 = QLabel(guiSettingDlg)
        self.label_5.setObjectName(u"label_5")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.LabelRole, self.label_5)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.showSpcNameCheck = QCheckBox(guiSettingDlg)
        self.showSpcNameCheck.setObjectName(u"showSpcNameCheck")

        self.horizontalLayout_5.addWidget(self.showSpcNameCheck)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_3)

        self.label_6 = QLabel(guiSettingDlg)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_5.addWidget(self.label_6)

        self.spcNameLengthEdit = QLineEdit(guiSettingDlg)
        self.spcNameLengthEdit.setObjectName(u"spcNameLengthEdit")

        self.horizontalLayout_5.addWidget(self.spcNameLengthEdit)


        self.formLayout.setLayout(4, QFormLayout.ItemRole.FieldRole, self.horizontalLayout_5)


        self.verticalLayout.addLayout(self.formLayout)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.cancelBtn = QPushButton(guiSettingDlg)
        self.cancelBtn.setObjectName(u"cancelBtn")

        self.horizontalLayout.addWidget(self.cancelBtn)

        self.saveBtn = QPushButton(guiSettingDlg)
        self.saveBtn.setObjectName(u"saveBtn")

        self.horizontalLayout.addWidget(self.saveBtn)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(guiSettingDlg)

        QMetaObject.connectSlotsByName(guiSettingDlg)
    # setupUi

    def retranslateUi(self, guiSettingDlg):
        guiSettingDlg.setWindowTitle(QCoreApplication.translate("guiSettingDlg", u"GUI Settings", None))
        self.label_21.setText(QCoreApplication.translate("guiSettingDlg", u"MeasureLineWidth", None))
        self.label_22.setText(QCoreApplication.translate("guiSettingDlg", u"MeasureLineTailLength", None))
        self.label_25.setText(QCoreApplication.translate("guiSettingDlg", u"BoxLineThickness", None))
        self.label_26.setText(QCoreApplication.translate("guiSettingDlg", u"LabelTextSize", None))
        self.label.setText(QCoreApplication.translate("guiSettingDlg", u"DefaultMetadataSelection", None))
        self.groupBox.setTitle("")
        self.metaSelRetainRadio.setText(QCoreApplication.translate("guiSettingDlg", u"Retain Selection", None))
        self.metaSelClearRadio.setText(QCoreApplication.translate("guiSettingDlg", u"Clear Selection", None))
        self.label_3.setText(QCoreApplication.translate("guiSettingDlg", u"RetainSpeciesSelection", None))
        self.groupBox_2.setTitle("")
        self.spcSelRetainRadio.setText(QCoreApplication.translate("guiSettingDlg", u"Retain Selection", None))
        self.spcSelClearRadio.setText(QCoreApplication.translate("guiSettingDlg", u"Clear Selection", None))
        self.label_2.setText(QCoreApplication.translate("guiSettingDlg", u"ShowClassOnLabel", None))
        self.classLabelCheckBox.setText("")
        self.label_24.setText(QCoreApplication.translate("guiSettingDlg", u"SceneColor", None))
        self.sceneColorLabel.setText("")
        self.sceneColorBtn.setText(QCoreApplication.translate("guiSettingDlg", u"Select color", None))
        self.label_23.setText(QCoreApplication.translate("guiSettingDlg", u"TargetLineColor", None))
        self.targetColorLabel.setText("")
        self.targetLineColorBtn.setText(QCoreApplication.translate("guiSettingDlg", u"Select color", None))
        self.label_4.setText(QCoreApplication.translate("guiSettingDlg", u"Playback scale", None))
        self.label_5.setText(QCoreApplication.translate("guiSettingDlg", u"LabelSpeciesName", None))
        self.showSpcNameCheck.setText(QCoreApplication.translate("guiSettingDlg", u"Show Species", None))
        self.label_6.setText(QCoreApplication.translate("guiSettingDlg", u"Number of characters to show ", None))
        self.cancelBtn.setText(QCoreApplication.translate("guiSettingDlg", u"Cancel", None))
        self.saveBtn.setText(QCoreApplication.translate("guiSettingDlg", u"Save", None))
    # retranslateUi

