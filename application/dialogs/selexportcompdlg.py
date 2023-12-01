

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from dialogs.ui import  ui_ExportProfileDlg
from dialogs import makeseldlg
from datetime import datetime
import csv,  os,  traceback, sys

class SelExportCompDlg(QDialog, ui_ExportProfileDlg.Ui_exportProfileDlg):
    
    def __init__(self, parent=None):
        super(SelExportCompDlg, self).__init__(parent)
        self.setupUi(self)
        self.appDB=parent.appDB
        self.selProfilesBtn.clicked.connect(self.callUpDlg)
        self.selSpcCollectionsBtn.clicked.connect(self.callUpDlg)
        self.selMetaGroupsBtn.clicked.connect(self.callUpDlg)
        self.okBtn.clicked.connect(self.close)
        self.importRadio.clicked.connect(self.importStuff)
        self.exportRadio.clicked.connect(self.enableButtons)
        
        self.selProfilesBtn.setEnabled(False)
        self.selSpcCollectionsBtn.setEnabled(False)
        self.selMetaGroupsBtn.setEnabled(False)
        
        self.selMetaGroupsBtn.clicked.connect(self.callUpDlg)
        self.appSettings = QSettings('afsc.noaa.gov', 'selexportcomdlg')
        self.__exportDir = self.appSettings.value('exportdir', QDir.home().path())
   
   
    def enableButtons(self):
        self.selProfilesBtn.setEnabled(True)
        self.selSpcCollectionsBtn.setEnabled(True)
        self.selMetaGroupsBtn.setEnabled(True)
        
    def callUpDlg(self):
        
        if self.sender()==self.selProfilesBtn:
            dlg=makeseldlg.MakeSelDlg(self,'profile', 'imp_exp')
            if dlg.exec_():
                self.readWriteAction('profile', dlg.value)
        elif self.sender()==self.selSpcCollectionsBtn:
            dlg=makeseldlg.MakeSelDlg(self,'species','imp_exp')
            if dlg.exec_():
                self.readWriteAction('species', dlg.value)
        else:
            dlg=makeseldlg.MakeSelDlg(self,'metadata','imp_exp')
            if dlg.exec_():
                self.readWriteAction('metadata', dlg.value)
                
    def readWriteAction(self, mode, name):

        start_time_string = datetime.now().strftime("D%Y%m%d-T%H%M%S")
        #choose directory for file
        dir_path=QFileDialog.getExistingDirectory(self,"Choose Directory",self.__exportDir)
        if dir_path !='':
            self.__exportDir=dir_path
        filename=mode+"_"+name+"_"+start_time_string+".csv"
        File=open(dir_path+os.sep+filename, mode='w')
        stream = csv.writer(File, dialect='excel',delimiter=',',lineterminator='\n')
        if mode=='profile':
            stream.writerow(['PROFILE', 'ACTIVE', 'DESCRIPTION'])
            query=self.appDB.dbQuery("SELECT description FROM PROFILES WHERE PROFILE='"+name+"'")
            desc, =query.first()
            stream.writerow([name, 'Yes', desc])
            stream.writerow([''])
            stream.writerow(['PROFILE', 'SETTING', 'VALUE'])
            query=self.appDB.dbQuery("SELECT setting, value FROM PROFILE_SETTINGS WHERE PROFILE='"+name+"'")
            for setting, value in query:
                stream.writerow([name,  setting,  value])
        elif mode=='species':
            stream.writerow(['SPECIES_COLLECTION', 'ACTIVE', 'DESCRIPTION'])
            query=self.appDB.dbQuery("SELECT description FROM SPECIES_COLLECTIONS WHERE SPECIES_COLLECTION='"+name+"'")
            desc, =query.first()
            stream.writerow([name, 'Yes', desc])
            stream.writerow([''])
            stream.writerow(['SPECIES_COLLECTION', 'SPECIES_GROUP', 'DESCRIPTION', 'BUTTON_COLOR', 'SORT_ORDER'])
            query=self.appDB.dbQuery("SELECT species_group,description,button_color,sort_order FROM SPECIES_SETUP WHERE SPECIES_COLLECTION='"+name+"'")
            for species_group,description,button_color,sort_order in query:
                stream.writerow([name, species_group,description,button_color,sort_order])
        elif mode=='metadata':
            stream.writerow(['METADATA_GROUP', 'ACTIVE', 'DESCRIPTION'])
            query=self.appDB.dbQuery("SELECT description FROM METADATA_GROUPS WHERE METADATA_GROUP='"+name+"'")
            desc, =query.first()
            stream.writerow([name, 'Yes', desc])
            stream.writerow([''])
            stream.writerow(['METADATA_GROUP', 'METADATA_TAG', 'METADATA_TYPE', 'DESCRIPTION', 'METADATA_GUI_ELEMENT','SORT_ORDER'])
            query=self.appDB.dbQuery("SELECT metadata_tag,metadata_type,description,metadata_gui_element,sort_order FROM FRAME_METADATA_SETUP WHERE METADATA_GROUP='"+name+"'")
            for metadata_tag,metadata_type,description,metadata_gui_element,sort_order in query:
                stream.writerow([name, metadata_tag,metadata_type,description,metadata_gui_element,sort_order])
        else:
            print('bbbbad mode')
        File.close()
        QMessageBox.information(self, 'INFO',  mode+" export was successful!" )
            
    def importStuff(self):
        #choose file
        file_path=QFileDialog.getOpenFileName(self,"Choose file",self.__exportDir, "CSV files (*.csv)")
        File=open(file_path[0], mode='r')
        self.__exportDir=os.path.dirname(File.name)
        # figure out what it is
        parts=file_path[0].split('/')
        parts2=parts[-1:][0].split('_')
        mode=parts2[0]
        
        try:
            reader = csv.reader(File)
            if mode=='profile':
                for row in reader:
                    if reader.line_num==2:
                        # check to see if this is already in
                        query=self.appDB.dbQuery("SELECT description FROM PROFILES WHERE PROFILE='"+row[0]+"'")
                        desc, =query.first()
                        if desc!=None:
                            reply=QMessageBox.warning(self, "WARNING", "This profile already exists, Do you want to overwrite it?",  QMessageBox.Yes, QMessageBox.No)
                            if reply==QMessageBox.No:
                                return
                            # we are replaing profile
                            # delete
                            query=self.appDB.dbQuery("DELETE FROM PROFILE_SETTINGS WHERE PROFILE='"+row[0]+"'")
                            query=self.appDB.dbQuery("DELETE FROM PROFILES WHERE PROFILE='"+row[0]+"'")
                        # now insert
                        query=self.appDB.dbQuery("INSERT INTO PROFILES (PROFILE, ACTIVE, DESCRIPTION) VALUES('"+row[0]+"','"+row[1]+"','"+row[2]+"')")
                    if reader.line_num>4:
                        query=self.appDB.dbQuery("INSERT INTO PROFILE_SETTINGS (PROFILE,SETTING,VALUE) VALUES('"+row[0]+"','"+row[1]+"','"+row[2]+"')")
            elif mode=='species':
                for row in reader:
                    if reader.line_num==2:
                        # check to see if this is already in
                        query=self.appDB.dbQuery("SELECT description FROM SPECIES_COLLECTIONS WHERE SPECIES_COLLECTION='"+row[0]+"'")
                        desc, =query.first()
                        if desc!=None:
                            reply=QMessageBox.warning(self, "WARNING", "This species composition already exists, Do you want to overwrite it?",  QMessageBox.Yes, QMessageBox.No)
                            if reply==QMessageBox.No:
                                return
                            # we are replaing profile
                            # delete
                            query=self.appDB.dbQuery("DELETE FROM SPECIES_SETUP WHERE SPECIES_COLLECTION='"+row[0]+"'")
                            query=self.appDB.dbQuery("DELETE FROM SPECIES_COLLECTIONS WHERE SPECIES_COLLECTION='"+row[0]+"'")
                        # now insert
                        query=self.appDB.dbQuery("INSERT INTO SPECIES_COLLECTIONS (SPECIES_COLLECTION, ACTIVE, DESCRIPTION) VALUES('"+row[0]+"','"+row[1]+"','"+row[2]+"')")
                    if reader.line_num>4:
                        if row[4] in (None, ''):
                            row[4]='NULL'
                        if len(row)<5:
                            row.append('NULL')
                        
                                

                        query=self.appDB.dbQuery("INSERT INTO SPECIES_SETUP (SPECIES_COLLECTION,SPECIES_GROUP,DESCRIPTION,BUTTON_COLOR,SORT_ORDER) VALUES('"+\
                            row[0]+"','"+row[1]+"','"+row[2]+"','"+row[3]+"',"+row[4]+")")

            elif mode=='metadata':
                for row in reader:
                    if reader.line_num==2:
                        # check to see if this is already in
                        query=self.appDB.dbQuery("SELECT description FROM METADATA_GROUPS WHERE METADATA_GROUP='"+row[0]+"'")
                        desc, =query.first()
                        if desc!=None:
                            reply=QMessageBox.warning(self, "WARNING", "This metadata group already exists, Do you want to overwrite it?",  QMessageBox.Yes, QMessageBox.No)
                            if reply==QMessageBox.No:
                                return
                            # we are replaing profile
                            # delete
                            query=self.appDB.dbQuery("DELETE FROM FRAME_METADATA_SETUP WHERE METADATA_GROUP='"+row[0]+"'")
                            query=self.appDB.dbQuery("DELETE FROM METADATA_GROUPS WHERE METADATA_GROUP='"+row[0]+"'")
                        # now insert
                        query=self.appDB.dbQuery("INSERT INTO METADATA_GROUPS (METADATA_GROUP, ACTIVE, DESCRIPTION) VALUES('"+row[0]+"','"+row[1]+"','"+row[2]+"')")
                    if reader.line_num>4:
                        query=self.appDB.dbQuery("INSERT INTO FRAME_METADATA_SETUP (METADATA_GROUP,METADATA_TAG,METADATA_TYPE,DESCRIPTION,METADATA_GUI_ELEMENT,SORT_ORDER) VALUES('"+\
                        row[0]+"','"+row[1]+"','"+row[2]+"','"+row[3]+"','"+row[4]+"',"+row[5]+")")
            File.close()
            QMessageBox.information(self, 'INFO',  "Successfully imported "+mode+" "+row[0]+"!" )
        except:
            t=traceback.format_exception(*sys.exc_info())
            txt=''
            for line in t:
                txt=txt+line+'\n'

            QMessageBox.warning(self,"ERROR","Couldn't insert "+mode+" because"+txt)
            

    def closeEvent(self,  event):
        self.appSettings.setValue('exportdir', self.__exportDir)
        event.accept()


