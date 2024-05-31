
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from dialogs.ui import  ui_GuiSettingDlg

class GuiSettingDlg(QDialog, ui_GuiSettingDlg.Ui_guiSettingDlg):
    def __init__(self, parent=None):
        super(GuiSettingDlg, self).__init__(parent)
        self.setupUi(self)
        self.guiSettings=parent.guiSettings
        self.saveBtn.clicked.connect(self.exit)
        self.cancelBtn.clicked.connect(self.cancel)
        self.targetLineColorBtn.clicked.connect(self.getColor)
        self.sceneColorBtn.clicked.connect(self.getColor)
        self.loadSettings()
        
    def loadSettings(self):
        self.measureLineWidthBox.addItems(['1','2' , '3'])
        self.measureLineWidthBox.setCurrentIndex(self.measureLineWidthBox.findText(str(self.guiSettings['MeasureLineWidth']), Qt.MatchExactly))
        self.measureLineTailLengthBox.addItems(['20', '40', '60'])
        self.measureLineTailLengthBox.setCurrentIndex(self.measureLineTailLengthBox.findText(str(self.guiSettings['MeasureLineTailLength']), Qt.MatchExactly))
        self.tLineCol=QColor(self.guiSettings['TargetLineColor'][0], self.guiSettings['TargetLineColor'][1], self.guiSettings['TargetLineColor'][2])
        colstr=str(self.tLineCol.getRgb()[0])+","+str(self.tLineCol.getRgb()[1])+","+str(self.tLineCol.getRgb()[2])
        self.targetColorLabel.setStyleSheet("QLabel { background-color : rgb("+colstr+");}")
        self.sceneCol=QColor(self.guiSettings['SceneColor'][0], self.guiSettings['SceneColor'][1], self.guiSettings['SceneColor'][2])
        colstr=str(self.sceneCol.getRgb()[0])+","+str(self.sceneCol.getRgb()[1])+","+str(self.sceneCol.getRgb()[2])
        self.sceneColorLabel.setStyleSheet("QLabel { background-color : rgb("+colstr+");}")
        self.boxLineThicknessBox.addItems(['1','2' , '3'])
        self.boxLineThicknessBox.setCurrentIndex(self.boxLineThicknessBox.findText(str(self.guiSettings['BoxLineThickness']), Qt.MatchExactly))
        self.labelTextSizeBox.addItems(['8' , '10' , '12' , '14' , '24'])
        self.labelTextSizeBox.setCurrentIndex(self.labelTextSizeBox.findText(str(self.guiSettings['LabelTextSize']), Qt.MatchExactly))
        self.speedAdjLabel.setText(str(self.guiSettings['PlaybackSpeedAdjust']))
        spcLabelSize=int(self.guiSettings['LabelSpeciesParam'])
        if spcLabelSize==0:
            self.showSpcNameCheck.setChecked(False)
            self.spcNameLengthEdit.setText('')
        elif spcLabelSize>0 and spcLabelSize<99:
            self.showSpcNameCheck.setChecked(True)
            self.spcNameLengthEdit.setText(str(spcLabelSize))
        else:# this setting is for full name to be shown
            self.showSpcNameCheck.setChecked(True)
            self.spcNameLengthEdit.setText('')
        if self.guiSettings['DefaultMetadataSelection']=='retain':
            self.metaSelRetainRadio.setChecked(True)
        else:
            self.metaSelClearRadio.setChecked(True)
        if self.guiSettings['ShowClassOnLabel']=='true':
            self.classLabelCheckBox.setChecked(True)
        else:
            self.classLabelCheckBox.setChecked(False)
        if self.guiSettings['RetainSpeciesSelection']=='retain':
            self.spcSelRetainRadio.setChecked(True)
        else:
            self.spcSelClearRadio.setChecked(True)

    def getColor(self):
        if self.sender()==self.targetLineColorBtn:
            self.tLineCol=QColorDialog().getColor(self.tLineCol,  self)
            colstr=str(self.tLineCol.getRgb()[0])+","+str(self.tLineCol.getRgb()[1])+","+str(self.tLineCol.getRgb()[2])
            self.targetColorLabel.setStyleSheet("QLabel { background-color : rgb("+colstr+");}")
        else:
            self.sceneCol=QColorDialog().getColor(self.sceneCol,  self)
            colstr=str(self.sceneCol.getRgb()[0])+","+str(self.sceneCol.getRgb()[1])+","+str(self.sceneCol.getRgb()[2])
            self.sceneColorLabel.setStyleSheet("QLabel { background-color : rgb("+colstr+");}")
            
    def readSettings(self):
        self.guiSettings['MeasureLineWidth']=int(self.measureLineWidthBox.currentText())
        self.guiSettings['MeasureLineTailLength']=int(self.measureLineTailLengthBox.currentText())
        self.guiSettings['BoxLineThickness']=int(self.boxLineThicknessBox.currentText())
        self.guiSettings['LabelTextSize']=int(self.labelTextSizeBox.currentText())
        spcLabelSize=0
        if self.showSpcNameCheck.isChecked():
            try:
                if self.spcNameLengthEdit.text()=='':
                    spcLabelSize=99
                else:
                    spcLabelSize=int(self.spcNameLengthEdit.text())
            except:
                pass
        self.guiSettings['LabelSpeciesParam']=spcLabelSize
        self.guiSettings['SceneColor']=self.sceneCol.getRgb()[0:3]
        self.guiSettings['TargetLineColor']=self.tLineCol.getRgb()[0:3]
        if self.metaSelRetainRadio.isChecked():
            self.guiSettings['DefaultMetadataSelection']='retain'
        else:
            self.guiSettings['DefaultMetadataSelection']='clear'
        if self.spcSelRetainRadio.isChecked():
            self.guiSettings['RetainSpeciesSelection']='retain'
        else:
            self.guiSettings['RetainSpeciesSelection']='clear'
        if self.classLabelCheckBox.isChecked():
            self.guiSettings['ShowClassOnLabel']='true'
        else:
            self.guiSettings['ShowClassOnLabel']='false'
        self.guiSettings['PlaybackSpeedAdjust']=float(self.speedAdjLabel.text())
                
    @pyqtSlot()
    def cancel(self):
        self.reject()
        
    @pyqtSlot()
    def exit(self):
        self.readSettings()
        self.accept()
