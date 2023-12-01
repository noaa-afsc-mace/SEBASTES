
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from dialogs.ui import  ui_NewProjectDlg

class NewProjectDlg(QDialog, ui_NewProjectDlg.Ui_newProjectDlg):
    def __init__(self, parent):
        super(NewProjectDlg, self).__init__(parent)
        self.setupUi(self)
        self.appDB=parent.appDB
        self.okBtn.clicked.connect(self.exitCheck)
        self.cancelBtn.clicked.connect(self.cancel)
        self.findPathBtn.clicked.connect(self.findDBPath)
        self.bad=False
        self.populateBoxWidgets()
        
    def populateBoxWidgets(self):
        query=self.appDB.dbQuery("SELECT SPECIES_COLLECTION FROM SPECIES_COLLECTIONS")
        for val,  in query:
            self.speciesBox.addItem(val)
        self.speciesBox.setCurrentIndex(-1)
        query=self.appDB.dbQuery("SELECT METADATA_GROUP FROM METADATA_GROUPS")
        for val,  in query:
            self.metadataBox.addItem(val)
        self.metadataBox.setCurrentIndex(-1)
        self.yesRadio.setChecked(True)
        
    def findDBPath(self):
        dirDlg = QFileDialog(self)
        dbPath = dirDlg.getExistingDirectory(self, 'Select project database directory', 'C:\\',
                                              QFileDialog.ShowDirsOnly)
        self.dbLocEdit.setText(dbPath)
        
    def insertProject(self):
        desc=self.descEdit.toPlainText()
        desc=desc.strip("'")
        desc=desc.strip(",")
        if self.yesRadio.isChecked():
            active='Yes'
        else:
            active='No'
        if self.speciesBox.currentIndex()<0 or self.metadataBox.currentIndex()<0:
            QMessageBox.warning(self, "ERROR", 'Select species and metadata!')
            self.bad=True
            return
        query=self.appDB.dbExec("INSERT INTO PROJECTS (PROJECT, DESCRIPTION,  DATABASE_PATH,  SPECIES_COLLECTION,  METADATA_GROUP,  ACTIVE) VALUES("+
        "'"+self.projNameEdit.text()+"', '"+desc+"', '"+self.dbLocEdit.text()+"', '"+self.speciesBox.currentText()+"', '"+self.metadataBox.currentText()+"', '"+active+"')")
        # make sure it happened and tell folks so
        query1=self.appDB.dbQuery("SELECT PROJECT FROM PROJECTS WHERE PROJECT='"+self.projNameEdit.text()+"'")
        if query1.first():
            QMessageBox.information(self, "NOTE", 'Project has been created!')
        else:
            QMessageBox.warning(self, "ERROR", 'Something is wrong: '+query.lastError().text())
        
    @pyqtSlot()
    def cancel(self):
        self.reject()
        

    def exitCheck(self):
        if not self.bad:
            self.insertProject()
            self.exit()
        else:
            return
            
    @pyqtSlot()        
    def exit(self):
        self.accept()
        
