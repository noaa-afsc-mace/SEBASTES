# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ClassDlg.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QHBoxLayout,
    QListWidget, QListWidgetItem, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_classDlg(object):
    def setupUi(self, classDlg):
        if not classDlg.objectName():
            classDlg.setObjectName(u"classDlg")
        classDlg.resize(212, 298)
        self.verticalLayout = QVBoxLayout(classDlg)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.listWidget = QListWidget(classDlg)
        self.listWidget.setObjectName(u"listWidget")

        self.verticalLayout.addWidget(self.listWidget)

        self.addBtn = QPushButton(classDlg)
        self.addBtn.setObjectName(u"addBtn")

        self.verticalLayout.addWidget(self.addBtn)

        self.frame = QFrame(classDlg)
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


        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(classDlg)

        QMetaObject.connectSlotsByName(classDlg)
    # setupUi

    def retranslateUi(self, classDlg):
        classDlg.setWindowTitle(QCoreApplication.translate("classDlg", u"Select a class", None))
        self.addBtn.setText(QCoreApplication.translate("classDlg", u"Add New Class", None))
        self.cancelBtn.setText(QCoreApplication.translate("classDlg", u"Cancel", None))
        self.okBtn.setText(QCoreApplication.translate("classDlg", u"OK", None))
    # retranslateUi

