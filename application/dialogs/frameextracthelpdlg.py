
import sys,  traceback
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from dialogs.ui import  ui_FrameExtractHelpDlg

class FrameExtractHelpDlg(QDialog, ui_FrameExtractHelpDlg.Ui_frameExtractHelpDlg):
    def __init__(self, parent=None):
        super(FrameExtractHelpDlg, self).__init__(parent)
        self.setupUi(self)
        self.okBtn.clicked.connect(self.exit)
        self.extractBtn.clicked.connect(self.extractFrameNum)
    
    @pyqtSlot()
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
        
    @pyqtSlot()
    def exit(self):
        self.accept()
