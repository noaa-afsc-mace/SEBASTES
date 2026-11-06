# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'SEBASTES_dockable.ui'
##
## Created by: Qt User Interface Compiler version 6.11.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDockWidget,
    QFrame, QGridLayout, QGroupBox, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QMenu,
    QMenuBar, QPushButton, QRadioButton, QSizePolicy,
    QSlider, QSpacerItem, QStatusBar, QTabWidget,
    QVBoxLayout, QWidget)

from QImageViewer.QImageViewer import QImageViewer

class Ui_SEBASTES(object):
    def setupUi(self, SEBASTES):
        if not SEBASTES.objectName():
            SEBASTES.setObjectName(u"SEBASTES")
        SEBASTES.resize(1962, 905)
        SEBASTES.setMinimumSize(QSize(0, 0))
        SEBASTES.setMaximumSize(QSize(9999, 9999))
        font = QFont()
        font.setPointSize(10)
        SEBASTES.setFont(font)
        self.actionLoad = QAction(SEBASTES)
        self.actionLoad.setObjectName(u"actionLoad")
        self.actionExit = QAction(SEBASTES)
        self.actionExit.setObjectName(u"actionExit")
        self.actionProfiles = QAction(SEBASTES)
        self.actionProfiles.setObjectName(u"actionProfiles")
        self.actionGUI_settings = QAction(SEBASTES)
        self.actionGUI_settings.setObjectName(u"actionGUI_settings")
        self.actionGrid_setup = QAction(SEBASTES)
        self.actionGrid_setup.setObjectName(u"actionGrid_setup")
        self.actionSet_Active_Profiles = QAction(SEBASTES)
        self.actionSet_Active_Profiles.setObjectName(u"actionSet_Active_Profiles")
        self.actionImport_Export_Profiles = QAction(SEBASTES)
        self.actionImport_Export_Profiles.setObjectName(u"actionImport_Export_Profiles")
        self.actionCreate_New_Project = QAction(SEBASTES)
        self.actionCreate_New_Project.setObjectName(u"actionCreate_New_Project")
        self.actionviewApplicationDB = QAction(SEBASTES)
        self.actionviewApplicationDB.setObjectName(u"actionviewApplicationDB")
        self.actionedit_DB_tables = QAction(SEBASTES)
        self.actionedit_DB_tables.setObjectName(u"actionedit_DB_tables")
        self.centralwidget = QWidget(SEBASTES)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(6, 6, 6, 6)
        self.upperFrame = QFrame(self.centralwidget)
        self.upperFrame.setObjectName(u"upperFrame")
        self.upperFrame.setEnabled(True)
        self.upperFrame.setFrameShape(QFrame.StyledPanel)
        self.upperFrame.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.upperFrame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(2, 2, 2, 2)
        self.deploymentBox = QLabel(self.upperFrame)
        self.deploymentBox.setObjectName(u"deploymentBox")
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        self.deploymentBox.setFont(font1)

        self.gridLayout_2.addWidget(self.deploymentBox, 0, 1, 1, 1)

        self.label_7 = QLabel(self.upperFrame)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_2.addWidget(self.label_7, 0, 10, 1, 1)

        self.label = QLabel(self.upperFrame)
        self.label.setObjectName(u"label")

        self.gridLayout_2.addWidget(self.label, 0, 15, 1, 1)

        self.lastFrameBtn = QPushButton(self.upperFrame)
        self.lastFrameBtn.setObjectName(u"lastFrameBtn")

        self.gridLayout_2.addWidget(self.lastFrameBtn, 0, 17, 1, 1)

        self.label_18 = QLabel(self.upperFrame)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setFont(font)

        self.gridLayout_2.addWidget(self.label_18, 1, 12, 1, 1)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_6, 0, 9, 1, 1)

        self.maxFrame = QLabel(self.upperFrame)
        self.maxFrame.setObjectName(u"maxFrame")
        font2 = QFont()
        font2.setPointSize(12)
        self.maxFrame.setFont(font2)

        self.gridLayout_2.addWidget(self.maxFrame, 0, 16, 1, 1)

        self.label_20 = QLabel(self.upperFrame)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setFont(font)
        self.label_20.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_20, 1, 13, 1, 1)

        self.label_6 = QLabel(self.upperFrame)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font)
        self.label_6.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_6, 1, 14, 1, 1)

        self.rateOffsetEdit = QLineEdit(self.upperFrame)
        self.rateOffsetEdit.setObjectName(u"rateOffsetEdit")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rateOffsetEdit.sizePolicy().hasHeightForWidth())
        self.rateOffsetEdit.setSizePolicy(sizePolicy)
        self.rateOffsetEdit.setMinimumSize(QSize(71, 41))
        self.rateOffsetEdit.setMaximumSize(QSize(71, 41))
        font3 = QFont()
        font3.setPointSize(14)
        self.rateOffsetEdit.setFont(font3)

        self.gridLayout_2.addWidget(self.rateOffsetEdit, 0, 13, 1, 1)

        self.sampleRateEdit = QLineEdit(self.upperFrame)
        self.sampleRateEdit.setObjectName(u"sampleRateEdit")
        sizePolicy.setHeightForWidth(self.sampleRateEdit.sizePolicy().hasHeightForWidth())
        self.sampleRateEdit.setSizePolicy(sizePolicy)
        self.sampleRateEdit.setMinimumSize(QSize(71, 41))
        self.sampleRateEdit.setMaximumSize(QSize(71, 41))
        self.sampleRateEdit.setFont(font3)

        self.gridLayout_2.addWidget(self.sampleRateEdit, 0, 12, 1, 1)

        self.frameBox = QLineEdit(self.upperFrame)
        self.frameBox.setObjectName(u"frameBox")
        self.frameBox.setMinimumSize(QSize(91, 41))
        self.frameBox.setMaximumSize(QSize(91, 41))
        self.frameBox.setFont(font3)

        self.gridLayout_2.addWidget(self.frameBox, 0, 14, 1, 1)

        self.annotatorLabel = QLabel(self.upperFrame)
        self.annotatorLabel.setObjectName(u"annotatorLabel")
        self.annotatorLabel.setMinimumSize(QSize(71, 0))
        self.annotatorLabel.setFont(font1)
        self.annotatorLabel.setFrameShape(QFrame.Box)

        self.gridLayout_2.addWidget(self.annotatorLabel, 0, 11, 1, 1)


        self.verticalLayout.addWidget(self.upperFrame)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(-1, -1, -1, 5)
        self.frameLeft = QFrame(self.centralwidget)
        self.frameLeft.setObjectName(u"frameLeft")
        self.frameLeft.setFrameShape(QFrame.StyledPanel)
        self.frameLeft.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frameLeft)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(-1, -1, -1, 5)
        self.adjLeftBtn = QPushButton(self.frameLeft)
        self.adjLeftBtn.setObjectName(u"adjLeftBtn")
        self.adjLeftBtn.setFont(font)

        self.horizontalLayout_9.addWidget(self.adjLeftBtn)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer)


        self.verticalLayout_9.addLayout(self.horizontalLayout_9)

        self.gvLeft = QImageViewer(self.frameLeft)
        self.gvLeft.setObjectName(u"gvLeft")

        self.verticalLayout_9.addWidget(self.gvLeft)


        self.horizontalLayout_19.addWidget(self.frameLeft)

        self.frameRight = QFrame(self.centralwidget)
        self.frameRight.setObjectName(u"frameRight")
        self.frameRight.setFrameShape(QFrame.StyledPanel)
        self.frameRight.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frameRight)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(-1, -1, -1, 5)
        self.adjRightBtn = QPushButton(self.frameRight)
        self.adjRightBtn.setObjectName(u"adjRightBtn")
        self.adjRightBtn.setFont(font)

        self.horizontalLayout_10.addWidget(self.adjRightBtn)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_5)


        self.verticalLayout_8.addLayout(self.horizontalLayout_10)

        self.gvRight = QImageViewer(self.frameRight)
        self.gvRight.setObjectName(u"gvRight")

        self.verticalLayout_8.addWidget(self.gvRight)


        self.horizontalLayout_19.addWidget(self.frameRight)


        self.verticalLayout.addLayout(self.horizontalLayout_19)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(-1, -1, -1, 10)
        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMaximumSize(QSize(251, 16777215))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")

        self.horizontalLayout_12.addWidget(self.frame_2)

        self.frame_10 = QFrame(self.centralwidget)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setMinimumSize(QSize(0, 20))
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_11.setSpacing(2)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(-1, 2, -1, 2)
        self.minFrame = QLabel(self.frame_10)
        self.minFrame.setObjectName(u"minFrame")
        self.minFrame.setFont(font2)

        self.horizontalLayout_11.addWidget(self.minFrame)

        self.imageSlider = QSlider(self.frame_10)
        self.imageSlider.setObjectName(u"imageSlider")
        self.imageSlider.setOrientation(Qt.Horizontal)

        self.horizontalLayout_11.addWidget(self.imageSlider)

        self.frame_11 = QFrame(self.frame_10)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_11.addWidget(self.frame_11)


        self.horizontalLayout_12.addWidget(self.frame_10)


        self.verticalLayout.addLayout(self.horizontalLayout_12)

        SEBASTES.setCentralWidget(self.centralwidget)
        self.statusBar = QStatusBar(SEBASTES)
        self.statusBar.setObjectName(u"statusBar")
        SEBASTES.setStatusBar(self.statusBar)
        self.menuBar = QMenuBar(SEBASTES)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 1962, 29))
        self.menuFile = QMenu(self.menuBar)
        self.menuFile.setObjectName(u"menuFile")
        SEBASTES.setMenuBar(self.menuBar)
        self.metadataDockWidget = QDockWidget(SEBASTES)
        self.metadataDockWidget.setObjectName(u"metadataDockWidget")
        self.dockWidgetContents_4 = QWidget()
        self.dockWidgetContents_4.setObjectName(u"dockWidgetContents_4")
        self.verticalLayout_13 = QVBoxLayout(self.dockWidgetContents_4)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.exclusiveRadioBox1 = QGroupBox(self.dockWidgetContents_4)
        self.exclusiveRadioBox1.setObjectName(u"exclusiveRadioBox1")
        font4 = QFont()
        font4.setPointSize(8)
        self.exclusiveRadioBox1.setFont(font4)
        self.verticalLayout_2 = QVBoxLayout(self.exclusiveRadioBox1)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.radioButton1_1 = QRadioButton(self.exclusiveRadioBox1)
        self.radioButton1_1.setObjectName(u"radioButton1_1")

        self.verticalLayout_2.addWidget(self.radioButton1_1)

        self.radioButton1_2 = QRadioButton(self.exclusiveRadioBox1)
        self.radioButton1_2.setObjectName(u"radioButton1_2")

        self.verticalLayout_2.addWidget(self.radioButton1_2)

        self.radioButton1_3 = QRadioButton(self.exclusiveRadioBox1)
        self.radioButton1_3.setObjectName(u"radioButton1_3")

        self.verticalLayout_2.addWidget(self.radioButton1_3)

        self.radioButton1_4 = QRadioButton(self.exclusiveRadioBox1)
        self.radioButton1_4.setObjectName(u"radioButton1_4")

        self.verticalLayout_2.addWidget(self.radioButton1_4)

        self.radioButton1_5 = QRadioButton(self.exclusiveRadioBox1)
        self.radioButton1_5.setObjectName(u"radioButton1_5")

        self.verticalLayout_2.addWidget(self.radioButton1_5)

        self.radioButton1_6 = QRadioButton(self.exclusiveRadioBox1)
        self.radioButton1_6.setObjectName(u"radioButton1_6")

        self.verticalLayout_2.addWidget(self.radioButton1_6)

        self.radioButton1_7 = QRadioButton(self.exclusiveRadioBox1)
        self.radioButton1_7.setObjectName(u"radioButton1_7")

        self.verticalLayout_2.addWidget(self.radioButton1_7)

        self.radioButton1_8 = QRadioButton(self.exclusiveRadioBox1)
        self.radioButton1_8.setObjectName(u"radioButton1_8")

        self.verticalLayout_2.addWidget(self.radioButton1_8)

        self.radioButton1_9 = QRadioButton(self.exclusiveRadioBox1)
        self.radioButton1_9.setObjectName(u"radioButton1_9")

        self.verticalLayout_2.addWidget(self.radioButton1_9)

        self.radioButton1_10 = QRadioButton(self.exclusiveRadioBox1)
        self.radioButton1_10.setObjectName(u"radioButton1_10")

        self.verticalLayout_2.addWidget(self.radioButton1_10)


        self.horizontalLayout_8.addWidget(self.exclusiveRadioBox1)

        self.exclusiveRadioBox2 = QGroupBox(self.dockWidgetContents_4)
        self.exclusiveRadioBox2.setObjectName(u"exclusiveRadioBox2")
        self.exclusiveRadioBox2.setFont(font4)
        self.verticalLayout_5 = QVBoxLayout(self.exclusiveRadioBox2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.radioButton2_1 = QRadioButton(self.exclusiveRadioBox2)
        self.radioButton2_1.setObjectName(u"radioButton2_1")

        self.verticalLayout_5.addWidget(self.radioButton2_1)

        self.radioButton2_2 = QRadioButton(self.exclusiveRadioBox2)
        self.radioButton2_2.setObjectName(u"radioButton2_2")

        self.verticalLayout_5.addWidget(self.radioButton2_2)

        self.radioButton2_3 = QRadioButton(self.exclusiveRadioBox2)
        self.radioButton2_3.setObjectName(u"radioButton2_3")

        self.verticalLayout_5.addWidget(self.radioButton2_3)

        self.radioButton2_4 = QRadioButton(self.exclusiveRadioBox2)
        self.radioButton2_4.setObjectName(u"radioButton2_4")

        self.verticalLayout_5.addWidget(self.radioButton2_4)

        self.radioButton2_5 = QRadioButton(self.exclusiveRadioBox2)
        self.radioButton2_5.setObjectName(u"radioButton2_5")

        self.verticalLayout_5.addWidget(self.radioButton2_5)

        self.radioButton2_6 = QRadioButton(self.exclusiveRadioBox2)
        self.radioButton2_6.setObjectName(u"radioButton2_6")

        self.verticalLayout_5.addWidget(self.radioButton2_6)

        self.radioButton2_7 = QRadioButton(self.exclusiveRadioBox2)
        self.radioButton2_7.setObjectName(u"radioButton2_7")

        self.verticalLayout_5.addWidget(self.radioButton2_7)

        self.radioButton2_8 = QRadioButton(self.exclusiveRadioBox2)
        self.radioButton2_8.setObjectName(u"radioButton2_8")

        self.verticalLayout_5.addWidget(self.radioButton2_8)

        self.radioButton2_9 = QRadioButton(self.exclusiveRadioBox2)
        self.radioButton2_9.setObjectName(u"radioButton2_9")

        self.verticalLayout_5.addWidget(self.radioButton2_9)

        self.radioButton2_10 = QRadioButton(self.exclusiveRadioBox2)
        self.radioButton2_10.setObjectName(u"radioButton2_10")

        self.verticalLayout_5.addWidget(self.radioButton2_10)


        self.horizontalLayout_8.addWidget(self.exclusiveRadioBox2)


        self.verticalLayout_13.addLayout(self.horizontalLayout_8)

        self.exclusiveRadioBox3 = QGroupBox(self.dockWidgetContents_4)
        self.exclusiveRadioBox3.setObjectName(u"exclusiveRadioBox3")
        self.exclusiveRadioBox3.setFont(font4)
        self.horizontalLayout_21 = QHBoxLayout(self.exclusiveRadioBox3)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.radioButton3_1 = QRadioButton(self.exclusiveRadioBox3)
        self.radioButton3_1.setObjectName(u"radioButton3_1")
        self.radioButton3_1.setFont(font4)

        self.horizontalLayout_21.addWidget(self.radioButton3_1)

        self.radioButton3_2 = QRadioButton(self.exclusiveRadioBox3)
        self.radioButton3_2.setObjectName(u"radioButton3_2")
        self.radioButton3_2.setFont(font4)

        self.horizontalLayout_21.addWidget(self.radioButton3_2)


        self.verticalLayout_13.addWidget(self.exclusiveRadioBox3)

        self.metadataStickyBox = QCheckBox(self.dockWidgetContents_4)
        self.metadataStickyBox.setObjectName(u"metadataStickyBox")
        self.metadataStickyBox.setFont(font)

        self.verticalLayout_13.addWidget(self.metadataStickyBox)

        self.extraMetadataFrame = QFrame(self.dockWidgetContents_4)
        self.extraMetadataFrame.setObjectName(u"extraMetadataFrame")
        self.extraMetadataFrame.setFrameShape(QFrame.StyledPanel)
        self.extraMetadataFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_22 = QHBoxLayout(self.extraMetadataFrame)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(-1, -1, 10, -1)
        self.metadataTypeLabel2 = QLabel(self.extraMetadataFrame)
        self.metadataTypeLabel2.setObjectName(u"metadataTypeLabel2")
        font5 = QFont()
        font5.setPointSize(10)
        font5.setBold(True)
        self.metadataTypeLabel2.setFont(font5)

        self.verticalLayout_11.addWidget(self.metadataTypeLabel2)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label1_1 = QLabel(self.extraMetadataFrame)
        self.label1_1.setObjectName(u"label1_1")

        self.horizontalLayout_14.addWidget(self.label1_1)

        self.lineEdit1_1 = QLineEdit(self.extraMetadataFrame)
        self.lineEdit1_1.setObjectName(u"lineEdit1_1")
        self.lineEdit1_1.setMaximumSize(QSize(41, 16777215))

        self.horizontalLayout_14.addWidget(self.lineEdit1_1)


        self.verticalLayout_11.addLayout(self.horizontalLayout_14)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setSpacing(0)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.label1_2 = QLabel(self.extraMetadataFrame)
        self.label1_2.setObjectName(u"label1_2")

        self.horizontalLayout_15.addWidget(self.label1_2)

        self.lineEdit1_2 = QLineEdit(self.extraMetadataFrame)
        self.lineEdit1_2.setObjectName(u"lineEdit1_2")
        self.lineEdit1_2.setMaximumSize(QSize(41, 16777215))

        self.horizontalLayout_15.addWidget(self.lineEdit1_2)


        self.verticalLayout_11.addLayout(self.horizontalLayout_15)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setSpacing(0)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label1_3 = QLabel(self.extraMetadataFrame)
        self.label1_3.setObjectName(u"label1_3")

        self.horizontalLayout_16.addWidget(self.label1_3)

        self.lineEdit1_3 = QLineEdit(self.extraMetadataFrame)
        self.lineEdit1_3.setObjectName(u"lineEdit1_3")
        self.lineEdit1_3.setMaximumSize(QSize(41, 16777215))

        self.horizontalLayout_16.addWidget(self.lineEdit1_3)


        self.verticalLayout_11.addLayout(self.horizontalLayout_16)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setSpacing(0)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.label1_4 = QLabel(self.extraMetadataFrame)
        self.label1_4.setObjectName(u"label1_4")

        self.horizontalLayout_17.addWidget(self.label1_4)

        self.lineEdit1_4 = QLineEdit(self.extraMetadataFrame)
        self.lineEdit1_4.setObjectName(u"lineEdit1_4")
        self.lineEdit1_4.setMaximumSize(QSize(41, 16777215))

        self.horizontalLayout_17.addWidget(self.lineEdit1_4)


        self.verticalLayout_11.addLayout(self.horizontalLayout_17)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setSpacing(0)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.label1_5 = QLabel(self.extraMetadataFrame)
        self.label1_5.setObjectName(u"label1_5")

        self.horizontalLayout_18.addWidget(self.label1_5)

        self.lineEdit1_5 = QLineEdit(self.extraMetadataFrame)
        self.lineEdit1_5.setObjectName(u"lineEdit1_5")
        self.lineEdit1_5.setMaximumSize(QSize(41, 16777215))

        self.horizontalLayout_18.addWidget(self.lineEdit1_5)


        self.verticalLayout_11.addLayout(self.horizontalLayout_18)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_11.addItem(self.verticalSpacer_2)


        self.horizontalLayout_22.addLayout(self.verticalLayout_11)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(-1, -1, 10, -1)
        self.metadataTypeLabel3 = QLabel(self.extraMetadataFrame)
        self.metadataTypeLabel3.setObjectName(u"metadataTypeLabel3")
        self.metadataTypeLabel3.setFont(font5)

        self.verticalLayout_6.addWidget(self.metadataTypeLabel3)

        self.checkBox1_1 = QCheckBox(self.extraMetadataFrame)
        self.checkBox1_1.setObjectName(u"checkBox1_1")

        self.verticalLayout_6.addWidget(self.checkBox1_1)

        self.checkBox1_2 = QCheckBox(self.extraMetadataFrame)
        self.checkBox1_2.setObjectName(u"checkBox1_2")

        self.verticalLayout_6.addWidget(self.checkBox1_2)

        self.checkBox1_3 = QCheckBox(self.extraMetadataFrame)
        self.checkBox1_3.setObjectName(u"checkBox1_3")

        self.verticalLayout_6.addWidget(self.checkBox1_3)

        self.checkBox1_4 = QCheckBox(self.extraMetadataFrame)
        self.checkBox1_4.setObjectName(u"checkBox1_4")

        self.verticalLayout_6.addWidget(self.checkBox1_4)

        self.checkBox1_5 = QCheckBox(self.extraMetadataFrame)
        self.checkBox1_5.setObjectName(u"checkBox1_5")

        self.verticalLayout_6.addWidget(self.checkBox1_5)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer)


        self.horizontalLayout_22.addLayout(self.verticalLayout_6)


        self.verticalLayout_13.addWidget(self.extraMetadataFrame)

        self.metadataDockWidget.setWidget(self.dockWidgetContents_4)
        SEBASTES.addDockWidget(Qt.DockWidgetArea.LeftDockWidgetArea, self.metadataDockWidget)
        self.speciesDockWidget = QDockWidget(SEBASTES)
        self.speciesDockWidget.setObjectName(u"speciesDockWidget")
        self.dockWidgetContents_5 = QWidget()
        self.dockWidgetContents_5.setObjectName(u"dockWidgetContents_5")
        self.verticalLayout_14 = QVBoxLayout(self.dockWidgetContents_5)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.speciesTabWidget = QTabWidget(self.dockWidgetContents_5)
        self.speciesTabWidget.setObjectName(u"speciesTabWidget")
        self.speciesTabWidget.setMinimumSize(QSize(201, 0))
        self.speciesTabWidget.setTabPosition(QTabWidget.East)
        self.tab_1 = QWidget()
        self.tab_1.setObjectName(u"tab_1")
        self.verticalLayout_3 = QVBoxLayout(self.tab_1)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.btn1 = QPushButton(self.tab_1)
        self.btn1.setObjectName(u"btn1")
        self.btn1.setMinimumSize(QSize(0, 0))
        self.btn1.setMaximumSize(QSize(16777215, 16777215))
        self.btn1.setFont(font4)
        self.btn1.setCheckable(True)
        self.btn1.setAutoExclusive(True)

        self.verticalLayout_3.addWidget(self.btn1)

        self.btn2 = QPushButton(self.tab_1)
        self.btn2.setObjectName(u"btn2")
        self.btn2.setMinimumSize(QSize(0, 0))
        self.btn2.setMaximumSize(QSize(16777215, 16777215))
        self.btn2.setFont(font4)
        self.btn2.setCheckable(True)
        self.btn2.setAutoExclusive(True)

        self.verticalLayout_3.addWidget(self.btn2)

        self.btn3 = QPushButton(self.tab_1)
        self.btn3.setObjectName(u"btn3")
        self.btn3.setMinimumSize(QSize(0, 0))
        self.btn3.setMaximumSize(QSize(16777215, 16777215))
        self.btn3.setFont(font4)
        self.btn3.setCheckable(True)
        self.btn3.setAutoExclusive(True)

        self.verticalLayout_3.addWidget(self.btn3)

        self.btn4 = QPushButton(self.tab_1)
        self.btn4.setObjectName(u"btn4")
        self.btn4.setMinimumSize(QSize(0, 0))
        self.btn4.setMaximumSize(QSize(16777215, 16777215))
        self.btn4.setFont(font4)
        self.btn4.setCheckable(True)
        self.btn4.setAutoExclusive(True)

        self.verticalLayout_3.addWidget(self.btn4)

        self.btn5 = QPushButton(self.tab_1)
        self.btn5.setObjectName(u"btn5")
        self.btn5.setMinimumSize(QSize(0, 0))
        self.btn5.setMaximumSize(QSize(16777215, 16777215))
        self.btn5.setFont(font4)
        self.btn5.setCheckable(True)
        self.btn5.setAutoExclusive(True)

        self.verticalLayout_3.addWidget(self.btn5)

        self.btn6 = QPushButton(self.tab_1)
        self.btn6.setObjectName(u"btn6")
        self.btn6.setMinimumSize(QSize(0, 0))
        self.btn6.setMaximumSize(QSize(16777215, 16777215))
        self.btn6.setFont(font4)
        self.btn6.setCheckable(True)
        self.btn6.setAutoExclusive(True)

        self.verticalLayout_3.addWidget(self.btn6)

        self.btn7 = QPushButton(self.tab_1)
        self.btn7.setObjectName(u"btn7")
        self.btn7.setMinimumSize(QSize(0, 0))
        self.btn7.setMaximumSize(QSize(16777215, 16777215))
        self.btn7.setFont(font4)
        self.btn7.setCheckable(True)
        self.btn7.setAutoExclusive(True)

        self.verticalLayout_3.addWidget(self.btn7)

        self.btn8 = QPushButton(self.tab_1)
        self.btn8.setObjectName(u"btn8")
        self.btn8.setMinimumSize(QSize(0, 0))
        self.btn8.setMaximumSize(QSize(16777215, 16777215))
        self.btn8.setFont(font4)
        self.btn8.setCheckable(True)
        self.btn8.setAutoExclusive(True)

        self.verticalLayout_3.addWidget(self.btn8)

        self.btn9 = QPushButton(self.tab_1)
        self.btn9.setObjectName(u"btn9")
        self.btn9.setMinimumSize(QSize(0, 0))
        self.btn9.setMaximumSize(QSize(16777215, 16777215))
        self.btn9.setFont(font4)
        self.btn9.setCheckable(True)
        self.btn9.setAutoExclusive(True)

        self.verticalLayout_3.addWidget(self.btn9)

        self.btn10 = QPushButton(self.tab_1)
        self.btn10.setObjectName(u"btn10")
        self.btn10.setMinimumSize(QSize(0, 0))
        self.btn10.setMaximumSize(QSize(16777215, 16777215))
        self.btn10.setFont(font4)
        self.btn10.setCheckable(True)
        self.btn10.setAutoExclusive(True)

        self.verticalLayout_3.addWidget(self.btn10)

        self.btn11 = QPushButton(self.tab_1)
        self.btn11.setObjectName(u"btn11")
        self.btn11.setMinimumSize(QSize(0, 0))
        self.btn11.setMaximumSize(QSize(16777215, 16777215))
        self.btn11.setFont(font4)
        self.btn11.setCheckable(True)
        self.btn11.setAutoExclusive(True)

        self.verticalLayout_3.addWidget(self.btn11)

        self.btn12 = QPushButton(self.tab_1)
        self.btn12.setObjectName(u"btn12")
        self.btn12.setMinimumSize(QSize(0, 0))
        self.btn12.setMaximumSize(QSize(16777215, 16777215))
        self.btn12.setFont(font4)
        self.btn12.setCheckable(True)
        self.btn12.setAutoExclusive(True)

        self.verticalLayout_3.addWidget(self.btn12)

        self.btn13 = QPushButton(self.tab_1)
        self.btn13.setObjectName(u"btn13")
        self.btn13.setMinimumSize(QSize(0, 0))
        self.btn13.setMaximumSize(QSize(16777215, 16777215))
        self.btn13.setFont(font4)
        self.btn13.setCheckable(True)
        self.btn13.setAutoExclusive(True)

        self.verticalLayout_3.addWidget(self.btn13)

        self.btn14 = QPushButton(self.tab_1)
        self.btn14.setObjectName(u"btn14")
        self.btn14.setMinimumSize(QSize(0, 0))
        self.btn14.setMaximumSize(QSize(16777215, 16777215))
        self.btn14.setFont(font4)
        self.btn14.setCheckable(True)
        self.btn14.setAutoExclusive(True)

        self.verticalLayout_3.addWidget(self.btn14)

        self.btn15 = QPushButton(self.tab_1)
        self.btn15.setObjectName(u"btn15")
        self.btn15.setMinimumSize(QSize(0, 0))
        self.btn15.setMaximumSize(QSize(16777215, 16777215))
        self.btn15.setFont(font4)
        self.btn15.setCheckable(True)
        self.btn15.setAutoExclusive(True)

        self.verticalLayout_3.addWidget(self.btn15)

        self.speciesTabWidget.addTab(self.tab_1, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_7 = QVBoxLayout(self.tab_2)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.btn16 = QPushButton(self.tab_2)
        self.btn16.setObjectName(u"btn16")
        self.btn16.setMinimumSize(QSize(0, 0))
        self.btn16.setMaximumSize(QSize(16777215, 16777215))
        self.btn16.setFont(font4)
        self.btn16.setCheckable(True)
        self.btn16.setAutoExclusive(True)

        self.verticalLayout_7.addWidget(self.btn16)

        self.btn17 = QPushButton(self.tab_2)
        self.btn17.setObjectName(u"btn17")
        self.btn17.setMinimumSize(QSize(0, 0))
        self.btn17.setMaximumSize(QSize(16777215, 16777215))
        self.btn17.setFont(font4)
        self.btn17.setCheckable(True)
        self.btn17.setAutoExclusive(True)

        self.verticalLayout_7.addWidget(self.btn17)

        self.btn18 = QPushButton(self.tab_2)
        self.btn18.setObjectName(u"btn18")
        self.btn18.setMinimumSize(QSize(0, 0))
        self.btn18.setMaximumSize(QSize(16777215, 16777215))
        self.btn18.setFont(font4)
        self.btn18.setCheckable(True)
        self.btn18.setAutoExclusive(True)

        self.verticalLayout_7.addWidget(self.btn18)

        self.btn19 = QPushButton(self.tab_2)
        self.btn19.setObjectName(u"btn19")
        self.btn19.setMinimumSize(QSize(0, 0))
        self.btn19.setMaximumSize(QSize(16777215, 16777215))
        self.btn19.setFont(font4)
        self.btn19.setCheckable(True)
        self.btn19.setAutoExclusive(True)

        self.verticalLayout_7.addWidget(self.btn19)

        self.btn20 = QPushButton(self.tab_2)
        self.btn20.setObjectName(u"btn20")
        self.btn20.setMinimumSize(QSize(0, 0))
        self.btn20.setMaximumSize(QSize(16777215, 16777215))
        self.btn20.setFont(font4)
        self.btn20.setCheckable(True)
        self.btn20.setAutoExclusive(True)

        self.verticalLayout_7.addWidget(self.btn20)

        self.btn21 = QPushButton(self.tab_2)
        self.btn21.setObjectName(u"btn21")

        self.verticalLayout_7.addWidget(self.btn21)

        self.btn22 = QPushButton(self.tab_2)
        self.btn22.setObjectName(u"btn22")

        self.verticalLayout_7.addWidget(self.btn22)

        self.btn23 = QPushButton(self.tab_2)
        self.btn23.setObjectName(u"btn23")

        self.verticalLayout_7.addWidget(self.btn23)

        self.btn24 = QPushButton(self.tab_2)
        self.btn24.setObjectName(u"btn24")

        self.verticalLayout_7.addWidget(self.btn24)

        self.btn25 = QPushButton(self.tab_2)
        self.btn25.setObjectName(u"btn25")

        self.verticalLayout_7.addWidget(self.btn25)

        self.btn26 = QPushButton(self.tab_2)
        self.btn26.setObjectName(u"btn26")

        self.verticalLayout_7.addWidget(self.btn26)

        self.btn27 = QPushButton(self.tab_2)
        self.btn27.setObjectName(u"btn27")

        self.verticalLayout_7.addWidget(self.btn27)

        self.btn28 = QPushButton(self.tab_2)
        self.btn28.setObjectName(u"btn28")

        self.verticalLayout_7.addWidget(self.btn28)

        self.btn29 = QPushButton(self.tab_2)
        self.btn29.setObjectName(u"btn29")

        self.verticalLayout_7.addWidget(self.btn29)

        self.btn30 = QPushButton(self.tab_2)
        self.btn30.setObjectName(u"btn30")

        self.verticalLayout_7.addWidget(self.btn30)

        self.speciesTabWidget.addTab(self.tab_2, "")

        self.verticalLayout_14.addWidget(self.speciesTabWidget)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_3 = QLabel(self.dockWidgetContents_5)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(55, 16777215))

        self.horizontalLayout_7.addWidget(self.label_3)

        self.countInFrameLabel = QLabel(self.dockWidgetContents_5)
        self.countInFrameLabel.setObjectName(u"countInFrameLabel")
        self.countInFrameLabel.setFrameShape(QFrame.Box)

        self.horizontalLayout_7.addWidget(self.countInFrameLabel)


        self.verticalLayout_14.addLayout(self.horizontalLayout_7)

        self.speciesDockWidget.setWidget(self.dockWidgetContents_5)
        SEBASTES.addDockWidget(Qt.DockWidgetArea.RightDockWidgetArea, self.speciesDockWidget)
        self.toolsDockWidget = QDockWidget(SEBASTES)
        self.toolsDockWidget.setObjectName(u"toolsDockWidget")
        self.dockWidgetContents_8 = QWidget()
        self.dockWidgetContents_8.setObjectName(u"dockWidgetContents_8")
        self.verticalLayout_4 = QVBoxLayout(self.dockWidgetContents_8)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.recordBtn = QPushButton(self.dockWidgetContents_8)
        self.recordBtn.setObjectName(u"recordBtn")
        self.recordBtn.setFont(font)
        self.recordBtn.setCheckable(True)

        self.horizontalLayout_3.addWidget(self.recordBtn)

        self.copyBtn = QPushButton(self.dockWidgetContents_8)
        self.copyBtn.setObjectName(u"copyBtn")
        self.copyBtn.setFont(font)

        self.horizontalLayout_3.addWidget(self.copyBtn)

        self.recomputeBtn = QPushButton(self.dockWidgetContents_8)
        self.recomputeBtn.setObjectName(u"recomputeBtn")
        self.recomputeBtn.setFont(font)

        self.horizontalLayout_3.addWidget(self.recomputeBtn)

        self.trainBtn = QPushButton(self.dockWidgetContents_8)
        self.trainBtn.setObjectName(u"trainBtn")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
        sizePolicy1.setHorizontalStretch(105)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.trainBtn.sizePolicy().hasHeightForWidth())
        self.trainBtn.setSizePolicy(sizePolicy1)
        self.trainBtn.setFont(font)
        self.trainBtn.setCheckable(True)

        self.horizontalLayout_3.addWidget(self.trainBtn)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, -1, 5, -1)
        self.label_5 = QLabel(self.dockWidgetContents_8)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout.addWidget(self.label_5)


        self.horizontalLayout_3.addLayout(self.horizontalLayout)

        self.groupBox = QGroupBox(self.dockWidgetContents_8)
        self.groupBox.setObjectName(u"groupBox")
        self.horizontalLayout_20 = QHBoxLayout(self.groupBox)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.monoRadio = QRadioButton(self.groupBox)
        self.monoRadio.setObjectName(u"monoRadio")

        self.horizontalLayout_20.addWidget(self.monoRadio)

        self.stereoRadio = QRadioButton(self.groupBox)
        self.stereoRadio.setObjectName(u"stereoRadio")

        self.horizontalLayout_20.addWidget(self.stereoRadio)


        self.horizontalLayout_3.addWidget(self.groupBox)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.measureBtn = QPushButton(self.dockWidgetContents_8)
        self.measureBtn.setObjectName(u"measureBtn")
        self.measureBtn.setMaximumSize(QSize(16777215, 16777215))
        self.measureBtn.setFont(font)
        self.measureBtn.setCheckable(True)

        self.horizontalLayout_3.addWidget(self.measureBtn)

        self.label_8 = QLabel(self.dockWidgetContents_8)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_3.addWidget(self.label_8)

        self.measurementBox = QComboBox(self.dockWidgetContents_8)
        self.measurementBox.setObjectName(u"measurementBox")

        self.horizontalLayout_3.addWidget(self.measurementBox)

        self.linkBtn = QPushButton(self.dockWidgetContents_8)
        self.linkBtn.setObjectName(u"linkBtn")
        self.linkBtn.setMaximumSize(QSize(16777215, 16777215))
        self.linkBtn.setFont(font)
        self.linkBtn.setCheckable(True)

        self.horizontalLayout_3.addWidget(self.linkBtn)

        self.editSpeciesBtn = QPushButton(self.dockWidgetContents_8)
        self.editSpeciesBtn.setObjectName(u"editSpeciesBtn")

        self.horizontalLayout_3.addWidget(self.editSpeciesBtn)

        self.label_4 = QLabel(self.dockWidgetContents_8)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_3.addWidget(self.label_4)

        self.targetLinkLabel = QLabel(self.dockWidgetContents_8)
        self.targetLinkLabel.setObjectName(u"targetLinkLabel")
        self.targetLinkLabel.setMinimumSize(QSize(21, 0))
        self.targetLinkLabel.setFrameShape(QFrame.Box)

        self.horizontalLayout_3.addWidget(self.targetLinkLabel)

        self.delLinkBtn = QPushButton(self.dockWidgetContents_8)
        self.delLinkBtn.setObjectName(u"delLinkBtn")

        self.horizontalLayout_3.addWidget(self.delLinkBtn)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_8)

        self.targetCommentBtn = QPushButton(self.dockWidgetContents_8)
        self.targetCommentBtn.setObjectName(u"targetCommentBtn")
        self.targetCommentBtn.setFont(font)

        self.horizontalLayout_3.addWidget(self.targetCommentBtn)

        self.frameCommentBtn = QPushButton(self.dockWidgetContents_8)
        self.frameCommentBtn.setObjectName(u"frameCommentBtn")
        self.frameCommentBtn.setFont(font)
        self.frameCommentBtn.setCheckable(True)

        self.horizontalLayout_3.addWidget(self.frameCommentBtn)


        self.verticalLayout_4.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.computeMatchBox = QCheckBox(self.dockWidgetContents_8)
        self.computeMatchBox.setObjectName(u"computeMatchBox")
        self.computeMatchBox.setFont(font)

        self.horizontalLayout_2.addWidget(self.computeMatchBox)

        self.matchThresholdEdit = QLineEdit(self.dockWidgetContents_8)
        self.matchThresholdEdit.setObjectName(u"matchThresholdEdit")
        self.matchThresholdEdit.setMaximumSize(QSize(41, 16777215))
        self.matchThresholdEdit.setFont(font2)
        self.matchThresholdEdit.setInputMethodHints(Qt.ImhPreferNumbers)

        self.horizontalLayout_2.addWidget(self.matchThresholdEdit)

        self.label_2 = QLabel(self.dockWidgetContents_8)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)

        self.horizontalLayout_2.addWidget(self.label_2)

        self.stereoOnlyCheckBox = QCheckBox(self.dockWidgetContents_8)
        self.stereoOnlyCheckBox.setObjectName(u"stereoOnlyCheckBox")

        self.horizontalLayout_2.addWidget(self.stereoOnlyCheckBox)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_4)

        self.metadataCheckBox = QCheckBox(self.dockWidgetContents_8)
        self.metadataCheckBox.setObjectName(u"metadataCheckBox")

        self.horizontalLayout_2.addWidget(self.metadataCheckBox)

        self.closeupCheck = QCheckBox(self.dockWidgetContents_8)
        self.closeupCheck.setObjectName(u"closeupCheck")
        self.closeupCheck.setFont(font)

        self.horizontalLayout_2.addWidget(self.closeupCheck)

        self.labelCheck = QCheckBox(self.dockWidgetContents_8)
        self.labelCheck.setObjectName(u"labelCheck")
        self.labelCheck.setFont(font)
        self.labelCheck.setChecked(True)

        self.horizontalLayout_2.addWidget(self.labelCheck)

        self.showDataCheck = QCheckBox(self.dockWidgetContents_8)
        self.showDataCheck.setObjectName(u"showDataCheck")
        self.showDataCheck.setFont(font)

        self.horizontalLayout_2.addWidget(self.showDataCheck)

        self.gridCheck = QCheckBox(self.dockWidgetContents_8)
        self.gridCheck.setObjectName(u"gridCheck")

        self.horizontalLayout_2.addWidget(self.gridCheck)

        self.clearGridBtn = QPushButton(self.dockWidgetContents_8)
        self.clearGridBtn.setObjectName(u"clearGridBtn")

        self.horizontalLayout_2.addWidget(self.clearGridBtn)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_7)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.playBtn = QPushButton(self.dockWidgetContents_8)
        self.playBtn.setObjectName(u"playBtn")
        self.playBtn.setFont(font)
        self.playBtn.setCheckable(True)

        self.horizontalLayout_4.addWidget(self.playBtn)

        self.playSpeedSlider = QSlider(self.dockWidgetContents_8)
        self.playSpeedSlider.setObjectName(u"playSpeedSlider")
        self.playSpeedSlider.setMinimumSize(QSize(51, 0))
        self.playSpeedSlider.setMinimum(1)
        self.playSpeedSlider.setMaximum(100)
        self.playSpeedSlider.setSingleStep(10)
        self.playSpeedSlider.setOrientation(Qt.Horizontal)

        self.horizontalLayout_4.addWidget(self.playSpeedSlider)


        self.horizontalLayout_2.addLayout(self.horizontalLayout_4)


        self.verticalLayout_4.addLayout(self.horizontalLayout_2)

        self.toolsDockWidget.setWidget(self.dockWidgetContents_8)
        SEBASTES.addDockWidget(Qt.DockWidgetArea.TopDockWidgetArea, self.toolsDockWidget)

        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuFile.addAction(self.actionLoad)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionCreate_New_Project)
        self.menuFile.addAction(self.actionProfiles)
        self.menuFile.addAction(self.actionGUI_settings)
        self.menuFile.addAction(self.actionGrid_setup)
        self.menuFile.addAction(self.actionSet_Active_Profiles)
        self.menuFile.addAction(self.actionImport_Export_Profiles)
        self.menuFile.addAction(self.actionviewApplicationDB)
        self.menuFile.addAction(self.actionedit_DB_tables)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)

        self.retranslateUi(SEBASTES)

        self.speciesTabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(SEBASTES)
    # setupUi

    def retranslateUi(self, SEBASTES):
        SEBASTES.setWindowTitle(QCoreApplication.translate("SEBASTES", u"SEBASTES", None))
        self.actionLoad.setText(QCoreApplication.translate("SEBASTES", u"Load Deployment...", None))
        self.actionExit.setText(QCoreApplication.translate("SEBASTES", u"Exit", None))
        self.actionProfiles.setText(QCoreApplication.translate("SEBASTES", u"Setup Profiles, Species, Etc", None))
