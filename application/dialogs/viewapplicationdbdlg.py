
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import QtSql
from dialogs.ui import ui_ViewApplicationDBDlg

class ViewApplicationDBDlg(QDialog, ui_ViewApplicationDBDlg.Ui_viewApplicationDB):
#    selectionEvent = pyqtSignal(int, int)
#    keyPress = pyqtSignal(object, object)
    
    def __init__(self, parent=None):
        super(ViewApplicationDBDlg, self).__init__(parent)
        self.setupUi(self)
        self.db=parent.appDB.db
        
        self.tables=['projects','profiles' , 'profile_settings', 'metadata_groups', 'frame_metadata_setup', 'species_collections', 'species_setup']
        self.views=[self.projectsView,self.profilesView, self.profileSettingsView, self.metadataGroupsView,self.frameMetadataSetupView, self.speciesCollectionsView, self.speciesSetupView]
        self.models=[]
        for i, table in  enumerate(self.tables):
            model=QtSql.QSqlQueryModel()
            model.setQuery("SELECT * FROM '"+table+"'", self.db)
            self.views[i].setModel(model)
            self.views[i].show()
            self.views[i].resizeColumnsToContents()
            

        
    def closeEvent(self,  event):
        event.accept()


