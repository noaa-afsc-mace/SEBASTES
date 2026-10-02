# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'LoadDlg.ui'
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
    QHeaderView, QLabel, QPushButton, QSizePolicy,
    QSpacerItem, QTableView, QVBoxLayout, QWidget)

class Ui_loadDlg(object):
    def setupUi(self, loadDlg):
        if not loadDlg.objectName():
            loadDlg.setObjectName(u"loadDlg")
        loadDlg.resize(291, 300)
        self.verticalLayout = QVBoxLayout(loadDlg)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(loadDlg)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.tableView = QTableView(loadDlg)
        self.tableView.setObjectName(u"tableView")

        self.verticalLayout.addWidget(self.tableView)

        self.frame = QFrame(loadDlg)
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


        self.retranslateUi(loadDlg)

        QMetaObject.connectSlotsByName(loadDlg)
    # setupUi

    def retranslateUi(self, loadDlg):
        loadDlg.setWindowTitle(QCoreApplication.translate("loadDlg", u"Load Deployment", None))
        self.label.setText(QCoreApplication.translate("loadDlg", u"Existing Deployments", None))
        self.cancelBtn.setText(QCoreApplication.translate("loadDlg", u"Cancel", None))
        self.okBtn.setText(QCoreApplication.translate("loadDlg", u"OK", None))
    # retranslateUi

