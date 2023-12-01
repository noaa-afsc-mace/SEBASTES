
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from dialogs.ui import  ui_SubsampleMaskHelpDlg

class SubsampleMaskHelpDlg(QDialog, ui_SubsampleMaskHelpDlg.Ui_subsampleMaskHelpDlg):
    def __init__(self, parent=None):
        super(SubsampleMaskHelpDlg, self).__init__(parent)
        self.setupUi(self)
        self.okBtn.clicked.connect(self.exit)

    @pyqtSlot()
    def exit(self):
        self.accept()
