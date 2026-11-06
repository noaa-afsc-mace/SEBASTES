# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MakeSelDlg.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QHeaderView,
    QLabel, QPushButton, QSizePolicy, QSpacerItem,
    QTableView, QVBoxLayout, QWidget)

class Ui_makeSelDlg(object):
    def setupUi(self, makeSelDlg):
        if not makeSelDlg.objectName():
            makeSelDlg.setObjectName(u"makeSelDlg")
        makeSelDlg.resize(400, 252)
        self.verticalLayout = QVBoxLayout(makeSelDlg)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(makeSelDlg)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.dataView = QTableView(makeSelDlg)
        self.dataView.setObjectName(u"dataView")

        self.verticalLayout.addWidget(self.dataView)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, -1, -1, 0)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.cancelBtn = QPushButton(makeSelDlg)
        self.cancelBtn.setObjectName(u"cancelBtn")

        self.horizontalLayout.addWidget(self.cancelBtn)

        self.selectBtn = QPushButton(makeSelDlg)
        self.selectBtn.setObjectName(u"selectBtn")

        self.horizontalLayout.addWidget(self.selectBtn)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(makeSelDlg)

        QMetaObject.connectSlotsByName(makeSelDlg)
    # setupUi

    def retranslateUi(self, makeSelDlg):
        makeSelDlg.setWindowTitle(QCoreApplication.translate("makeSelDlg", u"Make a selection", None))
        self.label.setText(QCoreApplication.translate("makeSelDlg", u"Profiles", None))
        self.cancelBtn.setText(QCoreApplication.translate("makeSelDlg", u"Cancel", None))
        self.selectBtn.setText(QCoreApplication.translate("makeSelDlg", u"Select", None))
    # retranslateUi

