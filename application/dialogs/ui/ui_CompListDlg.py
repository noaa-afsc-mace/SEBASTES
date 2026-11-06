# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'CompListDlg.ui'
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

class Ui_assignActivesDlg(object):
    def setupUi(self, assignActivesDlg):
        if not assignActivesDlg.objectName():
            assignActivesDlg.setObjectName(u"assignActivesDlg")
        assignActivesDlg.resize(354, 378)
        self.verticalLayout = QVBoxLayout(assignActivesDlg)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, -1, -1, 0)
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(-1, -1, -1, 0)
        self.label1 = QLabel(assignActivesDlg)
        self.label1.setObjectName(u"label1")
        font = QFont()
        font.setPointSize(8)
        self.label1.setFont(font)

        self.verticalLayout_5.addWidget(self.label1)

        self.inactiveView = QTableView(assignActivesDlg)
        self.inactiveView.setObjectName(u"inactiveView")
        self.inactiveView.setFont(font)

        self.verticalLayout_5.addWidget(self.inactiveView)


        self.horizontalLayout.addLayout(self.verticalLayout_5)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(-1, -1, 0, -1)
        self.addBtn = QPushButton(assignActivesDlg)
        self.addBtn.setObjectName(u"addBtn")
        self.addBtn.setFont(font)

        self.verticalLayout_6.addWidget(self.addBtn)

        self.remBtn = QPushButton(assignActivesDlg)
        self.remBtn.setObjectName(u"remBtn")
        self.remBtn.setFont(font)

        self.verticalLayout_6.addWidget(self.remBtn)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer)


        self.horizontalLayout.addLayout(self.verticalLayout_6)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(-1, -1, 0, -1)
        self.label2 = QLabel(assignActivesDlg)
        self.label2.setObjectName(u"label2")
        self.label2.setFont(font)

        self.verticalLayout_7.addWidget(self.label2)

        self.activeView = QTableView(assignActivesDlg)
        self.activeView.setObjectName(u"activeView")
        self.activeView.setFont(font)

        self.verticalLayout_7.addWidget(self.activeView)


        self.horizontalLayout.addLayout(self.verticalLayout_7)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(-1, -1, -1, 0)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)

        self.okBtn = QPushButton(assignActivesDlg)
        self.okBtn.setObjectName(u"okBtn")
        self.okBtn.setFont(font)

        self.horizontalLayout_4.addWidget(self.okBtn)


        self.verticalLayout.addLayout(self.horizontalLayout_4)


        self.retranslateUi(assignActivesDlg)

        QMetaObject.connectSlotsByName(assignActivesDlg)
    # setupUi

    def retranslateUi(self, assignActivesDlg):
        assignActivesDlg.setWindowTitle(QCoreApplication.translate("assignActivesDlg", u"Assign Species", None))
        self.label1.setText(QCoreApplication.translate("assignActivesDlg", u"Inactive", None))
        self.addBtn.setText(QCoreApplication.translate("assignActivesDlg", u"Add", None))
        self.remBtn.setText(QCoreApplication.translate("assignActivesDlg", u"Remove", None))
        self.label2.setText(QCoreApplication.translate("assignActivesDlg", u"Active", None))
        self.okBtn.setText(QCoreApplication.translate("assignActivesDlg", u"Done", None))
    # retranslateUi

