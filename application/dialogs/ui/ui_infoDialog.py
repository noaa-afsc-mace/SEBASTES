# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'infoDialog.ui'
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
    QPlainTextEdit, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_infoDialog(object):
    def setupUi(self, infoDialog):
        if not infoDialog.objectName():
            infoDialog.setObjectName(u"infoDialog")
        infoDialog.resize(400, 650)
        self.verticalLayout = QVBoxLayout(infoDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.statusText = QPlainTextEdit(infoDialog)
        self.statusText.setObjectName(u"statusText")
        self.statusText.setAcceptDrops(False)
        self.statusText.setUndoRedoEnabled(False)
        self.statusText.setReadOnly(True)
        self.statusText.setCenterOnScroll(False)

        self.verticalLayout.addWidget(self.statusText)

        self.frame = QFrame(infoDialog)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.saveBtn = QPushButton(self.frame)
        self.saveBtn.setObjectName(u"saveBtn")

        self.horizontalLayout.addWidget(self.saveBtn)


        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(infoDialog)

        QMetaObject.connectSlotsByName(infoDialog)
    # setupUi

    def retranslateUi(self, infoDialog):
        infoDialog.setWindowTitle(QCoreApplication.translate("infoDialog", u"Information Dialog", None))
        self.saveBtn.setText(QCoreApplication.translate("infoDialog", u"OK", None))
    # retranslateUi

