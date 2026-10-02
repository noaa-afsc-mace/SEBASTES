
from PySide6.QtCore  import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from dialogs.ui import  ui_InsertMtdDlg

class InsertMtdDlg(QDialog, ui_InsertMtdDlg.Ui_insertMtdDlg):
    def __init__(self, parent=None):
        super(InsertMtdDlg, self).__init__(parent)
        self.setupUi(self)
        self.saveBtn.clicked.connect(self.save)
        self.cancelBtn.clicked.connect(self.cancel)
        self.out_of_sorts=[]
        self.categoryBox.addItems(['ExclusiveRadioBox1', 'ExclusiveRadioBox2', 'LineEdit', 'CheckBox'])
        
    @Slot()
    def cancel(self):
        self.reject()
        
    @Slot()
    def save(self):
        if self.metadataEdit.text()=='':
            QMessageBox.warning(self, "ERROR", "No species entered!")
            return
        if self.orderSpinBox.value() in self.out_of_sorts:
            QMessageBox.warning(self, "ERROR", "This sort value is already in the system! Pick a different (higher) value.")
            return
        self.accept()
