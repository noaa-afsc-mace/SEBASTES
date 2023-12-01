
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import QtSql
from dialogs.ui import  ui_AssignActivesDlg

class SetActiveCompDlg(QDialog, ui_AssignActivesDlg.Ui_assignActivesDlg):
    
    def __init__(self,  thing,  parent=None):
        super(SetActiveCompDlg, self).__init__(parent)
        self.setupUi(self)
        self.db=parent.db# its the profile db
        self.thing=thing

            
        self.inactiveModel = QtSql.QSqlQueryModel()
        self.inactiveView.setModel(self.inactiveModel)
        self.inactiveView.show()
        
        self.activeModel = QtSql.QSqlQueryModel()
        self.activeView.setModel(self.activeModel)
        self.activeView.show()

        self.inactiveSelModel=QItemSelectionModel(self.inactiveModel, self.inactiveView)
        self.inactiveView.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.inactiveView.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.inactiveView.setSelectionModel(self.inactiveSelModel)
        
        self.activeSelModel=QItemSelectionModel(self.activeModel, self.activeView)
        self.activeView.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.activeView.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.activeView.setSelectionModel(self.activeSelModel)
        

        
        self.addBtn.clicked.connect(self.activate)
        self.remBtn.clicked.connect(self.deactivate)
        self.okBtn.clicked.connect(self.close)
        
        self.refreshViews()
        
    def refreshViews(self):
        if self.thing=='project':
            self.inactiveModel.setQuery("SELECT * FROM projects WHERE active='No'", self.db)
            self.inactiveView.reset()
            self.activeModel.setQuery("SELECT * FROM projects WHERE active='Yes'", self.db)
            self.activeView.reset()
        elif self.thing=='profile':
            self.inactiveModel.setQuery("SELECT * FROM profiles WHERE active='No'", self.db)
            self.inactiveView.reset()
            self.activeModel.setQuery("SELECT * FROM profiles WHERE active='Yes'", self.db)
            self.activeView.reset()
        elif self.thing=='species':
            query = QtSql.QSqlQuery(self.db)
            ok = query.exec_("SELECT active from species_collections")
            if not ok:
                query = QtSql.QSqlQuery(self.db)
                query.exec_("ALTER TABLE SPECIES_COLLECTIONS ADD active TEXT")
                QtSql.QSqlQuery("UPDATE SPECIES_COLLECTIONS SET active='Yes'",self.db)

            self.inactiveModel.setQuery("SELECT * FROM SPECIES_COLLECTIONS WHERE active='No'", self.db)
            self.inactiveView.reset()
            self.activeModel.setQuery("SELECT * FROM SPECIES_COLLECTIONS WHERE active='Yes'", self.db)
            self.activeView.reset()
        elif self.thing=='metadata':
            query = QtSql.QSqlQuery(self.db)
            ok = query.exec_("SELECT active FROM METADATA_GROUPS")
            if not ok:
                query = QtSql.QSqlQuery(self.db)
                query.exec_("ALTER TABLE METADATA_GROUPS ADD active TEXT")
                QtSql.QSqlQuery("UPDATE METADATA_GROUPS SET active='Yes'",self.db)

            self.inactiveModel.setQuery("SELECT * FROM METADATA_GROUPS WHERE active='No'", self.db)
            self.inactiveView.reset()
            self.activeModel.setQuery("SELECT * FROM METADATA_GROUPS WHERE active='Yes'", self.db)
            self.activeView.reset()

        
    def activate(self):
        selObj=self.inactiveView.currentIndex()
        index1= self.inactiveModel.index(selObj.row(), 0, QModelIndex())
        obj=self.inactiveModel.data(index1, Qt.DisplayRole)
        if self.thing=='project':
            QtSql.QSqlQuery("UPDATE PROJECTS SET active='Yes' WHERE project='"+obj+"'",self.db)
        elif self.thing=='profile':
            QtSql.QSqlQuery("UPDATE PROFILES SET active='Yes' WHERE profile='"+obj+"'",self.db)
        elif self.thing=='species':
            QtSql.QSqlQuery("UPDATE SPECIES_COLLECTIONS SET active='Yes' WHERE species_collection='"+obj+"'",self.db)
        elif self.thing=='metadata':
            QtSql.QSqlQuery("UPDATE METADATA_GROUPS SET active='Yes' WHERE metadata_group='"+obj+"'",self.db)
        self.refreshViews()
        
    def deactivate(self):
        selObj=self.activeView.currentIndex()
        index1= self.activeModel.index(selObj.row(), 0, QModelIndex())
        obj=self.activeModel.data(index1, Qt.DisplayRole)
        if self.thing=='project':
            QtSql.QSqlQuery("UPDATE PROJECTS SET active='No' WHERE project='"+obj+"'",self.db)
        elif self.thing=='profile':
            QtSql.QSqlQuery("UPDATE PROFILES SET active='No' WHERE profile='"+obj+"'",self.db)
        elif self.thing=='species':
            QtSql.QSqlQuery("UPDATE SPECIES_COLLECTIONS SET active='No' WHERE species_collection='"+obj+"'",self.db)
        elif self.thing=='metadata':
            QtSql.QSqlQuery("UPDATE METADATA_GROUPS SET active='No' WHERE metadata_group='"+obj+"'",self.db)
        self.refreshViews()
            

    def closeEvent(self,  event):
        event.accept()


