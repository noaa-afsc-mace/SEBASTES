
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import QtSql
from dialogs.ui import  ui_MakeSelDlg

class MakeSelDlg(QDialog, ui_MakeSelDlg.Ui_makeSelDlg):
    def __init__(self, parent=None,  mode='profile',  action='imp_exp'):
        super(MakeSelDlg, self).__init__(parent)
        self.setupUi(self)
        
        self.selectBtn.clicked.connect(self.exit)
        self.cancelBtn.clicked.connect(self.cancel)
        self.mode=mode
        self.action=action
        self.value=None
        self.new=False
        self.viewModel = QtSql.QSqlQueryModel()
        self.dataView.setModel(self.viewModel)
        self.viewSelModel=QItemSelectionModel(self.viewModel, self.dataView)
        self.dataView.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.dataView.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.dataView.setSelectionModel(self.viewSelModel)
        self.viewSelModel.selectionChanged.connect(self.selectionAction)
        
        
        self.appDB=parent.appDB
        self.loadView()
        if mode=='profile':
            self.label.setText('Select Profile')
        elif mode=='species':
            self.label.setText('Select Species Collection')
        elif mode=='metadata':
            self.label.setText('Select Metadata Group')
            
    def loadView(self):
        if self.mode=='profile':
            if self.action=='imp_exp':
                self.viewModel.setQuery("SELECT profile, description FROM PROFILES", self.appDB.db)
            else:
                self.viewModel.setQuery("SELECT profile, description FROM PROFILES WHERE active='Yes'", self.appDB.db)
        elif self.mode=='species':
            if self.action=='imp_exp':
                self.viewModel.setQuery("SELECT species_collection, description FROM SPECIES_COLLECTIONS", self.appDB.db)
            else:
                query = QtSql.QSqlQuery(self.appDB.db)
                ok = query.exec_("SELECT active from species_collections")
                if not ok:
                    query = QtSql.QSqlQuery(self.appDB.db)
                    query.exec_("ALTER TABLE SPECIES_COLLECTIONS ADD active TEXT")
                    QtSql.QSqlQuery("UPDATE SPECIES_COLLECTIONS SET active='Yes'",self.appDB.db)
                self.viewModel.setQuery("SELECT species_collection, description FROM SPECIES_COLLECTIONS WHERE active='Yes'", self.appDB.db)
        elif self.mode=='metadata':
            if self.action=='imp_exp':
                self.viewModel.setQuery("SELECT metadata_group, description FROM METADATA_GROUPS", self.appDB.db)
            else:
                query = QtSql.QSqlQuery(self.appDB.db)
                ok = query.exec_("SELECT active FROM METADATA_GROUPS")
                if not ok:
                    query = QtSql.QSqlQuery(self.appDB.db)
                    query.exec_("ALTER TABLE METADATA_GROUPS ADD active TEXT")
                    QtSql.QSqlQuery("UPDATE METADATA_GROUPS SET active='Yes'",self.appDB.db)
                self.viewModel.setQuery("SELECT metadata_group, description FROM METADATA_GROUPS WHERE active='Yes'", self.appDB.db)
        self.dataView.reset()
        self.dataView.resizeColumnsToContents()
    def selectionAction(self):
        selObj=self.dataView.currentIndex()
        index1= self.viewModel.index(selObj.row(), 0, QModelIndex())
        self.value=self.viewModel.data(index1, Qt.DisplayRole)
           
    @pyqtSlot()
    def cancel(self):
        self.reject()
        
    @pyqtSlot()
    def exit(self):
        if self.value==None:
            QMessageBox.warning(self, "ERROR", "Ya didn't select anythin'!")
            self.reject()

        self.accept()
