# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'TargetLFViewDlg.ui'
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
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

from mplwidget import mplwidget

class Ui_targetLFViewDlg(object):
    def setupUi(self, targetLFViewDlg):
        if not targetLFViewDlg.objectName():
            targetLFViewDlg.setObjectName(u"targetLFViewDlg")
        targetLFViewDlg.resize(645, 351)
        self.verticalLayout_2 = QVBoxLayout(targetLFViewDlg)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.plotWindow = mplwidget(targetLFViewDlg)
        self.plotWindow.setObjectName(u"plotWindow")

        self.verticalLayout.addWidget(self.plotWindow)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.frame = QFrame(targetLFViewDlg)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(16777215, 60))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.exitBtn = QPushButton(self.frame)
        self.exitBtn.setObjectName(u"exitBtn")

        self.horizontalLayout.addWidget(self.exitBtn)


        self.horizontalLayout_2.addLayout(self.horizontalLayout)


        self.verticalLayout_2.addWidget(self.frame)


        self.retranslateUi(targetLFViewDlg)

        QMetaObject.connectSlotsByName(targetLFViewDlg)
    # setupUi

    def retranslateUi(self, targetLFViewDlg):
        targetLFViewDlg.setWindowTitle(QCoreApplication.translate("targetLFViewDlg", u"Dialog", None))
        self.exitBtn.setText(QCoreApplication.translate("targetLFViewDlg", u"Exit", None))
    # retranslateUi

