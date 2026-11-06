# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'CameraDlg.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFormLayout, QFrame,
    QHBoxLayout, QLabel, QLineEdit, QPlainTextEdit,
    QPushButton, QSizePolicy, QSpacerItem, QTextEdit,
    QWidget)

class Ui_cameraDlg(object):
    def setupUi(self, cameraDlg):
        if not cameraDlg.objectName():
            cameraDlg.setObjectName(u"cameraDlg")
        cameraDlg.resize(400, 381)
        self.formLayout = QFormLayout(cameraDlg)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setFieldGrowthPolicy(QFormLayout.AllNonFixedFieldsGrow)
        self.label = QLabel(cameraDlg)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label)

        self.cameraGearBox = QLineEdit(cameraDlg)
        self.cameraGearBox.setObjectName(u"cameraGearBox")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.cameraGearBox)

        self.label_8 = QLabel(cameraDlg)
        self.label_8.setObjectName(u"label_8")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.label_8)

        self.lCameraDesc = QPlainTextEdit(cameraDlg)
        self.lCameraDesc.setObjectName(u"lCameraDesc")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.lCameraDesc)

        self.label_2 = QLabel(cameraDlg)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.label_2)

        self.rCameraDesc = QTextEdit(cameraDlg)
        self.rCameraDesc.setObjectName(u"rCameraDesc")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.rCameraDesc)

        self.frame = QFrame(cameraDlg)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 40))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.cancelBtn = QPushButton(self.frame)
        self.cancelBtn.setObjectName(u"cancelBtn")

        self.horizontalLayout.addWidget(self.cancelBtn)

        self.okBtn = QPushButton(self.frame)
        self.okBtn.setObjectName(u"okBtn")

        self.horizontalLayout.addWidget(self.okBtn)


        self.formLayout.setWidget(6, QFormLayout.ItemRole.FieldRole, self.frame)

        self.bsEdit = QLineEdit(cameraDlg)
        self.bsEdit.setObjectName(u"bsEdit")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.FieldRole, self.bsEdit)

        self.label_3 = QLabel(cameraDlg)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.LabelRole, self.label_3)

        self.descEdit = QTextEdit(cameraDlg)
        self.descEdit.setObjectName(u"descEdit")

        self.formLayout.setWidget(5, QFormLayout.ItemRole.FieldRole, self.descEdit)

        self.label_4 = QLabel(cameraDlg)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(5, QFormLayout.ItemRole.LabelRole, self.label_4)


        self.retranslateUi(cameraDlg)

        QMetaObject.connectSlotsByName(cameraDlg)
    # setupUi

    def retranslateUi(self, cameraDlg):
        cameraDlg.setWindowTitle(QCoreApplication.translate("cameraDlg", u"Camera Gear", None))
        self.label.setText(QCoreApplication.translate("cameraDlg", u"Camera Gear", None))
        self.label_8.setText(QCoreApplication.translate("cameraDlg", u"Left Camera", None))
        self.label_2.setText(QCoreApplication.translate("cameraDlg", u"Right Camera", None))
        self.cancelBtn.setText(QCoreApplication.translate("cameraDlg", u"cancel", None))
        self.okBtn.setText(QCoreApplication.translate("cameraDlg", u"OK", None))
        self.label_3.setText(QCoreApplication.translate("cameraDlg", u"Baseline \n"
"separation", None))
        self.label_4.setText(QCoreApplication.translate("cameraDlg", u"Description", None))
    # retranslateUi

