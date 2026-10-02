# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ViewApplicationDBDlg.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QHeaderView, QSizePolicy,
    QTabWidget, QTableView, QVBoxLayout, QWidget)

class Ui_viewApplicationDB(object):
    def setupUi(self, viewApplicationDB):
        if not viewApplicationDB.objectName():
            viewApplicationDB.setObjectName(u"viewApplicationDB")
        viewApplicationDB.resize(681, 542)
        self.verticalLayout = QVBoxLayout(viewApplicationDB)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tabs = QTabWidget(viewApplicationDB)
        self.tabs.setObjectName(u"tabs")
        self.projects = QWidget()
        self.projects.setObjectName(u"projects")
        self.verticalLayout_2 = QVBoxLayout(self.projects)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.projectsView = QTableView(self.projects)
        self.projectsView.setObjectName(u"projectsView")

        self.verticalLayout_2.addWidget(self.projectsView)

        self.tabs.addTab(self.projects, "")
        self.profiles = QWidget()
        self.profiles.setObjectName(u"profiles")
        self.verticalLayout_3 = QVBoxLayout(self.profiles)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.profilesView = QTableView(self.profiles)
        self.profilesView.setObjectName(u"profilesView")

        self.verticalLayout_3.addWidget(self.profilesView)

        self.tabs.addTab(self.profiles, "")
        self.profile_settings = QWidget()
        self.profile_settings.setObjectName(u"profile_settings")
        self.verticalLayout_4 = QVBoxLayout(self.profile_settings)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.profileSettingsView = QTableView(self.profile_settings)
        self.profileSettingsView.setObjectName(u"profileSettingsView")

        self.verticalLayout_4.addWidget(self.profileSettingsView)

        self.tabs.addTab(self.profile_settings, "")
        self.metadata_groups = QWidget()
        self.metadata_groups.setObjectName(u"metadata_groups")
        self.verticalLayout_5 = QVBoxLayout(self.metadata_groups)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.metadataGroupsView = QTableView(self.metadata_groups)
        self.metadataGroupsView.setObjectName(u"metadataGroupsView")

        self.verticalLayout_5.addWidget(self.metadataGroupsView)

        self.tabs.addTab(self.metadata_groups, "")
        self.frame_metadata_setup = QWidget()
        self.frame_metadata_setup.setObjectName(u"frame_metadata_setup")
        self.verticalLayout_6 = QVBoxLayout(self.frame_metadata_setup)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.frameMetadataSetupView = QTableView(self.frame_metadata_setup)
        self.frameMetadataSetupView.setObjectName(u"frameMetadataSetupView")

        self.verticalLayout_6.addWidget(self.frameMetadataSetupView)

        self.tabs.addTab(self.frame_metadata_setup, "")
        self.species_collections = QWidget()
        self.species_collections.setObjectName(u"species_collections")
        self.verticalLayout_7 = QVBoxLayout(self.species_collections)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.speciesCollectionsView = QTableView(self.species_collections)
        self.speciesCollectionsView.setObjectName(u"speciesCollectionsView")

        self.verticalLayout_7.addWidget(self.speciesCollectionsView)

        self.tabs.addTab(self.species_collections, "")
        self.species_setup = QWidget()
        self.species_setup.setObjectName(u"species_setup")
        self.verticalLayout_8 = QVBoxLayout(self.species_setup)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.speciesSetupView = QTableView(self.species_setup)
        self.speciesSetupView.setObjectName(u"speciesSetupView")

        self.verticalLayout_8.addWidget(self.speciesSetupView)

        self.tabs.addTab(self.species_setup, "")

        self.verticalLayout.addWidget(self.tabs)


        self.retranslateUi(viewApplicationDB)

        self.tabs.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(viewApplicationDB)
    # setupUi

    def retranslateUi(self, viewApplicationDB):
        viewApplicationDB.setWindowTitle(QCoreApplication.translate("viewApplicationDB", u"Dialog", None))
        self.tabs.setTabText(self.tabs.indexOf(self.projects), QCoreApplication.translate("viewApplicationDB", u"Projects", None))
        self.tabs.setTabText(self.tabs.indexOf(self.profiles), QCoreApplication.translate("viewApplicationDB", u"Profiles", None))
        self.tabs.setTabText(self.tabs.indexOf(self.profile_settings), QCoreApplication.translate("viewApplicationDB", u"Profile Settings", None))
        self.tabs.setTabText(self.tabs.indexOf(self.metadata_groups), QCoreApplication.translate("viewApplicationDB", u"Metadata Groups", None))
        self.tabs.setTabText(self.tabs.indexOf(self.frame_metadata_setup), QCoreApplication.translate("viewApplicationDB", u"Frame Metadata Setup", None))
        self.tabs.setTabText(self.tabs.indexOf(self.species_collections), QCoreApplication.translate("viewApplicationDB", u"Species Collections", None))
        self.tabs.setTabText(self.tabs.indexOf(self.species_setup), QCoreApplication.translate("viewApplicationDB", u"Species Setup", None))
    # retranslateUi

