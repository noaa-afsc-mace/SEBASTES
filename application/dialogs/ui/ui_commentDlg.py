# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'commentDlg.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QGridLayout, QLabel,
    QPlainTextEdit, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_commentDlg(object):
    def setupUi(self, commentDlg):
        if not commentDlg.objectName():
            commentDlg.setObjectName(u"commentDlg")
        commentDlg.resize(400, 300)
        self.verticalLayout_2 = QVBoxLayout(commentDlg)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(-1, 10, -1, -1)
        self.classLabel = QLabel(commentDlg)
        self.classLabel.setObjectName(u"classLabel")
        font = QFont()
        font.setPointSize(12)
        self.classLabel.setFont(font)

        self.gridLayout.addWidget(self.classLabel, 0, 0, 1, 1)

        self.tClassLabel = QLabel(commentDlg)
        self.tClassLabel.setObjectName(u"tClassLabel")
        self.tClassLabel.setFont(font)

        self.gridLayout.addWidget(self.tClassLabel, 0, 1, 1, 1)

        self.targetLabel = QLabel(commentDlg)
        self.targetLabel.setObjectName(u"targetLabel")
        self.targetLabel.setFont(font)

        self.gridLayout.addWidget(self.targetLabel, 1, 0, 1, 1)

        self.tNumLabel = QLabel(commentDlg)
        self.tNumLabel.setObjectName(u"tNumLabel")
        self.tNumLabel.setFont(font)

        self.gridLayout.addWidget(self.tNumLabel, 1, 1, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.commentBox = QPlainTextEdit(commentDlg)
        self.commentBox.setObjectName(u"commentBox")
        self.commentBox.setFont(font)

        self.verticalLayout.addWidget(self.commentBox)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.saveAndExitBtn = QPushButton(commentDlg)
        self.saveAndExitBtn.setObjectName(u"saveAndExitBtn")
        self.saveAndExitBtn.setFont(font)

        self.verticalLayout_2.addWidget(self.saveAndExitBtn)


        self.retranslateUi(commentDlg)

        QMetaObject.connectSlotsByName(commentDlg)
    # setupUi

    def retranslateUi(self, commentDlg):
        commentDlg.setWindowTitle(QCoreApplication.translate("commentDlg", u"Insert Comment", None))
        self.classLabel.setText(QCoreApplication.translate("commentDlg", u"Active Target Class", None))
        self.tClassLabel.setText("")
        self.targetLabel.setText(QCoreApplication.translate("commentDlg", u"Active Target number", None))
        self.tNumLabel.setText("")
        self.saveAndExitBtn.setText(QCoreApplication.translate("commentDlg", u"Save Comment", None))
    # retranslateUi

