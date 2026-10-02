# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'SelectProjectDlg.ui'
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
    QPushButton, QSizePolicy, QSpacerItem, QTableView,
    QVBoxLayout, QWidget)

class Ui_selectProjectDlg(object):
    def setupUi(self, selectProjectDlg):
        if not selectProjectDlg.objectName():
            selectProjectDlg.setObjectName(u"selectProjectDlg")
        selectProjectDlg.resize(516, 189)
        self.verticalLayout = QVBoxLayout(selectProjectDlg)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.projectView = QTableView(selectProjectDlg)
        self.projectView.setObjectName(u"projectView")

        self.verticalLayout.addWidget(self.projectView)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, -1, -1, 0)
        self.createNewProjBtn = QPushButton(selectProjectDlg)
        self.createNewProjBtn.setObjectName(u"createNewProjBtn")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.createNewProjBtn.sizePolicy().hasHeightForWidth())
        self.createNewProjBtn.setSizePolicy(sizePolicy)

        self.horizontalLayout_2.addWidget(self.createNewProjBtn)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.cancelBtn = QPushButton(selectProjectDlg)
        self.cancelBtn.setObjectName(u"cancelBtn")

        self.horizontalLayout_2.addWidget(self.cancelBtn)

        self.okBtn = QPushButton(selectProjectDlg)
        self.okBtn.setObjectName(u"okBtn")

        self.horizontalLayout_2.addWidget(self.okBtn)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.retranslateUi(selectProjectDlg)

        QMetaObject.connectSlotsByName(selectProjectDlg)
    # setupUi

    def retranslateUi(self, selectProjectDlg):
        selectProjectDlg.setWindowTitle(QCoreApplication.translate("selectProjectDlg", u"Select a project", None))
        self.createNewProjBtn.setText(QCoreApplication.translate("selectProjectDlg", u"Create Project", None))
        self.cancelBtn.setText(QCoreApplication.translate("selectProjectDlg", u"Cancel", None))
        self.okBtn.setText(QCoreApplication.translate("selectProjectDlg", u"OK", None))
    # retranslateUi