#if QT_CONFIG(tooltip)
        self.actionProfiles.setToolTip(QCoreApplication.translate("SEBASTES", u"create and edit profiles", None))
#endif // QT_CONFIG(tooltip)
        self.actionGUI_settings.setText(QCoreApplication.translate("SEBASTES", u"GUI settings", None))
#if QT_CONFIG(tooltip)
        self.actionGUI_settings.setToolTip(QCoreApplication.translate("SEBASTES", u"Change fonts and line colors etc.", None))
#endif // QT_CONFIG(tooltip)
        self.actionGrid_setup.setText(QCoreApplication.translate("SEBASTES", u"Grid setup", None))
        self.actionSet_Active_Profiles.setText(QCoreApplication.translate("SEBASTES", u"Set Active Profiles, Species Etc.", None))
#if QT_CONFIG(tooltip)
        self.actionSet_Active_Profiles.setToolTip(QCoreApplication.translate("SEBASTES", u"Set which profiles, metadata group and species groups can be selected", None))
#endif // QT_CONFIG(tooltip)
        self.actionImport_Export_Profiles.setText(QCoreApplication.translate("SEBASTES", u"Import/Export Profiles", None))
#if QT_CONFIG(tooltip)
        self.actionImport_Export_Profiles.setToolTip(QCoreApplication.translate("SEBASTES", u"Import or export profiles from text files", None))
