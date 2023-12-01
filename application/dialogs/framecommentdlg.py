
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from dialogs.ui import ui_commentDlg

class CommentDlg(QDialog, ui_commentDlg.Ui_commentDlg):
    def __init__(self,  parent=None):
        super(CommentDlg, self).__init__(parent)
        self.setupUi(self)
        self.parentBtnWidget=parent.frameCommentBtn
        self.deployment=parent.deployment
        self.saveAndExitBtn.hide()
        self.dataDB=parent.dataDB
        self.frame=parent.frameBox.text()
        self.classLabel.hide()
        self.targetLabel.setText('Active Frame Number')
        self.tNumLabel.setText(self.frame)
        self.showComment(self.frame)
       
    def showComment(self, frame):
        self.frame=frame
        query = self.dataDB.dbQuery("SELECT comment FROM frames WHERE frame_number = "+frame+" AND deployment_id='"+self.deployment+"' ")
        self.frameComment, =query.first()
        if self.frameComment==None:
            self.frameComment=''
        self.commentBox.setPlainText(self.frameComment)
        self.tNumLabel.setText(self.frame)
        
#    @pyqtSlot()
#    def save(self):
#        self.comment=self.commentBox.toPlainText()
#        self.comment=self.comment.replace("'", "")
#        # write to db
#        self.dataDB.dbExec("UPDATE frames SET comment = '"+self.comment+"' WHERE frame_number = "+self.frame)
        
    def closeEvent(self, event):
        self.parentBtnWidget.setChecked(False)
        event.accept()
