# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'FrameExtractHelpDlg.ui'
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
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_frameExtractHelpDlg(object):
    def setupUi(self, frameExtractHelpDlg):
        if not frameExtractHelpDlg.objectName():
            frameExtractHelpDlg.setObjectName(u"frameExtractHelpDlg")
        frameExtractHelpDlg.resize(400, 238)
        self.verticalLayout = QVBoxLayout(frameExtractHelpDlg)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(frameExtractHelpDlg)
        self.label.setObjectName(u"label")
        self.label.setWordWrap(True)

        self.verticalLayout.addWidget(self.label)

        self.filenameEdit = QLineEdit(frameExtractHelpDlg)
        self.filenameEdit.setObjectName(u"filenameEdit")

        self.verticalLayout.addWidget(self.filenameEdit)

        self.label_2 = QLabel(frameExtractHelpDlg)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.startInd = QLineEdit(frameExtractHelpDlg)
        self.startInd.setObjectName(u"startInd")

        self.horizontalLayout.addWidget(self.startInd)

        self.label_3 = QLabel(frameExtractHelpDlg)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout.addWidget(self.label_3)

        self.endInd = QLineEdit(frameExtractHelpDlg)
        self.endInd.setObjectName(u"endInd")

        self.horizontalLayout.addWidget(self.endInd)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.extractBtn = QPushButton(frameExtractHelpDlg)
        self.extractBtn.setObjectName(u"extractBtn")

        self.verticalLayout.addWidget(self.extractBtn)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_4 = QLabel(frameExtractHelpDlg)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_2.addWidget(self.label_4)

        self.resultLabel = QLabel(frameExtractHelpDlg)
        self.resultLabel.setObjectName(u"resultLabel")
        self.resultLabel.setFrameShape(QFrame.Box)

        self.horizontalLayout_2.addWidget(self.resultLabel)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.okBtn = QPushButton(frameExtractHelpDlg)
        self.okBtn.setObjectName(u"okBtn")

        self.horizontalLayout_3.addWidget(self.okBtn)


        self.verticalLayout.addLayout(self.horizontalLayout_3)


        self.retranslateUi(frameExtractHelpDlg)

        QMetaObject.connectSlotsByName(frameExtractHelpDlg)
    # setupUi

    def retranslateUi(self, frameExtractHelpDlg):
        frameExtractHelpDlg.setWindowTitle(QCoreApplication.translate("frameExtractHelpDlg", u"Help Dialog", None))
        self.label.setText(QCoreApplication.translate("frameExtractHelpDlg", u"Frame numbers are extracted from the image file name.  Fo rthis to work they have to be in the same location for each file.  This window helps with setting the indices for the frame number within the name. Please copy and paste the full image name (with or wihtout extension) into the box below.", None))
        self.label_2.setText(QCoreApplication.translate("frameExtractHelpDlg", u"Now put the starting and ending values (inclusive) into the two boxes below.", None))
        self.label_3.setText(QCoreApplication.translate("frameExtractHelpDlg", u"to", None))
        self.extractBtn.setText(QCoreApplication.translate("frameExtractHelpDlg", u"Extract frame number", None))
        self.label_4.setText(QCoreApplication.translate("frameExtractHelpDlg", u"Result", None))
        self.resultLabel.setText("")
        self.okBtn.setText(QCoreApplication.translate("frameExtractHelpDlg", u"OK", None))
    # retranslateUi