#endif // QT_CONFIG(tooltip)
        self.actionCreate_New_Project.setText(QCoreApplication.translate("SEBASTES", u"Create New Project", None))
#if QT_CONFIG(tooltip)
        self.actionCreate_New_Project.setToolTip(QCoreApplication.translate("SEBASTES", u"create new projects", None))
#endif // QT_CONFIG(tooltip)
        self.actionviewApplicationDB.setText(QCoreApplication.translate("SEBASTES", u"view Application DB", None))
#if QT_CONFIG(tooltip)
        self.actionviewApplicationDB.setToolTip(QCoreApplication.translate("SEBASTES", u"view teh application level database (read only)", None))
#endif // QT_CONFIG(tooltip)
        self.actionedit_DB_tables.setText(QCoreApplication.translate("SEBASTES", u"edit DB tables", None))
#if QT_CONFIG(tooltip)
        self.actionedit_DB_tables.setToolTip(QCoreApplication.translate("SEBASTES", u"edit databaset tables", None))
#endif // QT_CONFIG(tooltip)
        self.deploymentBox.setText(QCoreApplication.translate("SEBASTES", u"No deployment loaded", None))
        self.label_7.setText(QCoreApplication.translate("SEBASTES", u"Annotator", None))
        self.label.setText(QCoreApplication.translate("SEBASTES", u"\\", None))
        self.lastFrameBtn.setText(QCoreApplication.translate("SEBASTES", u"Go to last \n"
"sampled frame", None))
        self.label_18.setText(QCoreApplication.translate("SEBASTES", u"Sample Interval", None))
        self.maxFrame.setText(QCoreApplication.translate("SEBASTES", u"0", None))
        self.label_20.setText(QCoreApplication.translate("SEBASTES", u"Offset", None))
        self.label_6.setText(QCoreApplication.translate("SEBASTES", u"Frame Number", None))
        self.annotatorLabel.setText("")
        self.adjLeftBtn.setText(QCoreApplication.translate("SEBASTES", u"Adjust image", None))
        self.adjRightBtn.setText(QCoreApplication.translate("SEBASTES", u"Adjust Image", None))
        self.minFrame.setText(QCoreApplication.translate("SEBASTES", u"0", None))
        self.menuFile.setTitle(QCoreApplication.translate("SEBASTES", u"File", None))
        self.metadataDockWidget.setWindowTitle(QCoreApplication.translate("SEBASTES", u"Habitat", None))
        self.exclusiveRadioBox1.setTitle(QCoreApplication.translate("SEBASTES", u"Primary", None))
        self.radioButton1_1.setText(QCoreApplication.translate("SEBASTES", u"RadioButton", None))
        self.radioButton1_2.setText(QCoreApplication.translate("SEBASTES", u"RadioButton", None))
        self.radioButton1_3.setText(QCoreApplication.translate("SEBASTES", u"RadioButton", None))
        self.radioButton1_4.setText(QCoreApplication.translate("SEBASTES", u"RadioButton", None))
        self.radioButton1_5.setText(QCoreApplication.translate("SEBASTES", u"RadioButton", None))
        self.radioButton1_6.setText(QCoreApplication.translate("SEBASTES", u"RadioButton", None))
        self.radioButton1_7.setText(QCoreApplication.translate("SEBASTES", u"RadioButton", None))
        self.radioButton1_8.setText(QCoreApplication.translate("SEBASTES", u"RadioButton", None))
        self.radioButton1_9.setText(QCoreApplication.translate("SEBASTES", u"RadioButton", None))
        self.radioButton1_10.setText(QCoreApplication.translate("SEBASTES", u"RadioButton", None))
        self.exclusiveRadioBox2.setTitle(QCoreApplication.translate("SEBASTES", u"Secondary", None))
        self.radioButton2_1.setText(QCoreApplication.translate("SEBASTES", u"RadioButton", None))
        self.radioButton2_2.setText(QCoreApplication.translate("SEBASTES", u"RadioButton", None))
        self.radioButton2_3.setText(QCoreApplication.translate("SEBASTES", u"RadioButton", None))
        self.radioButton2_4.setText(QCoreApplication.translate("SEBASTES", u"RadioButton", None))
        self.radioButton2_5.setText(QCoreApplication.translate("SEBASTES", u"RadioButton", None))
        self.radioButton2_6.setText(QCoreApplication.translate("SEBASTES", u"RadioButton", None))
        self.radioButton2_7.setText(QCoreApplication.translate("SEBASTES", u"RadioButton", None))
        self.radioButton2_8.setText(QCoreApplication.translate("SEBASTES", u"RadioButton", None))
        self.radioButton2_9.setText(QCoreApplication.translate("SEBASTES", u"RadioButton", None))
        self.radioButton2_10.setText(QCoreApplication.translate("SEBASTES", u"RadioButton", None))
        self.exclusiveRadioBox3.setTitle(QCoreApplication.translate("SEBASTES", u"GroupBox", None))
        self.radioButton3_1.setText(QCoreApplication.translate("SEBASTES", u"RadioButton", None))
        self.radioButton3_2.setText(QCoreApplication.translate("SEBASTES", u"RadioButton", None))
        self.metadataStickyBox.setText(QCoreApplication.translate("SEBASTES", u"retain selection", None))
        self.metadataTypeLabel2.setText(QCoreApplication.translate("SEBASTES", u"Coverage", None))
        self.label1_1.setText(QCoreApplication.translate("SEBASTES", u"TextLabel", None))
        self.label1_2.setText(QCoreApplication.translate("SEBASTES", u"TextLabel", None))
        self.label1_3.setText(QCoreApplication.translate("SEBASTES", u"TextLabel", None))
        self.label1_4.setText(QCoreApplication.translate("SEBASTES", u"TextLabel", None))
        self.label1_5.setText(QCoreApplication.translate("SEBASTES", u"TextLabel", None))
        self.metadataTypeLabel3.setText(QCoreApplication.translate("SEBASTES", u"Presence/abscence", None))
        self.checkBox1_1.setText(QCoreApplication.translate("SEBASTES", u"CheckBox", None))
        self.checkBox1_2.setText(QCoreApplication.translate("SEBASTES", u"CheckBox", None))
        self.checkBox1_3.setText(QCoreApplication.translate("SEBASTES", u"CheckBox", None))
        self.checkBox1_4.setText(QCoreApplication.translate("SEBASTES", u"CheckBox", None))
        self.checkBox1_5.setText(QCoreApplication.translate("SEBASTES", u"CheckBox", None))
        self.speciesDockWidget.setWindowTitle(QCoreApplication.translate("SEBASTES", u"Species", None))
        self.btn1.setText("")
        self.btn2.setText("")
        self.btn3.setText("")
        self.btn4.setText("")
        self.btn5.setText("")
        self.btn6.setText("")
        self.btn7.setText("")
        self.btn8.setText("")
        self.btn9.setText("")
        self.btn10.setText("")
        self.btn11.setText("")
        self.btn12.setText("")
        self.btn13.setText("")
        self.btn14.setText("")
        self.btn15.setText("")
        self.speciesTabWidget.setTabText(self.speciesTabWidget.indexOf(self.tab_1), QCoreApplication.translate("SEBASTES", u"Species List 1", None))
        self.btn16.setText("")
        self.btn17.setText("")
        self.btn18.setText("")
        self.btn19.setText("")
        self.btn20.setText("")
        self.btn21.setText("")
        self.btn22.setText("")
        self.btn23.setText("")
        self.btn24.setText("")
        self.btn25.setText("")
        self.btn26.setText("")
        self.btn27.setText("")
        self.btn28.setText("")
        self.btn29.setText("")
        self.btn30.setText("")
        self.speciesTabWidget.setTabText(self.speciesTabWidget.indexOf(self.tab_2), QCoreApplication.translate("SEBASTES", u"Species List 2", None))
        self.label_3.setText(QCoreApplication.translate("SEBASTES", u"Count in \n"
"frame", None))
        self.countInFrameLabel.setText("")
        self.toolsDockWidget.setWindowTitle(QCoreApplication.translate("SEBASTES", u"Tools", None))
        self.recordBtn.setText(QCoreApplication.translate("SEBASTES", u"Record", None))
        self.copyBtn.setText(QCoreApplication.translate("SEBASTES", u"Copy Images to...", None))
        self.recomputeBtn.setText(QCoreApplication.translate("SEBASTES", u"Recompute 3D", None))
        self.trainBtn.setText(QCoreApplication.translate("SEBASTES", u"Create training set", None))
        self.label_5.setText(QCoreApplication.translate("SEBASTES", u"Mode: ", None))
        self.groupBox.setTitle("")
        self.monoRadio.setText(QCoreApplication.translate("SEBASTES", u"Mono", None))
        self.stereoRadio.setText(QCoreApplication.translate("SEBASTES", u"Stereo", None))
        self.measureBtn.setText(QCoreApplication.translate("SEBASTES", u"Measure Target", None))
        self.label_8.setText(QCoreApplication.translate("SEBASTES", u"Measurement type", None))
        self.linkBtn.setText(QCoreApplication.translate("SEBASTES", u"Link Target", None))
        self.editSpeciesBtn.setText(QCoreApplication.translate("SEBASTES", u"Edit Species", None))
        self.label_4.setText(QCoreApplication.translate("SEBASTES", u"Selected target:", None))
        self.targetLinkLabel.setText("")
        self.delLinkBtn.setText(QCoreApplication.translate("SEBASTES", u"Delete Link", None))
        self.targetCommentBtn.setText(QCoreApplication.translate("SEBASTES", u"Target Comment", None))
        self.frameCommentBtn.setText(QCoreApplication.translate("SEBASTES", u"Frame Comment", None))
        self.computeMatchBox.setText(QCoreApplication.translate("SEBASTES", u"Auto Match", None))
        self.label_2.setText(QCoreApplication.translate("SEBASTES", u"Match Threshold", None))
        self.stereoOnlyCheckBox.setText(QCoreApplication.translate("SEBASTES", u"Stereo Targets Only", None))
        self.metadataCheckBox.setText(QCoreApplication.translate("SEBASTES", u"Collect metadata", None))
        self.closeupCheck.setText(QCoreApplication.translate("SEBASTES", u"Show Closeup Window", None))
        self.labelCheck.setText(QCoreApplication.translate("SEBASTES", u"Show Labels", None))
        self.showDataCheck.setText(QCoreApplication.translate("SEBASTES", u"Show Data", None))
        self.gridCheck.setText(QCoreApplication.translate("SEBASTES", u"Grid Overlay", None))
        self.clearGridBtn.setText(QCoreApplication.translate("SEBASTES", u"Clear Grid Data", None))
        self.playBtn.setText(QCoreApplication.translate("SEBASTES", u"Play", None))
    # retranslateUi

