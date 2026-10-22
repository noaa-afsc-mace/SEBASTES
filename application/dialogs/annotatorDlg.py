
from PySide6.QtCore  import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from dialogs.ui import  ui_AnnotatorDlg

class AnnotatorDlg(QDialog, ui_AnnotatorDlg.Ui_annotatorDlg):
    def __init__(self, parent=None):
        super(AnnotatorDlg, self).__init__(parent)
        self.setupUi(self)
        self.annotator='UNID'
        self.okBtn.clicked.connect(self.getAnnotator)
        self.cancelBtn.clicked.connect(self.close)

    @Slot()
    def getAnnotator(self):
        # check to see if somethig was entered
        self.annotator=self.annotatorEdit.text()
        if self.annotator in (None, ''):
            QMessageBox.warning(self, "ERROR", "Ya didn't give me initials!")
            return
        self.close()
