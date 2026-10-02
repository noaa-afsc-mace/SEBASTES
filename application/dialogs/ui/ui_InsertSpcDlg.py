# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'InsertSpcDlg.ui'
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
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QTextEdit, QVBoxLayout, QWidget)

class Ui_insertSpcDlg(object):
    def setupUi(self, insertSpcDlg):
        if not insertSpcDlg.objectName():
            insertSpcDlg.setObjectName(u"insertSpcDlg")
        insertSpcDlg.resize(538, 294)
        self.verticalLayout_3 = QVBoxLayout(insertSpcDlg)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(insertSpcDlg)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.speciesEdit = QLineEdit(insertSpcDlg)
        self.speciesEdit.setObjectName(u"speciesEdit")

        self.verticalLayout.addWidget(self.speciesEdit)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, -1, -1, 0)
        self.label_3 = QLabel(insertSpcDlg)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_3.addWidget(self.label_3)

        self.btnColLabel = QLabel(insertSpcDlg)
        self.btnColLabel.setObjectName(u"btnColLabel")
        self.btnColLabel.setFrameShape(QFrame.Box)

        self.horizontalLayout_3.addWidget(self.btnColLabel)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.setColorBtn = QPushButton(insertSpcDlg)
        self.setColorBtn.setObjectName(u"setColorBtn")

        self.verticalLayout.addWidget(self.setColorBtn)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(-1, -1, 0, 6)
        self.label_4 = QLabel(insertSpcDlg)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_4.addWidget(self.label_4)

        self.sortEdit = QLineEdit(insertSpcDlg)
        self.sortEdit.setObjectName(u"sortEdit")

        self.horizontalLayout_4.addWidget(self.sortEdit)


        self.verticalLayout.addLayout(self.horizontalLayout_4)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, -1, 0, -1)
        self.label_2 = QLabel(insertSpcDlg)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_2.addWidget(self.label_2)

        self.descEdit = QTextEdit(insertSpcDlg)
        self.descEdit.setObjectName(u"descEdit")

        self.verticalLayout_2.addWidget(self.descEdit)


        self.horizontalLayout.addLayout(self.verticalLayout_2)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, -1, -1, 0)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.cancelBtn = QPushButton(insertSpcDlg)
        self.cancelBtn.setObjectName(u"cancelBtn")

        self.horizontalLayout_2.addWidget(self.cancelBtn)

        self.saveBtn = QPushButton(insertSpcDlg)
        self.saveBtn.setObjectName(u"saveBtn")

        self.horizontalLayout_2.addWidget(self.saveBtn)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)


        self.retranslateUi(insertSpcDlg)

        QMetaObject.connectSlotsByName(insertSpcDlg)
    # setupUi

    def retranslateUi(self, insertSpcDlg):
        insertSpcDlg.setWindowTitle(QCoreApplication.translate("insertSpcDlg", u"Insert species group", None))
        self.label.setText(QCoreApplication.translate("insertSpcDlg", u"Species Group", None))
        self.label_3.setText(QCoreApplication.translate("insertSpcDlg", u"Button color", None))
        self.btnColLabel.setText("")
        self.setColorBtn.setText(QCoreApplication.translate("insertSpcDlg", u"Set Color", None))
        self.label_4.setText(QCoreApplication.translate("insertSpcDlg", u"Button  Order", None))
        self.label_2.setText(QCoreApplication.translate("insertSpcDlg", u"Description", None))
        self.cancelBtn.setText(QCoreApplication.translate("insertSpcDlg", u"Cancel", None))
        self.saveBtn.setText(QCoreApplication.translate("insertSpcDlg", u"Save", None))
    # retranslateUi

