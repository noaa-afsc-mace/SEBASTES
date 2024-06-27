
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from dialogs.ui import ui_EditDBDlg
import traceback

class DirectEditDBDlg(QDialog, ui_EditDBDlg.Ui_editDBDlg):
    
    def __init__(self, parent=None):
        super(DirectEditDBDlg, self).__init__(parent)
        self.setupUi(self)
        self.appDB=parent.appDB
        self.dataDB=parent.dataDB
        self.updateFrame.hide()
        self.deleteFrame.hide()
        
        self.appRadio.clicked.connect(self.dbChoice)
        self.locRadio.clicked.connect(self.dbChoice)
        self.updateBtn.clicked.connect(self.actionChoice)
        self.deleteBtn.clicked.connect(self.actionChoice)
        self.runBtn.clicked.connect(self.runSQL)
        self.okBtn.clicked.connect(self.close)
        
        self.updateSQLBtn.clicked.connect(self.buildSQL)
        self.deleteSQLBtn.clicked.connect(self.buildSQL)
        
        self.updateTableBox.activated.connect(self.populateBoxes)
        self.deleteTableBox.activated.connect(self.populateBoxes)
        self.updateSignBox.activated.connect(self.setupQueryWhereItem)
        self.deleteSignBox.activated.connect(self.setupQueryWhereItem)
        self.updateConditionFieldBox.activated.connect(self.setupQueryWhereItem)
        self.deleteConditionFieldBox.activated.connect(self.setupQueryWhereItem)

        if not self.dataDB:
            self.locRadio.setChecked(False)
            self.locRadio.setEnabled(False)
        self.appRadio.setChecked(True)
        self.mode='application'
        self.activeDB=self.appDB
        
        self.updateSignBox.addItems(['=', '>', '<','<>'])
        self.deleteSignBox.addItems(['=', '>', '<','<>'])
        self.updateSignBox.setCurrentIndex(0)
        self.deleteSignBox.setCurrentIndex(0)
        self.setupQueryWhereItem()
        
    def dbChoice(self):
        if self.appRadio.isChecked():
            self.activeDB=self.appDB
            self.mode='application'
        elif self.locRadio.isChecked():
            self.activeDB=self.dataDB
            self.mode='local'

            #QMessageBox.warning(self, "ERROR", 'you havent selected a deployment, no local data to edit')
    def actionChoice(self):
        self.updateFrame.hide()
        self.deleteFrame.hide()
        if self.sender()==self.updateBtn:
            if self.updateBtn.isChecked():
                self.updateFrame.show()
        else:
            if self.deleteBtn.isChecked():
                self.deleteFrame.show()
        self.populateBoxes()
    
    def populateBoxes(self):
        if self.mode=='application':
            self.updateTableBox.addItems(['PROJECTS', 'PROFILES',  'PROFILE_SETTINGS', 'SETTING_DESCRIPTIONS', 'METADATA_GROUPS','FRAME_METADATA_SETUP',  'SPECIES_COLLECTIONS', 'SPECIES_SETUP'])
            self.updateTableBox.setCurrentIndex(0)
            self.deleteTableBox.addItems(['PROJECTS', 'PROFILES',  'PROFILE_SETTINGS', 'SETTING_DESCRIPTIONS', 'METADATA_GROUPS','FRAME_METADATA_SETUP',  'SPECIES_COLLECTIONS', 'SPECIES_SETUP'])
            self.deleteTableBox.setCurrentIndex(0)
        else:
            self.updateTableBox.addItems(['BOUNDING_BOXES',  'DEPLOYMENT',  'FRAMES',  'FRAME_METADATA', 'TARGETS'])
            self.updateTableBox.setCurrentIndex(0)
            self.deleteTableBox.addItems(['BOUNDING_BOXES',  'DEPLOYMENT',  'FRAMES',  'FRAME_METADATA', 'TARGETS'])
            self.deleteTableBox.setCurrentIndex(0)
        self.populateFields()
        
    def populateFields(self):
        for box in [self.updateFieldBox, self.updateConditionFieldBox, self.deleteConditionFieldBox]:
            box.clear()

        query = self.activeDB.dbQuery("PRAGMA table_info('"+self.updateTableBox.currentText()+"')")
        for field in query:
            self.updateFieldBox.addItem(field[1])
            self.updateConditionFieldBox.addItem(field[1])
        self.updateFieldBox.setCurrentIndex(0)
        
        query = self.activeDB.dbQuery("PRAGMA table_info('"+self.deleteTableBox.currentText()+"')")
        for field in query:
            self.deleteConditionFieldBox.addItem(field[1])
        self.deleteConditionFieldBox.setCurrentIndex(0)
        self.setupQueryWhereItem()
        
    def setupQueryWhereItem(self):
        if not self.updateSignBox.currentText()=="=":
            self.updateWhereValueEdit.show()
            self.updateWhereValueBox.hide()
        else:
            self.updateWhereValueBox.show()
            self.updateWhereValueEdit.hide()
            self.populateUpdateWhereValueBoxes()
        if not self.deleteSignBox.currentText()=="=":
            self.deleteWhereValueEdit.show()
            self.deleteWhereValueBox.hide()
        else:
            self.deleteWhereValueBox.show()
            self.deleteWhereValueEdit.hide()
            
    def populateUpdateWhereValueBoxes(self):
        self.deleteWhereValueBox.clear()
        self.updateWhereValueBox.clear()
        
        if self.updateConditionFieldBox.currentText()!='':
            query = self.activeDB.dbQuery("SELECT "+self.updateConditionFieldBox.currentText()+" FROM "+
            self.updateTableBox.currentText()+ " GROUP BY "+self.updateConditionFieldBox.currentText())
            for val,  in query:
                self.updateWhereValueBox.addItem(val)
            self.updateWhereValueBox.adjustSize()
        if self.deleteConditionFieldBox.currentText()!='':
            query = self.activeDB.dbQuery("SELECT "+self.deleteConditionFieldBox.currentText()+" FROM "+
            self.deleteTableBox.currentText()+" GROUP BY "+self.deleteConditionFieldBox.currentText())
            for val,  in query:
                self.deleteWhereValueBox.addItem(val)
            self.deleteWhereValueBox.adjustSize()
            
    def buildSQL(self):
        self.sqlCmdTable.clear()
        testvals=[self.updateValueEdit.text()]
        if self.updateSignBox.currentText()=="=":
            testvals.append(self.updateWhereValueBox.currentText())
        else:
            testvals.append(self.updateWhereValueEdit.text())
        if self.deleteSignBox.currentText()=="=":
            testvals.append(self.deleteWhereValueBox.currentText())
        else:
            testvals.append(self.deleteWhereValueEdit.text())
        stringyfield=[]
        for val in testvals:
            
            try:
                float(val)
                stringyfield.append(val)
            except:
                # first remove nay quotes
                val=val.strip("'")
                stringyfield.append("'"+val+"'")
                
        if self.sender()==self.updateSQLBtn:
            phrase="UPDATE "+self.updateTableBox.currentText()+" SET "+self.updateFieldBox.currentText()+" = "+stringyfield[0]+\
            " WHERE "+self.updateConditionFieldBox.currentText()+" "+self.updateSignBox.currentText()+" "+stringyfield[1]
            self.sqlCmdTable.setPlainText(phrase)
        else:
            phrase="DELETE FROM "+self.deleteTableBox.currentText()+\
            " WHERE "+self.deleteConditionFieldBox.currentText()+" "+self.deleteSignBox.currentText()+" "+stringyfield[2]
            self.sqlCmdTable.setPlainText(phrase)
        
    def runSQL(self):
        reply=QMessageBox.warning(self, "WARNING", "Sure you want to run this SQL statement?  This is not undoable! ",  QMessageBox.Yes, QMessageBox.No)
        if reply==QMessageBox.No:
            return
        else:
            phrase=self.sqlCmdTable.toPlainText()
            self.sqlCmdTable.setPlainText("SQL executed!")
            try:
                # create backup?
                if self.mode=='application':
                    k=self.activeDB.db.databaseName()
                    bits=k.split('Application.db')
                    QFile().copy(k, bits[0]+'Backup.db')
                self.activeDB.dbExec(phrase)
            except:
                t=traceback.format_exception(*sys.exc_info())
                txt=''
                for line in t:
                    txt=txt+line+'\n'
                self.sqlCmdTable.setPlainText(txt)
            
        
    def closeEvent(self,  event):
        event.accept()


