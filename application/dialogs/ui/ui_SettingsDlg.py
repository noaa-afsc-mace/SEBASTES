# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'SettingsDlg.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QDialog, QFrame,
    QGridLayout, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_settingsDlg(object):
    def setupUi(self, settingsDlg):
        if not settingsDlg.objectName():
            settingsDlg.setObjectName(u"settingsDlg")
        settingsDlg.resize(404, 427)
        self.verticalLayout = QVBoxLayout(settingsDlg)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_2 = QFrame(settingsDlg)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setBold(True)
        self.label.setFont(font)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.label_4 = QLabel(self.frame_2)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 1)

        self.dbName = QLineEdit(self.frame_2)
        self.dbName.setObjectName(u"dbName")

        self.gridLayout.addWidget(self.dbName, 1, 1, 1, 1)

        self.label_3 = QLabel(self.frame_2)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)

        self.dbUser = QLineEdit(self.frame_2)
        self.dbUser.setObjectName(u"dbUser")

        self.gridLayout.addWidget(self.dbUser, 2, 1, 1, 1)

        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 1)

        self.dbPassword = QLineEdit(self.frame_2)
        self.dbPassword.setObjectName(u"dbPassword")

        self.gridLayout.addWidget(self.dbPassword, 3, 1, 1, 1)

        self.label_6 = QLabel(self.frame_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font)

        self.gridLayout.addWidget(self.label_6, 4, 0, 1, 1)

        self.label_5 = QLabel(self.frame_2)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 5, 0, 1, 1)

        self.magCheck = QCheckBox(self.frame_2)
        self.magCheck.setObjectName(u"magCheck")
        self.magCheck.setLayoutDirection(Qt.RightToLeft)

        self.gridLayout.addWidget(self.magCheck, 5, 1, 1, 1)

        self.label_8 = QLabel(self.frame_2)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout.addWidget(self.label_8, 7, 0, 1, 1)

        self.tailCheck = QCheckBox(self.frame_2)
        self.tailCheck.setObjectName(u"tailCheck")
        self.tailCheck.setLayoutDirection(Qt.RightToLeft)

        self.gridLayout.addWidget(self.tailCheck, 7, 1, 1, 1)

        self.label_7 = QLabel(self.frame_2)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout.addWidget(self.label_7, 6, 0, 1, 1)

        self.closeupWinSize = QLineEdit(self.frame_2)
        self.closeupWinSize.setObjectName(u"closeupWinSize")

        self.gridLayout.addWidget(self.closeupWinSize, 6, 1, 1, 1)

        self.label_9 = QLabel(self.frame_2)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout.addWidget(self.label_9, 8, 0, 1, 1)

        self.tailLength = QLineEdit(self.frame_2)
        self.tailLength.setObjectName(u"tailLength")

        self.gridLayout.addWidget(self.tailLength, 8, 1, 1, 1)


        self.verticalLayout.addWidget(self.frame_2)

        self.frame = QFrame(settingsDlg)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(16777215, 50))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.cancelBtn = QPushButton(self.frame)
        self.cancelBtn.setObjectName(u"cancelBtn")

        self.horizontalLayout.addWidget(self.cancelBtn)

        self.okBtn = QPushButton(self.frame)
        self.okBtn.setObjectName(u"okBtn")

        self.horizontalLayout.addWidget(self.okBtn)


        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(settingsDlg)

        QMetaObject.connectSlotsByName(settingsDlg)
    # setupUi

    def retranslateUi(self, settingsDlg):
        settingsDlg.setWindowTitle(QCoreApplication.translate("settingsDlg", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("settingsDlg", u"Database Connectivity", None))
        self.label_4.setText(QCoreApplication.translate("settingsDlg", u"Name", None))
        self.label_3.setText(QCoreApplication.translate("settingsDlg", u"User ID", None))
        self.label_2.setText(QCoreApplication.translate("settingsDlg", u"password", None))
        self.label_6.setText(QCoreApplication.translate("settingsDlg", u"Other Settings", None))
        self.label_5.setText(QCoreApplication.translate("settingsDlg", u"Show magnification window?", None))
        self.magCheck.setText("")
        self.label_8.setText(QCoreApplication.translate("settingsDlg", u"Show measureLine tails?", None))
        self.tailCheck.setText("")
        self.label_7.setText(QCoreApplication.translate("settingsDlg", u"magnification window pixels", None))
        self.label_9.setText(QCoreApplication.translate("settingsDlg", u"Tail length", None))
        self.cancelBtn.setText(QCoreApplication.translate("settingsDlg", u"cancel", None))
        self.okBtn.setText(QCoreApplication.translate("settingsDlg", u"save", None))
    # retranslateUi

