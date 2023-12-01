
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from dialogs.ui import ui_CamViewSelDlg

class CamViewSelDlg(QDialog, ui_CamViewSelDlg.Ui_camViewSelDlg):
    def __init__(self,  parent=None):
        super(CamViewSelDlg, self).__init__(parent)
        self.setupUi(self)
        
        self.okBtn.clicked.connect(self.close)
        self.cancelBtn.clicked.connect(self.close)
        
    def closeEvent(self, event):
        if self.sender()==self.okBtn:
            self.accept()
        else:
            self.reject()
