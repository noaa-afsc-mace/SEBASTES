# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ExportProfileDlg.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QGroupBox, QHBoxLayout,
    QPushButton, QRadioButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_exportProfileDlg(object):
    def setupUi(self, exportProfileDlg):
        if not exportProfileDlg.objectName():
            exportProfileDlg.setObjectName(u"exportProfileDlg")
        exportProfileDlg.resize(333, 186)
        self.verticalLayout = QVBoxLayout(exportProfileDlg)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox = QGroupBox(exportProfileDlg)
        self.groupBox.setObjectName(u"groupBox")
        self.horizontalLayout_2 = QHBoxLayout(self.groupBox)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.importRadio = QRadioButton(self.groupBox)
        self.importRadio.setObjectName(u"importRadio")

        self.horizontalLayout_2.addWidget(self.importRadio)

        self.exportRadio = QRadioButton(self.groupBox)
        self.exportRadio.setObjectName(u"exportRadio")

        self.horizontalLayout_2.addWidget(self.exportRadio)


        self.verticalLayout.addWidget(self.groupBox)

        self.selProfilesBtn = QPushButton(exportProfileDlg)
        self.selProfilesBtn.setObjectName(u"selProfilesBtn")

        self.verticalLayout.addWidget(self.selProfilesBtn)

        self.selSpcCollectionsBtn = QPushButton(exportProfileDlg)
        self.selSpcCollectionsBtn.setObjectName(u"selSpcCollectionsBtn")

        self.verticalLayout.addWidget(self.selSpcCollectionsBtn)

        self.selMetaGroupsBtn = QPushButton(exportProfileDlg)
        self.selMetaGroupsBtn.setObjectName(u"selMetaGroupsBtn")

        self.verticalLayout.addWidget(self.selMetaGroupsBtn)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.okBtn = QPushButton(exportProfileDlg)
        self.okBtn.setObjectName(u"okBtn")

        self.horizontalLayout.addWidget(self.okBtn)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(exportProfileDlg)

        QMetaObject.connectSlotsByName(exportProfileDlg)
    # setupUi

    def retranslateUi(self, exportProfileDlg):
        exportProfileDlg.setWindowTitle(QCoreApplication.translate("exportProfileDlg", u"Import Export Profiles", None))
        self.groupBox.setTitle(QCoreApplication.translate("exportProfileDlg", u"Action", None))
        self.importRadio.setText(QCoreApplication.translate("exportProfileDlg", u"Import", None))
        self.exportRadio.setText(QCoreApplication.translate("exportProfileDlg", u"Export", None))
        self.selProfilesBtn.setText(QCoreApplication.translate("exportProfileDlg", u"Select Profiles", None))
        self.selSpcCollectionsBtn.setText(QCoreApplication.translate("exportProfileDlg", u"Select Species Collections", None))
        self.selMetaGroupsBtn.setText(QCoreApplication.translate("exportProfileDlg", u"Select Metadata Groups", None))
        self.okBtn.setText(QCoreApplication.translate("exportProfileDlg", u"Done", None))
    # retranslateUi

