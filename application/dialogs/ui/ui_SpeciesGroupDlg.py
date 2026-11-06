# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'SpeciesGroupDlg.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QListWidget,
    QListWidgetItem, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_speciesGroupDlg(object):
    def setupUi(self, speciesGroupDlg):
        if not speciesGroupDlg.objectName():
            speciesGroupDlg.setObjectName(u"speciesGroupDlg")
        speciesGroupDlg.resize(224, 227)
        self.verticalLayout = QVBoxLayout(speciesGroupDlg)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.listWidget = QListWidget(speciesGroupDlg)
        self.listWidget.setObjectName(u"listWidget")

        self.verticalLayout.addWidget(self.listWidget)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, -1, -1, 0)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.cancelBtn = QPushButton(speciesGroupDlg)
        self.cancelBtn.setObjectName(u"cancelBtn")

        self.horizontalLayout_2.addWidget(self.cancelBtn)

        self.okBtn = QPushButton(speciesGroupDlg)
        self.okBtn.setObjectName(u"okBtn")

        self.horizontalLayout_2.addWidget(self.okBtn)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        QWidget.setTabOrder(self.okBtn, self.cancelBtn)
        QWidget.setTabOrder(self.cancelBtn, self.listWidget)

        self.retranslateUi(speciesGroupDlg)

        QMetaObject.connectSlotsByName(speciesGroupDlg)
    # setupUi

    def retranslateUi(self, speciesGroupDlg):
        speciesGroupDlg.setWindowTitle(QCoreApplication.translate("speciesGroupDlg", u"Select a species group", None))
        self.cancelBtn.setText(QCoreApplication.translate("speciesGroupDlg", u"Cancel", None))
        self.okBtn.setText(QCoreApplication.translate("speciesGroupDlg", u"OK", None))
    # retranslateUi

