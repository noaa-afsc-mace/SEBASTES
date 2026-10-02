# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'SubsampleMaskHelpDlg.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_subsampleMaskHelpDlg(object):
    def setupUi(self, subsampleMaskHelpDlg):
        if not subsampleMaskHelpDlg.objectName():
            subsampleMaskHelpDlg.setObjectName(u"subsampleMaskHelpDlg")
        subsampleMaskHelpDlg.resize(400, 191)
        self.verticalLayout = QVBoxLayout(subsampleMaskHelpDlg)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(subsampleMaskHelpDlg)
        self.label.setObjectName(u"label")
        self.label.setWordWrap(True)

        self.verticalLayout.addWidget(self.label)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.okBtn = QPushButton(subsampleMaskHelpDlg)
        self.okBtn.setObjectName(u"okBtn")

        self.horizontalLayout.addWidget(self.okBtn)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(subsampleMaskHelpDlg)

        QMetaObject.connectSlotsByName(subsampleMaskHelpDlg)
    # setupUi

    def retranslateUi(self, subsampleMaskHelpDlg):
        subsampleMaskHelpDlg.setWindowTitle(QCoreApplication.translate("subsampleMaskHelpDlg", u"Subsample Mask Help", None))
        self.label.setText(QCoreApplication.translate("subsampleMaskHelpDlg", u"The Subsample Mask provides an opportunity for a graphical region of interest (ROI) to be drawn on an image to constrain the are where analysis takes place.  it is specified in pixel coordinates.  Four comma separated values are required, indicating the origin x, origin y, rectangle width and rectangle height.  For example, a value of 10,10,100,100 will mask out all areas of the image except a rectangle that starts at pixel x,y position 10,10 (from top left) and that extends 100 pixels in width and height.", None))
        self.okBtn.setText(QCoreApplication.translate("subsampleMaskHelpDlg", u"OK", None))
    # retranslateUi

