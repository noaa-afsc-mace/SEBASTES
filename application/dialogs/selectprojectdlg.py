
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import QtSql
from dialogs.ui import  ui_SelectProjectDlg


class SelectProjectDlg(QDialog, ui_SelectProjectDlg.Ui_selectProjectDlg):
    def __init__(self, parent):
        super(SelectProjectDlg, self).__init__(parent)
        self.setupUi(self)
        self.appDB=parent.appDB
        self.okBtn.clicked.connect(self.exit)
        self.cancelBtn.clicked.connect(self.cancel)
        self.createNewProjBtn.clicked.connect(self.createProject)
        self.selectedProject=None
        self.selectedProjectDict={}
        
        self.projModel = QtSql.QSqlQueryModel()
        self.projectView.setModel(self.projModel)
        self.projectView.show()

        self.projSelModel=QItemSelectionModel(self.projModel, self.projectView)
        self.projectView.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.projectView.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.projectView.setSelectionModel(self.projSelModel)
        
        self.projSelModel.selectionChanged.connect(self.selectionAction)
        
        self.refreshList()
        
    def refreshList(self):
        self.projModel.setQuery("SELECT * FROM PROJECTS WHERE ACTIVE='Yes'", self.appDB.db)
        self.projectView.reset()
        self.projectView.resizeColumnsToContents()
        self.projectView.scrollToBottom()
        
    def selectionAction(self):
        self.selectedProjectDict={}
        selObj=self.projectView.currentIndex()
        index= self.projModel.index(selObj.row(), 0, QModelIndex())
        self.selectedProject=self.projModel.data(index, Qt.DisplayRole)
        index= self.projModel.index(selObj.row(), 2, QModelIndex())
        db_path=self.projModel.data(index, Qt.DisplayRole)
        index= self.projModel.index(selObj.row(), 3, QModelIndex())
        spc_collection=self.projModel.data(index, Qt.DisplayRole)
        index= self.projModel.index(selObj.row(), 4, QModelIndex())
        metadata=self.projModel.data(index, Qt.DisplayRole)
        self.selectedProjectDict.update({'project':self.selectedProject,
                                                    'database_path':db_path, 
                                                    'species_collection':spc_collection, 
                                                    'metadata_group':metadata})
        
    def createProject(self):
        from dialogs import newprojectdlg
        dlg=newprojectdlg.NewProjectDlg(self)
        if dlg.exec_():
            self.refreshList()
            # select the new one
            self.selectedProject=dlg.projectNameEdit.text()
            for i in range(self.projModel.rowCount()):
                index1= self.projModel.index(i, 0, QModelIndex())
                if self.projModel.data(index1, Qt.DisplayRole)==self.selectedProject :
                    self.projectView.selectRow(i)
                    break

    @pyqtSlot()
    def cancel(self):
        self.reject()
        
    @pyqtSlot()
    def exit(self):
        if not self.selectedProject:
            QMessageBox.warning(self, "ERROR", 'Nothing was selected!')
            self.reject()
        self.accept()
