# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MetadataDlg.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QGridLayout,
    QLabel, QSizePolicy, QWidget)

class Ui_MetadataDlg(object):
    def setupUi(self, MetadataDlg):
        if not MetadataDlg.objectName():
            MetadataDlg.setObjectName(u"MetadataDlg")
        MetadataDlg.resize(631, 105)
        self.gridLayout_2 = QGridLayout(MetadataDlg)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.metaLabel1 = QLabel(MetadataDlg)
        self.metaLabel1.setObjectName(u"metaLabel1")
        font = QFont()
        font.setPointSize(12)
        self.metaLabel1.setFont(font)

        self.gridLayout.addWidget(self.metaLabel1, 0, 0, 1, 1)

        self.metaValue1 = QLabel(MetadataDlg)
        self.metaValue1.setObjectName(u"metaValue1")
        self.metaValue1.setFont(font)
        self.metaValue1.setFrameShape(QFrame.Panel)

        self.gridLayout.addWidget(self.metaValue1, 1, 0, 1, 1)

        self.metaLabel2 = QLabel(MetadataDlg)
        self.metaLabel2.setObjectName(u"metaLabel2")
        self.metaLabel2.setFont(font)

        self.gridLayout.addWidget(self.metaLabel2, 0, 1, 1, 1)

        self.metaValue2 = QLabel(MetadataDlg)
        self.metaValue2.setObjectName(u"metaValue2")
        self.metaValue2.setFont(font)
        self.metaValue2.setFrameShape(QFrame.Panel)

        self.gridLayout.addWidget(self.metaValue2, 1, 1, 1, 1)

        self.metaLabel3 = QLabel(MetadataDlg)
        self.metaLabel3.setObjectName(u"metaLabel3")
        self.metaLabel3.setFont(font)

        self.gridLayout.addWidget(self.metaLabel3, 0, 2, 1, 1)

        self.metaValue3 = QLabel(MetadataDlg)
        self.metaValue3.setObjectName(u"metaValue3")
        self.metaValue3.setFont(font)
        self.metaValue3.setFrameShape(QFrame.Panel)

        self.gridLayout.addWidget(self.metaValue3, 1, 2, 1, 1)

        self.metaLabel4 = QLabel(MetadataDlg)
        self.metaLabel4.setObjectName(u"metaLabel4")
        self.metaLabel4.setFont(font)

        self.gridLayout.addWidget(self.metaLabel4, 0, 3, 1, 1)

        self.metaValue4 = QLabel(MetadataDlg)
        self.metaValue4.setObjectName(u"metaValue4")
        self.metaValue4.setFont(font)
        self.metaValue4.setFrameShape(QFrame.Panel)

        self.gridLayout.addWidget(self.metaValue4, 1, 3, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)


        self.retranslateUi(MetadataDlg)

        QMetaObject.connectSlotsByName(MetadataDlg)
    # setupUi

    def retranslateUi(self, MetadataDlg):
        MetadataDlg.setWindowTitle(QCoreApplication.translate("MetadataDlg", u"Image Metadata", None))
        self.metaLabel1.setText(QCoreApplication.translate("MetadataDlg", u"TextLabel", None))
        self.metaValue1.setText("")
        self.metaLabel2.setText(QCoreApplication.translate("MetadataDlg", u"TextLabel", None))
        self.metaValue2.setText("")
        self.metaLabel3.setText(QCoreApplication.translate("MetadataDlg", u"TextLabel", None))
        self.metaValue3.setText("")
        self.metaLabel4.setText(QCoreApplication.translate("MetadataDlg", u"TextLabel", None))
        self.metaValue4.setText("")
    # retranslateUi

