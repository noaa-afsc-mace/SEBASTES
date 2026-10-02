
from PySide6.QtCore  import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from dialogs.ui import ui_CloseupDlg

class CloseupDlg(QDialog, ui_CloseupDlg.Ui_closeupDlg):
    closeWindowEvent = Signal(bool)
    def __init__(self, parent=None):
        super(CloseupDlg, self).__init__(parent)
        self.setupUi(self)

        
    def closeEvent(self,  event):
        self.closeWindowEvent.emit(True)
        event.accept()
