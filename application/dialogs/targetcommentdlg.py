
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from dialogs.ui import ui_TargetCommentDlg

class TargetCommentDlg(QDialog, ui_TargetCommentDlg.Ui_targetCommentDlg):
    def __init__(self, comment, targetClass,  targetNumber,   parent=None):
        super(TargetCommentDlg, self).__init__(parent)
        self.setupUi(self)
        
        self.saveAndExitBtn.clicked.connect(self.saveandexit)
        self.tClassLabel.setText(targetClass)
        self.tNumLabel.setText(str(targetNumber))
        self.commentBox.setPlainText(comment)
            
    @pyqtSlot()
    def saveandexit(self):
        self.comment=self.commentBox.toPlainText()
        self.comment.replace("'", "")
        self.close()
        
    def closeEvent(self, event):
        if self.sender()==self.saveAndExitBtn:
            self.accept()
        else:
            self.reject()
