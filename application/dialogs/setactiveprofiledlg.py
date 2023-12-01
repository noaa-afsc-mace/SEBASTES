
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from dialogs.ui import  ui_SetActiveProfilesDlg
from dialogs import setactivecompdlg

class SetActiveProfilesDlg(QDialog, ui_SetActiveProfilesDlg.Ui_setActiveProfilesDlg):
    
    def __init__(self, parent=None):
        super(SetActiveProfilesDlg, self).__init__(parent)
        self.setupUi(self)
        self.db=parent.appDB.db
        self.setProjectsBtn.clicked.connect(self.callUpDlg)
        self.setProfilesBtn.clicked.connect(self.callUpDlg)
        self.setSpcCollectionsBtn.clicked.connect(self.callUpDlg)
        self.setMetaGroupsBtn.clicked.connect(self.callUpDlg)
        self.okBtn.clicked.connect(self.close)
        
        
        
    def callUpDlg(self):
        if self.sender()==self.setProjectsBtn:
            dlg=setactivecompdlg.SetActiveCompDlg('project', self)
        elif self.sender()==self.setProfilesBtn:
            dlg=setactivecompdlg.SetActiveCompDlg('profile', self)
        elif self.sender()==self.setSpcCollectionsBtn:
            dlg=setactivecompdlg.SetActiveCompDlg('species', self)
        else:
            dlg=setactivecompdlg.SetActiveCompDlg('metadata', self)
        dlg.exec_()

    def closeEvent(self,  event):
        event.accept()


