
from PySide6.QtCore  import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from dialogs.ui import  ui_SubsampleMaskHelpDlg

class SubsampleMaskHelpDlg(QDialog, ui_SubsampleMaskHelpDlg.Ui_subsampleMaskHelpDlg):
    def __init__(self, parent=None):
        super(SubsampleMaskHelpDlg, self).__init__(parent)
        self.setupUi(self)
        self.okBtn.clicked.connect(self.exit)

    @Slot()
    def exit(self):
        self.accept()
