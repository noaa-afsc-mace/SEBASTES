# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'TimestampExtractHelpDlg.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFormLayout, QFrame,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_timestampExtractHelpDlg(object):
    def setupUi(self, timestampExtractHelpDlg):
        if not timestampExtractHelpDlg.objectName():
            timestampExtractHelpDlg.setObjectName(u"timestampExtractHelpDlg")
        timestampExtractHelpDlg.resize(400, 325)
        self.verticalLayout = QVBoxLayout(timestampExtractHelpDlg)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(timestampExtractHelpDlg)
        self.label.setObjectName(u"label")
        self.label.setWordWrap(True)

        self.verticalLayout.addWidget(self.label)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label_2 = QLabel(timestampExtractHelpDlg)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_2)

        self.timestampFormat = QLineEdit(timestampExtractHelpDlg)
        self.timestampFormat.setObjectName(u"timestampFormat")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.timestampFormat)

        self.label_3 = QLabel(timestampExtractHelpDlg)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.label_3)

        self.timestampStartIndex = QLineEdit(timestampExtractHelpDlg)
        self.timestampStartIndex.setObjectName(u"timestampStartIndex")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.timestampStartIndex)

        self.label_4 = QLabel(timestampExtractHelpDlg)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_4)

        self.filenameEdit = QLineEdit(timestampExtractHelpDlg)
        self.filenameEdit.setObjectName(u"filenameEdit")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.filenameEdit)


        self.verticalLayout.addLayout(self.formLayout)

        self.extractBtn = QPushButton(timestampExtractHelpDlg)
        self.extractBtn.setObjectName(u"extractBtn")

        self.verticalLayout.addWidget(self.extractBtn)

        self.resultLabel = QLabel(timestampExtractHelpDlg)
        self.resultLabel.setObjectName(u"resultLabel")
        self.resultLabel.setFrameShape(QFrame.Box)

        self.verticalLayout.addWidget(self.resultLabel)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.okBtn = QPushButton(timestampExtractHelpDlg)
        self.okBtn.setObjectName(u"okBtn")

        self.horizontalLayout.addWidget(self.okBtn)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(timestampExtractHelpDlg)

        QMetaObject.connectSlotsByName(timestampExtractHelpDlg)
    # setupUi

    def retranslateUi(self, timestampExtractHelpDlg):
        timestampExtractHelpDlg.setWindowTitle(QCoreApplication.translate("timestampExtractHelpDlg", u"Help Dialog", None))
        self.label.setText(QCoreApplication.translate("timestampExtractHelpDlg", u"To correcly label each frame with the appropriate timestamp, the time has to be known.  It can either be extracted from the image file name, or retrieved from teh image metadate using the EXIV library, which is standard for most image file types such as JPEG. If you want to extract the timestamp from teh name, this dialog can help figure out the format.  It uses Qt standard for designating days, months and times.  For example if the timestamp is 04.05.2020, the timestamp format would be \" dd.MM.yyyy\", and if the time was 13:47:10.234, the time format would be \"hh:mm:ss.zzz\".  To test timestamp extraction, paste an example of your image file name (with or without extension) and fill in the format string as well as the staring index  if the time is correctly extracted you will get positive feedback.", None))
        self.label_2.setText(QCoreApplication.translate("timestampExtractHelpDlg", u"Date format string", None))
        self.label_3.setText(QCoreApplication.translate("timestampExtractHelpDlg", u"date index start", None))
        self.label_4.setText(QCoreApplication.translate("timestampExtractHelpDlg", u"Filename", None))
        self.extractBtn.setText(QCoreApplication.translate("timestampExtractHelpDlg", u"Extract", None))
        self.resultLabel.setText("")
        self.okBtn.setText(QCoreApplication.translate("timestampExtractHelpDlg", u"OK", None))
    # retranslateUi

