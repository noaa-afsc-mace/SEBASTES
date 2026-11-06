# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'CloseupDlg.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QLabel,
    QSizePolicy, QWidget)

class Ui_closeupDlg(object):
    def setupUi(self, closeupDlg):
        if not closeupDlg.objectName():
            closeupDlg.setObjectName(u"closeupDlg")
        closeupDlg.resize(275, 275)
        closeupDlg.setModal(False)
        self.imgLabel = QLabel(closeupDlg)
        self.imgLabel.setObjectName(u"imgLabel")
        self.imgLabel.setGeometry(QRect(10, 10, 256, 256))
        self.imgLabel.setFrameShape(QFrame.Box)

        self.retranslateUi(closeupDlg)

        QMetaObject.connectSlotsByName(closeupDlg)
    # setupUi

    def retranslateUi(self, closeupDlg):
        closeupDlg.setWindowTitle(QCoreApplication.translate("closeupDlg", u"CloseupView", None))
        self.imgLabel.setText("")
    # retranslateUi

