# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'EvrDlg.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QDialog, QFormLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QWidget)

class Ui_EvrDlg(object):
    def setupUi(self, EvrDlg):
        if not EvrDlg.objectName():
            EvrDlg.setObjectName(u"EvrDlg")
        EvrDlg.resize(239, 165)
        self.formLayout = QFormLayout(EvrDlg)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setFieldGrowthPolicy(QFormLayout.AllNonFixedFieldsGrow)
        self.regSize = QLineEdit(EvrDlg)
        self.regSize.setObjectName(u"regSize")
        self.regSize.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.regSize)

        self.label = QLabel(EvrDlg)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label)

        self.label_2 = QLabel(EvrDlg)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(100, 0))

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_2)

        self.vertDens = QLineEdit(EvrDlg)
        self.vertDens.setObjectName(u"vertDens")
        self.vertDens.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.vertDens)

        self.label_3 = QLabel(EvrDlg)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.label_3)

        self.regHeight = QLineEdit(EvrDlg)
        self.regHeight.setObjectName(u"regHeight")
        self.regHeight.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.regHeight)

        self.evlCheckBox = QCheckBox(EvrDlg)
        self.evlCheckBox.setObjectName(u"evlCheckBox")
        self.evlCheckBox.setChecked(True)

        self.formLayout.setWidget(4, QFormLayout.ItemRole.LabelRole, self.evlCheckBox)

        self.cancelBtn = QPushButton(EvrDlg)
        self.cancelBtn.setObjectName(u"cancelBtn")

        self.formLayout.setWidget(5, QFormLayout.ItemRole.LabelRole, self.cancelBtn)

        self.okBtn = QPushButton(EvrDlg)
        self.okBtn.setObjectName(u"okBtn")

        self.formLayout.setWidget(5, QFormLayout.ItemRole.FieldRole, self.okBtn)

        self.mergeCheckBox = QCheckBox(EvrDlg)
        self.mergeCheckBox.setObjectName(u"mergeCheckBox")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.mergeCheckBox)


        self.retranslateUi(EvrDlg)

        QMetaObject.connectSlotsByName(EvrDlg)
    # setupUi

    def retranslateUi(self, EvrDlg):
        EvrDlg.setWindowTitle(QCoreApplication.translate("EvrDlg", u"EchoView region file", None))
        self.regSize.setText(QCoreApplication.translate("EvrDlg", u"200", None))
        self.label.setText(QCoreApplication.translate("EvrDlg", u"Region Size in Frames", None))
        self.label_2.setText(QCoreApplication.translate("EvrDlg", u"Vertex density in Frames", None))
        self.vertDens.setText(QCoreApplication.translate("EvrDlg", u"20", None))
        self.label_3.setText(QCoreApplication.translate("EvrDlg", u"Region Height in Meters", None))
        self.regHeight.setText(QCoreApplication.translate("EvrDlg", u"20", None))
        self.evlCheckBox.setText(QCoreApplication.translate("EvrDlg", u"Create evl File", None))
        self.cancelBtn.setText(QCoreApplication.translate("EvrDlg", u"Cancel", None))
        self.okBtn.setText(QCoreApplication.translate("EvrDlg", u"Proceed", None))
        self.mergeCheckBox.setText(QCoreApplication.translate("EvrDlg", u"Merge Adjacent Regions", None))
    # retranslateUi

