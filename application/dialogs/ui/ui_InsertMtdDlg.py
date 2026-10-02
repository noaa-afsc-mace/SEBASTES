# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'InsertMtdDlg.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QSpinBox, QTextEdit, QVBoxLayout,
    QWidget)

class Ui_insertMtdDlg(object):
    def setupUi(self, insertMtdDlg):
        if not insertMtdDlg.objectName():
            insertMtdDlg.setObjectName(u"insertMtdDlg")
        insertMtdDlg.resize(564, 227)
        self.verticalLayout_3 = QVBoxLayout(insertMtdDlg)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.habitatLabel = QLabel(insertMtdDlg)
        self.habitatLabel.setObjectName(u"habitatLabel")

        self.verticalLayout.addWidget(self.habitatLabel)

        self.metadataEdit = QLineEdit(insertMtdDlg)
        self.metadataEdit.setObjectName(u"metadataEdit")

        self.verticalLayout.addWidget(self.metadataEdit)

        self.label = QLabel(insertMtdDlg)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.metadataTypeEdit = QLineEdit(insertMtdDlg)
        self.metadataTypeEdit.setObjectName(u"metadataTypeEdit")

        self.verticalLayout.addWidget(self.metadataTypeEdit)

        self.label_4 = QLabel(insertMtdDlg)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout.addWidget(self.label_4)

        self.categoryBox = QComboBox(insertMtdDlg)
        self.categoryBox.setObjectName(u"categoryBox")

        self.verticalLayout.addWidget(self.categoryBox)

        self.label_3 = QLabel(insertMtdDlg)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout.addWidget(self.label_3)

        self.orderSpinBox = QSpinBox(insertMtdDlg)
        self.orderSpinBox.setObjectName(u"orderSpinBox")
        self.orderSpinBox.setMinimum(1)

        self.verticalLayout.addWidget(self.orderSpinBox)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, -1, 0, -1)
        self.label_2 = QLabel(insertMtdDlg)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_2.addWidget(self.label_2)

        self.descEdit = QTextEdit(insertMtdDlg)
        self.descEdit.setObjectName(u"descEdit")

        self.verticalLayout_2.addWidget(self.descEdit)


        self.horizontalLayout.addLayout(self.verticalLayout_2)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, -1, -1, 0)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.cancelBtn = QPushButton(insertMtdDlg)
        self.cancelBtn.setObjectName(u"cancelBtn")

        self.horizontalLayout_3.addWidget(self.cancelBtn)

        self.saveBtn = QPushButton(insertMtdDlg)
        self.saveBtn.setObjectName(u"saveBtn")

        self.horizontalLayout_3.addWidget(self.saveBtn)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)


        self.retranslateUi(insertMtdDlg)

        QMetaObject.connectSlotsByName(insertMtdDlg)
    # setupUi

    def retranslateUi(self, insertMtdDlg):
        insertMtdDlg.setWindowTitle(QCoreApplication.translate("insertMtdDlg", u"Insert metadata information", None))
        self.habitatLabel.setText(QCoreApplication.translate("insertMtdDlg", u"Metadata tag", None))
        self.label.setText(QCoreApplication.translate("insertMtdDlg", u"Metadata Type", None))
        self.label_4.setText(QCoreApplication.translate("insertMtdDlg", u"Metadata gui element", None))
        self.label_3.setText(QCoreApplication.translate("insertMtdDlg", u"GUI order", None))
        self.label_2.setText(QCoreApplication.translate("insertMtdDlg", u"Description", None))
        self.cancelBtn.setText(QCoreApplication.translate("insertMtdDlg", u"Cancel", None))
        self.saveBtn.setText(QCoreApplication.translate("insertMtdDlg", u"Save", None))
    # retranslateUi

