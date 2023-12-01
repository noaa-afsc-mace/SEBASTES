
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from dialogs.ui import  ui_infoDialog
import numpy as np

class InfoDlg(QDialog, ui_infoDialog.Ui_infoDialog):

    def __init__(self, parent=None):

        #  set up the UI
        super(InfoDlg, self).__init__(parent)
        self.setupUi(self)


        #  set a few porperties of the SimpleTextEdit object that we can't set in designer
        self.statusText.setMaximumBlockCount(1000)
        self.statusText.setWordWrapMode(QTextOption.NoWrap)
        self.saveBtn.clicked.connect(self.close)
        #  restore the application state
        self.__appSettings = QSettings('afsc.noaa.gov', 'InfoDlg')
        size = self.__appSettings.value('winsize', QSize(1271,647))
        self.resize(size)
#        position = self.__appSettings.value('winposition', QPoint(10,10)).toPoint()
#        self.move(position)


    def closeEvent(self, event=None):
        self.__appSettings.setValue('winposition', self.pos())
        self.__appSettings.setValue('winsize', self.size())
        self.close()

    def updateLog(self, text, color):
        if type(text)==type(np.array([])):
            for line in text:
                t=str(line)
                logText = '<text style="color:' + color +'">' + str(t[1:-1])
                self.statusText.appendHtml(logText)
        else:
            logText = '<text style="color:' + color +'">' + str(text)
            self.statusText.appendHtml(logText)

        #  ensure that the window is scrolled to see the new line(s) of text.
        self.statusText.verticalScrollBar().setValue(self.statusText.verticalScrollBar().maximum())




