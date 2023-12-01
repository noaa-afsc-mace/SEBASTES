
import sys,  traceback
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from dialogs.ui import  ui_TimestampExtractHelpDlg

class TimestampExtractHelpDlg(QDialog, ui_TimestampExtractHelpDlg.Ui_timestampExtractHelpDlg):
    def __init__(self, parent=None):
        super(TimestampExtractHelpDlg, self).__init__(parent)
        self.setupUi(self)
        self.okBtn.clicked.connect(self.exit)
        self.extractBtn.clicked.connect(self.extractTimestamp)
    
    @pyqtSlot()
    def extractTimestamp(self):
        try:
            filename_string=self.filenameEdit.text()
            format=self.timestampFormat.text()
            start=int(self.timestampStartIndex.text())-1
            DateTime=QDateTime.fromString(filename_string[start:start+len(format)],format)
            backString=DateTime.toString()
            if backString!='':
                self.resultLabel.setText("SUCCESS! -"+backString)
            else:
                self.resultLabel.setText("NO GOOD - try again!")
        except:
            t=traceback.format_exception(*sys.exc_info())
            txt=''
            for line in t:
                txt=txt+line+'\n'
            print(txt)
            QMessageBox.warning(self, "ERROR", txt)
            self.resultLabel.setText("NO GOOD!")
        
    @pyqtSlot()
    def exit(self):
        self.accept()
