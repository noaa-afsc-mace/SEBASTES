
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import QtSql
from dialogs.ui import  ui_ProfileSetupDlg
from dialogs import makeseldlg, frameextracthelpdlg,  timestampextracthelpdlg, subsamplemaskhelpdlg, insertspcdlg, insertmtddlg
import sys, traceback

class ProfileSetupDlg(QDialog, ui_ProfileSetupDlg.Ui_profileSetupDlg):
    def __init__(self, parent=None):
        super(ProfileSetupDlg, self).__init__(parent)
        self.setupUi(self)
        # pass in profile database
        self.appDB=parent.appDB
        self.activeProfile=parent.activeProfile
        self.metadataGroup=parent.metadataGroup
        self.speciesCollection=parent.speciesCollection
        # defaults
        self.commited=False
        self.reloadFlag=False
        # signals
        # profile tab
        self.selectProfileBtn.clicked.connect(self.selectAction)
        self.newProfileBtn.clicked.connect(self.newProfile)
        self.frameIndHelpBtn.clicked.connect(self.frameIndexHelper)
        self.timestampFormatBtn.clicked.connect(self.timestampFormatHelper)
        self.subsampleMaskBtn.clicked.connect(self.subsampleMaskHelper)
        # species tab
        self.selectSpcCollectionBtn.clicked.connect(self.selectAction)
        self.newSpcCollectionBtn.clicked.connect(self.newSpeciesCollection)
        self.speciesInsertBtn.clicked.connect(self.viewAction)
        self.speciesEditBtn.clicked.connect(self.viewAction)
        self.speciesDeleteBtn.clicked.connect(self.viewAction)
        # metadata tab
        self.selectMetadataGroupBtn.clicked.connect(self.selectAction)
        self.newMetadataGroupBtn.clicked.connect(self.newMetadataGroup)
        self.metadataInsertBtn.clicked.connect(self.viewAction)
        self.metadataEditBtn.clicked.connect(self.viewAction)
        self.metadataDeleteBtn.clicked.connect(self.viewAction)
        
        # save or concel
        self.cancelBtn.clicked.connect(self.cancelAction)
        self.saveBtn.clicked.connect(self.saveBtnAction)
        self.reloadBtn.clicked.connect(self.reloadAction)
        # set up the views
        self.speciesModel = QtSql.QSqlQueryModel()
        self.speciesView.setModel(self.speciesModel)
        self.speciesView.show()
        self.speciesSelModel=QItemSelectionModel(self.speciesModel, self.speciesView)
        self.speciesView.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.speciesView.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.speciesView.setSelectionModel(self.speciesSelModel)
        
        self.metadataModel = QtSql.QSqlQueryModel()
        self.metadataView.setModel(self.metadataModel)
        self.metadataView.show()
        self.metadataTypesSelModel=QItemSelectionModel(self.metadataModel, self.metadataView)
        self.metadataView.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.metadataView.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.metadataView.setSelectionModel(self.metadataTypesSelModel)

        self.clearProfilePage()
        self.loadProfileComboBoxes()
        self.profileFrame.setEnabled(False)
        self.metadataFrame.setEnabled(False)
        self.speciesFrame.setEnabled(False)
        
        # set tooltips
        widgets={'LeftCameraImagePath':self.leftCamPathEdit,'RightCameraImagePath':self.rightCamPathEdit, 'CalibrationFileName': self.calFilePathEdit, \
            'FrameNumberIndices':self.stFrameIndEdit,'ImageTimestampType': self.timestampTypeBox,\
            'ImageTimestampFormat':self.timestampFormatEdit,'ImageTimestampStart':self.timestampStartEdit,'CollectMetadata':self.metadataYesBtn, \
            'RotateLeftImage': self.rotateLeftBox,'RotateRightImage':self.rotateRightBox, \
            'SubsampleMask':self.subsampleMaskEdit}
        query=self.appDB.dbQuery("SELECT setting, description FROM SETTING_DESCRIPTIONS")
        for setting, desc  in query:
            widgets[setting].setToolTip(desc)
        
        # initial action
        if self.activeProfile !=None:
            self.loadProfile()
        if self.speciesCollection !=None:
            self.loadSpecies()
        if self.metadataGroup !=None:
            self.loadMetadata()
        # start transaction so we can roll back on cancel?
        self.appDB.startTransaction()
        
           
    def selectAction(self):
        if self.sender()==self.selectProfileBtn:
            self.profileFrame.setEnabled(True)
            self.profileNameEdit.setEnabled(False)# cant change the profile name
            dlg=makeseldlg.MakeSelDlg(self,  'profile')
            dlg.newBtn.hide()
            if dlg.exec_():
                self.activeProfile=dlg.value
                self.loadProfile()
        elif self.sender()==self.selectSpcCollectionBtn:
            self.spcCollectionNameEdit.setEnabled(False)
            dlg=makeseldlg.MakeSelDlg(self,  'species')
            dlg.newBtn.hide()
            if dlg.exec_():
                self.speciesCollection=dlg.value
                self.loadSpecies()
        elif self.sender()==self.selectMetadataGroupBtn:
            self.metadataGroupEdit.setEnabled(False)
            dlg=makeseldlg.MakeSelDlg(self,  'metadata')
            dlg.newBtn.hide()
            if dlg.exec_():
                self.metadataGroup=dlg.value
                self.loadMetadata()
                
    def newProfile(self):
        self.profileFrame.setEnabled(True)
        self.selectProfileBtn.setEnabled(False)
        self.clearProfilePage()
        self.profileNameEdit.setEnabled(True)
    
    def showError(self):
        t=traceback.format_exception(*sys.exc_info())
        txt=''
        for line in t:
            txt=txt+line+'\n'
        print(txt)
        QMessageBox.warning(self, "ERROR", txt)
    
    def clearProfilePage(self):
        lineEdits=[self.leftCamPathEdit, self.rightCamPathEdit, self.calFilePathEdit, self.stFrameIndEdit,  self.endFrameIndEdit, \
        self.timestampFormatEdit, self.timestampStartEdit, self.subsampleMaskEdit]
        comboBoxes=[self.timestampTypeBox, self.rotateLeftBox, self.rotateRightBox]
        for lineEdit in lineEdits:
            lineEdit.clear()
        for box in comboBoxes:
            box.clear()
        self.loadProfileComboBoxes()
        
    def frameIndexHelper(self):
        dlg=frameextracthelpdlg.FrameExtractHelpDlg()
        dlg.exec_()
        
    def timestampFormatHelper(self):
        dlg=timestampextracthelpdlg.TimestampExtractHelpDlg()
        dlg.exec_()
        
    def subsampleMaskHelper(self):
        dlg=subsamplemaskhelpdlg.SubsampleMaskHelpDlg()
        dlg.exec_()
        
    def newSpeciesCollection(self):
        self.spcCollectionNameEdit.clear()
        self.spcCollectionNameEdit.setEnabled(True)
        self.spcCollectionDescEdit.clear()
        self.speciesCollection=None
        self.loadSpecies()

        
    def newMetadataGroup(self):
        self.metadataGroupEdit.clear()
        self.metadataGroupEdit.setEnabled(True)
        self.metadataGroupDescEdit.clear()
        self.metadataGroup=None
        self.loadMetadata()# this will clear out all the tables

        
    def viewAction(self):
        try:
            sender=self.sender()
            if sender==self.speciesDeleteBtn:
                selObj=self.speciesView.currentIndex()
                index= self.speciesModel.index(selObj.row(), 0, QModelIndex())
                species=self.speciesModel.data(index, Qt.DisplayRole)
                # give warning
                reply=QMessageBox.warning(self, "ERROR", "If you delete this species, it will not appear for this collection in the future!",  QMessageBox.Yes, QMessageBox.No)
                if reply==QMessageBox.No:
                    return
                # delete
                self.appDB.dbExec("DELETE FROM SPECIES_SETUP WHERE species_group='"+species+"' AND species_collection='"+self.speciesCollection+"'")
                self.loadSpecies()
            elif sender==self.speciesEditBtn:
                selObj=self.speciesView.currentIndex()
                index1= self.speciesModel.index(selObj.row(), 0, QModelIndex())
                index2= self.speciesModel.index(selObj.row(), 1, QModelIndex())
                index3= self.speciesModel.index(selObj.row(), 2, QModelIndex())
                index4= self.speciesModel.index(selObj.row(), 3, QModelIndex())
                species=self.speciesModel.data(index1, Qt.DisplayRole)
                dlg=insertspcdlg.InsertSpcDlg(self)
                dlg.speciesEdit.setText(self.speciesModel.data(index1, Qt.DisplayRole))
                dlg.speciesEdit.setEnabled(False)
                dlg.descEdit.setText(self.speciesModel.data(index2, Qt.DisplayRole))
                col=self.speciesModel.data(index3, Qt.DisplayRole)
                cols=col.split(",")
                dlg.col=QColor(int(cols[0]), int(cols[1]), int(cols[2]))
                dlg.btnColLabel.setStyleSheet("QLabel { background-color : rgb("+col+");}")
                dlg.sortEdit.setText(str(self.speciesModel.data(index4, Qt.DisplayRole)))
                
                if dlg.exec_():
                    desc=dlg.descEdit.toPlainText()
                    if "'" in desc:
                        desc = desc.replace("'", "''")
                    col=dlg.col
                    sortOrder=dlg.sortEdit.text()
                    if sortOrder=='':
                        sortOrder='NULL'
                    # update
                    self.appDB.dbExec("UPDATE SPECIES_SETUP set description='"+desc+"',  button_color='"+str(col.getRgb()[0])+","+
                    str(col.getRgb()[1])+","+str(col.getRgb()[2])+"', sort_order="+sortOrder+"  WHERE species_group='"+species+"' AND species_collection='"+self.speciesCollection+"'") 
                self.loadSpecies()
            elif sender==self.speciesInsertBtn:
                if self.speciesCollection==None:
                    self.speciesCollection=self.spcCollectionNameEdit.text()
                    if self.speciesCollection=='':
                        QMessageBox.warning(self, "ERROR", "Need to enter a species colection name first!")
                        self.speciesCollection=None
                        return
                    desc=self.spcCollectionDescEdit.toPlainText()
                    if "'" in desc:
                        desc = desc.replace("'", "''")
                    # put it in the db
                    self.appDB.dbExec("INSERT INTO SPECIES_COLLECTIONS (species_collection, description) VALUES ('"+
                    self.speciesCollection+"','"+desc+"')")
                dlg=insertspcdlg.InsertSpcDlg(self)
                if dlg.exec_():
                    species=dlg.speciesEdit.text()
                    desc=dlg.descEdit.toPlainText()
                    if "'" in desc:
                        desc = desc.replace("'", "''")
                    col=dlg.col
                    sortOrder=dlg.sortEdit.text()
                    if sortOrder=='':
                        sortOrder='NULL'
                    # insert
                    self.appDB.dbExec("INSERT INTO SPECIES_SETUP (species_collection, species_group, description, button_color, sort_order) VALUES ('"+
                    self.speciesCollection+"','"+species+"', '"+desc+"', '"+str(col.getRgb()[0])+","+
                    str(col.getRgb()[1])+","+str(col.getRgb()[2])+"',"+sortOrder+")")
                self.loadSpecies()
            elif sender == self.metadataInsertBtn:
                if self.metadataGroup==None:
                    self.metadataGroup=self.metadataGroupEdit.text()
                    if self.metadataGroup=='':
                        QMessageBox.warning(self, "ERROR", "Need to enter a metadata group name first!")
                        self.metadataGroup=None
                        return
                    desc=self.metadataGroupDescEdit.toPlainText()
                    if "'" in desc:
                        desc = desc.replace("'", "''")
                    # put it in the db
                    self.appDB.dbExec("INSERT INTO METADATA_GROUPS (metadata_group, description) VALUES ('"+
                    self.metadataGroup+"','"+desc+"')")
                        
                dlg=insertmtddlg.InsertMtdDlg(self)
                query=self.appDB.dbQuery("SELECT sort_order FROM FRAME_METADATA_SETUP WHERE metadata_group='"+self.metadataGroup+"'")
                out_of_sorts=[]
                for sort_val, in query:
                    out_of_sorts.append(int(sort_val))
                if len(out_of_sorts)>0:
                    val=int(max(out_of_sorts))+1
                else:
                    val=1
                dlg.orderSpinBox.setValue(val)
                dlg.out_of_sorts=out_of_sorts
                if dlg.exec_():
                    metadata_var=dlg.metadataEdit.text()
                    desc=dlg.descEdit.toPlainText()
                    mtd_type=dlg.metadataTypeEdit.text()
                    if "'" in desc:
                        desc = desc.replace("'", "''")
                    mtd_gui=dlg.categoryBox.currentText()
                    sort_order=str(dlg.orderSpinBox.value())
                    sql=("INSERT INTO FRAME_METADATA_SETUP (metadata_group, metadata_tag, metadata_type, metadata_gui_element, description, sort_order) VALUES ('"+self.metadataGroup+
                    "','"+metadata_var+"', '"+mtd_type+"','"+mtd_gui+"','"+desc+"',"+sort_order+")")
                    self.appDB.dbExec(sql)
                self.loadMetadata()
                
            elif sender == self.metadataEditBtn:
                dlg=insertmtddlg.InsertMtdDlg(self)
                selObj=self.metadataView.currentIndex()
                index1= self.metadataModel.index(selObj.row(), 0, QModelIndex())
                index2= self.metadataModel.index(selObj.row(), 1, QModelIndex())
                index3= self.metadataModel.index(selObj.row(), 2, QModelIndex())
                index4= self.metadataModel.index(selObj.row(), 3, QModelIndex())
                index5= self.metadataModel.index(selObj.row(), 4, QModelIndex())
                metadata_var=self.metadataModel.data(index1, Qt.DisplayRole)
                dlg.metadataEdit.setText(metadata_var)
                dlg.metadataTypeEdit.setText(self.metadataModel.data(index2, Qt.DisplayRole))
                dlg.categoryBox.setCurrentIndex(dlg.categoryBox.findText(self.metadataModel.data(index3, Qt.DisplayRole), Qt.MatchExactly))
                dlg.descEdit.setText(self.metadataModel.data(index4, Qt.DisplayRole))
                dlg.orderSpinBox.setValue(int(self.metadataModel.data(index5, Qt.DisplayRole)))
                dlg.metadataEdit.setEnabled(False)
                if dlg.exec_():
                    desc=dlg.descEdit.toPlainText()
                    if "'" in desc:
                        desc = desc.replace("'", "''")
                    sort_order=str(dlg.orderSpinBox.value())
                    mtd_type=dlg.metadataTypeEdit.text()
                    mtd_gui=dlg.categoryBox.currentText()
                    sql=("UPDATE FRAME_METADATA_SETUP SET description='"+desc+"', metadata_type='"+mtd_type+"', metadata_gui_element='"+mtd_gui+
                    "', sort_order="+sort_order+" WHERE metadata_group='"+self.metadataGroup+"' AND metadata_tag='"+metadata_var+"'")
                    self.appDB.dbExec(sql)
                self.loadMetadata()
            elif sender == self.metadataDeleteBtn:

                selObj=self.metadataView.currentIndex()
                index1= self.metadataModel.index(selObj.row(), 0, QModelIndex())
                metadata_var=self.metadataModel.data(index1, Qt.DisplayRole)
                sql=("DELETE FROM FRAME_METADATA_SETUP WHERE metadata_group='"+self.metadataGroup+
                    " AND metadata_tag='"+metadata_var+"'")
                # give warning
                reply=QMessageBox.warning(self, "ERROR", "If you delete this metadata record, it will not appear in sebasstes in the future!",  QMessageBox.Yes, QMessageBox.No)
                if reply==QMessageBox.No:
                    return
                # delete
                self.appDB.dbExec(sql)
                self.loadMetadata()
        except:
            self.showError()
            
    def loadProfileComboBoxes(self):
        
        self.timestampTypeBox.clear()
        self.timestampTypeBox.addItems(['in_file_name', 'EXIV', 'none'])
        self.timestampTypeBox.setCurrentIndex(-1)
        
        self.rotateLeftBox.clear()
        self.rotateLeftBox.addItems(['0', '90', '180', '270'])
        self.rotateLeftBox.setCurrentIndex(0)
        
        self.rotateRightBox.clear()
        self.rotateRightBox.addItems(['0', '90', '180', '270'])
        self.rotateRightBox.setCurrentIndex(0)
        
        
    def loadProfile(self):
        self.profileFrame.setEnabled(True)
        # put in the name and description
        self.profileNameEdit.setText(self.activeProfile)
        self.profileNameEdit.setEnabled(False)# can't change the name
        query=self.appDB.dbQuery("SELECT description FROM PROFILES WHERE profile='"+self.activeProfile+"'")
        desc, =query.first()
        self.profileDescriptionEdit.setText(desc)
        query=self.appDB.dbQuery("SELECT setting,  value FROM PROFILE_SETTINGS WHERE profile='"+self.activeProfile+"'")
        for setting, value in query:
            
            if setting=='LeftCameraImagePath':
                self.leftCamPathEdit.setText(value)
            elif setting=='RightCameraImagePath':
                self.rightCamPathEdit.setText(value)
            elif setting=='CalibrationFileName':
                self.calFilePathEdit.setText(value)
            elif setting=='FrameNumberIndices':
                values=value.split('-')
                self.stFrameIndEdit.setText(values[0])
                self.endFrameIndEdit.setText(values[1])
            elif setting=='ImageTimestampType':
                self.timestampTypeBox.setCurrentIndex(self.timestampTypeBox.findText(value,  Qt.MatchExactly))
            elif setting=='ImageTimestampFormat':
                self.timestampFormatEdit.setText(value)
            elif setting=='ImageTimestampStart':
                self.timestampStartEdit.setText(value)
            elif setting=='CollectMetadata':
                if value.lower()=='yes' or value.lower()=='true':
                    self.metadataYesBtn.setChecked(True)
                else:
                    self.metadataYesBtn.setChecked(False)
            elif setting=='RotateLeftImage':
                self.rotateLeftBox.setCurrentIndex(self.rotateLeftBox.findText(value,  Qt.MatchExactly))
            elif setting=='RotateRightImage':
                self.rotateRightBox.setCurrentIndex(self.rotateRightBox.findText(value,  Qt.MatchExactly)) 
            elif setting=='SubsampleMask':
                self.subsampleMaskEdit.setText(value)
            else:
                print((setting, value))
                QMessageBox.warning(self, "ERROR", "Unknown setting!")

    def saveProfile(self):
        new=False
        if self.activeProfile==None:# this is a new profile
            if self.profileNameEdit.text()=='':
                return
            self.activeProfile=self.profileNameEdit.text()
            desc=self.profileDescriptionEdit.text()
            if "'" in desc:
                desc = desc.replace("'", "''")
            self.appDB.dbExec("INSERT INTO PROFILES (profile, active, description)  VALUES('"+self.activeProfile+
            "','Yes','"+desc+"')")
            new=True
        query=self.appDB.dbQuery("SELECT setting FROM SETTING_DESCRIPTIONS")
        for setting,  in query:
            if setting=='LeftCameraImagePath':
                value=self.leftCamPathEdit.text()
            elif setting=='RightCameraImagePath':
                value=self.rightCamPathEdit.text()
            elif setting=='CalibrationFileName':
                value=self.calFilePathEdit.text()
            elif setting=='FrameNumberIndices':
                value=self.stFrameIndEdit.text()+"-"+self.endFrameIndEdit.text()
            elif setting=='ImageTimestampType':
                value=self.timestampTypeBox.currentText()
            elif setting=='ImageTimestampFormat':
                value=self.timestampFormatEdit.text()
            elif setting=='ImageTimestampStart':
               value= self.timestampStartEdit.text()
            elif setting=='CollectMetadata':
                if self.metadataYesBtn.isChecked():
                    value='Yes'
                else:
                   value='No'
            elif setting=='RotateLeftImage':
                 value=self.rotateLeftBox.currentText()
            elif setting=='RotateRightImage':
                 value=self.rotateRightBox.currentText()
            elif setting=='SubsampleMask':
                value=self.subsampleMaskEdit.text()
            else:
                print((setting, value))
                QMessageBox.warning(self, "ERROR", "Unknown setting!")
            
            if new:
                self.appDB.dbExec("INSERT INTO PROFILE_SETTINGS (profile, setting, value)  VALUES('"+self.activeProfile+
            "','"+setting+"','"+value+"')")
            else:
                self.appDB.dbExec("UPDATE PROFILE_SETTINGS SET value='"+value+"' WHERE setting='"+setting+"' AND profile='"+self.activeProfile+"'")
            
    def loadSpecies(self):
        self.speciesFrame.setEnabled(True)
        if self.speciesCollection==None:
            # clear the tables please and get out
            self.speciesModel.setQuery("SELECT species_group, description, button_color, sort_order FROM SPECIES_SETUP WHERE species_collection=''", self.appDB.db)
            self.speciesView.reset()
            return
        # get description will ya
        query=self.appDB.dbQuery("SELECT description FROM SPECIES_COLLECTIONS WHERE species_collection='"+self.speciesCollection+"'")
        desc, =query.first()
        self.spcCollectionNameEdit.setText(self.speciesCollection)
        self.spcCollectionNameEdit.setEnabled(False)# can't change the name
        self.spcCollectionDescEdit.setText(desc)
        self.speciesModel.setQuery("SELECT species_group, description, button_color, sort_order FROM SPECIES_SETUP WHERE species_collection='"+
        self.speciesCollection+"'", self.appDB.db)
        self.speciesView.reset()
    
    def loadMetadata(self):
        self.metadataFrame.setEnabled(True)
        if self.metadataGroup==None:
            # clear the tables please and get out
            self.metadataModel.setQuery("SELECT metadata_tag,  metadata_type, metadata_gui_element, description, sort_order FROM FRAME_METADATA_SETUP WHERE metadata_group=''", self.appDB.db)
            self.metadataView.reset()
            return
        # get description will ya
        query=self.appDB.dbQuery("SELECT description FROM METADATA_GROUPS WHERE metadata_group='"+self.metadataGroup+"'")
        desc, =query.first()
        self.metadataGroupEdit.setText(self.metadataGroup)
        self.metadataGroupEdit.setEnabled(False)# can't change the name
        self.metadataGroupDescEdit.setText(desc)
        self.metadataModel.setQuery("SELECT metadata_tag, metadata_type, metadata_gui_element,  description, sort_order FROM FRAME_METADATA_SETUP WHERE metadata_group='"+
        self.metadataGroup+"' ORDER BY sort_order", self.appDB.db)
        self.metadataView.reset()

                
    def cancelAction(self):
        self.reloadFlag=False
        self.close()
        
    def saveData(self):
        if self.speciesCollection!='':
            self.saveProfile()
        # save descriptions from species and metadata
        if self.speciesCollection!=None:
            desc=self.spcCollectionDescEdit.toPlainText()
            if "'" in desc:
                desc = desc.replace("'", "''")
            query=self.appDB.dbQuery("SELECT species_collection FROM SPECIES_COLLECTIONS")
            val, =query.first()
            if val=='':
                self.appDB.dbExec("INSERT INTO SPECIES_COLLECTIONS (species_collection, description)  VALUES('"+self.speciesCollection+"','"+desc+"')")
            else:
                self.appDB.dbExec("UPDATE SPECIES_COLLECTIONS SET description='"+desc+"' WHERE species_collection='"+self.speciesCollection+"'")
        if self.metadataGroup!=None:
            desc=self.metadataGroupDescEdit.toPlainText()
            if "'" in desc:
                desc = desc.replace("'", "''")
            query=self.appDB.dbQuery("SELECT metadata_group FROM METADATA_GROUPS")
            val, =query.first()
            if val=='':
                self.appDB.dbExec("INSERT INTO METADATA_GROUPS (metadata_group, description)  VALUES('"+self.metadataGroup+"','"+desc+"')")
            else:
                self.appDB.dbExec("UPDATE METADATA_GROUPS SET description='"+desc+"' WHERE metadata_group='"+self.metadataGroup+"'")
        self.appDB.commit()
        self.commited=True
        
    def saveBtnAction(self):
        self.saveData()
        self.reloadFlag=False
        self.close()
        
    def reloadAction(self):
        self.saveData()
        self.reloadFlag=True
        self.close()
        
    def closeEvent(self,  event):
        if not self.commited:
            self.appDB.rollback()
        event.accept()


