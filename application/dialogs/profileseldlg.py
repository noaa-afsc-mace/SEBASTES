
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import QtSql
from dialogs.ui import  ui_ProfileSelDlg

class ProfileSelDlg(QDialog, ui_ProfileSelDlg.Ui_profileSelDlg):
    def __init__(self, parent=None):
        super(ProfileSelDlg, self).__init__(parent)
        self.setupUi(self)
        self.db=parent.profileDB.db
        self.selectBtn.clicked.connect(self.exit)
        self.cancelBtn.clicked.connect(self.cancel)

        self.activeProfile=None
        
        self.profilesModel = QtSql.QSqlQueryModel()
        self.profilesView.setModel(self.profilesModel)
        self.profilesView.show()
        self.profilesSelModel=QItemSelectionModel(self.profilesModel, self.profilesView)
        self.profilesView.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.profilesView.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.profilesView.setSelectionModel(self.profilesSelModel)
        self.profilesSelModel.selectionChanged.connect(self.selectionAction)
        self.loadProfiles()
        
    def loadProfiles(self):
        self.profilesModel.setQuery("SELECT profile_name, description FROM PROFILES WHERE active='Yes'", self.db)
        self.profilesView.reset()
        
    def selectionAction(self):
            selObj=self.profilesView.currentIndex()
            index1= self.profilesModel.index(selObj.row(), 0, QModelIndex())
            self.activeProfile=self.profilesModel.data(index1, Qt.DisplayRole)
        
    @pyqtSlot()
    def cancel(self):
        self.reject()
        
    @pyqtSlot()
    def exit(self):
        if self.activeProfile==None:
            QMessageBox.warning(self, "ERROR", "Ya didn't select anythin'!")
            self.reject()
        self.accept()
