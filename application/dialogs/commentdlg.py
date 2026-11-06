
from PySide6.QtCore  import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from dialogs.ui import ui_commentDlg

class CommentDlg(QDialog, ui_commentDlg.Ui_commentDlg):
    def __init__(self, comment, targetClass,  targetNumber,   parent=None):
        super(CommentDlg, self).__init__(parent)
        self.setupUi(self)
        self.comment=None
        self.saveAndExitBtn.clicked.connect(self.saveandexit)
        self.tClassLabel.setText(targetClass)
        self.tNumLabel.setText(str(targetNumber))
        self.commentBox.setPlainText(comment)
            
    @Slot()
    def saveandexit(self):
        self.comment=self.commentBox.toPlainText()
        self.comment=self.comment.replace("'", "")
        self.close()
        
    def closeEvent(self, event):
        self.accept()

