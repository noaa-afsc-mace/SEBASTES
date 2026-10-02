# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'targetDlg.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QFormLayout,
    QFrame, QHBoxLayout, QLabel, QPushButton,
    QSizePolicy, QSpacerItem, QWidget)

class Ui_targetDlg(object):
    def setupUi(self, targetDlg):
        if not targetDlg.objectName():
            targetDlg.setObjectName(u"targetDlg")
        targetDlg.resize(300, 217)
        self.formLayout = QFormLayout(targetDlg)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setFieldGrowthPolicy(QFormLayout.AllNonFixedFieldsGrow)
        self.label = QLabel(targetDlg)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label)

        self.targetLabel = QLabel(targetDlg)
        self.targetLabel.setObjectName(u"targetLabel")
        self.targetLabel.setMinimumSize(QSize(0, 23))
        self.targetLabel.setFrameShape(QFrame.Box)

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.targetLabel)

        self.label_3 = QLabel(targetDlg)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_3)

        self.classBox = QComboBox(targetDlg)
        self.classBox.setObjectName(u"classBox")
        self.classBox.setMinimumSize(QSize(0, 23))

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.classBox)

        self.frame = QFrame(targetDlg)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 50))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.cancelBtn = QPushButton(self.frame)
        self.cancelBtn.setObjectName(u"cancelBtn")

        self.horizontalLayout.addWidget(self.cancelBtn)

        self.saveBtn = QPushButton(self.frame)
        self.saveBtn.setObjectName(u"saveBtn")

        self.horizontalLayout.addWidget(self.saveBtn)


        self.formLayout.setWidget(5, QFormLayout.ItemRole.SpanningRole, self.frame)

        self.label_2 = QLabel(targetDlg)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.label_2)

        self.measureLabel = QLabel(targetDlg)
        self.measureLabel.setObjectName(u"measureLabel")
        self.measureLabel.setMinimumSize(QSize(0, 23))
        self.measureLabel.setFrameShape(QFrame.Box)

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.measureLabel)

        self.label_4 = QLabel(targetDlg)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.LabelRole, self.label_4)

        self.rangeLabel = QLabel(targetDlg)
        self.rangeLabel.setObjectName(u"rangeLabel")
        self.rangeLabel.setMinimumSize(QSize(0, 23))
        self.rangeLabel.setFrameShape(QFrame.Box)

        self.formLayout.setWidget(4, QFormLayout.ItemRole.FieldRole, self.rangeLabel)

        self.measureBtn = QPushButton(targetDlg)
        self.measureBtn.setObjectName(u"measureBtn")
        self.measureBtn.setMinimumSize(QSize(0, 28))

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.measureBtn)


        self.retranslateUi(targetDlg)

        QMetaObject.connectSlotsByName(targetDlg)
    # setupUi

    def retranslateUi(self, targetDlg):
        targetDlg.setWindowTitle(QCoreApplication.translate("targetDlg", u"Target Actions", None))
        self.label.setText(QCoreApplication.translate("targetDlg", u"Target ID", None))
        self.targetLabel.setText("")
        self.label_3.setText(QCoreApplication.translate("targetDlg", u"Class", None))
        self.cancelBtn.setText(QCoreApplication.translate("targetDlg", u"Cancel", None))
        self.saveBtn.setText(QCoreApplication.translate("targetDlg", u"Save", None))
        self.label_2.setText(QCoreApplication.translate("targetDlg", u"Length", None))
        self.measureLabel.setText("")
        self.label_4.setText(QCoreApplication.translate("targetDlg", u"Range", None))
        self.rangeLabel.setText("")
        self.measureBtn.setText(QCoreApplication.translate("targetDlg", u"Measure", None))
    # retranslateUi

