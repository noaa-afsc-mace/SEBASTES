
import sys,  traceback
from PySide6.QtCore  import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from dialogs.ui import  ui_FrameExtractHelpDlg

class FrameExtractHelpDlg(QDialog, ui_FrameExtractHelpDlg.Ui_frameExtractHelpDlg):
    def __init__(self, parent=None):
        super(FrameExtractHelpDlg, self).__init__(parent)
        self.setupUi(self)
        self.okBtn.clicked.connect(self.exit)
        self.extractBtn.clicked.connect(self.extractFrameNum)
    
    @Slot()
    def extractFrameNum(self):
        try:
            filename_string=self.filenameEdit.text()
            start=int(self.startInd.text())-1
            end=int(self.endInd.text())
            framenum=filename_string[start:end]
            self.resultLabel.setText(str(int(framenum)))
        except:
            t=traceback.format_exception(*sys.exc_info())
            txt=''
            for line in t:
                txt=txt+line+'\n'
            print(txt)
            QMessageBox.warning(self, "ERROR", txt)
        
    @Slot()
    def exit(self):
        self.accept()
