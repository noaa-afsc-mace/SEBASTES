# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DataviewDlg.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QDialog, QHBoxLayout,
    QHeaderView, QPushButton, QSizePolicy, QSpacerItem,
    QTabWidget, QTableView, QVBoxLayout, QWidget)

class Ui_dataviewDlg(object):
    def setupUi(self, dataviewDlg):
        if not dataviewDlg.objectName():
            dataviewDlg.setObjectName(u"dataviewDlg")
        dataviewDlg.setWindowModality(Qt.NonModal)
        dataviewDlg.resize(354, 394)
        self.horizontalLayout = QHBoxLayout(dataviewDlg)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.tabWidget = QTabWidget(dataviewDlg)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.horizontalLayout_2 = QHBoxLayout(self.tab)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.metadataTable = QTableView(self.tab)
        self.metadataTable.setObjectName(u"metadataTable")

        self.horizontalLayout_2.addWidget(self.metadataTable)

        self.tabWidget.addTab(self.tab, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.horizontalLayout_4 = QHBoxLayout(self.tab_3)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.frameTable = QTableView(self.tab_3)
        self.frameTable.setObjectName(u"frameTable")
        self.frameTable.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.frameTable.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.horizontalLayout_4.addWidget(self.frameTable)

        self.tabWidget.addTab(self.tab_3, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout = QVBoxLayout(self.tab_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.targetTable = QTableView(self.tab_2)
        self.targetTable.setObjectName(u"targetTable")
        self.targetTable.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.targetTable.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.verticalLayout.addWidget(self.targetTable)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, -1, -1, 0)
        self.filterBtn = QPushButton(self.tab_2)
        self.filterBtn.setObjectName(u"filterBtn")
        self.filterBtn.setCheckable(True)

        self.horizontalLayout_3.addWidget(self.filterBtn)

        self.editBtn = QPushButton(self.tab_2)
        self.editBtn.setObjectName(u"editBtn")

        self.horizontalLayout_3.addWidget(self.editBtn)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.tabWidget.addTab(self.tab_2, "")

        self.horizontalLayout.addWidget(self.tabWidget)


        self.retranslateUi(dataviewDlg)

        self.tabWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(dataviewDlg)
    # setupUi

    def retranslateUi(self, dataviewDlg):
        dataviewDlg.setWindowTitle(QCoreApplication.translate("dataviewDlg", u"Dialog", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("dataviewDlg", u"Metadata", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("dataviewDlg", u"Frames", None))
        self.filterBtn.setText(QCoreApplication.translate("dataviewDlg", u"Filter by Species", None))
        self.editBtn.setText(QCoreApplication.translate("dataviewDlg", u"Edit Species", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("dataviewDlg", u"Targets", None))
    # retranslateUi

