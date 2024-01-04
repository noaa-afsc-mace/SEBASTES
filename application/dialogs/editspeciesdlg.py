
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from dialogs.ui import  ui_EditSpeciesDlg


class EditSpeciesDlg(QDialog, ui_EditSpeciesDlg.Ui_editSpeciesDlg):
    goToTargetEvent = pyqtSignal(int, int,  int)
    
    def __init__(self, parent=None):
        super(EditSpeciesDlg, self).__init__(parent)
        self.setupUi(self)
        self.dataDB=parent.dataDB
        self.deployment=parent.deployment
        self.fullSpeciesList=parent.speciesList
        self.speciesList=[]
        speciesList=[]
        self.zoomLevelChange=0
        self.zoomLevel=0
        query=self.dataDB.dbQuery("SELECT species_group FROM targets WHERE deployment_id='"+self.deployment+"' GROUP BY species_group ORDER BY species_group")
        for species,  in query:
                speciesList.append(species)
        self.currentFrame=None
        self.currentTarget=None
        
        # populate lists
        self.toSpeciesBox.addItems(self.fullSpeciesList)
        self.fromSpeciesBox.addItems(speciesList)
        self.toSpeciesBox.setCurrentIndex(-1)
        self.fromSpeciesBox.setCurrentIndex(-1)
        self.fromSpeciesBox.currentIndexChanged.connect(self.getSpeciesTargets)
        #populate frame range boxes
        query=self.dataDB.dbQuery("SELECT min(frame_number) as minfr,  max(frame_number) as maxfr FROM targets WHERE deployment_id='"+self.deployment+"' GROUP BY species_group ORDER BY species_group")
        minfr, maxfr=query.first()
        self.startFrameEdit.setText(minfr)
        self.endFrameEdit.setText(maxfr)
        self.nextBtn.clicked.connect(self.goToNextFish)
        self.changeBtn.clicked.connect(self.changeSpecies)
        self.changeAllBtn.clicked.connect(self.changeAll)
        self.spinBox.valueChanged.connect(self.changeZoom)
        self.doneBtn.clicked.connect(self.close)
        
        
    def goToNextFish(self):
        if len(self.targetList)>0:
            values=self.targetList.pop(0)
            # navigate to this fish
            # check to see if frame changes!!!
            if self.currentFrame!=values[0]:
                self.zoomLevel=0
            self.currentFrame=values[0]
            self.currentTarget=values[1]
            self.zoomLevelChange=self.spinBox.value()-self.zoomLevel
            self.goToTargetEvent.emit(int(self.currentFrame),  int(self.currentTarget), self.zoomLevelChange)
            self.zoomLevel=self.spinBox.value()
            self.targetCountLabel.setText(str(len(self.targetList)))
        else:
            self.targetCountLabel.setText('0')
            QMessageBox.warning(self, "ERROR", "No more of this species is found in the data.")
        
    def getSpeciesTargets(self):
        query=self.dataDB.dbQuery("SELECT frame_number, target_number FROM targets WHERE deployment_id='"+self.deployment+
        "'  AND species_group='"+self.fromSpeciesBox.currentText()+"' AND frame_number between "+self.startFrameEdit.text()+" AND "+self.endFrameEdit.text()+
        " ORDER BY frame_number, target_number")
        self.targetList=[]
        for frame,  target in query:
            self.targetList.append([frame, target])
        self.goToNextFish()
            
            
    def changeSpecies(self):
        if self.currentFrame and self.currentTarget:
            if self.toSpeciesBox.currentIndex()>=0:
                self.dataDB.dbExec("UPDATE targets SET species_group='"+self.toSpeciesBox.currentText()+
                    "' WHERE deployment_id='"+self.deployment+"' AND frame_number="+self.currentFrame+" AND target_number="+self.currentTarget)
                self.goToNextFish()
            else:
                QMessageBox.warning(self, "ERROR", 'Select a "Change to" species.')
    def changeAll(self):
        if self.toSpeciesBox.currentIndex()>=0 and self.fromSpeciesBox.currentIndex()>=0:
            reply=QMessageBox.warning(self, "WARNING", "Are you sure you want to change all "+self.fromSpeciesBox.currentText()+" to "+self.toSpeciesBox.currentText()+"?",  QMessageBox.Yes, QMessageBox.No)
            if reply==QMessageBox.No:
                return
            else:
                self.dataDB.dbExec("UPDATE targets SET species_group='"+self.toSpeciesBox.currentText()+
                    "' WHERE deployment_id='"+self.deployment+"' AND species_group='"+self.fromSpeciesBox.currentText()+"'")
                self.getSpeciesTargets()
        else:
            QMessageBox.warning(self, "ERROR", 'Select Speceis Options first!')
                
    def changeZoom(self):
        self.zoomLevelChange=self.spinBox.value()-self.zoomLevel
        self.goToTargetEvent.emit(int(self.currentFrame),  int(self.currentTarget), self.zoomLevelChange)
        self.zoomLevel=self.spinBox.value()

    def closeEvent(self,  event):
        event.accept()


