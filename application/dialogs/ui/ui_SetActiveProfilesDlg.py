# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'SetActiveProfilesDlg.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_setActiveProfilesDlg(object):
    def setupUi(self, setActiveProfilesDlg):
        if not setActiveProfilesDlg.objectName():
            setActiveProfilesDlg.setObjectName(u"setActiveProfilesDlg")
        setActiveProfilesDlg.resize(230, 196)
        self.verticalLayout = QVBoxLayout(setActiveProfilesDlg)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.setProjectsBtn = QPushButton(setActiveProfilesDlg)
        self.setProjectsBtn.setObjectName(u"setProjectsBtn")

        self.verticalLayout.addWidget(self.setProjectsBtn)

        self.setProfilesBtn = QPushButton(setActiveProfilesDlg)
        self.setProfilesBtn.setObjectName(u"setProfilesBtn")

        self.verticalLayout.addWidget(self.setProfilesBtn)

        self.setSpcCollectionsBtn = QPushButton(setActiveProfilesDlg)
        self.setSpcCollectionsBtn.setObjectName(u"setSpcCollectionsBtn")

        self.verticalLayout.addWidget(self.setSpcCollectionsBtn)

        self.setMetaGroupsBtn = QPushButton(setActiveProfilesDlg)
        self.setMetaGroupsBtn.setObjectName(u"setMetaGroupsBtn")

        self.verticalLayout.addWidget(self.setMetaGroupsBtn)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.okBtn = QPushButton(setActiveProfilesDlg)
        self.okBtn.setObjectName(u"okBtn")

        self.horizontalLayout.addWidget(self.okBtn)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(setActiveProfilesDlg)

        QMetaObject.connectSlotsByName(setActiveProfilesDlg)
    # setupUi

    def retranslateUi(self, setActiveProfilesDlg):
        setActiveProfilesDlg.setWindowTitle(QCoreApplication.translate("setActiveProfilesDlg", u"Set Active Profiles", None))
        self.setProjectsBtn.setText(QCoreApplication.translate("setActiveProfilesDlg", u"Set Active Projects", None))
        self.setProfilesBtn.setText(QCoreApplication.translate("setActiveProfilesDlg", u"Set Active Profiles", None))
        self.setSpcCollectionsBtn.setText(QCoreApplication.translate("setActiveProfilesDlg", u"Set Active Species Collections", None))
        self.setMetaGroupsBtn.setText(QCoreApplication.translate("setActiveProfilesDlg", u"Set Active Metadata Groups", None))
        self.okBtn.setText(QCoreApplication.translate("setActiveProfilesDlg", u"OK", None))
    # retranslateUi

