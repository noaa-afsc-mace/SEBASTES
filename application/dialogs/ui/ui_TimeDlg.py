# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'TimeDlg.ui'
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
from PySide6.QtWidgets import (QApplication, QDateEdit, QDialog, QLabel,
    QPushButton, QSizePolicy, QTimeEdit, QWidget)

class Ui_timeDlg(object):
    def setupUi(self, timeDlg):
        if not timeDlg.objectName():
            timeDlg.setObjectName(u"timeDlg")
        timeDlg.resize(274, 216)
        self.timeEdit = QTimeEdit(timeDlg)
        self.timeEdit.setObjectName(u"timeEdit")
        self.timeEdit.setGeometry(QRect(20, 100, 171, 41))
        font = QFont()
        font.setPointSize(14)
        self.timeEdit.setFont(font)
        self.timeEdit.setTime(QTime(0, 0, 0))
        self.dateEdit = QDateEdit(timeDlg)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setGeometry(QRect(20, 40, 171, 41))
        self.dateEdit.setFont(font)
        self.okBtn = QPushButton(timeDlg)
        self.okBtn.setObjectName(u"okBtn")
        self.okBtn.setGeometry(QRect(150, 160, 111, 41))
        self.okBtn.setFont(font)
        self.cancelBtn = QPushButton(timeDlg)
        self.cancelBtn.setObjectName(u"cancelBtn")
        self.cancelBtn.setGeometry(QRect(20, 160, 121, 41))
        self.cancelBtn.setFont(font)
        self.label = QLabel(timeDlg)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 10, 181, 16))
        self.label.setFont(font)

        self.retranslateUi(timeDlg)

        QMetaObject.connectSlotsByName(timeDlg)
    # setupUi

    def retranslateUi(self, timeDlg):
        timeDlg.setWindowTitle(QCoreApplication.translate("timeDlg", u"Dialog", None))
        self.timeEdit.setDisplayFormat(QCoreApplication.translate("timeDlg", u"hh:mm:ss", None))
        self.okBtn.setText(QCoreApplication.translate("timeDlg", u"OK", None))
        self.cancelBtn.setText(QCoreApplication.translate("timeDlg", u"Cancel", None))
        self.label.setText(QCoreApplication.translate("timeDlg", u"Enter a date/ time...", None))
    # retranslateUi

