# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'TargetCommentDlg.ui'
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

class Ui_targetCommentDlg(object):
    def setupUi(self, targetCommentDlg):
        if not targetCommentDlg.objectName():
            targetCommentDlg.setObjectName(u"targetCommentDlg")
        targetCommentDlg.resize(400, 300)
        self.verticalLayout_2 = QVBoxLayout(targetCommentDlg)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(-1, 10, -1, -1)
        self.label = QLabel(targetCommentDlg)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(12)
        self.label.setFont(font)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.tClassLabel = QLabel(targetCommentDlg)
        self.tClassLabel.setObjectName(u"tClassLabel")
        self.tClassLabel.setFont(font)

        self.gridLayout.addWidget(self.tClassLabel, 0, 1, 1, 1)

        self.label_3 = QLabel(targetCommentDlg)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)

        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)

        self.tNumLabel = QLabel(targetCommentDlg)
        self.tNumLabel.setObjectName(u"tNumLabel")
        self.tNumLabel.setFont(font)

        self.gridLayout.addWidget(self.tNumLabel, 1, 1, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.commentBox = QPlainTextEdit(targetCommentDlg)
        self.commentBox.setObjectName(u"commentBox")
        self.commentBox.setFont(font)

        self.verticalLayout.addWidget(self.commentBox)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.saveAndExitBtn = QPushButton(targetCommentDlg)
        self.saveAndExitBtn.setObjectName(u"saveAndExitBtn")
        self.saveAndExitBtn.setFont(font)

        self.verticalLayout_2.addWidget(self.saveAndExitBtn)


        self.retranslateUi(targetCommentDlg)

        QMetaObject.connectSlotsByName(targetCommentDlg)
    # setupUi

    def retranslateUi(self, targetCommentDlg):
        targetCommentDlg.setWindowTitle(QCoreApplication.translate("targetCommentDlg", u"Insert Target Comment", None))
        self.label.setText(QCoreApplication.translate("targetCommentDlg", u"Active Target Class", None))
        self.tClassLabel.setText("")
        self.label_3.setText(QCoreApplication.translate("targetCommentDlg", u"Active Target number", None))
        self.tNumLabel.setText("")
        self.saveAndExitBtn.setText(QCoreApplication.translate("targetCommentDlg", u"Save Comment", None))
    # retranslateUi

