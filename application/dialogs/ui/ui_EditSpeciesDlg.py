# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'EditSpeciesDlg.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QFrame,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QSpinBox, QVBoxLayout,
    QWidget)

class Ui_editSpeciesDlg(object):
    def setupUi(self, editSpeciesDlg):
        if not editSpeciesDlg.objectName():
            editSpeciesDlg.setObjectName(u"editSpeciesDlg")
        editSpeciesDlg.resize(636, 233)
        self.verticalLayout_3 = QVBoxLayout(editSpeciesDlg)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_5 = QLabel(editSpeciesDlg)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_4.addWidget(self.label_5)

        self.startFrameEdit = QLineEdit(editSpeciesDlg)
        self.startFrameEdit.setObjectName(u"startFrameEdit")

        self.verticalLayout_4.addWidget(self.startFrameEdit)


        self.horizontalLayout_4.addLayout(self.verticalLayout_4)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_6 = QLabel(editSpeciesDlg)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_6.addWidget(self.label_6)

        self.endFrameEdit = QLineEdit(editSpeciesDlg)
        self.endFrameEdit.setObjectName(u"endFrameEdit")

        self.verticalLayout_6.addWidget(self.endFrameEdit)


        self.horizontalLayout_4.addLayout(self.verticalLayout_6)


        self.verticalLayout_3.addLayout(self.horizontalLayout_4)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(editSpeciesDlg)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.fromSpeciesBox = QComboBox(editSpeciesDlg)
        self.fromSpeciesBox.setObjectName(u"fromSpeciesBox")

        self.verticalLayout.addWidget(self.fromSpeciesBox)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_2 = QLabel(editSpeciesDlg)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_2.addWidget(self.label_2)

        self.toSpeciesBox = QComboBox(editSpeciesDlg)
        self.toSpeciesBox.setObjectName(u"toSpeciesBox")

        self.verticalLayout_2.addWidget(self.toSpeciesBox)


        self.horizontalLayout.addLayout(self.verticalLayout_2)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(editSpeciesDlg)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_3.addWidget(self.label_3)

        self.targetCountLabel = QLabel(editSpeciesDlg)
        self.targetCountLabel.setObjectName(u"targetCountLabel")
        font = QFont()
        font.setBold(True)
        self.targetCountLabel.setFont(font)
        self.targetCountLabel.setFrameShape(QFrame.Box)

        self.horizontalLayout_3.addWidget(self.targetCountLabel)

        self.label_4 = QLabel(editSpeciesDlg)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_3.addWidget(self.label_4)

        self.spinBox = QSpinBox(editSpeciesDlg)
        self.spinBox.setObjectName(u"spinBox")

        self.horizontalLayout_3.addWidget(self.spinBox)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.changeBtn = QPushButton(editSpeciesDlg)
        self.changeBtn.setObjectName(u"changeBtn")
        self.changeBtn.setFont(font)

        self.horizontalLayout_2.addWidget(self.changeBtn)

        self.nextBtn = QPushButton(editSpeciesDlg)
        self.nextBtn.setObjectName(u"nextBtn")

        self.horizontalLayout_2.addWidget(self.nextBtn)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.changeAllBtn = QPushButton(editSpeciesDlg)
        self.changeAllBtn.setObjectName(u"changeAllBtn")
        self.changeAllBtn.setFont(font)

        self.horizontalLayout_2.addWidget(self.changeAllBtn)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.doneBtn = QPushButton(editSpeciesDlg)
        self.doneBtn.setObjectName(u"doneBtn")

        self.horizontalLayout_2.addWidget(self.doneBtn)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)


        self.retranslateUi(editSpeciesDlg)

        QMetaObject.connectSlotsByName(editSpeciesDlg)
    # setupUi

    def retranslateUi(self, editSpeciesDlg):
        editSpeciesDlg.setWindowTitle(QCoreApplication.translate("editSpeciesDlg", u"Edit Species", None))
        self.label_5.setText(QCoreApplication.translate("editSpeciesDlg", u"Start Frame", None))
        self.label_6.setText(QCoreApplication.translate("editSpeciesDlg", u"End Frame", None))
        self.label.setText(QCoreApplication.translate("editSpeciesDlg", u"Species to find", None))
        self.label_2.setText(QCoreApplication.translate("editSpeciesDlg", u"Change to species", None))
        self.label_3.setText(QCoreApplication.translate("editSpeciesDlg", u"Target count:", None))
        self.targetCountLabel.setText("")
        self.label_4.setText(QCoreApplication.translate("editSpeciesDlg", u"Zoom level:", None))
        self.changeBtn.setText(QCoreApplication.translate("editSpeciesDlg", u"Change", None))
        self.nextBtn.setText(QCoreApplication.translate("editSpeciesDlg", u"Skip", None))
        self.changeAllBtn.setText(QCoreApplication.translate("editSpeciesDlg", u"Change All", None))
        self.doneBtn.setText(QCoreApplication.translate("editSpeciesDlg", u"Done", None))
    # retranslateUi

