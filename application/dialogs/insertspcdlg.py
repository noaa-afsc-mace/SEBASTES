
from PySide6.QtCore  import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from dialogs.ui import  ui_InsertSpcDlg

class InsertSpcDlg(QDialog, ui_InsertSpcDlg.Ui_insertSpcDlg):
    def __init__(self, parent=None):
        super(InsertSpcDlg, self).__init__(parent)
        self.setupUi(self)
        self.saveBtn.clicked.connect(self.save)
        self.cancelBtn.clicked.connect(self.cancel)
        self.setColorBtn.clicked.connect(self.getColor)
        self.label_4.setToolTip('This value indicated the order in which species buttons will appear (max 30). Can be left blank.')
        self.col=QColor(255, 0, 0)
        self.btnColLabel.setStyleSheet("QLabel { background-color : rgb("+str(self.col.getRgb()[0])+","+str(self.col.getRgb()[1])+","+str(self.col.getRgb()[2])+");}")
        
    @Slot()
    def getColor(self):
        self.col=QColorDialog().getColor(self.col,  self)
        self.btnColLabel.setStyleSheet("QLabel { background-color : rgb("+str(self.col.getRgb()[0])+","+str(self.col.getRgb()[1])+","+str(self.col.getRgb()[2])+");}")
        
    @Slot()
    def cancel(self):
        self.reject()
        
    @Slot()
    def save(self):
        if self.speciesEdit.text()=='':
            QMessageBox.warning(self, "ERROR", "No species entered!")
            return
        self.accept()
