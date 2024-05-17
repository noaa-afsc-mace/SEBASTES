
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from dialogs.ui import  ui_AnnotatorDlg

class AnnotatorDlg(QDialog, ui_AnnotatorDlg.Ui_annotatorDlg):
    def __init__(self, parent=None):
        super(AnnotatorDlg, self).__init__(parent)
        self.setupUi(self)
        
        self.okBtn.clicked.connect(self.close)
        self.cancelBtn.clicked.connect(self.close)

    @pyqtSlot()
    def close(self):
        if self.sender()==self.okBtn:
            # check to see if somethig was entered
            self.annotator=self.annotatorEdit.text()
            if self.annotator in (None, ''):
                QMessageBox.warning(self, "ERROR", "Ya didn't give me initials!")
                return
            self.accept()
        else:
            self.reject()
