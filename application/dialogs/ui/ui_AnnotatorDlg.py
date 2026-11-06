# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'AnnotatorDlg.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_annotatorDlg(object):
    def setupUi(self, annotatorDlg):
        if not annotatorDlg.objectName():
            annotatorDlg.setObjectName(u"annotatorDlg")
        annotatorDlg.resize(264, 120)
        self.verticalLayout = QVBoxLayout(annotatorDlg)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(annotatorDlg)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(12)
        self.label.setFont(font)

        self.verticalLayout.addWidget(self.label)

        self.annotatorEdit = QLineEdit(annotatorDlg)
        self.annotatorEdit.setObjectName(u"annotatorEdit")
        self.annotatorEdit.setFont(font)

        self.verticalLayout.addWidget(self.annotatorEdit)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.cancelBtn = QPushButton(annotatorDlg)
        self.cancelBtn.setObjectName(u"cancelBtn")
        font1 = QFont()
        font1.setPointSize(8)
        self.cancelBtn.setFont(font1)
        self.cancelBtn.setFocusPolicy(Qt.NoFocus)

        self.horizontalLayout.addWidget(self.cancelBtn)

        self.okBtn = QPushButton(annotatorDlg)
        self.okBtn.setObjectName(u"okBtn")
        self.okBtn.setFont(font1)

        self.horizontalLayout.addWidget(self.okBtn)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(annotatorDlg)

        QMetaObject.connectSlotsByName(annotatorDlg)
    # setupUi

    def retranslateUi(self, annotatorDlg):
        annotatorDlg.setWindowTitle(QCoreApplication.translate("annotatorDlg", u"Tell me about yourself...", None))
        self.label.setText(QCoreApplication.translate("annotatorDlg", u"Your initials please", None))
        self.cancelBtn.setText(QCoreApplication.translate("annotatorDlg", u"Cancel", None))
        self.okBtn.setText(QCoreApplication.translate("annotatorDlg", u"OK", None))
    # retranslateUi

