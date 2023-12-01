
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from dialogs.ui import  ui_SpeciesGroupDlg

class SpeciesGroupDlg(QDialog, ui_SpeciesGroupDlg.Ui_speciesGroupDlg):
    def __init__(self, parent=None):
        super(SpeciesGroupDlg, self).__init__(parent)
        self.setupUi(self)
        self.okBtn.clicked.connect(self.exit)
        self.cancelBtn.clicked.connect(self.cancel)
        
    def setList(self, spcList):
        self.listWidget.clear()
        self.listWidget.addItems(spcList)

    @pyqtSlot()
    def cancel(self):
        self.reject()
        
    @pyqtSlot()
    def exit(self):
        self.accept()
