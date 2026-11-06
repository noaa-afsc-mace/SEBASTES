# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'GridSetupDlg.ui'
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
    QFormLayout, QFrame, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_gridSetupDlg(object):
    def setupUi(self, gridSetupDlg):
        if not gridSetupDlg.objectName():
            gridSetupDlg.setObjectName(u"gridSetupDlg")
        gridSetupDlg.resize(398, 242)
        self.verticalLayout = QVBoxLayout(gridSetupDlg)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label_2 = QLabel(gridSetupDlg)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_2)

        self.gridSizeBox = QComboBox(gridSetupDlg)
        self.gridSizeBox.setObjectName(u"gridSizeBox")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.gridSizeBox)

        self.label_4 = QLabel(gridSetupDlg)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.label_4)

        self.lineThicknessBox = QComboBox(gridSetupDlg)
        self.lineThicknessBox.setObjectName(u"lineThicknessBox")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.lineThicknessBox)

        self.label_3 = QLabel(gridSetupDlg)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(5, QFormLayout.ItemRole.LabelRole, self.label_3)

        self.randomCheck = QCheckBox(gridSetupDlg)
        self.randomCheck.setObjectName(u"randomCheck")

        self.formLayout.setWidget(5, QFormLayout.ItemRole.FieldRole, self.randomCheck)

        self.label = QLabel(gridSetupDlg)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.gridlineColorLabel = QLabel(gridSetupDlg)
        self.gridlineColorLabel.setObjectName(u"gridlineColorLabel")
        self.gridlineColorLabel.setMinimumSize(QSize(51, 0))
        self.gridlineColorLabel.setFrameShape(QFrame.Box)

        self.horizontalLayout_15.addWidget(self.gridlineColorLabel)

        self.gridlineColorBtn = QPushButton(gridSetupDlg)
        self.gridlineColorBtn.setObjectName(u"gridlineColorBtn")

        self.horizontalLayout_15.addWidget(self.gridlineColorBtn)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_7)


        self.formLayout.setLayout(1, QFormLayout.ItemRole.FieldRole, self.horizontalLayout_15)

        self.label_5 = QLabel(gridSetupDlg)
        self.label_5.setObjectName(u"label_5")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.label_5)

        self.lineStyleBox = QComboBox(gridSetupDlg)
        self.lineStyleBox.setObjectName(u"lineStyleBox")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.lineStyleBox)

        self.label_6 = QLabel(gridSetupDlg)
        self.label_6.setObjectName(u"label_6")

        self.formLayout.setWidget(7, QFormLayout.ItemRole.LabelRole, self.label_6)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.cellColorLabel = QLabel(gridSetupDlg)
        self.cellColorLabel.setObjectName(u"cellColorLabel")
        self.cellColorLabel.setMinimumSize(QSize(51, 0))
        self.cellColorLabel.setFrameShape(QFrame.Box)

        self.horizontalLayout_14.addWidget(self.cellColorLabel)

        self.cellColorBtn = QPushButton(gridSetupDlg)
        self.cellColorBtn.setObjectName(u"cellColorBtn")

        self.horizontalLayout_14.addWidget(self.cellColorBtn)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_6)


        self.formLayout.setLayout(7, QFormLayout.ItemRole.FieldRole, self.horizontalLayout_14)

        self.label_7 = QLabel(gridSetupDlg)
        self.label_7.setObjectName(u"label_7")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.LabelRole, self.label_7)

        self.persistentGridBox = QCheckBox(gridSetupDlg)
        self.persistentGridBox.setObjectName(u"persistentGridBox")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.FieldRole, self.persistentGridBox)

        self.label_8 = QLabel(gridSetupDlg)
        self.label_8.setObjectName(u"label_8")

        self.formLayout.setWidget(6, QFormLayout.ItemRole.LabelRole, self.label_8)

        self.cellBoundaryBox = QCheckBox(gridSetupDlg)
        self.cellBoundaryBox.setObjectName(u"cellBoundaryBox")

        self.formLayout.setWidget(6, QFormLayout.ItemRole.FieldRole, self.cellBoundaryBox)


        self.verticalLayout.addLayout(self.formLayout)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.cancelBtn = QPushButton(gridSetupDlg)
        self.cancelBtn.setObjectName(u"cancelBtn")

        self.horizontalLayout.addWidget(self.cancelBtn)

        self.okBtn = QPushButton(gridSetupDlg)
        self.okBtn.setObjectName(u"okBtn")

        self.horizontalLayout.addWidget(self.okBtn)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(gridSetupDlg)

        QMetaObject.connectSlotsByName(gridSetupDlg)
    # setupUi

    def retranslateUi(self, gridSetupDlg):
        gridSetupDlg.setWindowTitle(QCoreApplication.translate("gridSetupDlg", u"Grid Setup", None))
        self.label_2.setText(QCoreApplication.translate("gridSetupDlg", u"Grid Size", None))
        self.label_4.setText(QCoreApplication.translate("gridSetupDlg", u"Line Thickness", None))
        self.label_3.setText(QCoreApplication.translate("gridSetupDlg", u"Radomize Cell", None))
        self.randomCheck.setText("")
        self.label.setText(QCoreApplication.translate("gridSetupDlg", u"Grid Line Color", None))
        self.gridlineColorLabel.setText("")
        self.gridlineColorBtn.setText(QCoreApplication.translate("gridSetupDlg", u"Select color", None))
        self.label_5.setText(QCoreApplication.translate("gridSetupDlg", u"Grid Line Style", None))
        self.label_6.setText(QCoreApplication.translate("gridSetupDlg", u"Cell Color", None))
        self.cellColorLabel.setText("")
        self.cellColorBtn.setText(QCoreApplication.translate("gridSetupDlg", u"Select color", None))
        self.label_7.setText(QCoreApplication.translate("gridSetupDlg", u"Persistent Grid?", None))
        self.persistentGridBox.setText("")
        self.label_8.setText(QCoreApplication.translate("gridSetupDlg", u"Enforce Cell Boundary?", None))
        self.cellBoundaryBox.setText("")
        self.cancelBtn.setText(QCoreApplication.translate("gridSetupDlg", u"Cancel", None))
        self.okBtn.setText(QCoreApplication.translate("gridSetupDlg", u"OK", None))
    # retranslateUi

