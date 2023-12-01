
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from dialogs.ui import  ui_GridSetupDlg

class GridSetupDlg(QDialog, ui_GridSetupDlg.Ui_gridSetupDlg):
    def __init__(self, parent=None):
        super(GridSetupDlg, self).__init__(parent)
        self.setupUi(self)
        self.gridSetup=parent.gridSetup
        self.okBtn.clicked.connect(self.exit)
        self.cancelBtn.clicked.connect(self.cancel)
        self.gridlineColorBtn.clicked.connect(self.getColor)
        self.cellColorBtn.clicked.connect(self.getColor)
        self.loadSettings()
        
    def loadSettings(self):
        self.gridSizeBox.addItems(['1x2','2x2' , '2x3', '3x3'])
        self.gridSizeBox.setCurrentIndex(self.gridSizeBox.findText(str(self.gridSetup['GridSize']), Qt.MatchExactly))
        self.lineThicknessBox.addItems(['1', '2', '3','4'])
        self.lineThicknessBox.setCurrentIndex(self.lineThicknessBox.findText(str(self.gridSetup['GridLineThickness']), Qt.MatchExactly))
        self.lineStyleBox.addItems(['_', '-', '.'])
        self.lineStyleBox.setCurrentIndex(self.lineStyleBox.findText(str(self.gridSetup['GridLineStyle']), Qt.MatchExactly))
        self.gLineCol=QColor(self.gridSetup['GridLineColor'][0], self.gridSetup['GridLineColor'][1], self.gridSetup['GridLineColor'][2])
        colstr=str(self.gLineCol.getRgb()[0])+","+str(self.gLineCol.getRgb()[1])+","+str(self.gLineCol.getRgb()[2])
        self.gridlineColorLabel.setStyleSheet("QLabel { background-color : rgb("+colstr+");}")
        if self.gridSetup['RandomizeCell']==True:
            self.randomCheck.setChecked(True)
        else:
            self.randomCheck.setChecked(False)
        if self.gridSetup['PersistentGrid']==True:
            self.persistentGridBox.setChecked(True)
        else:
            self.persistentGridBox.setChecked(False)
        if self.gridSetup['CellBoundary']==True:
            self.cellBoundaryBox.setChecked(True)
        else:
            self.cellBoundaryBox.setChecked(False)
        self.cLineCol=QColor(self.gridSetup['CellLineColor'][0], self.gridSetup['CellLineColor'][1], self.gridSetup['CellLineColor'][2])
        colstr=str(self.cLineCol.getRgb()[0])+","+str(self.cLineCol.getRgb()[1])+","+str(self.cLineCol.getRgb()[2])
        self.cellColorLabel.setStyleSheet("QLabel { background-color : rgb("+colstr+");}")

    def getColor(self):
        if self.sender()==self.gridlineColorBtn:
            self.gLineCol=QColorDialog().getColor(self.gLineCol,  self)
            colstr=str(self.gLineCol.getRgb()[0])+","+str(self.gLineCol.getRgb()[1])+","+str(self.gLineCol.getRgb()[2])
            self.gridlineColorLabel.setStyleSheet("QLabel { background-color : rgb("+colstr+");}")
        else:
            self.cLineCol=QColorDialog().getColor(self.cLineCol,  self)
            colstr=str(self.cLineCol.getRgb()[0])+","+str(self.cLineCol.getRgb()[1])+","+str(self.cLineCol.getRgb()[2])
            self.cellColorLabel.setStyleSheet("QLabel { background-color : rgb("+colstr+");}")
            
    def readSettings(self):
        self.gridSetup['GridSize']=self.gridSizeBox.currentText()
        self.gridSetup['GridLineThickness']=int(self.lineThicknessBox.currentText())
        self.gridSetup['GridLineStyle']=self.lineStyleBox.currentText()
        self.gridSetup['GridLineColor']=self.gLineCol.getRgb()[0:3]
        if self.randomCheck.isChecked():
            self.gridSetup['RandomizeCell']=True
        else:
            self.gridSetup['RandomizeCell']=False
        if self.persistentGridBox.isChecked():
            self.gridSetup['PersistentGrid']=True
        else:
            self.gridSetup['PersistentGrid']=False
        if self.cellBoundaryBox.isChecked():
            self.gridSetup['CellBoundary']=True
        else:
            self.gridSetup['CellBoundary']=False
        self.gridSetup['CellLineColor']=self.cLineCol.getRgb()[0:3]
                
    @pyqtSlot()
    def cancel(self):
        self.reject()
        
    @pyqtSlot()
    def exit(self):
        self.readSettings()
        self.accept()
