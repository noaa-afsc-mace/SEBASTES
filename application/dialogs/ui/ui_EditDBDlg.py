# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'EditDBDlg.ui'
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
    QGroupBox, QHBoxLayout, QLabel, QLineEdit,
    QPlainTextEdit, QPushButton, QRadioButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_editDBDlg(object):
    def setupUi(self, editDBDlg):
        if not editDBDlg.objectName():
            editDBDlg.setObjectName(u"editDBDlg")
        editDBDlg.resize(1097, 391)
        self.verticalLayout = QVBoxLayout(editDBDlg)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.groupBox = QGroupBox(editDBDlg)
        self.groupBox.setObjectName(u"groupBox")
        self.horizontalLayout_4 = QHBoxLayout(self.groupBox)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.appRadio = QRadioButton(self.groupBox)
        self.appRadio.setObjectName(u"appRadio")

        self.horizontalLayout_4.addWidget(self.appRadio)

        self.locRadio = QRadioButton(self.groupBox)
        self.locRadio.setObjectName(u"locRadio")

        self.horizontalLayout_4.addWidget(self.locRadio)


        self.horizontalLayout.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(editDBDlg)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.horizontalLayout_5 = QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_2)

        self.updateBtn = QPushButton(self.groupBox_2)
        self.updateBtn.setObjectName(u"updateBtn")
        self.updateBtn.setCheckable(True)
        self.updateBtn.setAutoExclusive(True)

        self.horizontalLayout_5.addWidget(self.updateBtn)

        self.deleteBtn = QPushButton(self.groupBox_2)
        self.deleteBtn.setObjectName(u"deleteBtn")
        self.deleteBtn.setCheckable(True)
        self.deleteBtn.setAutoExclusive(True)

        self.horizontalLayout_5.addWidget(self.deleteBtn)


        self.horizontalLayout.addWidget(self.groupBox_2)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.updateFrame = QFrame(editDBDlg)
        self.updateFrame.setObjectName(u"updateFrame")
        self.updateFrame.setFrameShape(QFrame.StyledPanel)
        self.updateFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.updateFrame)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label = QLabel(self.updateFrame)
        self.label.setObjectName(u"label")

        self.horizontalLayout_6.addWidget(self.label)

        self.updateTableBox = QComboBox(self.updateFrame)
        self.updateTableBox.setObjectName(u"updateTableBox")

        self.horizontalLayout_6.addWidget(self.updateTableBox)

        self.label_2 = QLabel(self.updateFrame)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_6.addWidget(self.label_2)

        self.updateFieldBox = QComboBox(self.updateFrame)
        self.updateFieldBox.setObjectName(u"updateFieldBox")

        self.horizontalLayout_6.addWidget(self.updateFieldBox)

        self.label_3 = QLabel(self.updateFrame)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_6.addWidget(self.label_3)

        self.updateValueEdit = QLineEdit(self.updateFrame)
        self.updateValueEdit.setObjectName(u"updateValueEdit")

        self.horizontalLayout_6.addWidget(self.updateValueEdit)

        self.label_4 = QLabel(self.updateFrame)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_6.addWidget(self.label_4)

        self.updateConditionFieldBox = QComboBox(self.updateFrame)
        self.updateConditionFieldBox.setObjectName(u"updateConditionFieldBox")

        self.horizontalLayout_6.addWidget(self.updateConditionFieldBox)

        self.updateSignBox = QComboBox(self.updateFrame)
        self.updateSignBox.setObjectName(u"updateSignBox")

        self.horizontalLayout_6.addWidget(self.updateSignBox)

        self.updateWhereValueEdit = QLineEdit(self.updateFrame)
        self.updateWhereValueEdit.setObjectName(u"updateWhereValueEdit")

        self.horizontalLayout_6.addWidget(self.updateWhereValueEdit)

        self.updateWhereValueBox = QComboBox(self.updateFrame)
        self.updateWhereValueBox.setObjectName(u"updateWhereValueBox")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.updateWhereValueBox.sizePolicy().hasHeightForWidth())
        self.updateWhereValueBox.setSizePolicy(sizePolicy)
        self.updateWhereValueBox.setMinimumSize(QSize(200, 0))

        self.horizontalLayout_6.addWidget(self.updateWhereValueBox)

        self.updateSQLBtn = QPushButton(self.updateFrame)
        self.updateSQLBtn.setObjectName(u"updateSQLBtn")

        self.horizontalLayout_6.addWidget(self.updateSQLBtn)


        self.verticalLayout.addWidget(self.updateFrame)

        self.deleteFrame = QFrame(editDBDlg)
        self.deleteFrame.setObjectName(u"deleteFrame")
        self.deleteFrame.setFrameShape(QFrame.StyledPanel)
        self.deleteFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.deleteFrame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_6 = QLabel(self.deleteFrame)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_2.addWidget(self.label_6)

        self.deleteTableBox = QComboBox(self.deleteFrame)
        self.deleteTableBox.setObjectName(u"deleteTableBox")

        self.horizontalLayout_2.addWidget(self.deleteTableBox)

        self.label_7 = QLabel(self.deleteFrame)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_2.addWidget(self.label_7)

        self.deleteConditionFieldBox = QComboBox(self.deleteFrame)
        self.deleteConditionFieldBox.setObjectName(u"deleteConditionFieldBox")

        self.horizontalLayout_2.addWidget(self.deleteConditionFieldBox)

        self.deleteSignBox = QComboBox(self.deleteFrame)
        self.deleteSignBox.setObjectName(u"deleteSignBox")

        self.horizontalLayout_2.addWidget(self.deleteSignBox)

        self.deleteWhereValueEdit = QLineEdit(self.deleteFrame)
        self.deleteWhereValueEdit.setObjectName(u"deleteWhereValueEdit")

        self.horizontalLayout_2.addWidget(self.deleteWhereValueEdit)

        self.deleteWhereValueBox = QComboBox(self.deleteFrame)
        self.deleteWhereValueBox.setObjectName(u"deleteWhereValueBox")
        sizePolicy.setHeightForWidth(self.deleteWhereValueBox.sizePolicy().hasHeightForWidth())
        self.deleteWhereValueBox.setSizePolicy(sizePolicy)
        self.deleteWhereValueBox.setMinimumSize(QSize(200, 0))

        self.horizontalLayout_2.addWidget(self.deleteWhereValueBox)

        self.deleteSQLBtn = QPushButton(self.deleteFrame)
        self.deleteSQLBtn.setObjectName(u"deleteSQLBtn")

        self.horizontalLayout_2.addWidget(self.deleteSQLBtn)


        self.verticalLayout.addWidget(self.deleteFrame)

        self.sqlCmdTable = QPlainTextEdit(editDBDlg)
        self.sqlCmdTable.setObjectName(u"sqlCmdTable")
        self.sqlCmdTable.setReadOnly(True)

        self.verticalLayout.addWidget(self.sqlCmdTable)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.runBtn = QPushButton(editDBDlg)
        self.runBtn.setObjectName(u"runBtn")

        self.horizontalLayout_3.addWidget(self.runBtn)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.okBtn = QPushButton(editDBDlg)
        self.okBtn.setObjectName(u"okBtn")

        self.horizontalLayout_3.addWidget(self.okBtn)


        self.verticalLayout.addLayout(self.horizontalLayout_3)


        self.retranslateUi(editDBDlg)

        QMetaObject.connectSlotsByName(editDBDlg)
    # setupUi

    def retranslateUi(self, editDBDlg):
        editDBDlg.setWindowTitle(QCoreApplication.translate("editDBDlg", u"Dialog", None))
        self.groupBox.setTitle(QCoreApplication.translate("editDBDlg", u"Database", None))
        self.appRadio.setText(QCoreApplication.translate("editDBDlg", u"Application", None))
        self.locRadio.setText(QCoreApplication.translate("editDBDlg", u"Local", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("editDBDlg", u"Action", None))
        self.updateBtn.setText(QCoreApplication.translate("editDBDlg", u"UPDATE", None))
        self.deleteBtn.setText(QCoreApplication.translate("editDBDlg", u"DELETE", None))
        self.label.setText(QCoreApplication.translate("editDBDlg", u"UPDATE", None))
        self.label_2.setText(QCoreApplication.translate("editDBDlg", u"SET", None))
        self.label_3.setText(QCoreApplication.translate("editDBDlg", u"=", None))
        self.label_4.setText(QCoreApplication.translate("editDBDlg", u"WHERE", None))
        self.updateSQLBtn.setText(QCoreApplication.translate("editDBDlg", u"generate SQL", None))
        self.label_6.setText(QCoreApplication.translate("editDBDlg", u"DELETE FROM", None))
        self.label_7.setText(QCoreApplication.translate("editDBDlg", u"WHERE", None))
        self.deleteSQLBtn.setText(QCoreApplication.translate("editDBDlg", u"generate SQL", None))
        self.runBtn.setText(QCoreApplication.translate("editDBDlg", u"Run Action", None))
        self.okBtn.setText(QCoreApplication.translate("editDBDlg", u"Done", None))
    # retranslateUi

