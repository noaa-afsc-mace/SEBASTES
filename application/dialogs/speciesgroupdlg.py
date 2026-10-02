
from PySide6.QtCore  import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
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

    @Slot()
    def cancel(self):
        self.reject()
        
    @Slot()
    def exit(self):
        self.accept()
