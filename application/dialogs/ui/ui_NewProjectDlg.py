# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'NewProjectDlg.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QGroupBox,
    QHBoxLayout, QLabel, QLineEdit, QPlainTextEdit,
    QPushButton, QRadioButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_newProjectDlg(object):
    def setupUi(self, newProjectDlg):
        if not newProjectDlg.objectName():
            newProjectDlg.setObjectName(u"newProjectDlg")
        newProjectDlg.resize(827, 212)
        self.verticalLayout_8 = QVBoxLayout(newProjectDlg)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(newProjectDlg)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.projNameEdit = QLineEdit(newProjectDlg)
        self.projNameEdit.setObjectName(u"projNameEdit")

        self.verticalLayout.addWidget(self.projNameEdit)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_2 = QLabel(newProjectDlg)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_2.addWidget(self.label_2)

        self.descEdit = QPlainTextEdit(newProjectDlg)
        self.descEdit.setObjectName(u"descEdit")

        self.verticalLayout_2.addWidget(self.descEdit)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_3 = QLabel(newProjectDlg)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_3.addWidget(self.label_3)

        self.speciesBox = QComboBox(newProjectDlg)
        self.speciesBox.setObjectName(u"speciesBox")

        self.verticalLayout_3.addWidget(self.speciesBox)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)


        self.horizontalLayout.addLayout(self.verticalLayout_3)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_4 = QLabel(newProjectDlg)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_4.addWidget(self.label_4)

        self.metadataBox = QComboBox(newProjectDlg)
        self.metadataBox.setObjectName(u"metadataBox")

        self.verticalLayout_4.addWidget(self.metadataBox)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_3)


        self.horizontalLayout.addLayout(self.verticalLayout_4)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_6 = QLabel(newProjectDlg)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_6.addWidget(self.label_6)

        self.groupBox = QGroupBox(newProjectDlg)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_7 = QVBoxLayout(self.groupBox)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.yesRadio = QRadioButton(self.groupBox)
        self.yesRadio.setObjectName(u"yesRadio")

        self.verticalLayout_7.addWidget(self.yesRadio)

        self.noRadio = QRadioButton(self.groupBox)
        self.noRadio.setObjectName(u"noRadio")

        self.verticalLayout_7.addWidget(self.noRadio)


        self.verticalLayout_6.addWidget(self.groupBox)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_5)


        self.horizontalLayout.addLayout(self.verticalLayout_6)


        self.verticalLayout_8.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.cancelBtn = QPushButton(newProjectDlg)
        self.cancelBtn.setObjectName(u"cancelBtn")

        self.horizontalLayout_2.addWidget(self.cancelBtn)

        self.okBtn = QPushButton(newProjectDlg)
        self.okBtn.setObjectName(u"okBtn")

        self.horizontalLayout_2.addWidget(self.okBtn)


        self.verticalLayout_8.addLayout(self.horizontalLayout_2)


        self.retranslateUi(newProjectDlg)

        QMetaObject.connectSlotsByName(newProjectDlg)
    # setupUi

    def retranslateUi(self, newProjectDlg):
        newProjectDlg.setWindowTitle(QCoreApplication.translate("newProjectDlg", u"Create a new project", None))
        self.label.setText(QCoreApplication.translate("newProjectDlg", u"Project Name", None))
        self.label_2.setText(QCoreApplication.translate("newProjectDlg", u"Description", None))
        self.label_3.setText(QCoreApplication.translate("newProjectDlg", u"Species Collection", None))
        self.label_4.setText(QCoreApplication.translate("newProjectDlg", u"Metadata Group", None))
        self.label_6.setText(QCoreApplication.translate("newProjectDlg", u"Active", None))
        self.groupBox.setTitle("")
        self.yesRadio.setText(QCoreApplication.translate("newProjectDlg", u"Yes", None))
        self.noRadio.setText(QCoreApplication.translate("newProjectDlg", u"No", None))
        self.cancelBtn.setText(QCoreApplication.translate("newProjectDlg", u"Cancel", None))
        self.okBtn.setText(QCoreApplication.translate("newProjectDlg", u"OK", None))
    # retranslateUi

