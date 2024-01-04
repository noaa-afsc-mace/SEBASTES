
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import QtSql
from dialogs.ui import  ui_DataviewDlg
from dialogs import speciesgroupdlg




class DataViewDlg(QDialog, ui_DataviewDlg.Ui_dataviewDlg):
    selectionEvent = pyqtSignal(int, int)
    keyPress = pyqtSignal(object, object)
    
    def __init__(self, parent=None):
        super(DataViewDlg, self).__init__(parent)
        self.setupUi(self)
        self.db=parent.dataDB.db
        self.deployment=parent.deployment
        self.speciesList=parent.speciesList
        self.checkWidget=parent.showDataCheck
        
        self.frameModel = QtSql.QSqlQueryModel()
        self.frameTable.setModel(self.frameModel)
        self.frameTable.show()

        self.frameSelModel=QItemSelectionModel(self.frameModel, self.frameTable)
        self.frameTable.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.frameTable.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.frameTable.setSelectionModel(self.frameSelModel)
        
        self.metadataModel = QtSql.QSqlQueryModel()
        self.metadataTable.setModel(self.metadataModel)
        self.metadataTable.show()

        self.metadataSelModel=QItemSelectionModel(self.metadataModel, self.metadataTable)
        self.metadataTable.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.metadataTable.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.metadataTable.setSelectionModel(self.metadataSelModel)
        
        self.targetModel = QtSql.QSqlQueryModel()
        self.targetTable.setModel(self.targetModel)
        self.targetTable.show()
        
        self.targetSelModel=QItemSelectionModel(self.targetModel, self.targetTable)
        self.targetTable.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.targetTable.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.targetTable.setSelectionModel(self.targetSelModel)
        
        self.targetSelModel.selectionChanged.connect(self.selectionAction)
        self.frameSelModel.selectionChanged.connect(self.selectionAction)
        self.metadataSelModel.selectionChanged.connect(self.selectionAction)
        
        self.filterBtn.clicked.connect(self.filterBySpecies)
        self.editBtn.clicked.connect(self.editSpecies)
        

        
        self.refreshView()
        
        
    def refreshView(self, scroll=True):
        self.metadataModel.setQuery("SELECT FRAME_NUMBER,METADATA_GROUP,METADATA_TAG,METADATA_TYPE,METADATA_VALUE FROM frame_metadata WHERE deployment_id='"+self.deployment+"'", self.db)
        self.metadataTable.reset()
        self.metadataTable.scrollToBottom()
        self.frameModel.setQuery("SELECT FRAME_NUMBER, FRAME_TIME, COMMENT FROM frames WHERE deployment_id='"+self.deployment+"' ORDER BY frame_number", self.db)
        self.frameTable.reset()
        self.frameTable.scrollToBottom()
        self.targetModel.setQuery("SELECT FRAME_NUMBER,TARGET_NUMBER,SPECIES_GROUP,LX,LY,RX,RY,LENGTH,RANGE,ERROR,TARGET_LINK,COMMENT FROM targets WHERE deployment_id='"+self.deployment+"' ORDER BY frame_number, target_number", self.db)
        self.targetTable.reset()
        if scroll:
            self.targetTable.scrollToBottom()
        
    def filterBySpecies(self):
        if self.filterBtn.isChecked():
            dlg=speciesgroupdlg.SpeciesGroupDlg(self)
            speciesList=[]
            query=QtSql.QSqlQuery("SELECT species_group FROM targets WHERE deployment_id='"+self.deployment+"' GROUP BY species_group ORDER BY species_group", self.db)
            while query.next():
                speciesList.append(query.value(0))
            dlg.setList(speciesList)
            if dlg.exec_():
                self.targetModel.setQuery("SELECT FRAME_NUMBER,TARGET_NUMBER,SPECIES_GROUP,LX,LY,RX,RY,LENGTH,RANGE,ERROR,TARGET_LINK,COMMENT FROM targets WHERE species_group='"+dlg.listWidget.currentItem().text()+"' AND deployment_id='"+self.deployment+"' ORDER BY frame_number, target_number", self.db)
                self.targetTable.reset()
        else:
            self.refreshView()
            
    def editSpecies(self):
        selObj=self.targetTable.currentIndex()
        index1= self.targetModel.index(selObj.row(), 1, QModelIndex())
        index2= self.targetModel.index(selObj.row(), 0, QModelIndex())
        target_number=self.targetModel.data(index1, Qt.DisplayRole)
        frame_number=self.targetModel.data(index2, Qt.DisplayRole)
        dlg=speciesgroupdlg.SpeciesGroupDlg(self)
#        speciesList=[]
#        query=QtSql.QSqlQuery("SELECT species_group FROM targets GROUP BY species_group ORDER BY species_group", self.db)
#        while query.next():
#            speciesList.append(query.value(0))
        dlg.setList(self.speciesList)
        if dlg.exec_():
            QtSql.QSqlQuery("UPDATE targets SET species_group='"+dlg.listWidget.currentItem().text()+
            "' WHERE frame_number="+str(frame_number)+" AND target_number="+str(target_number)+ " AND deployment_id='"+self.deployment+"'" , self.db)
        self.refreshView(False)
        
    def keyPressEvent(self, ev):
        """
        Event handler for keyboard key press events
        """
        self.keyPress.emit(self, ev)
        
    def selectionAction(self):
        if self.sender()==self.targetSelModel:
            selObj=self.targetTable.currentIndex()
            index1= self.targetModel.index(selObj.row(), 1, QModelIndex())
            index2= self.targetModel.index(selObj.row(), 0, QModelIndex())
            target_number=self.targetModel.data(index1, Qt.DisplayRole)
            frame_number=self.targetModel.data(index2, Qt.DisplayRole)
        elif self.sender()==self.frameSelModel:
            selObj=self.frameTable.currentIndex()
            index= self.frameModel.index(selObj.row(), 1, QModelIndex())
            frame_number=self.frameModel.data(index, Qt.DisplayRole)
            target_number=None
        else:
            selObj=self.metadataTable.currentIndex()
            index= self.metadataModel.index(selObj.row(), 0, QModelIndex())
            frame_number=int(self.metadataModel.data(index, Qt.DisplayRole))
            target_number=None
        if frame_number>0:
            self.selectionEvent.emit(frame_number,  target_number)
            
    def setSelectedRowFromData(self, frame, target):
        for i in range(self.targetModel.rowCount()):
            index1= self.targetModel.index(i, 1, QModelIndex())
            index2= self.targetModel.index(i, 0, QModelIndex())
            if self.targetModel.data(index1, Qt.DisplayRole)==target and self.targetModel.data(index2, Qt.DisplayRole)==frame:
                self.targetTable.selectRow(i)
        
    def closeEvent(self,  event):
        self.checkWidget.setChecked(False)
        event.accept()


