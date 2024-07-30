
 #!/usr/bin/env python

import sys
import os
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from ui import ui_SEBASTES_dockable
import pyStereoComp, dbConnection
import numpy as ny
from math import *
import traceback
import glob
import re
import random
import distutils.util
from datetime import datetime,  timezone
from dialogs import speciesgroupdlg, closeupdlg, dataviewdlg, commentdlg, editspeciesdlg, framecommentdlg,  makeseldlg,  profilesetupdlg,  guisettingdlg,  selectprojectdlg, annotatorDlg, viewapplicationdbdlg,  directeditDBdlg
from exif import Image

class SEBASTES(QMainWindow, ui_SEBASTES_dockable.Ui_SEBASTES):

    def __init__(self, parent=None):
        super(SEBASTES, self).__init__(parent)
        self.setupUi(self)

        self.__leftDirScanned = False
        self.__rightDirScanned = False
        self.__leftDateTime = None
        self.__rightDateTime = None
        self.noLoad=True
        self.matchMode=False
        self.pairPoints=[]
        self.linkData=[]
        self.garbage=[]
        self.datadlg = None
        self.activeProfile = None
        self.speciesCollection = None
        self.metadataGroup = None
        self.frameComment=''
        self.frameCommentDlg=None
        self.defaultMonoCamera=None
        self.activeGV='Both'
        self.defaultMetadataGroup='CamTrawl_metadata'
        self.randomCellBounds=None
        self.annotator=None
        self.timestamp_format='%Y-%m-%d %H:%M:%S'

#        self.keystrokeMap={}

        self.key=None
        self.dataDB=None
        self.appDB=None
        self.deployment=None
        self.pairedTarget=False
        self.Habitat1=None
        self.Habitat2=None
        self.selColor=[0, 255, 0]
        self.selThickness=4
        self.textOffset = QPointF(-4,-4)
        
        #  color palettes
        self.red=QPalette()
        self.red.setColor(QPalette.ButtonText,QColor(255, 0, 0))
        self.black=QPalette()
        self.black.setColor(QPalette.ButtonText,QColor(0, 0, 0))
        self.green=QPalette()
        self.green.setColor(QPalette.ButtonText,QColor(77,223,77))

        # dont mess with this code
        self.spcButtons=[self.btn1, self.btn2, self.btn3, self.btn4, self.btn5, self.btn6, self.btn7, self.btn8, self.btn9, self.btn10,
            self.btn11, self.btn12, self.btn13, self.btn14, self.btn15, self.btn16, self.btn17, self.btn18, self.btn19, self.btn20, 
            self.btn21, self.btn22, self.btn23, self.btn24, self.btn25, self.btn26, self.btn27, self.btn28, self.btn29, self.btn30]
        self.optionsBoxes=[self.labelCheck, self.showDataCheck, self.closeupCheck]
        self.metadataLineEdits=[self.lineEdit1_1, self.lineEdit1_2, self.lineEdit1_3, self.lineEdit1_4, self.lineEdit1_5]
        self.metadataLineEditLabels=[self.label1_1, self.label1_2, self.label1_3, self.label1_4, self.label1_5]
        self.metadataCheckBoxes=[self.checkBox1_1, self.checkBox1_2, self.checkBox1_3, self.checkBox1_4, self.checkBox1_5]
        self.radioBtnTags1=[self.radioButton1_1, self.radioButton1_2, self.radioButton1_3, self.radioButton1_4, self.radioButton1_5, self.radioButton1_6,
                           self.radioButton1_7, self.radioButton1_8, self.radioButton1_9, self.radioButton1_10]
        self.radioBtnTags2=[self.radioButton2_1, self.radioButton2_2, self.radioButton2_3, self.radioButton2_4, self.radioButton2_5, self.radioButton2_6,
                           self.radioButton2_7, self.radioButton2_8, self.radioButton2_9, self.radioButton2_10]
        self.radioBtnTags3=[self.radioButton3_1, self.radioButton3_2]
        self.metadataStickyBox.setEnabled(False)
        self.metadataTypesDict={}
        self.recordEnableWidgets=[self.recomputeBtn,self.trainBtn,self.measureBtn, self.measureScBtn, self.rangeBtn,self.linkBtn , self.targetCommentBtn, self.frameCommentBtn, 
                            self.computeMatchBox, self.matchThresholdEdit, self.stereoOnlyCheckBox, self.showDataCheck, self.editSpeciesBtn, self.gridCheck,  self.clearGridBtn,  self.delLinkBtn, self.lastFrameBtn]
        self.bboxEnableWidgets=[self.recomputeBtn,self.measureBtn, self.measureScBtn, self.rangeBtn,self.linkBtn, 
                            self.computeMatchBox, self.matchThresholdEdit, self.stereoOnlyCheckBox, self.showDataCheck]

        self.playBtn.setEnabled(False)
        #  set the base directory path - this is the full path to this application
        import functools
        self.baseDir = functools.reduce(lambda l,r: l + os.path.sep + r,
                              os.path.dirname(os.path.realpath(__file__)).split(os.path.sep))
        try:
            self.setWindowIcon(QIcon(self.baseDir + '/'  + 'resources' + '/' + 'rockfish.png'))
        except:
            pass

        self.gotData = False
        self.first=True
        self.__selectedItems=[]
        self.targetComment=''

        self.rubberBanding = False
        self.pointMarks = {}
        self.lineMarks = {}
        self.boxMarks = {}
        self.makeBoxes = False
        self.activeMark = {self.gvLeft:None, self.gvRight:None}
        self.activeLine = {self.gvLeft:None, self.gvRight:None}
        self.gridLines = {self.gvLeft:[], self.gvRight:[]}
        self.randomCellLines = {self.gvLeft:[], self.gvRight:[]}
        self.speciesInGrid=set()
        self.gridCount=0
        self.flip= {self.gvLeft:False, self.gvRight:False}
        self.rubberBanding = False
        self.mousebits=[None, None, None]
        self.lastItem=[]
        self.matchThresholdEdit.setText('20')
        self.frameBox.returnPressed.connect(self.getFrame)
        self.stereoOnlyCheckBox.setChecked(False)
        self.bkpDep=None
        self.bkpDepPath=None
        self.camtrawlMetadataFlag=False
        
        
        cnt=0
        for btn in self.spcButtons:
            btn.setCheckable(True)
            btn.setAutoExclusive(False)
            btn.pressed.connect(self.btnPress)
            btn.released.connect(self.btnRelease)
            cnt+=1
        self.pressTime=QTime()
        self.pressTime.start()
        
        self.recomputeBtn.clicked.connect(self.recompute3D)
        self.recordBtn.clicked.connect(self.toggleRecord)
#        self.rangeBtn.clicked.connect(self.toggleRange)
        self.measureBtn.clicked.connect(self.toggleMeasure)
        self.trainBtn.clicked.connect(self.toggleTraining)
        self.copyBtn.clicked.connect(self.copyImg)
        self.playBtn.clicked.connect(self.play)
        self.linkBtn.clicked.connect(self.toggleLink)
        self.delLinkBtn.clicked.connect(self.deleteLink)
        self.targetCommentBtn.clicked.connect(self.getTargetComment)
        self.frameCommentBtn.clicked.connect(self.getFrameComment)
        self.clearGridBtn.clicked.connect(self.clearGridData)
        self.editSpeciesBtn.clicked.connect(self.editSpecies)
        self.lastFrameBtn.clicked.connect(self.goToLastFrame)
        
        # docking widgets
        self.metadataDockWidget.setFeatures(QDockWidget.DockWidgetFloatable | QDockWidget.DockWidgetMovable)
        self.metadataDockWidget.hide()
        self.speciesDockWidget.setFeatures(QDockWidget.DockWidgetFloatable | QDockWidget.DockWidgetMovable)
        self.speciesDockWidget.hide()
        self.toolsDockWidget.setFeatures(QDockWidget.DockWidgetFloatable | QDockWidget.DockWidgetMovable)

        for box in self.optionsBoxes:
            box.stateChanged.connect(self.checkBoxAction)

        # camera view radio button
        self.stereoRadio.setChecked(True)# default state - remeber?
        self.monoRadio.clicked.connect(self.cameraViewAction)
        self.stereoRadio.clicked.connect(self.cameraViewAction)
        
        # grid cehckbox
        self.gridCheck.stateChanged.connect(self.gridBoxAction)
        
        #  connect the GUI signals and slots
        self.actionExit.triggered.connect(self.close)
        self.actionLoad.triggered.connect(self.loadDeployment)
        self.actionProfiles.triggered.connect(self.setupProfiles)
        self.actionGUI_settings.triggered.connect(self.getGuiSettings)
        self.actionGrid_setup.triggered.connect(self.getGridSetup)
        self.actionSet_Active_Profiles.triggered.connect(self.setActiveProfiles)
        self.actionImport_Export_Profiles.triggered.connect(self.importExportProfiles)
        self.actionCreate_New_Project.triggered.connect(self.createNewProject)
        self.actionviewApplicationDB.triggered.connect(self.viewApplicationDB)
        self.actionedit_DB_tables.triggered.connect(self.directEditDBTables)
        self.playSpeedSlider.valueChanged.connect(self.speedSet)
        self.imageSlider.valueChanged.connect( self.__changeImage)
        

        self.adjLeftBtn.clicked.connect(self.showAdjustmentsDialog)
        self.adjRightBtn.clicked.connect(self.showAdjustmentsDialog)

        for obj in [self.gvLeft, self.gvRight]:
            #signals
            obj.mousePress.connect(self.imageClick)
            obj.mouseRelease.connect(self.imageUnClick)
            obj.mouseWheel.connect(self.myWheelEvent)
            obj.mouseMove.connect(self.mouseInWidget)
            obj.keyPress.connect(self.__keyPressEvent)
            obj.keyRelease.connect(self.__keyReleaseEvent)
            # settings
            obj.setSelectionRadius(8)
            obj.autoWheelZoom=False
            obj.doSelections=False
            obj.selectAddKey=None
            #obj.panKey = None
            obj.rubberBandKey=None
            obj.image.keepEnhanced=True
            
        #  determine the current screen size
        screenObj = QGuiApplication.primaryScreen();
        screenGeometery = screenObj.geometry()
        #  restore the application state
        self.appSettings = QSettings('afsc.noaa.gov', 'Sebastes')
        position = self.appSettings.value('winposition', QPoint(10,10))
        size = self.appSettings.value('winsize', QSize(940,646))

        #  check if our last window size is too big for our current screen
        if (size.width() > screenGeometery.width()):
            size.setWidth(screenGeometery.width() - 50)
        if (size.height() > screenGeometery.height()):
            size.setHeight(screenGeometery.height() - 50)

        #  now check if our last position is at least on our current desktop
        #  if it is off the screen we just throw it up at 0
        if (position.x() > size.width() - 50):
            position.setX(0)
        if (position.y() > size.height() - 50):
            position.setY(0)

        #  now move and resize the window
        self.move(position)
        self.resize(size)

        self.__dataDir = self.appSettings.value('self.dataPath', QDir.home().path())
        self.__copyImageDir = self.appSettings.value('copyimagedir', QDir.home().path())
        try:
            sample_rate=int(self.appSettings.value('samplerate', 10))
            sample_rate=str(sample_rate)
        except:
            sample_rate='1'
        self.sampleRateEdit.setText(sample_rate)
        self.closeupWinSize= int(self.appSettings.value('closeupwinsize', '50'))
        # other gui settings
        self.guiSettings={}
        self.guiSettings.update({'MeasureLineWidth':int(self.appSettings.value('MeasureLineWidth', 1))})
        self.guiSettings.update({'MeasureLineTailLength':int(self.appSettings.value('MeasureLineTailLength', 40))})
        self.guiSettings.update({'TargetLineColor':self.rgbStr2Lists(self.appSettings.value('TargetLineColor', '255,255,0'))})
        self.guiSettings.update({'SceneColor':self.rgbStr2Lists(self.appSettings.value('SceneColor', '255,0,0'))})
        self.guiSettings.update({'BoxLineThickness':int(self.appSettings.value('BoxLineThickness', 1))})
        self.guiSettings.update({'LabelTextSize':int(self.appSettings.value('LabelTextSize', 12))})
        self.guiSettings.update({'LabelSpeciesParam':int(self.appSettings.value('LabelSpeciesParam', 0))})
        self.guiSettings.update({'ShowClassOnLabel':self.appSettings.value('ShowClassOnLabel', 'false')})
        self.guiSettings.update({'DefaultMetadataSelection':self.appSettings.value('DefaultMetadataSelection','clear')})
        self.guiSettings.update({'RetainSpeciesSelection':self.appSettings.value('RetainSpeciesSelection','clear')})
        self.guiSettings.update({'PlaybackSpeedAdjust':self.appSettings.value('PlaybackSpeedAdjust',1.)})
        self.gridSetup={}
        self.gridSetup.update({'GridLineThickness':int(self.appSettings.value('GridLineThickness', 1))})
        self.gridSetup.update({'MeasureLineTailLength':int(self.appSettings.value('MeasureLineTailLength', 40))})
        self.gridSetup.update({'GridLineColor':self.rgbStr2Lists(self.appSettings.value('GridLineColor', '255,255,0'))})
        self.gridSetup.update({'CellLineColor':self.rgbStr2Lists(self.appSettings.value('CellLineColor', '255,0,0'))})
        self.gridSetup.update({'RandomizeCell':bool(distutils.util.strtobool(self.appSettings.value('RandomizeCell', 'True')))})
        self.gridSetup.update({'PersistentGrid':bool(distutils.util.strtobool(self.appSettings.value('PersistentGrid', 'False')))})
        self.gridSetup.update({'CellBoundary':bool(distutils.util.strtobool(self.appSettings.value('CellBoundary', 'False')))})
        self.gridSetup.update({'GridSize':self.appSettings.value('GridSize', '2x2')})
        self.gridSetup.update({'GridLineStyle':self.appSettings.value('GridLineStyle','_')})
        
        #reoccuring dialogs
        
        self.stereoComp=pyStereoComp.pyStereoComp()
        self.closeup=closeupdlg.CloseupDlg()
        self.closeup.setWindowFlags(Qt.WindowStaysOnTopHint)
        self.closeup.closeWindowEvent.connect(self.uncheckCloseupWindowBox)
        position = self.appSettings.value('zoomwinposition', QPoint(10,10))
        self.spcSelDlg=speciesgroupdlg.SpeciesGroupDlg(self)
        

       #self.closeup.move(position)

        # open and load up prfile db
        if not QFile('../db/Application.db').exists():
            QMessageBox.warning(self, "ERROR", 'The "Application.db" file is not in its expected location (SEBASTES/db folder).  Something is not right with the file setup.')
        else:
            self.appDB = dbConnection.dbConnection('../db/Application.db', '', '', label='appDB', driver="QSQLITE")
            try:
                self.appDB.dbOpen()
            except:
                self.showError()
        # do some stuff to gv viewer
        self.gvLeft.disableContextMenu()
        self.gvRight.disableContextMenu()
        # disable buttons at start
        for widget in self.recordEnableWidgets:
            widget.setEnabled(False)
            self.recordBtn.setEnabled(False)
        
        #  start a timer event to load the help image
        self.__helpTimer = QTimer(self)
        self.__helpTimer.setSingleShot(True)
        self.__helpTimer.start(500)
        self.__helpTimer.timeout.connect(self.showHelpImage)

        self.playTimer = QTimer(self)
        self.playTimer.timeout.connect(self.moveSlider)
        self.speedSet()

    ######################1. SETUP FUNCTIONS################################
    
    def cameraViewAction(self):
        if self.stereoRadio.isChecked():
            # restore stereo state
            self.frameLeft.show()
            self.frameRight.show()
            self.measureBtn.setEnabled(True)
            self.measureScBtn.setEnabled(True)
            self.rangeBtn.setEnabled(True)
            self.activeGV='Both'
        else: # we are going mono
            if not self.defaultMonoCamera:
                from dialogs import camviewseldlg 
                dlg=camviewseldlg.CamViewSelDlg(self)
                if dlg.exec_():
                    if dlg.leftRadio.isChecked():
                        self.frameRight.hide()
                        self.activeGV='Left'
                    else:
                        self.frameLeft.hide()
                        self.activeGV='Right'
                    self.measureBtn.setEnabled(False)
                    self.measureScBtn.setEnabled(False)
                    self.rangeBtn.setEnabled(False)
                else:
                    # restore stereo state
                    self.frameLeft.show()
                    self.frameRight.show()
                    self.measureBtn.setEnabled(True)
                    self.measureScBtn.setEnabled(True)
                    self.rangeBtn.setEnabled(True)
                    self.stereoRadio.setChecked(True)
    
    def getGuiSettings(self):
        dlg=guisettingdlg.GuiSettingDlg(self)
        if dlg.exec_():
            self.guiSettings=dlg.guiSettings
            if self.recordBtn.isChecked():
                self.__changeImage()
                
    def getGridSetup(self):
        from dialogs import gridsetupdlg
        dlg=gridsetupdlg.GridSetupDlg(self)
        if dlg.exec_():
            self.gridSetup=dlg.gridSetup
            if self.recordBtn.isChecked():
                self.__changeImage()
                
    def setupProfiles(self):
        dlg=profilesetupdlg.ProfileSetupDlg(self)
        if self.activeProfile==None:
            dlg.reloadBtn.hide()
        dlg.exec_()
        if dlg.reloadFlag:
            self.loadProfile()
                
    def setActiveProfiles(self):
        
        from dialogs import setactiveprofiledlg
        dlg=setactiveprofiledlg.SetActiveProfilesDlg(self)
        dlg.exec_()
        
    def importExportProfiles(self):
        
        from dialogs import selexportcompdlg
        dlg=selexportcompdlg.SelExportCompDlg(self)
        dlg.exec_()
    
    def createNewProject(self):
        from dialogs import newprojectdlg
        dlg=newprojectdlg.NewProjectDlg(self)
        if dlg.exec_():
            pass
    
    def setupSpcBtns(self):
            # species
            self.speciesList=[]
            self.speciesDescList=[]
            self.spcColors=[]
            query=self.appDB.dbQuery("SELECT species_group, button_color, description FROM SPECIES_SETUP WHERE species_collection='"+self.speciesCollection+"' ORDER BY sort_order NULLS LAST, species_group")
            cnt=0
            for spc, color,  desc in query:
                self.speciesList.append(spc)
                self.speciesDescList.append(desc)
                val=color.split(',')
                try:
                    self.spcColors.append([int(val[0]), int(val[1]), int(val[2])])
                except:
                    self.spcColors.append([255, 255, 0])
                    color=''
                # add names to buttons
                if cnt<len(self.spcButtons):
                    btn=self.spcButtons[cnt]
                    btn.setEnabled(True)
                    btn.setText(self.speciesList[cnt])
                    btn.setToolTip(self.speciesDescList[cnt])
                    if color=='':
                        rgb='255,255,0'
                    else:
                        rgb=color
                    btn.setStyleSheet("QPushButton { background-color: rgb("+rgb+")}")
                cnt+=1
    
    def loadProfile(self):
        try:
            # settings
            self.settings={}
            query=self.appDB.dbQuery("SELECT setting, value as val FROM PROFILE_SETTINGS WHERE profile='"+self.activeProfile+"'")
            for parameter, value in query:
                self.settings.update({parameter:value})

            self.setupSpcBtns()
            self.spcSelDlg.setList(self.speciesList)


            # populate metadata
            if self.settings['CollectMetadata'].lower()=='true' or self.settings['CollectMetadata'].lower()=='yes':
                self.metadataDockWidget.setWindowTitle(self.metadataGroup)
                self.radioBtnList1=[]
                self.radioBtnDescriptionsList1=[]
                query=self.appDB.dbQuery("SELECT metadata_tag, metadata_type, description FROM FRAME_METADATA_SETUP WHERE metadata_group='"+self.metadataGroup+
                "' AND metadata_gui_element='ExclusiveRadioBox1' ORDER BY sort_order")
                value=None
                for value, Type,  desc in query:
                        self.radioBtnList1.append(value)
                        self.radioBtnDescriptionsList1.append(desc)
                if len(self.radioBtnList1)>0:
                    self.metadataTypesDict.update({'ExclusiveRadioBox1':Type})
                
                self.radioBtnList2=[]
                self.radioBtnDescriptionsList2=[]
                query=self.appDB.dbQuery("SELECT metadata_tag, metadata_type, description FROM FRAME_METADATA_SETUP WHERE metadata_group='"+self.metadataGroup+
                "' AND metadata_gui_element='ExclusiveRadioBox2' ORDER BY sort_order")
                for value, Type,  desc in query:
                        self.radioBtnList2.append(value)
                        self.radioBtnDescriptionsList2.append(desc)
                if len(self.radioBtnList2)>0:
                    self.metadataTypesDict.update({'ExclusiveRadioBox2':Type})
                    
                self.radioBtnList3=[]
                self.radioBtnDescriptionsList3=[]# this one is for horizontal single line radios
                query=self.appDB.dbQuery("SELECT metadata_tag, metadata_type, description FROM FRAME_METADATA_SETUP WHERE metadata_group='"+self.metadataGroup+
                "' AND metadata_gui_element='ExclusiveRadioBox3' ORDER BY sort_order")
                for value, Type,  desc in query:
                        self.radioBtnList3.append(value)
                        self.radioBtnDescriptionsList3.append(desc)
                if len(self.radioBtnList3)>0:
                    self.metadataTypesDict.update({'ExclusiveRadioBox3':Type})
                
                self.lineEditList=[]
                self.metadataTypeLabel2.setText('')
                query=self.appDB.dbQuery("SELECT metadata_tag, metadata_type FROM FRAME_METADATA_SETUP WHERE metadata_group='"+self.metadataGroup+
                "' AND metadata_gui_element='LineEdit' ORDER BY sort_order")
                for value, Type in query:
                        self.lineEditList.append(value)
                if len(self.lineEditList)>0:
                    self.metadataTypesDict.update({'LineEdit':Type})
                    self.metadataTypeLabel2.setText(Type)
                
                self.checkBoxList=[]
                self.metadataTypeLabel3.setText('')
                query=self.appDB.dbQuery("SELECT metadata_tag, metadata_type FROM FRAME_METADATA_SETUP WHERE metadata_group='"+self.metadataGroup+
                "' AND metadata_gui_element='CheckBox' ORDER BY sort_order")
                for value, Type in query:
                        self.checkBoxList.append(value)
                if len(self.checkBoxList)>0:
                    self.metadataTypesDict.update({'CheckBox':Type})
                    self.metadataTypeLabel3.setText(Type)
                
                if len(self.radioBtnList1)>0:# we have some of this type
                    self.exclusiveRadioBox1.show()
                    self.exclusiveRadioBox1.setTitle(self.metadataTypesDict['ExclusiveRadioBox1'])
                    for i in list(range(len(self.radioBtnTags1))):
                        if i<len(self.radioBtnList1):
                            self.radioBtnTags1[i].show()
                            self.radioBtnTags1[i].setText(self.radioBtnList1[i])
                            self.radioBtnTags1[i].setToolTip(self.radioBtnDescriptionsList1[i])
                        else:
                            self.radioBtnTags1[i].setText('')
                            self.radioBtnTags1[i].hide()
                else:
                    self.exclusiveRadioBox1.hide()
                    
                if len(self.radioBtnList2)>0:# we have some of this type
                    self.exclusiveRadioBox2.show()
                    self.exclusiveRadioBox2.setTitle(self.metadataTypesDict['ExclusiveRadioBox2'])
                    for i in list(range(len(self.radioBtnTags2))):
                        if i<len(self.radioBtnList2):
                            self.radioBtnTags2[i].show()
                            self.radioBtnTags2[i].setText(self.radioBtnList2[i])
                            self.radioBtnTags2[i].setToolTip(self.radioBtnDescriptionsList2[i])
                        else:
                            self.radioBtnTags2[i].setText('')
                            self.radioBtnTags2[i].hide()
                else:
                    self.exclusiveRadioBox2.hide()
                    
                if len(self.radioBtnList3)>0:# we have some of this type
                    self.exclusiveRadioBox3.show()
                    self.exclusiveRadioBox3.setTitle(self.metadataTypesDict['ExclusiveRadioBox3'])
                    for i in list(range(len(self.radioBtnTags3))):
                        if i<len(self.radioBtnList3):
                            self.radioBtnTags3[i].show()
                            self.radioBtnTags3[i].setText(self.radioBtnList3[i])
                            self.radioBtnTags3[i].setToolTip(self.radioBtnDescriptionsList3[i])
                        else:
                            self.radioBtnTags3[i].setText('')
                            self.radioBtnTags3[i].hide()
                else:
                    self.exclusiveRadioBox3.hide()
                # populate metadata Check boxes
                cnt=0
                for btn in self.metadataCheckBoxes:
                    if cnt<len(self.checkBoxList):
                        if self.checkBoxList[cnt]!='':
                            btn.setText(self.checkBoxList[cnt])
                        else:
                            btn.hide()
                    else:
                        btn.hide()
                    cnt+=1
                # populate coverage
                cnt=0
                for label in self.metadataLineEditLabels:
                    if cnt<len(self.lineEditList):
                        if self.lineEditList!='':
                            label.setText(self.lineEditList[cnt])
                        else:
                            label.hide()
                            self.metadataLineEdits[cnt].hide()
                    else:
                        label.hide()
                        self.metadataLineEdits[cnt].hide()
                    cnt+=1
                    if self.metadataGroup=='CamTrawl_metadata':
                        self.camtrawlMetadataFlag=True
                        import CamTrawlMetadata
                        self.metadata = CamTrawlMetadata.CamTrawlMetadata()
                        self.metadata.open(self.deploymentPath)
                        self.metadata.query()
            self.metadataStickyBox.setEnabled(True)
            if self.guiSettings['DefaultMetadataSelection']=='retain':
                self.metadataStickyBox.setChecked(True)
            else:
                self.metadataStickyBox.setChecked(False)
            if 'SubsampleMask' in self.settings:
                if self.settings['SubsampleMask'].lower()=='no' or self.settings['SubsampleMask'].lower()=='':
                    self.doMask=False
                else:
                    self.doMask=True
            else:
                self.doMask=False
                
            # this is fix form makng trawlable a radiobutton
            if self.metadataGroup in ['Habitat', 'Habitat_Coral']:
                if self.dataDB:
                    if self.dataDB.db.isOpen():
                        # look to see if there are any trawlability records under checkbox
                        query=self.dataDB.dbQuery("SELECT deployment_id, frame_number, metadata_group, metadata_tag, metadata_type, metadata_value FROM FRAME_METADATA "+" WHERE deployment_id='"+
                        self.deployment+"' AND metadata_tag='Trawlable' and metadata_type='Check Box'")
                        for deployment_id, frame_number, metadata_group, metadata_tag, metadata_type, metadata_value in query:
                            # insert net type of record
                            if metadata_value=='Checked':
                                self.dataDB.dbExec("INSERT INTO FRAME_METADATA (project, deployment_ID, frame_number, metadata_group, metadata_tag, metadata_type, metadata_value,annotator)"+
                                    " VALUES('"+self.activeProject+"', '"+deployment_id+"',"+frame_number+",'"+metadata_group+"','Yes','"+self.metadataTypesDict['ExclusiveRadioBox3']+
                                    "','Checked','"+self.annotator+"')")
                            else:
                                self.dataDB.dbExec("INSERT INTO FRAME_METADATA (project, deployment_ID, frame_number, metadata_group, metadata_tag, metadata_type, metadata_value,annotator)"+
                                    " VALUES('"+self.activeProject+"','"+deployment_id+"',"+frame_number+",'"+metadata_group+"','No','"+self.metadataTypesDict['ExclusiveRadioBox3']+
                                    "','Checked','"+self.annotator+"')")
                            
                        # delete old style records
                        self.dataDB.dbExec("DELETE FROM FRAME_METADATA WHERE"+
                        " metadata_tag='Trawlable' and metadata_type='Check Box'  AND deployment_ID='"+self.deployment+"'")

            return True
        except:
            self.showError()
            return False


    def showError(self):
        t=traceback.format_exception(*sys.exc_info())
        txt=''
        for line in t:
            txt=txt+line+'\n'
        print(txt)
        QMessageBox.warning(self, "ERROR", txt)


    def loadDeployment(self):
        # close the previous deployment , if any
        if not self.deployment==None:
            self.bkpDep=self.deployment
            self.bkpDepPath=self.deploymentPath
        #  get the deployment directory
        dirDlg = QFileDialog(self)
        self.deploymentPath = dirDlg.getExistingDirectory(self, 'Select Deployment Directory', self.__dataDir,
                                              QFileDialog.ShowDirsOnly)
        if (self.deploymentPath == ''):
            if not self.bkpDep==None: # we bailed on loading a new deployment
                self.deploymentPath=self.bkpDepPath # get us back where we were
                return
                
        else:
            if not self.deployment==None:# close out existing deployment if there is one
                if not self.dataDB == None:
                    self.writeFrameData()
                    self.dataDB.dbClose()
                    self.writeDatatoCSV()
                    # must clear out everything
                    self.activeProfile=None
            #  update the application settings with the data directory

            self.deployment = self.deploymentPath.split('/')[-1]
            self.sourcePath = QDir(self.deploymentPath)
            self.sourcePath.cdUp()
            self.__dataDir = self.sourcePath.path()
            
            # get projects
            dlg=selectprojectdlg.SelectProjectDlg(self)
            if dlg.exec_():
                self.activeProject=dlg.selectedProject
                if self.activeProject==None:
                    QMessageBox.warning(self, "ERROR", "You have to select a Project to load deployment.")
                    return 
                self.projectDict=dlg.selectedProjectDict
            else:
                QMessageBox.warning(self, "ERROR", "You have to select a Project to load deployment.")
                return 

            #  check if the database folder exists
            self.speciesCollection=self.projectDict['species_collection']
            self.metadataGroup=self.projectDict['metadata_group']

            ################   HERE we will open a local "data db" ######################
            self.dataPath = self.sourcePath.path()+ '/' +self.deployment + '/' + "data" + '/'
            #  check if the local SQLite database file exists
            if QDir(self.dataPath).exists():
                #  check if the SQLite database file exists
                if QFile(self.dataPath + self.activeProject+'_' + self.deployment+'.db').exists():
                    #  try to open the database
                    try:
                        self.dataDB = dbConnection.dbConnection(self.dataPath + self.activeProject+'_' + self.deployment+'.db', '', '',label='dataDB', driver="QSQLITE")
                    except:
                        QMessageBox.warning(self, "ERROR", "There's something amiss with the data folder. You need to clear this up to access this deployment.")
                        return
                    # check for existing profile in profile db
                    try:
                        self.dataDB.dbOpen()
                    except:
                        self.showError()
                        return
                
                elif QFile(self.dataPath +  self.deployment+'.db').exists():# legacy database
                    # rename file to current db naming convention with the project 
                    QFile().rename(self.dataPath +  self.deployment+'.db', self.dataPath + self.activeProject+'_' + self.deployment+'.db')
                    #  try to open the database
                    try:
                        self.dataDB = dbConnection.dbConnection(self.dataPath + self.activeProject+'_' + self.deployment+'.db', '', '',label='dataDB', driver="QSQLITE")
                    except:
                        QMessageBox.warning(self, "ERROR", "There's something amiss with the data folder. You need to clear this up to access this deployment.")
                        return
                    # check for existing profile in profile db
                    try:
                        self.dataDB.dbOpen()
                    except:
                        self.showError()
                        return
                else: # we have a new project, lets make a new db file, shall we?
                    try:
                        self.dataDB = dbConnection.dbConnection(self.dataPath + self.activeProject+'_' + self.deployment+'.db', '', '',label='dataDB', driver="QSQLITE")
                        self.dataDB.dbOpen()
                        if self.dataDB.db.isOpen():
                            self.makeDB()
                        else:
                            QMessageBox.warning(self, "ERROR", "Can't create local database.")
                            return 
                    except:
                        self.showError()
                        return
            else:# a new db file is needed - this is the first time we are opening this drop
                # make the folder
                QDir().mkdir(self.dataPath)
                try:
                    self.dataDB = dbConnection.dbConnection(self.dataPath + self.activeProject+'_' + self.deployment+'.db', '', '',label='dataDB', driver="QSQLITE")
                    self.dataDB.dbOpen()
                    if self.dataDB.db.isOpen():
                        self.makeDB()
                    else:
                        QMessageBox.warning(self, "ERROR", "Can't create local database.")
                        return 
                except:
                    self.showError()
                    return
                        
            # add annotator and time stamp field if it doesnt exist
            query = self.dataDB.dbQuery("PRAGMA table_info('TARGETS')")
            fields=[]
            for field in query:
                fields.append(field[1])
            if not 'ANNOTATOR' in fields:
                self.dataDB.dbExec("ALTER TABLE TARGETS ADD COLUMN ANNOTATOR TEXT;")
                self.dataDB.dbExec("ALTER TABLE FRAME_METADATA ADD COLUMN ANNOTATOR TEXT;")
                self.dataDB.dbExec("ALTER TABLE FRAMES ADD COLUMN ANNOTATOR TEXT;")
                self.dataDB.dbExec("ALTER TABLE BOUNDING_BOXES ADD COLUMN ANNOTATOR TEXT;")
                
            # check for timastamp field in db, if not, add it
            query = self.dataDB.dbQuery("PRAGMA table_info('TARGETS')")
            fields=[]
            for field in query:
                fields.append(field[1])
            if not 'TIME_STAMP' in fields:
                self.dataDB.dbExec("ALTER TABLE TARGETS ADD COLUMN TIME_STAMP TEXT;")
                self.dataDB.dbExec("ALTER TABLE FRAMES ADD COLUMN TIME_STAMP TEXT;")
                
            # check for timastamp field in db, if not, add it
            query = self.dataDB.dbQuery("PRAGMA table_info('TARGETS')")
            fields=[]
            for field in query:
                fields.append(field[1])
            if not 'PROJECT' in fields:
                self.dataDB.dbExec("ALTER TABLE DEPLOYMENT ADD COLUMN PROJECT TEXT;")
                self.dataDB.dbExec("ALTER TABLE TARGETS ADD COLUMN PROJECT TEXT;")
                self.dataDB.dbExec("ALTER TABLE FRAME_METADATA ADD COLUMN PROJECT TEXT;")
                self.dataDB.dbExec("ALTER TABLE FRAMES ADD COLUMN PROJECT TEXT;")
                self.dataDB.dbExec("ALTER TABLE BOUNDING_BOXES ADD COLUMN PROJECT TEXT;")
            
            # now select profile
            if not self.activeProfile:
                # check to see if theres already an entry frop this dep
                query=self.dataDB.dbQuery("SELECT profile FROM deployment WHERE deployment_ID = '"+self.deployment+"'")
                profile, =query.first()
                if profile:
                    self.activeProfile=profile
                else:
                    query=self.appDB.dbQuery("SELECT count(*) FROM PROFILES WHERE active='Yes'")
                    val, =query.first()

                    dlg=makeseldlg.MakeSelDlg(self,  'profile', 'active')
                    if dlg.exec_():
                        self.activeProfile=dlg.value
                        # put it into the db
                        time_now=QDateTime().currentDateTime()
                        self.dataDB.dbExec("INSERT INTO deployment (project, deployment_ID,last_opened,profile)"+
                        " VALUES('"+self.activeProject+"', '"+self.deployment+"','"+time_now.toString()+"','"+self.activeProfile+"')")

                    else:
                        QMessageBox.warning(self, "ERROR", "Need a profile to work.")
                        return 

                        
            if not self.loadProfile():
                QMessageBox.warning(self, "ERROR", "There's something amiss with the profile settings.  Have a peek!")
                self.dataDB.dbExec("DELETE FROM deployment WHERE project='"+self.activeProject+"' and deployment_id='"+self.deployment+"'")
                return

            if not QDir(self.deploymentPath + '/' + self.settings['LeftCameraImagePath']+ '/').exists():
                QMessageBox.warning(self, "ERROR", "This is not a valid deployment folder.")
                # delete profile from deployments table in project db
                self.dataDB.dbExec("DELETE FROM deployment WHERE project='"+self.activeProject+"' and deployment_id='"+self.deployment+"'")
                return

            self.loadEnhancements()

            self.appSettings.setValue('self.dataPath', self.deploymentPath)
            if not self.setupDeployment():
                self.close()
                
    def loadEnhancements(self):
        try:
            if QDir(self.sourcePath.path() + '/' + self.deployment + '/' + "data" + '/').exists():
                if QFile(self.sourcePath.path() + '/' + self.deployment + '/' + "data" + '/' + self.deployment+'_image_adjustments.npy').exists():
                    temp=ny.load(self.sourcePath.path() + '/' + self.deployment + '/' + "data" + '/' + self.deployment+'_image_adjustments.npy', allow_pickle=True)
                    imageadjustments=temp.item()
                    
                    self.leftAdjustmentParms=imageadjustments['left']
                    self.rightAdjustmentParms=imageadjustments['right']
                    self.gvLeft.image.setParameters(self.leftAdjustmentParms)
                    self.gvRight.image.setParameters(self.rightAdjustmentParms)
        except:
            pass
    
        

        
    def setupDeployment(self):
        self.deploymentBox.setText(self.activeProject+":"+self.deployment)
        # clear out gv transform
        self.gvRight.resetTransform()
        self.gvLeft.resetTransform()
        # apply mask, if desired
        if self.doMask:
            val=self.settings['SubsampleMask']
            vals=val.split(',')
            rect=QRect(int(vals[0]), int(vals[1]), int(vals[2]), int(vals[3]))
            self.gvRight.setSubsampleRect(rect)
            self.gvLeft.setSubsampleRect(rect)

        # load in some fetcher properties
        p=self.settings['FrameNumberIndices'].split('-')
        self.imgNumInds=[int(p[0]), int(p[1])]

        if self.settings['ImageTimestampType'].strip()=='in_file_name':
            self.imgTimestamp=[self.settings['ImageTimestampFormat'].strip(), int(self.settings['ImageTimestampStart'].strip())]
        elif self.settings['ImageTimestampType'].strip()=='EXIF':
            self.imgTimestamp=['exif',0]
        else:
            self.imgTimestamp=['NoTimestamp',0]

        # get image names
        self.LPath=self.deploymentPath + '/' + self.settings['LeftCameraImagePath']+ '/'
        self.RPath=self.deploymentPath + '/' + self.settings['RightCameraImagePath']+ '/'
        # check for validity
        if not QDir(self.LPath).exists():
            QMessageBox.warning(self, "ERROR", self.LPath+" Is not a valid folder.")
            return False
        if not QDir(self.RPath).exists():
            QMessageBox.warning(self, "ERROR", self.RPath+" Is not a valid folder.")
            return False
        #  set the loading error var
        self.__loadingError = False
        #  create a couple of progress bars
        self.leftPB = QProgressBar()
        self.leftPB.setRange(0,100)
        self.leftPB.setValue(0)
        self.rightPB = QProgressBar()
        self.rightPB.setRange(0,100)
        self.rightPB.setValue(0)
        self.statusBar.addWidget(self.leftPB)
        self.statusBar.addWidget(self.rightPB)
        # turn s**t on
        for widget in self.recordEnableWidgets:
            widget.setEnabled(True)
        #  clear the viewers
        for obj in [self.gvLeft, self.gvRight]:
            obj.removeScene()
            obj.createScene()
        self.leftImageDict=self.getImageFiles(self.LPath,  self.leftPB)
        if not self.leftImageDict:
            return False
        keys=list(self.leftImageDict.keys())
        keys.sort()
        self.leftImageFrames=keys
        self.statusBar.removeWidget(self.leftPB)
        self.leftPB = None
        self.rightImageDict=self.getImageFiles(self.RPath,  self.rightPB)
        keys=list(self.rightImageDict.keys())
        keys.sort()
        self.rightImageFrames=keys
        self.statusBar.removeWidget(self.rightPB)
        self.rightPB = None

        self.noLoad=False
        self.datadlg=dataviewdlg.DataViewDlg(self)
        #position = self.appSettings.value('datawinposition', QPoint(10,10))
        #self.datadlg.move(position)
        self.datadlg.selectionEvent.connect(self.changeSelectionFromTable)
        
        self.datadlg.keyPress.connect(self.__keyPressEvent)
        # load in stereo calibration

        
        if 'CalibrationFileName' in self.settings:
            self.mode='stereo'
            filename=str(self.settings['CalibrationFileName'])
            filename=filename.strip()
            if filename[-4:]=='.npz':
                self.stereoComp.mode='openCV'
            elif filename[-4:]=='.mat':
                self.stereoComp.mode='matlab'
            elif filename[-4:]=='json':
                self.stereoComp.mode='json'
            else:
                QMessageBox.warning(self, "ERROR", filename+" is not an accepted file type.")
                return False
            if QFile('../calibrations/' + filename).exists():
                try:
                    State, cal = self.stereoComp.importCalData('../calibrations/' + filename)
                except:
                    QMessageBox.warning(self, "ERROR", filename+ "  Has issues!!!")
                    return False
            else:
                QMessageBox.warning(self, "ERROR", filename+" Is not located in the SEBASTES\calibration folder.  Please put it there.")
                return False
            if not State:
                QMessageBox.warning(self, "ERROR", cal)
                return False
        else:
            self.mode='mono'

        #  try to get the camera orientations
        if 'RotateRightImage' in self.settings:
            self.gvRight.setRotation(self.settings['RotateRightImage'])
        else:
            #  no orientation data available for this camera
            self.gvRight.setRotation('0')
        if 'RotateLeftImage' in self.settings:
            self.gvLeft.setRotation(self.settings['RotateLeftImage'])
        else:
            #  no orientation data available for this camera
            self.gvLeft.setRotation('0')


        self.minFr=min(min(self.leftImageFrames), min(self.rightImageFrames))
        self.maxFr=max(max(self.leftImageFrames), max(self.rightImageFrames))
        self.minFrame.setText(str(self.minFr))
        self.maxFrame.setText(str(self.maxFr))
        self.imageSlider.setMinimum(0)
        self.imageSlider.setMaximum(len(self.leftImageDict)-1)
        self.imageSlider.setSingleStep(1)
        self.recordBtn.setEnabled(True)
        self.toggleRecord()
        self.imageSlider.setValue(1)
        self.playBtn.setEnabled(True)
        return True
        
    def makeDB(self):
        file=open('../db/Project.db.sql')
        sql_script=file.read()
        statements=sql_script.split(';')
        for statement in statements:
            if statement !='':
                statement=statement.replace('\t', ' ')
                statement=statement.replace('\n', '')
                try:
                    self.dataDB.dbExec(statement)
                except:
                    pass


    def getImageFiles(self,  imPath,  progressbar):
        try:
            #  check if the cached directory structure exists
            # left images
#            if QFile(imPath+'.imListCache').exists(): # weve alread loaded this one
#                icacheFile = open(imPath + '.imListCache')
#                imageFileDict = pickle.load(icacheFile)
#                icacheFile.close()
#            else:#  get the directory listing
            imageFileDict={}
            if 'ImageFileType' in self.settings:
                type=self.settings['ImageFileType']
            else:
                type='jpg'
            lastProgress = 0
            totalFrames = len(os.listdir(str(imPath) ))
            i=1
            for file in glob.glob(str(imPath) + '/*.'+type):
                
                imageFile=file.split('\\')[-1]
                imageFrame=int(imageFile[max([(self.imgNumInds[0]-1), 0]):self.imgNumInds[1]])
                if self.settings['ImageTimestampType'].lower()=='in_file_name':
                    try:
                        dateStartInd=self.imgTimestamp[1]-1# for python's sake
                        if self.imgTimestamp[0]=='DyyyyMMdd-Thhmmss.zzz':
                            trim=3
                            pydateformat='D%Y%m%d-T%H%M%S.%f'
                        else:
                            pydateformat=self.imgTimestamp[0]
                            trim=0
                        try:
                            timestamp=datetime.strptime(imageFile[dateStartInd:dateStartInd+len(datetime.now().strftime(pydateformat))-trim], pydateformat)
                            goodtimestamp=True
                        except:
                            goodtimestamp=False
                            timestamp=None

                    except:# fix this in the future?
                        goodtimestamp=False
                        timestamp=None
                elif  self.settings['ImageTimestampType'].lower()=='exif':
                    try:
                        img = Image(open(file, 'rb'))
                        if img.has_exif:
                            goodtimestamp=True
                            timestamp=datetime.strptime(img.datetime,'%Y:%m:%d %H:%M:%S')
                        else:
                            goodtimestamp=False
                            timestamp=None
                    except:
                            goodtimestamp=False
                            timestamp=None
                else:
                    goodtimestamp=False
                    timestamp=None
                    
                imageFileDict.update({imageFrame:[timestamp, imageFile]})
                #  signal our progress
                progress = int((i / float(totalFrames)) * 100)
                if (progress !=  lastProgress):
                    lastProgress = progress
                    progressbar.setValue(progress)
                i+=1
#                icacheFile = open(imPath + '.imListCache', 'wb')
#                pickle.dump(imageFileDict, icacheFile)
#                icacheFile.close()
            if not goodtimestamp:
                QMessageBox.warning(self, "ERROR", "Timestamp could not be extracted from file name. Check the profile setup!")
            
            return imageFileDict
        except:
            self.showError()

    def viewApplicationDB(self):
        dlg=viewapplicationdbdlg.ViewApplicationDBDlg(self)
        dlg.exec_()
        
    def directEditDBTables(self):
        dlg=directeditDBdlg.DirectEditDBDlg(self)
        dlg.exec_()
##############################2. GV FUNCTIONS ######################################



    def showHelpImage(self):
        if self.appDB==None:
            self.close()

        #  clear the viewers
        self.gvLeft.removeScene()
        self.gvLeft.createScene()
        self.__leftCamLabel = []

        #  load the help images

        self.gvLeft.setImageFromFile(self.baseDir + '/' + 'resources' + '/' + 'help.jpg')
        self.gvLeft.fillExtent()

    def showAdjustmentsDialog(self):
        if self.sender()==self.adjLeftBtn:
            gv=self.gvLeft
            self.leftAdjustmentParms = gv.image.getParameters()
            gv.adjustmentDialog.setState(self.leftAdjustmentParms)
        else:
            gv=self.gvRight
            self.rightAdjustmentParms = gv.image.getParameters()
            gv.adjustmentDialog.setState(self.rightAdjustmentParms)
        gv.adjustmentDialog.show()

    def resizeEvent(self, event):

        #  Scale the image to fill the the image widget when we resize.
        #  This is a bit heavy handed, it will reset the zoom on resize,
        #  but we want the image to scale when we resize and dealing with
        #  the details of resizing when zoomed is a headache.
        self.gvLeft.fillExtent()
        self.gvRight.fillExtent()

    def __changeImage(self):
        '''
        This method is called whenever the images are changed, either by
        adjusting brightness, gamma, or contrast or by moving the image
        slider.
        '''
        try:
            #  tell the fetchers to send us an new/adjusted image
            if self.recordBtn.isChecked():
                self.deSelect()
                self.clearMarks()
                # deal with the grid
                if not self.gridSetup['PersistentGrid'] and self.gridCheck.isChecked():
                    self.gridCheck.setChecked(False)
                    self.gridBoxAction()
                for obj in [self.gvLeft, self.gvRight]:
                    obj.removeScene()
                    obj.createScene()

                    
            self.LFile=self.readImage(self.gvLeft)
            self.RFile=self.readImage(self.gvRight)
            if self.imageSlider.value()>len(self.leftImageFrames)-1:
                return
            currentFrame=self.leftImageFrames[self.imageSlider.value()]
            self.frameBox.setText(str(currentFrame))

            if self.measureBtn.isChecked():
                self.measureBtn.setChecked(False)
            self.zoomBtn=0
            self.targetLinkLabel.setText('')
            if self.recordBtn.isChecked():
                self.reloadData()
                self.incrementCounters()
            self.currentTarget=0
            if self.gridSetup['PersistentGrid'] and self.gridCheck.isChecked():
                self.gridBoxAction()
            if self.camtrawlMetadataFlag:
                # check to see if this has already had an entry in the metadata table
                query = self.dataDB.dbQuery("SELECT frame_number FROM frame_metadata WHERE frame_number = "+self.frameBox.text()+" AND deployment_id='"+self.deployment+"'")
                got_frame, =query.first()
                if got_frame==None:
                    self.getCamtrawlMetadataValues(self.imageSlider.value())
            
        except:
            self.showError()

    def getCamtrawlMetadataValues(self,  frame):
        if int(frame) in self.metadata.sensorData['CTControl']['$OHPR']:
            attitudeString = self.metadata.sensorData['CTControl']['$OHPR'][int(frame)]
            stringParts = attitudeString.split(',')
            depth = '%.1f' % (float(stringParts[5]))
            # populate line boxes
            self.metadataLineEdits[0].setText(depth)
            self.metadataLineEdits[1].setText(stringParts[2])
            self.metadataLineEdits[2].setText(stringParts[1])
            self.metadataLineEdits[3].setText(stringParts[3])

    def readImage(self, gvObj):
        if self.imageSlider.value()>len(self.leftImageFrames)-1:
            return
        currentFrame=self.leftImageFrames[self.imageSlider.value()]
        try:
            if gvObj==self.gvLeft:
                imFile=self.leftImageDict[currentFrame][1]
                imTime=self.leftImageDict[currentFrame][0]
                imPath=self.LPath
            else:
                if currentFrame in self.rightImageDict:
                    imFile=self.rightImageDict[currentFrame][1]
                    imTime=self.rightImageDict[currentFrame][0]
                    imPath=self.RPath
                else:
                    return
            imgFileLoc=imPath+imFile

            #  create the timestamp string
            if imTime:
                #self.dtString = dateTime.toString('yyyy-MM-dd hh:mm:ss.zzz')
                self.dtString = imTime.strftime('%Y-%m-%d %H:%M:%S.%f')
            else:
                self.dtString = ''
            gvObj.setImageFromFile(imgFileLoc)
            gvObj.resetView()
            gvObj.fillExtent()
            self.activeMark[gvObj]==None
            self.mouseInWidget(self.mousebits[0], self.mousebits[1], self.mousebits[2])
            return imgFileLoc

        except:
            self.showError()

    def mouseInWidget(self, imageObj, location, modifier):
        if imageObj==None:
            return
        #  you can use the mouseMoveEvent signal to provide a current pixel location
        #  on your GUI say in the status bar
        winsize=self.closeupWinSize
        source=QRect(max(int(round(location.x())-winsize/2), 0),max(int(round(location.y())-winsize/2), 0) , winsize, winsize)
        dest=QPixmap(256, 256)
        paint=QPainter(dest)
        paint.drawPixmap(QRect(0, 0, 256, 256), imageObj.imgPixmap,source)
        mark = QPolygonF()
        mark.append(QPointF(128,128-10))
        mark.append(QPointF(128,128+10))
        mark.append(QPointF(128,128))
        mark.append(QPointF(128-10,128))
        mark.append(QPointF(128+10,128))
        mark.append(QPointF(128,128))
        pen = QPen(QColor(255, 255, 0), 255)
        pen.setWidthF(1)
        paint.setPen(pen)

        paint.drawPolyline(mark)
        paint.end()
        self.closeup.imgLabel.setPixmap(dest)
        self.mousebits=[imageObj, location, modifier]

    def speedSet(self):
        speed=float(self.playSpeedSlider.value())*(float(self.guiSettings['PlaybackSpeedAdjust']))
        self.playTimer.setInterval(int(1./speed*1000))

    def play(self):
        if self.playBtn.isChecked():
            self.playBtn.setPalette(self.green)
            self.playTimer.start()
        else:
            self.playBtn.setPalette(self.black)
            self.playTimer.stop()

    def moveSlider(self):
        self.imageSlider.setValue(self.imageSlider.value()+1)

#####################4. UI FUNCTIONS########################################

    def btnPress(self):
        if self.pressTime.elapsed()<250:# user double clicked
            if self.spcSelDlg.exec_() and self.spcSelDlg.listWidget.currentIndex().row()>-1:
                new_spc=self.spcSelDlg.listWidget.currentItem().text()
                # check to see if it is already in the button list
                ind=self.speciesList.index(new_spc)
                if ind<len(self.spcButtons):# new species is already attached to a button
                    # switch sort orders
                    old_sort=str(ind+1)
                else:# new species is coming in hot
                    old_sort="NULL"
                    
                btn=self.sender()
                old_spc=btn.text()
                new_sort=str(self.spcButtons.index(btn)+1)
                # update db
                self.appDB.dbExec("UPDATE SPECIES_SETUP SET sort_order="+old_sort+" WHERE species_group='"+old_spc+"'")
                self.appDB.dbExec("UPDATE SPECIES_SETUP SET sort_order="+new_sort+" WHERE species_group='"+new_spc+"'")
                self.setupSpcBtns()
        else:
            self.pressTime.start()
            if self.sender() in self.spcButtons:
                templist=list(self.spcButtons)
                templist.remove(self.sender())
            for btn in templist:
                btn.setChecked(False)

    def btnRelease(self):
        self.incrementCounters()

    def event(self, event):
        if (event.type() == QEvent.KeyPress):
            self.__keyPressEvent(None, event)
            return True
        else:
            return QMainWindow.event(self, event)

    def __keyPressEvent(self, ivObj, ev):
        if self.noLoad:
            return
        # which key is being held down
        self.key=ev.key()

        if ev.key() == 65:
            if self.computeMatchBox.isChecked():
                self.computeMatchBox.setChecked(False)
            else:
                self.computeMatchBox.setChecked(True)
                
        elif (ev.key() == Qt.Key_Delete):

            self.deleteSelMark()
#        if (ev.key() == Qt.Key_R):
#            self.rangeBtn.setChecked(True)
#            self.toggleRange()

#        key=str(ev.text()).upper()
#        if key in self.keystrokeMap:
#            self.toggleClass(self.keystrokeMap[key])

        elif (ev.key() == Qt.Key_Home):
            self.linkBtn.setChecked(True)
            self.toggleLink()

#        elif (ev.key() == Qt.Key_Shift):
#            if not self.rangeBtn.isChecked() and not self.stereoOnlyCheckBox.isChecked():
#                self.matchMode=True
#                self.pairPoints=[]
        # navigate though images
        elif ev.key() in [ Qt.Key_Right, Qt.Key_Left]:
            if self.measureBtn.isChecked() or self.measureScBtn.isChecked():
                return# dont advance frame while measurements are taking place
            #  write any data to the database before changing image
            if self.recordBtn.isChecked():
                self.writeFrameData()
                self.clearValues()
            frameIndex=self.imageSlider.value()
            sampleRate = float(self.sampleRateEdit.text())
            try:
                offset = float(self.rateOffsetEdit.text())
            except:
                offset = 0
            if (ev.key() == Qt.Key_Right) or (ev.key() == Qt.Key_Left):
                if (ev.key() == Qt.Key_Right):
                    if (ev.modifiers() == Qt.ControlModifier):
                        #  increment one image
                        targetIndex=frameIndex + 1
                    else:
                        #  increment one sample step
                        targetIndex=int(round((float(frameIndex + sampleRate-offset)) /
                                        float(sampleRate)) * sampleRate)+offset
                else :
                    if (ev.modifiers() == Qt.ControlModifier):
                        #  decrement one image
                        targetIndex=frameIndex
                    else:
                        #  decrement one sample step
                        targetIndex=int(round((float(frameIndex - sampleRate-offset)) /
                                        float(sampleRate)) * sampleRate)+offset




            #  clamp the image numbers to a valid range
            if targetIndex < 1:
                targetIndex = 1
            if targetIndex > self.imageSlider.maximum():
                targetIndex = self.imageSlider.maximum()
            #  check for linked data, null out if more than one frame out
            if len(self.linkData)>0:
                if not (targetIndex - self.linkData[0]) in [0, 1]:
                    self.linkData=[]
                    self.linkBtn.setChecked(False)
            self.imageSlider.setValue(targetIndex)
            
        elif (ev.key() == Qt.Key_Escape):
            self.deSelect()
            self.clearMarks()
            self.measureScBtn.setChecked(False)
            self.rangeBtn.setChecked(False)
            self.activeLine[self.gvLeft]=None
            self.activeLine[self.gvRight]=None
            self.activeMark[self.gvLeft]=None
            self.activeMark[self.gvLeft]=None
            try:
                if self.rubberBanding:
                    self.rubberBanding = False
            except:
                self.showError()

            if len(self.pairPoints)==1: #user lifted shift button  but didn't mean to
                lZoom=self.gvLeft.zoomLevel
                rZoom=self.gvRight.zoomLevel
                            # get the zoom state
                if self.activeMark[self.gvLeft]:
                    lPoint=self.activeMark[self.gvLeft].mapToScene(self.activeMark[self.gvLeft].boundingRect().center())
                else:
                    lPoint=None
                if self.activeMark[self.gvRight]:
                    rPoint=self.activeMark[self.gvRight].mapToScene(self.activeMark[self.gvRight].boundingRect().center())
                else:
                    rPoint=None
                # find the pair
                self.__changeImage()
                # zoom back
                if lPoint!=None:
                    self.gvLeft.zoomToPoint(lPoint, lZoom)
                if rPoint!=None:
                    self.gvRight.zoomToPoint(rPoint, rZoom)
                self.pairPoints=[]

            self.__changeImage()
            
    def __keyReleaseEvent(self,ivObj, ev):
        # no key is being held down right now

        if (ev.key() == Qt.Key_Shift):
            if not self.rangeBtn.isChecked() and not self.stereoOnlyCheckBox.isChecked():
                if len(self.pairPoints)==1: #user lifted shift button  but didn't mean to
                    lZoom=self.gvLeft.zoomLevel
                    rZoom=self.gvRight.zoomLevel
                                # get the zoom state
                    if self.activeMark[self.gvLeft]:
                        lPoint=self.activeMark[self.gvLeft].mapToScene(self.activeMark[self.gvLeft].boundingRect().center())
                    else:
                        lPoint=None
                    if self.activeMark[self.gvRight]:
                        rPoint=self.activeMark[self.gvRight].mapToScene(self.activeMark[self.gvRight].boundingRect().center())
                    else:
                        rPoint=None
                    # find the pair
                    self.__changeImage()
                    # zoom back
                    if lPoint!=None:
                        self.gvLeft.zoomToPoint(lPoint, lZoom)
                    if rPoint!=None:
                        self.gvRight.zoomToPoint(rPoint, rZoom)
                    self.pairPoints=[]
        self.key=None



    def myWheelEvent(self, imageObj, ev):
        """
        Zoom using the wheel event.
        """

        #  ev is the Qt mouse wheel event structure. Important elements are:
        #   delta - which is +120 for a forward roll and -120 for a backward roll
        #   pos - which is the position as QPointF


        #  for this example we'll only zoom if we have an active mark in each
        #  image. This way the
        if (self.activeMark[self.gvLeft] or
            self.activeMark[self.gvRight]):

            #  For zooming in this example we'll zoom to our active mark. This
            #  means that when possible, the mark will be centered in the view.

            if (ev.angleDelta().y() > 0):
                #  mouse rolled forward - zoom in
                if self.activeMark[self.gvLeft]:
                    self.gvLeft.zoomToMark(self.activeMark[self.gvLeft], 1)
                if self.activeMark[self.gvRight]:
                    self.gvRight.zoomToMark(self.activeMark[self.gvRight], 1)
                self.zoomBtn=self.zoomBtn+1
            else:
                #  mouse rolled back - zoom out
                if self.activeMark[self.gvLeft]:
                    self.gvLeft.zoomToMark(self.activeMark[self.gvLeft], -1)
                if self.activeMark[self.gvRight]:
                    self.gvRight.zoomToMark(self.activeMark[self.gvRight], -1)
                self.zoomBtn=self.zoomBtn-1

#        else:
#            if (ev.angleDelta() > 0):
#                    self.gvLeft.scale( 1, 1)
#                    self.gvRight.scale( 1, 1)
#            else:
#                    self.gvLeft.zoomToPoint(ev.pos(), -1)
#                    self.gvRight.zoomToPoint(ev.pos(), -1)

    def deSelect(self):
        for items in self.__selectedItems:
            items.setSelected(False)
        self.activeMark [self.gvRight]=None
        self.activeMark [self.gvLeft]=None
        self.__selectedItems=[]


    def imageClick(self, imageObj, clickLoc, button, currentKbKey, item):
        # selection code
        if button==2:
            # first deselect everything
            self.deSelect()
            remList=[]
            for i in item:
                if not i in self.pointMarks and not i in self.boxMarks:
                    remList.append(i)
            for i in remList:
                item.remove(i)
            if len(item)>0:# we only want to select non temp marks!


                item=item[0]
                item.setSelected(True)
                self.__selectedItems.append(item)
                self.pairedTarget=False

                if item in self.pointMarks:#these are the points
                    self.activeMark [imageObj]=item
                    # check for paired item
                    target_number = int(self.pointMarks[item][0])
                    self.currentTarget=target_number
                    # get target level annotator
                    query = self.dataDB.dbQuery("SELECT annotator FROM TARGETS WHERE frame_number = "+self.frameBox.text()+" and target_number="+str(self.currentTarget)+" AND deployment_id='"+self.deployment+"'")
                    current_tator, =query.first()
                    if current_tator==None:
                        current_tator=''
                    self.annotatorLabel.setText(current_tator)
                    
                    query = self.dataDB.dbQuery("SELECT target_link FROM targets WHERE frame_number = "+self.frameBox.text()+" and target_number="+str(self.currentTarget)+" AND deployment_id='"+self.deployment+"'")
                    target_link, =query.first()
                    if target_link!='':
                        self.targetLinkLabel.setText(target_link)
                    for pairItem, info in self.pointMarks.items():
                        if info[0]==target_number:
                            if not info[1]==imageObj:
                                pairItem.setSelected(True)
                                self.pairedTarget=True
                                self.__selectedItems.append(pairItem)
                                if imageObj==self.gvLeft:
                                    self.activeMark [self.gvRight]=pairItem
                                else:
                                    self.activeMark [self.gvLeft]=pairItem
                if self.showDataCheck.isChecked():
                    self.selectValueFromImage()# this is to send delection signal to data view window and select the appropriate row
                # if we have checked link button, put in th elink
                # clear link display

                if len(self.linkData)>0:
                    self.dataDB.dbExec("UPDATE targets SET target_link = "+str(self.linkData[1])+
                    " WHERE frame_number = "+self.frameBox.text()+" AND target_number ="+str(self.currentTarget)+"  AND deployment_ID='"+self.deployment+"'")
                    self.linkData=[]
                    self.targetLinkLabel.setText(str(self.currentTarget))
                    self.linkBtn.setChecked(False)
        else:

            if self.measureBtn.isChecked():
                dimLine = imageObj.startDimensionLine(clickLoc, taillength=self.guiSettings['MeasureLineTailLength'],  thickness=self.guiSettings['MeasureLineWidth'], color=self.guiSettings['TargetLineColor'])
                self.rubberBanding = True
                #check to see if we already have amark on this gv?
                old_line=None
                for lineObj, descriptor in self.lineMarks.items():
                    if descriptor[1]==imageObj and descriptor[0]==self.currentTarget:# we already have a dimension line for this target in this image
                        old_line=lineObj
                        break
                if old_line:# we do, get rid of it
                    del self.lineMarks[old_line] 
                    imageObj.removeItem(old_line)
                self.lineMarks.update({dimLine:[self.currentTarget, imageObj]})
                
            elif self.measureScBtn.isChecked():
                # create  new target for this
                query = self.dataDB.dbQuery("SELECT max(target_number) FROM targets WHERE frame_number = "+self.frameBox.text()+" AND deployment_id='"+self.deployment+"'")
                max_target, =query.first()
                if max_target!=None:
                    self.currentTarget=int(max_target)+1
                else:# no targets yet for this frame
                    self.currentTarget=1
                dimLine = imageObj.startDimensionLine(clickLoc, taillength=self.guiSettings['MeasureLineTailLength'],  thickness=self.guiSettings['MeasureLineWidth'], color=self.guiSettings['SceneColor'])
                self.rubberBanding = True
                self.lineMarks.update({dimLine:[self.currentTarget, imageObj]})

            else:

                # add a species count marker
                # check to see if any species is selected
                self.spcInd=None
                for btn in self.spcButtons:
                    if btn.isChecked():
                        self.spcInd=self.spcButtons.index(btn)
                        break
                if not self.spcInd==None or self.rangeBtn.isChecked():# theres some kind of class selected
                    if item:
                        remList=[]
                        for i in item:
                            if not i in self.pointMarks:
                                remList.append(i)
                        for i in remList:
                            item.remove(i)
                    if self.rangeBtn.isChecked():
                        style='d'
                        col=self.guiSettings['SceneColor']
                    else:
                        if QGuiApplication.queryKeyboardModifiers()==Qt.ShiftModifier or self.stereoOnlyCheckBox.isChecked():
                            style='o'
                            col=self.spcColors[self.spcInd]
                            if len(self.pairPoints)>0:
                                if imageObj in self.pairPoints[0]:
                                    return
                        else:
                            style='+'
                        # extract color from button?
                        btn=self.spcButtons[self.spcInd]
                        colstr=re.findall(r'\d+', btn.styleSheet())
                        col=[int(colstr[0]), int(colstr[1]), int(colstr[2])]

                    if self.recordBtn.isChecked():
                        # check to see if in grid boundary, if needed
                        if self.gridSetup['CellBoundary'] and self.gridCheck.isChecked():
                            if self.randomCellBounds is not None:
                                if clickLoc.x()<self.randomCellBounds[0] or clickLoc.x()>self.randomCellBounds[1] or clickLoc.y()<self.randomCellBounds[2] or clickLoc.y()>self.randomCellBounds[3]:
                                    QMessageBox.warning(self, "ERROR", "Target not within selected grid cell! If you don't want this, check grid setup.")
                                    return
                        # add the mark
                        query = self.dataDB.dbQuery("SELECT max(target_number) FROM targets WHERE frame_number = "+self.frameBox.text()+" AND deployment_id='"+self.deployment+"'")
                        target_count, =query.first()
                        if target_count!=None:
                            self.currentTarget=int(target_count)+1
                        else:# no targets yet for this frame
                            self.currentTarget=1
                        if self.makeBoxes:
                            imageObj.startRubberBand(clickLoc, color=self.spcColors[self.spcInd],thickness=self.guiSettings['BoxLineThickness'])

                            self.rubberBanding = True
                            return# we are just rubberbanding, no need to do anythin else


                        marker = imageObj.addMark(clickLoc, style=style, color=col,
                                                  size=1.0, thickness=1.0, alpha=255, selectThickness=self.selThickness,  selectColor=self.selColor)
                        spcLabel=''
                        if self.guiSettings['LabelSpeciesParam']>0:
                            spcLabel=self.spcButtons[self.spcInd].text()
                            if len(spcLabel)>self.guiSettings['LabelSpeciesParam']:
                                spcLabel=spcLabel[0:self.guiSettings['LabelSpeciesParam']]

                        marker.addLabel(str(self.currentTarget)+" "+spcLabel, color=col, offset=self.textOffset, name='tnumber',  size=self.guiSettings['LabelTextSize'])
                        if not self.labelCheck.isChecked():
                            marker.hideLabels(None)


                        if QGuiApplication.queryKeyboardModifiers()==Qt.ShiftModifier  or self.stereoOnlyCheckBox.isChecked():# matched target
                            if len(self.pairPoints)<1:# have only half of the points for this matched target
                                if self.computeMatchBox.isChecked():# here we auto fill both points
                                    if imageObj==self.gvLeft:
                                        im1=self.gvLeft.image.enhancedData
                                        im2=self.gvRight.image.enhancedData
                                    else:
                                        im2=self.gvLeft.image.enhancedData
                                        im1=self.gvRight.image.enhancedData
                                    point=ny.array([[clickLoc.x(), clickLoc.y()]])
                                    state,  point_c,  score=self.stereoComp.computeMatch(im1, im2, point)
                                    if not state:
                                        QMessageBox.warning(self, "ERROR",score)
                                        self.__changeImage()
                                        self.computeMatchBox.setChecked(False)
                                        return
                                    try:
                                        t=float(self.matchThresholdEdit.text())
                                    except:
                                        t=None
#                                    if t[1]:
#                                        if score>t[0]:
#                                            print(score)
#                                            QMessageBox.warning(self, "ERROR", "Couldn't find an appropriate match!")
#                                            self.__changeImage()
#                                            return
                                    if imageObj==self.gvLeft:
                                        otherObj=self.gvRight
                                    else:
                                        otherObj=self.gvLeft
                                    # check projection error first!
                                    self.targetPosition=[]
                                    self.pairedTarget=True
                                    if  imageObj==self.gvLeft:
                                        self.targetPosition.append(QPointF(clickLoc.x(), clickLoc.y()))
                                        self.targetPosition.append(QPointF(point_c[0][0], point_c[0][1]))
                                        points=str(clickLoc.x())+","+str(clickLoc.y())+","+str(point_c[0][0])+","+str(point_c[0][1])
                                    else:
                                        self.targetPosition.append(QPointF(point_c[0][0], point_c[0][1]))
                                        self.targetPosition.append(QPointF(clickLoc.x(), clickLoc.y()))
                                        points=str(point_c[0][0])+","+str(point_c[0][1])+","+str(clickLoc.x())+","+str(clickLoc.y())
                                    self.calculate('point')
                                    if t:
                                        if self.targetStereoData[1]>t:
                                            QMessageBox.warning(self, "ERROR", "Couldn't find an appropriate match!")
                                            self.__changeImage()
                                            self.computeMatchBox.setChecked(False)
                                            return
                                    # crate mark for other side
                                    self.theOtherTarget = otherObj.addMark(QPoint(point_c[0][0], point_c[0][1]), style=style, color=col,
                                              size=1.0, thickness=1.0, alpha=255, selectThickness=self.selThickness,  selectColor=self.selColor)
                                    self.theOtherTarget.addLabel(str(self.currentTarget)+" "+spcLabel, color=col, offset=self.textOffset, name='tnumber',  size=self.guiSettings['LabelTextSize'])
                                    if not self.labelCheck.isChecked():
                                        self.theOtherTarget.hideLabels(None)
                                    self.pointMarks.update({marker:[self.currentTarget,  imageObj]})
                                    # and your twin too!

                                    if imageObj==self.gvLeft:
                                        self.activeMark [self.gvLeft]=marker
                                        self.activeMark [self.gvRight]=self.theOtherTarget
                                        self.pointMarks.update({self.theOtherTarget:[self.currentTarget,  self.gvRight]})
                                    else:
                                        self.activeMark [self.gvLeft]=self.theOtherTarget
                                        self.activeMark [self.gvRight]=marker
                                        self.pointMarks.update({self.theOtherTarget:[self.currentTarget,  self.gvLeft]})
                                    self.theOtherTarget=None

#                                    self.targetPosition=[]
#                                    self.pairedTarget=True
#                                    if  imageObj==self.gvLeft:
#                                        self.targetPosition.append(QPointF(clickLoc.x(), clickLoc.y()))
#                                        self.targetPosition.append(QPointF(point_c[0][0], point_c[0][1]))
#                                        points=str(clickLoc.x())+","+str(clickLoc.y())+","+str(point_c[0][0])+","+str(point_c[0][1])
#                                    else:
#                                        self.targetPosition.append(QPointF(point_c[0][0], point_c[0][1]))
#                                        self.targetPosition.append(QPointF(clickLoc.x(), clickLoc.y()))
#                                        points=str(point_c[0][0])+","+str(point_c[0][1])+","+str(clickLoc.x())+","+str(clickLoc.y())
                                    if self.rangeBtn.isChecked():# this is not an animal target, but just a range value
                                        tClass='SceneRange'
                                    else: # animal target
                                        tClass=self.spcButtons[self.spcInd].text()
                                    dt=datetime.now(timezone.utc)
                                    self.dataDB.dbExec("INSERT INTO targets (project, deployment_ID,frame_number, target_number, species_group, LX, LY, RX, RY, annotator, time_stamp)  "+
                                    "VALUES('"+self.activeProject+"','"+self.deployment+"',"+self.frameBox.text()+","+str(self.currentTarget)+",'"+tClass+"',"+points+",'"+self.annotator+"','"+dt.strftime(self.timestamp_format)+"')")
                                    self.pairPoints=[]
                                    if self.rangeBtn.isChecked():
                                        self.rangeBtn.setChecked(False)
#                                        self.toggleRange()
#                                    self.calculate('point')
                                    self.dataDB.dbExec("UPDATE targets SET Range = "+str(self.targetStereoData[0])+", Error = "+str(self.targetStereoData[1])+
                                    ", hx = "+str(self.targetStereoData[2])+",hy = "+str(self.targetStereoData[3])+", hz ="+str(self.targetStereoData[4])+
                                    " WHERE frame_number = "+self.frameBox.text()+" AND target_number ="+str(self.currentTarget)+"  AND deployment_ID='"+self.deployment+"'")
                                    if len(self.linkData)>0:
                                        self.dataDB.dbExec("UPDATE targets SET target_link = "+str(self.linkData[1])+
                                        " WHERE frame_number = "+self.frameBox.text()+" AND target_number ="+str(self.currentTarget)+"  AND deployment_ID='"+self.deployment+"'")
                                        self.linkData=[]
                                        self.linkBtn.setChecked(False)
                                    targetLabel=str(self.currentTarget)+" r = "+str(round(self.targetStereoData[0], 2))+"  e = "+str(round(self.targetStereoData[1], 2))
                                    if self.guiSettings['ShowClassOnLabel']=='true':
                                        targetLabel=targetLabel+' '+tClass
                                    self.activeMark[self.gvLeft].setLabelText('tnumber',targetLabel)
                                    if not self.labelCheck.isChecked():
                                        self.activeMark[self.gvLeft].hideLabels(None)
                                    if self.showDataCheck.isChecked():
                                        self.datadlg.refreshView()
                                    return




                                self.pairPoints.append([imageObj, clickLoc.x(), clickLoc.y()])
                                self.pairedTarget=False
                                # active mark stuff
                                self.activeMark [self.gvLeft]=None
                                self.activeMark [self.gvLeft]=None
                                self.theOtherTarget=marker
                            else:# this the second point of the pair
                                if imageObj==self.gvLeft:
                                    self.activeMark [self.gvLeft]=marker
                                    self.activeMark [self.gvRight]=self.theOtherTarget
                                    self.theOtherTarget=None
                                else:
                                    self.activeMark [self.gvLeft]=self.theOtherTarget
                                    self.activeMark [self.gvRight]=marker
                                    self.theOtherTarget=None

                                self.targetPosition=[]
                                self.pairedTarget=True
                                if  imageObj==self.gvLeft:
                                    self.targetPosition.append(QPointF(clickLoc.x(), clickLoc.y()))
                                    self.targetPosition.append(QPointF(self.pairPoints[0][1], self.pairPoints[0][2]))
                                    points=str(clickLoc.x())+","+str(clickLoc.y())+","+str(self.pairPoints[0][1])+","+str(self.pairPoints[0][2])
                                else:
                                    self.targetPosition.append(QPointF(self.pairPoints[0][1], self.pairPoints[0][2]))
                                    self.targetPosition.append(QPointF(clickLoc.x(), clickLoc.y()))
                                    points=str(self.pairPoints[0][1])+","+str(self.pairPoints[0][2])+","+str(clickLoc.x())+","+str(clickLoc.y())
                                if self.rangeBtn.isChecked():# this is not an animal target, but just a range value
                                    tClass='SceneRange'
                                else: # animal target
                                    tClass=self.spcButtons[self.spcInd].text()
                                dt=datetime.now(timezone.utc)
                                self.dataDB.dbExec("INSERT INTO targets (project, deployment_ID,frame_number, target_number, species_group, LX, LY, RX, RY, annotator, time_stamp)  "+
                                "VALUES('"+self.activeProject+"', '"+self.deployment+"',"+self.frameBox.text()+","+str(self.currentTarget)+",'"+tClass+"',"+points+",'"+self.annotator+"','"+dt.strftime(self.timestamp_format)+"')")
                                self.pairPoints=[]
                                if self.rangeBtn.isChecked():
                                    self.rangeBtn.setChecked(False)
#                                    self.toggleRange()
                                self.calculate('point')
                                self.dataDB.dbExec("UPDATE targets SET Range = "+str(self.targetStereoData[0])+", Error = "+str(self.targetStereoData[1])+
                                ", hx = "+str(self.targetStereoData[2])+",hy = "+str(self.targetStereoData[3])+", hz ="+str(self.targetStereoData[4])+
                                " WHERE frame_number = "+self.frameBox.text()+" AND target_number ="+str(self.currentTarget)+"  AND deployment_ID='"+self.deployment+"'")
                                if len(self.linkData)>0:
                                    self.dataDB.dbExec("UPDATE targets SET target_link = "+str(self.linkData[1])+
                                    " WHERE frame_number = "+self.frameBox.text()+" AND target_number ="+str(self.currentTarget)+"  AND deployment_ID='"+self.deployment+"'")
                                    self.linkData=[]
                                    self.linkBtn.setChecked(False)

                                targetLabel=str(self.currentTarget)+" r = "+str(round(self.targetStereoData[0], 2))+"  e = "+str(round(self.targetStereoData[1], 2))
                                if self.guiSettings['ShowClassOnLabel']=='true':
                                    targetLabel=targetLabel+' '+tClass
                                self.activeMark[self.gvLeft].setLabelText('tnumber',targetLabel)
                                if not self.labelCheck.isChecked():
                                    self.activeMark[self.gvLeft].hideLabels(None)
                                if self.showDataCheck.isChecked():
                                    self.datadlg.refreshView()
                                    ##########
                                self.pairPoints=[]
                                    
                        else:# non-matched target
                            #set active mark for zooming
                            if imageObj==self.gvLeft:
                                self.activeMark [self.gvLeft]=marker
                                self.activeMark [self.gvRight]=None
                            else:
                                self.activeMark [self.gvLeft]=None
                                self.activeMark [self.gvRight]=marker
                            # set selection
                            if  imageObj==self.gvLeft:
                                points=str(clickLoc.x())+","+str(clickLoc.y())+",NULL,NULL"
                            else:
                                points="NULL,NULL,"+str(clickLoc.x())+","+str(clickLoc.y())
                            dt=datetime.now(timezone.utc)
                            self.dataDB.dbExec("INSERT INTO targets (project, deployment_ID,frame_number, target_number, species_group, LX, LY, RX, RY,annotator, time_stamp)"+
                            " VALUES('"+self.activeProject+"', '"+self.deployment+"',"+self.frameBox.text()+","+str(self.currentTarget)+",'"+self.spcButtons[self.spcInd].text()+"',"+points+",'"+self.annotator+"','"+
                            dt.strftime(self.timestamp_format)+"')")
                            self.pairedTarget=False
                            if self.showDataCheck.isChecked():
                                self.datadlg.refreshView()
                            # add to speices in grid if grid is activated
                            if self.gridCheck.isChecked():
                                self.speciesInGrid.add(self.spcButtons[self.spcInd].text())
                        self.pointMarks.update({marker:[self.currentTarget,  imageObj]})
        self.incrementCounters()
        
    def deleteSelMark(self):
        if len(self.__selectedItems)>0:
            item =self.__selectedItems[0]# it it is a pair, grab just one
            reply=QMessageBox.warning(self, "WARNING", "Sure you want to delete the mark(s)?",  QMessageBox.Yes, QMessageBox.No)
            if reply==QMessageBox.No:
                return

            for i in self.__selectedItems:
                i.setSelected(False)
            self.__selectedItems=[]
            if item in self.pointMarks:
                target=self.pointMarks[item][0]
                if target in self.linkData:
                    if self.linkData[1]==target:
                        self.linkData=[]
                self.dataDB.dbExec("DELETE FROM targets WHERE frame_number = "+self.frameBox.text()+" AND target_number = "+str(target)+"  AND deployment_ID='"+self.deployment+"'")
            elif item in self.boxMarks:
                boxTarget=self.boxMarks[item][0]
                self.dataDB.dbExec("DELETE FROM bounding_boxes WHERE frame_number = "+self.frameBox.text()+" AND target_number = "+str(boxTarget)+"  AND deployment_ID='"+self.deployment+"'")
            self.__changeImage()
                # zoom back if there are any active targets in either frame
        self.incrementCounters()

    def imageUnClick(self, imageObj, clickLoc, button, modifier):

        if self.rubberBanding:
            if self.makeBoxes:
                rubberbandObj = imageObj.endRubberBand()
                #set minimum size in pix (makes it easer to delete bad regions)
                if rubberbandObj.width()<20.:
                    rubberbandObj.setWidth(20.)
                if rubberbandObj.height()<20.:
                    rubberbandObj.setHeight(20.)
                #  add a polygon item showing the RB selection
                boxObj = imageObj.addPolygon(rubberbandObj,color=self.spcColors[self.spcInd], thickness=self.guiSettings['BoxLineThickness'], selectable=True,
                        selectThickness=4.0, selectColor=self.selColor)
                # figure out bbox target number
                query = self.dataDB.dbQuery("SELECT max(target_number) FROM bounding_boxes WHERE frame_number = "+self.frameBox.text()+" AND deployment_id='"+self.deployment+"'")
                max_target, =query.first()
                if max_target!=None:
                    self.currentBBoxTarget=int(max_target)+1
                else:# no targets yet for this frame
                    self.currentBBoxTarget=1
                self.boxMarks.update({boxObj:[self.currentBBoxTarget,  imageObj]})
                #  and add a label - polygon labels are attached to the vertices and the first
                #  argument is the index of the vertex you want to attach the label to. For
                #  rubber band boxes, the verts are always ordered clockwise from the upper left
                spcLabel=''
                if self.guiSettings['LabelSpeciesParam']>0:
                    spcLabel=self.spcButtons[self.spcInd].text()
                    if len(spcLabel)>self.guiSettings['LabelSpeciesParam']:
                        spcLabel=spcLabel[0:self.guiSettings['LabelSpeciesParam']]

                boxObj.addLabel(0, str(self.currentBBoxTarget)+" "+spcLabel, size=self.guiSettings['LabelTextSize'],  color=self.spcColors[self.spcInd])
                BoxCoords=rubberbandObj.toRect()
                self.rubberBanding = False
                # this would be where we write the results
                #print("write stuff")
                if imageObj==self.gvLeft:
                    image_file_name=self.LFile
                    cam='left'
                else:
                    image_file_name=self.RFile
                    cam='right'
                width=imageObj.image.enhancedData.shape[1]
                height=imageObj.image.enhancedData.shape[0]
                self.dataDB.dbExec("INSERT INTO bounding_boxes (project, deployment_ID,frame_number, target_number, species_group, camera_id, image_file_name, origin_x,origin_y,width, height, frame_width, frame_height,annotator)"+
                                                    " VALUES('"+self.activeProject+"','"+self.deployment+"',"+self.frameBox.text()+","+str(self.currentBBoxTarget)+",'"+self.spcButtons[self.spcInd].text()+"','" +cam+"',"
                                                    "'"+image_file_name+"', "+str(BoxCoords.x())+", "+str(BoxCoords.y())+", "+str(BoxCoords.width())+", "+str(BoxCoords.height())+","+str(width)+","+str(height)+",'"+self.annotator+"')")
                return# we are just rubberbanding, no need to do anythin else

            dimLine = imageObj.endDimensionLine()
            self.rubberBanding = False
            self.activeLine[imageObj] = dimLine
            if self.measureBtn.isChecked() or self.measureScBtn.isChecked():
                if not self.activeLine[self.gvLeft]==None and not self.activeLine[self.gvRight]==None:
                    # measurement completed, let's do some math
                    if self.measureBtn.isChecked():
                        col=self.guiSettings['TargetLineColor']
                    else:
                        col=self.guiSettings['SceneColor']


                    # stereo triangulation
                    self.calculate('line')
                                        # check to see alignment of target and line
#                    if self.measureBtn.isChecked():
#                        for obj in [self.gvLeft,  self.gvRight]:
#                            # get position of current target
#                            point=None
#                            for mark,  bits in self.pointMarks.items():
#                                if bits[0]==self.currentTarget and bits[1]==obj:
#                                    point=mark.pos()
#                            line=self.activeLine[obj].getLine()
#                            if not point:
#                                return
#                            if point.x()<min([line.x1(),  line.x2()]) or point.x()>max([line.x1(),  line.x2()]) or point.y()<min([line.y1(),  line.y2()])-self.yBuffer or point.y()>max([line.y1(),  line.y2()])+self.yBuffer:
#                                # the target point is outside of box specified by the line
#                                reply=QMessageBox.warning(self, "ERROR", "Length Line does not seem to be in proximity of the traget. Do you have the right target?" ,  QMessageBox.Yes, QMessageBox.No)
#                                if reply==QMessageBox.No:
#                                    for obj in [self.gvLeft,  self.gvRight]:
#                                        obj.removeItem(self.activeLine[obj])
#                                        self.garbage.append(self.lineMarks.pop(self.activeLine[obj]))
#                                        self.activeLine[obj] = None
#                                        self.measureBtn.setChecked(False)
#                                    return
                    line=self.activeLine[self.gvLeft].getLine()
                    self.activeLine[self.gvLeft].addLabel(line.p1(), "l = "+str(round(self.targetStereoData[0], 2))+" e = "+str(round(self.targetStereoData[2], 2)), color=col,  size=self.guiSettings['LabelTextSize'])


                    if not self.labelCheck.isChecked():
                        self.activeLine[self.gvLeft].hideLabels(None)

                    self.activeLine[self.gvLeft]=None
                    self.activeLine[self.gvRight]=None
                    # write results
                    #[length, range, LHX, LHY,LTX,LTY, RHX, RHY,RTX,RTY,plhx, plhy, plhz,pltx,plty, pltz]
                    if self.measureBtn.isChecked():
                        if self.pairedTarget:
                            self.dataDB.dbExec("UPDATE targets SET Length = "+str(self.targetStereoData[0])+", Range = "+str(self.targetStereoData[1])+ ", Error = "+str(self.targetStereoData[2])+
                                        ", LHX = "+str(self.targetStereoData[3])+", LHY = "+str(self.targetStereoData[4])+", LTX = "+str(self.targetStereoData[5])+", LTY = "+str(self.targetStereoData[6])+
                                        ", RHX = "+str(self.targetStereoData[7])+", RHY = "+str(self.targetStereoData[8])+", RTX = "+str(self.targetStereoData[9])+", RTY = "+str(self.targetStereoData[10])+
                                        ", hx = "+str(self.targetStereoData[11])+", hy = "+str(self.targetStereoData[12])+", hz = "+str(self.targetStereoData[13])+
                                        ", tx = "+str(self.targetStereoData[14])+", ty = "+str(self.targetStereoData[15])+", tz = "+str(self.targetStereoData[16])+
                                            ", comment = '', annotator='"+self.annotatorLabel.text()+"' WHERE frame_number = "+self.frameBox.text()+" and target_number ="+str(self.currentTarget)+"  AND deployment_ID='"+self.deployment+"'")
                        self.measureBtn.setChecked(False)
                    elif self.measureScBtn.isChecked():# measure scene
                        valstring=""
                        for t in self.targetStereoData:
                            valstring=valstring+","+str(t)
                        LX=(self.targetStereoData[3]+self.targetStereoData[5])/2
                        LY=(self.targetStereoData[4]+self.targetStereoData[6])/2
                        RX=(self.targetStereoData[7]+self.targetStereoData[9])/2
                        RY=(self.targetStereoData[8]+self.targetStereoData[10])/2
                        # add a marker in the middle of the line that you can select and delete
                        marker = self.gvLeft.addMark(QPointF(LX, LY), style='d', color=self.guiSettings['SceneColor'],
                                                  size=1.0, thickness=1.0, alpha=255, selectThickness=self.selThickness,  selectColor=self.selColor)
                        # create label
                        spcLabel=''
                        if self.guiSettings['LabelSpeciesParam']>0:
                            spcLabel=self.spcButtons[self.spcInd].text()
                            if len(spcLabel)>self.guiSettings['LabelSpeciesParam']:
                                spcLabel=spcLabel[0:self.guiSettings['LabelSpeciesParam']]
                        marker.addLabel(str(self.currentTarget)+" "+spcLabel, color=col, offset=self.textOffset, name='tnumber',  size=self.guiSettings['LabelTextSize'])
                        self.activeMark [self.gvLeft]=marker
                        self.pointMarks.update({marker:[self.currentTarget,  self.gvLeft]})

                        marker = self.gvRight.addMark(QPointF(RX, RY), style='d', color=self.guiSettings['SceneColor'],
                                                  size=1.0, thickness=1.0, alpha=255, selectThickness=self.selThickness,  selectColor=self.selColor)
                        self.activeMark [self.gvRight]=marker
                        self.pointMarks.update({marker:[self.currentTarget,  self.gvRight]})
                        if not self.labelCheck.isChecked():
                            marker.hideLabels(None)
                        self.pairedTarget=True
                        dt=datetime.now(timezone.utc)
                        self.dataDB.dbExec("INSERT INTO targets (project, deployment_ID,frame_number, target_number, species_group, LX,LY,RX,RY,Length, Range, Error,  LHX, LHY, LTX, LTY, RHX, RHY,"+
                          "RTX, RTY, hx, hy, hz, tx, ty, tz, comment, annotator, time_stamp) VALUES('"+self.activeProject+"','"+self.deployment+"',"+self.frameBox.text()+","+str(self.currentTarget)+",'SceneMeasurement',"+str(LX)+","+str(LY)+
                          ","+str(RX)+","+str(RY)+valstring+",'','"+self.annotator+"','"+dt.strftime(self.timestamp_format)+"')")
                        self.measureScBtn.setChecked(False)
                else: # line is drawn on only one side
                    if self.computeMatchBox.isChecked():
                        #get the points
                        if not self.activeLine[self.gvLeft]==None: #we've clicked on the left' - search right for match
                            im1=self.gvLeft.image.enhancedData
                            im2=self.gvRight.image.enhancedData
                            line=self.activeLine[self.gvLeft].getLine()
                        else:
                            im2=self.gvLeft.image.enhancedData
                            im1=self.gvRight.image.enhancedData
                            line=self.activeLine[self.gvRight].getLine()
                        #get auto match

                        point1=ny.array([[line.x1(), line.y1()]])
                        point2=ny.array([[line.x2(), line.y2()]])
                        state,  point1_c, score=self.stereoComp.computeMatch(im1, im2, point1)
                        if not state:
                            QMessageBox.warning(self, "ERROR",score)
                            return
                        else:
                            state,  point2_c, score=self.stereoComp.computeMatch(im1, im2, point2)
                            if not state:
                                QMessageBox.warning(self, "ERROR",score)
                                return

                        #draw match line
                        stPoint=QPointF(point1_c[0, 0], point1_c[0, 1])
                        endPoint=QPointF(point2_c[0, 0], point2_c[0, 1])
                        if not self.activeLine[self.gvLeft]==None: #we've clicked on the left' - draw line on right
                            lineObjs=self.gvRight.addDimensionLine(stPoint,endPoint, taillength=self.guiSettings['MeasureLineTailLength'],
                            thickness=self.guiSettings['MeasureLineWidth'],  color=self.guiSettings['TargetLineColor'])
                            self.lineMarks.update({lineObjs:[self.currentTarget,  self.gvRight]})
                            self.activeLine[ self.gvRight] = lineObjs
                        else:
                            lineObjs=self.gvLeft.addDimensionLine(stPoint,endPoint, taillength=self.guiSettings['MeasureLineTailLength'],
                            thickness=self.guiSettings['MeasureLineWidth'],  color=self.guiSettings['TargetLineColor'])
                            self.lineMarks.update({lineObjs:[self.currentTarget,  self.gvLeft]})
                            self.activeLine[ self.gvLeft] = lineObjs
                        self.rubberBanding=False
                        # stereo triangulation
                        self.calculate('line')
                        self.targetStereoData[2]
                        try:
                            t=float(self.matchThresholdEdit.text())
                        except:
                            t=None
                        if t:
                            if self.targetStereoData[2]>t:
                                QMessageBox.warning(self, "ERROR", "Couldn't find an appropriate match!")
                                self.computeMatchBox.setChecked(False)
                                self.__changeImage()
                                return
                                            # check to see alignment of target and line
                        if self.measureBtn.isChecked():
                            for obj in [self.gvLeft,  self.gvRight]:
                                # get position of current target
                                point=None
                                for mark,  bits in self.pointMarks.items():
                                    if bits[0]==self.currentTarget and bits[1]==obj:
                                        point=mark.pos()
                                line=self.activeLine[obj].getLine()
                                if not point:
                                    return
                        line=self.activeLine[self.gvLeft].getLine()
                        targetLabel="l = "+str(round(self.targetStereoData[0], 2))+" e = "+str(round(self.targetStereoData[2], 2))
#                        if self.showClassInLabel:
#                            targetLabel=targetLabel+'\n'+tClass
                        self.activeLine[self.gvLeft].addLabel(line.p1(), targetLabel, color=self.guiSettings['TargetLineColor'],  size=self.guiSettings['LabelTextSize'])


                        if not self.labelCheck.isChecked():
                            self.activeLine[self.gvLeft].hideLabels(None)

                        self.activeLine[self.gvLeft]=None
                        self.activeLine[self.gvRight]=None
                        # write results
                        #[length, range, LHX, LHY,LTX,LTY, RHX, RHY,RTX,RTY,plhx, plhy, plhz,pltx,plty, pltz]
                        if self.measureBtn.isChecked():
                            if self.pairedTarget:
                                self.dataDB.dbExec("UPDATE targets SET Length = "+str(self.targetStereoData[0])+", Range = "+str(self.targetStereoData[1])+ ", Error = "+str(self.targetStereoData[2])+
                                            ", LHX = "+str(self.targetStereoData[3])+", LHY = "+str(self.targetStereoData[4])+", LTX = "+str(self.targetStereoData[5])+", LTY = "+str(self.targetStereoData[6])+
                                            ", RHX = "+str(self.targetStereoData[7])+", RHY = "+str(self.targetStereoData[8])+", RTX = "+str(self.targetStereoData[9])+", RTY = "+str(self.targetStereoData[10])+
                                            ", hx = "+str(self.targetStereoData[11])+", hy = "+str(self.targetStereoData[12])+", hz = "+str(self.targetStereoData[13])+
                                            ", tx = "+str(self.targetStereoData[14])+", ty = "+str(self.targetStereoData[15])+", tz = "+str(self.targetStereoData[16])+
                                                ", comment = '', annotator='"+self.annotatorLabel.text()+"' WHERE frame_number = "+self.frameBox.text()+" and target_number ="+str(self.currentTarget)+"  AND deployment_ID='"+self.deployment+"'")
                            self.measureBtn.setChecked(False)


                    if self.showDataCheck.isChecked():
                        self.datadlg.refreshView()
        self.incrementCounters()
                        
    def incrementCounters(self):
        self.spcInd=None
        for btn in self.spcButtons:
            if btn.isChecked():
                self.spcInd=self.spcButtons.index(btn)
                break
        if self.spcInd:
            species_selected=self.spcButtons[self.spcInd].text()
            query = self.dataDB.dbQuery("SELECT count(*) FROM targets WHERE species_group='"+species_selected+
            "' AND frame_number="+self.frameBox.text()+" AND LX is not null AND RX is null AND deployment_id='"+self.deployment+"'")
            left_count, =query.first()
            if left_count==None:
                left_count='0'
            query = self.dataDB.dbQuery("SELECT count(*) FROM targets WHERE species_group='"+species_selected+
            "' AND frame_number="+self.frameBox.text()+" AND RX is not null AND LX is null AND deployment_id='"+self.deployment+"'")
            right_count, =query.first()
            if right_count==None:
                right_count='0'
            query = self.dataDB.dbQuery("SELECT count(*) FROM targets WHERE species_group='"+species_selected+
            "' AND frame_number="+self.frameBox.text()+" AND RX is not null AND LX is not null AND deployment_id='"+self.deployment+"'")
            stereo_count, =query.first()
            if stereo_count==None:
                stereo_count='0'
            countstr="L = "+left_count+" R = "+right_count+" S = "+stereo_count
            self.countInFrameLabel.setText(countstr)

    def clearValues(self):
        if self.settings['CollectMetadata'].lower()=='true' or self.settings['CollectMetadata'].lower()=='yes':
            if not self.metadataStickyBox.isChecked():# reset the boxes
                self.clearAutoExclusiveRadioBtnBoxes()
                for box in self.metadataCheckBoxes:
                    if box.isVisible():
                        box.setChecked(False)
            for box in self.metadataLineEdits:
                if box.isVisible():
                    box.setText('')
        if self.guiSettings['RetainSpeciesSelection'].lower()=='clear':
            for btn in self.spcButtons:
                btn.setChecked(False)
#        self.frameComment=''

    def getFrame(self):
        if self.deployment==None:
            return
        if int(self.frameBox.text())>self.maxFr:
            QMessageBox.warning(self, "ERROR", "Max frame number is "+str(self.maxFr))
            return
        if int(self.frameBox.text())<self.minFr:
            QMessageBox.warning(self, "ERROR", "Min frame number is "+str(self.minFr) )
            return
        if int(self.frameBox.text()) in self.leftImageDict:
            
            frameIndex=self.leftImageFrames.index(int(self.frameBox.text()))
            self.imageSlider.setValue(frameIndex)
        else:
            QMessageBox.warning(self, "ERROR", "This frame number isn't in the image folder.")
            
            return

####################3. UTILITY FUNCTIONS AND CALCULATIONS ############################
    def getTargetComment(self):
        try:
            if self.currentTarget>0:
                query = self.dataDB.dbQuery("SELECT species_group, comment FROM targets WHERE frame_number = "+self.frameBox.text()+" and target_number ="+str(self.currentTarget)+" AND deployment_id='"+self.deployment+"'")
                species_group, comment=query.first()
                if species_group!=None:
                    targetClass=species_group
                    targetComment=comment

                dlg=commentdlg.CommentDlg(targetComment,  targetClass,  self.currentTarget)
                if dlg.exec_():
                    targetComment=dlg.comment
                    self.dataDB.dbExec("UPDATE targets SET comment = '"+targetComment+"' WHERE frame_number = "+self.frameBox.text()+" and target_number ="+str(self.currentTarget)+"  AND deployment_ID='"+self.deployment+"'")
            else:
                QMessageBox.warning(self, "ERROR", "No Active Target!")
        except:
            self.showError()

    def getFrameComment(self):
        if  self.frameCommentDlg==None:
            self.frameCommentDlg=framecommentdlg.CommentDlg(self)
            #self.frameCommentDlg.setWindowFlags(Qt.WindowStaysOnTopHint)
            self.frameCommentDlg.hide()
        if self.frameCommentBtn.isChecked():
            self.frameCommentDlg.show()
        else:
            self.frameCommentDlg.hide()

    def goToLastFrame(self):
        frameIndex=None
        query = self.dataDB.dbQuery("SELECT max(frame_number) FROM targets WHERE deployment_id='"+self.deployment+"'")
        frame, = query.first()
        if frame!=None:
            #get my index from targets
            frameIndex=self.leftImageFrames.index(int(frame))
        else:
            query = self.dataDB.dbQuery("SELECT max(frame_number) FROM frame_metadata WHERE deployment_id='"+self.deployment+"'")
            frame, = query.first()
            if frame!=None:
                #get my index from targets
                frameIndex=self.leftImageFrames.index(int(frame))
                
        if frameIndex:
            self.imageSlider.setValue(frameIndex)
        
    def editSpecies(self):
        dlg=editspeciesdlg.EditSpeciesDlg(self)
        dlg.goToTargetEvent.connect(self.changeSelectionFromTable)
        dlg.exec_()
        self.__changeImage()
    
    def changeSelectionFromTable(self, frame, target, zoom=None):
        frameIndex=self.leftImageFrames.index(frame)
        self.imageSlider.setValue(frameIndex)
        self.selectValueFromTable(frame, target, zoom)

    def selectValueFromTable(self, frame, target, zoom):
        if not target==None:
            for items in self.__selectedItems:
                items.setSelected(False)
            self.__selectedItems=[]
            self.activeMark [self.gvRight]=None
            self.activeMark [self.gvLeft]=None
            for item, info in self.pointMarks.items():
                if info[0]==target:
                    item.setSelected(True)
                    self.__selectedItems.append(item)
                    if info[1]==self.gvLeft:
                        self.activeMark [self.gvLeft]=item
                        if not zoom == None:
                            if zoom==0:
                                self.gvLeft.centerOnMark(self.activeMark[self.gvLeft])
                            else:
                                self.gvLeft.zoomToMark(self.activeMark[self.gvLeft], zoom)
                    else:
                        self.activeMark [self.gvRight]=item
                        if not zoom == None:
                            if zoom==0:
                                self.gvRight.centerOnMark(self.activeMark[self.gvRight])
                            else:
                                self.gvRight.zoomToMark(self.activeMark[self.gvRight],  zoom)
                        

    def selectValueFromImage(self):
        self.datadlg.setSelectedRowFromData( int(self.frameBox.text()), self.currentTarget)
        
    def uncheckCloseupWindowBox(self,  flag):
        if flag:
            self.closeupCheck.setChecked(False)

    def toggleRecord(self):
        if self.deployment==None:
            QMessageBox.warning(self, "ERROR", "Please load a deployment.")
            self.recordBtn.setChecked(False)
            return
        if self.recordBtn.isChecked():
            self.recordBtn.setPalette(self.red)
            self.imageSlider.setEnabled(False)
            self.speciesDockWidget.show()
            if self.settings['CollectMetadata'].lower()=='true' or self.settings['CollectMetadata'].lower()=='yes':
                self.metadataDockWidget.show()
            # get the annotator now!
            dlg=annotatorDlg.AnnotatorDlg()
            if dlg.exec_():
                self.annotator=dlg.annotator
            else:
                self.annotator='UNID'
                
            self.reloadData()
            for widget in self.recordEnableWidgets:
                if widget in [self.measureBtn,  self.measureScBtn,  self.rangeBtn] and self.monoRadio.isChecked(): # dont enable widgets for mono mode
                    continue
                widget.setEnabled(True)

                

        else:
            self.imageSlider.setEnabled(True)
            #self.__changeImage()
            self.speciesDockWidget.hide()
            self.metadataDockWidget.hide()
            # deselect spc buttons
            for btn in self.spcButtons:
                btn.setChecked(False)
            #self.groupBoxView.hide()
            self.recordBtn.setPalette(self.black)
            self.deSelect()
            self.clearMarks()

            try:
                self.datadlg.hide()
            except:
                pass
                
            for widget in self.recordEnableWidgets:
                widget.setEnabled(False)
        self.resizeEvent(None)
#
#    def toggleRange(self):
#        if self.rangeBtn.isChecked():
#            self.matchMode=True
#        else:
#            self.matchMode=False

    def toggleTraining(self):
        if self.trainBtn.isChecked():
            # we want to do some bounding box stuff
            for widget in self.bboxEnableWidgets:
                widget.setEnabled(False)

            self.makeBoxes=True
            # remove all marks
            self.__changeImage()
        else:
            # we want to go back to normal operations
            self.makeBoxes=False
            for widget in self.bboxEnableWidgets:
                widget.setEnabled(True)
            self.__changeImage()

    def toggleMeasure(self):
        if self.measureBtn.isChecked():
            if self.currentTarget==0:
                QMessageBox.warning(self, "ERROR", "You need to select a target first!")
                self.measureBtn.setChecked(False)
                return
            if not self.pairedTarget:
                QMessageBox.warning(self, "ERROR", "Currently active target is not a stereo target!")
                self.measureBtn.setChecked(False)
                return
                    # find line marks
            t=self.currentTarget
            query = self.dataDB.dbQuery("SELECT target_number FROM targets WHERE frame_number = "+self.frameBox.text()+" and target_number ="+str(self.currentTarget)+" AND deployment_id='"+self.deployment+"'")
            target_number, = query.first()
            if target_number!=None:
                # clear out current length measurements

                self.dataDB.dbExec("UPDATE targets SET Length = NULL"+
                ", LHX = NULL, LHY = NULL, LTX = NULL, LTY = NULL"+
                ", RHX = NULL, RHY = NULL, RTX = NULL, RTY = NULL"+
                ", tx = NULL, ty = NULL, tz = NULL WHERE frame_number = "+self.frameBox.text()+" and target_number ="+str(self.currentTarget)+"  AND deployment_ID='"+self.deployment+"'")
                # reload frame
                            # get the zoom state
                if self.activeMark[self.gvLeft]:
                    lPoint=self.activeMark[self.gvLeft].mapToScene(self.activeMark[self.gvLeft].boundingRect().center())
                else:
                    lPoint=None
                if self.activeMark[self.gvRight]:
                    rPoint=self.activeMark[self.gvRight].mapToScene(self.activeMark[self.gvRight].boundingRect().center())
                else:
                    rPoint=None

                lZoom=self.gvLeft.zoomLevel
                rZoom=self.gvRight.zoomLevel

                # find the pair
                self.__changeImage()
                # zoom back
                if lPoint!=None:
                    self.gvLeft.zoomToPoint(lPoint, lZoom)
                if rPoint!=None:
                    self.gvRight.zoomToPoint(rPoint, rZoom)
            # first time measurement
            self.measureBtn.setChecked(True)
            self.pairedTarget=True
            self.currentTarget=t
#            groupItems=[]
            for i, j in self.pointMarks.items():
                if j[0]==self.currentTarget and i !=None:
                    i.setSelected(True)
                    self.activeMark[j[1]]=i
                    self.__selectedItems.append(i)
#                    groupItems.append(i)
#            for i in groupItems:
#                if i in self.lineMarks:
#                    self.garbage.append(self.lineMarks.pop(i))

    def toggleLink(self):
        if self.linkBtn.isChecked():
            self.linkData=[int(self.frameBox.text()),  self.currentTarget]
        else:
            self.linkData=[]

    def deleteLink(self):
            reply=QMessageBox.warning(self, "WARNING", "Sure you want to delete the target link for \ntarget "+str(self.currentTarget)+" and linked target "+self.targetLinkLabel.text()+"?",  QMessageBox.Yes, QMessageBox.No)
            if reply==QMessageBox.No:
                return
            self.linkData=[]
            self.dataDB.dbQuery("UPDATE targets set target_link=NULL WHERE frame_number = "+self.frameBox.text()+" and target_number="+str(self.currentTarget)+"  AND deployment_ID='"+self.deployment+"'")
            self.targetLinkLabel.setText('')
                        
                        
    def metadataSelAction(self):

        self.sender().setAutoExclusive(False)
        if self.sender().isChecked():
            self.sender().setChecked(False)
            self.sender().setAutoExclusive(True)
            
    def writeCurrentFrame(self):
        pass

    def writeFrameData(self):
        try:
            if not self.recordBtn.isChecked():
                return
            # get the annotator business with commas
            current_tators=self.annotatorLabel.text()
            # get the current frame comment
            if self.frameCommentDlg!=None:
                comment=self.frameCommentDlg.commentBox.toPlainText()
            else:
                comment=''
            # see if current frame is already in 
            query=self.dataDB.dbQuery("SELECT frame_number FROM FRAMES WHERE frame_number="+self.frameBox.text()+" AND deployment_id='"+self.deployment+"'")
            frame, =query.first()
            if frame:# already exists
                self.dataDB.dbExec("UPDATE frames SET comment='"+comment+"', annotator='"+current_tators+"' WHERE frame_number="+self.frameBox.text()+
                "  AND deployment_ID='"+self.deployment+"'")
            else:
                dt=datetime.now(timezone.utc)
                self.dataDB.dbExec("INSERT INTO frames (project, deployment_ID, frame_number, frame_time, comment, annotator, time_stamp)"+
                    " VALUES('"+self.activeProject+"', '"+self.deployment+"',"+self.frameBox.text()+",'"+self.dtString+"','"+comment+"','"+current_tators+"','"+dt.strftime(self.timestamp_format)+"')")
            if self.settings['CollectMetadata'].lower()=='true' or self.settings['CollectMetadata'].lower()=='yes':
                # now we write metadata
                self.dataDB.dbExec("DELETE FROM FRAME_METADATA WHERE frame_number="+self.frameBox.text()+" AND metadata_group='"+self.metadataGroup+"' AND deployment_ID='"+self.deployment+"'")
                if 'ExclusiveRadioBox1' in self.metadataTypesDict:
                    for rBtn in self.radioBtnTags1:
                        if rBtn.isChecked():
                            mdt_tag=rBtn.text()
                            # write exclusive radio button 1
                            self.dataDB.dbExec("INSERT INTO FRAME_METADATA (project, deployment_ID, frame_number, metadata_group, metadata_tag, metadata_type, metadata_value,annotator)"+
                            " VALUES('"+self.activeProject+"','"+self.deployment+"',"+self.frameBox.text()+",'"+self.metadataGroup+"','"+mdt_tag+"','"+self.metadataTypesDict['ExclusiveRadioBox1']+
                            "','Checked','"+self.annotator+"')")
                            break # we can do this caouse its autoexclusive!
                            
                if 'ExclusiveRadioBox2' in self.metadataTypesDict:
                    for rBtn in self.radioBtnTags2:
                        if rBtn.isChecked():
                            mdt_tag=rBtn.text()
                            # write exclusive radio button 1
                            self.dataDB.dbExec("INSERT INTO FRAME_METADATA (project, deployment_ID, frame_number, metadata_group, metadata_tag, metadata_type, metadata_value, annotator)"+
                            " VALUES('"+self.activeProject+"', '"+self.deployment+"',"+self.frameBox.text()+",'"+self.metadataGroup+"','"+mdt_tag+"','"+self.metadataTypesDict['ExclusiveRadioBox2']+
                            "','Checked','"+self.annotator+"')")
                            break # we can do this caouse its autoexclusive!
                                    
                    for rBtn in self.radioBtnTags3:
                        if rBtn.isChecked():
                            mdt_tag=rBtn.text()
                            # write exclusive radio button 1
                            self.dataDB.dbExec("INSERT INTO FRAME_METADATA (project, deployment_ID, frame_number, metadata_group, metadata_tag, metadata_type, metadata_value,annotator)"+
                            " VALUES('"+self.activeProject+"', '"+self.deployment+"',"+self.frameBox.text()+",'"+self.metadataGroup+"','"+mdt_tag+"','"+self.metadataTypesDict['ExclusiveRadioBox3']+
                            "','Checked','"+self.annotator+"')")
                            break # we can do this caouse its autoexclusive!
                            
                if 'LineEdit' in self.metadataTypesDict:
                    for i in list(range(len(self.metadataLineEdits))):
                        if self.metadataLineEditLabels[i].isVisible():
                            mdt_tag=self.metadataLineEditLabels[i].text()
                            mtd_val=self.metadataLineEdits[i].text()
                            self.dataDB.dbExec("INSERT INTO FRAME_METADATA (project, deployment_ID, frame_number, metadata_group, metadata_tag, metadata_type, metadata_value, annotator)"+
                            " VALUES('"+self.activeProject+"','"+self.deployment+"',"+self.frameBox.text()+",'"+self.metadataGroup+"','"+mdt_tag+"','"+self.metadataTypesDict['LineEdit']+"','"+
                            mtd_val+"','"+self.annotator+"')")

                if 'CheckBox' in self.metadataTypesDict:
                    for i in list(range(len(self.metadataCheckBoxes))):
                        if self.metadataCheckBoxes[i].isVisible():
                            mdt_tag=self.metadataCheckBoxes[i].text()
                            if self.metadataCheckBoxes[i].isChecked():
                                mtd_val='Checked'
                            else:
                                mtd_val='Unchecked'
                            self.dataDB.dbExec("INSERT INTO FRAME_METADATA (project,deployment_ID, frame_number, metadata_group, metadata_tag, metadata_type, metadata_value, annotator)"+
                            " VALUES('"+self.activeProject+"', '"+self.deployment+"',"+self.frameBox.text()+",'"+self.metadataGroup+"','"+mdt_tag+"','"+self.metadataTypesDict['CheckBox']+"','"+
                            mtd_val+"','"+self.annotator+"')")
            if not self.metadataStickyBox.isChecked():# reset autoexclusive buttons
                self.clearAutoExclusiveRadioBtnBoxes()
            if self.showDataCheck.isChecked():
                self.datadlg.refreshView()
            if self.gridCheck.isChecked():
                self.writeGridDetailsToMetadata()
        except:
            self.showError()

    

    def reloadData(self):
        if not self.recordBtn.isChecked():
            return
        if self.makeBoxes:
            # redraw boxes
            query = self.dataDB.dbQuery("SELECT camera_id,species_group,origin_x,origin_y,width,height,target_number FROM bounding_boxes WHERE frame_number="+self.frameBox.text()+" AND deployment_id='"+self.deployment+"'", self.dataDB)
            for camera_id,species_group,origin_x,origin_y,width,height,target_number in query:
                if camera_id=='left':
                    imageObj=self.gvLeft
                else:
                    imageObj=self.gvRight
                spcInd=None
                for btn in self.spcButtons:
                    if btn.text()==species_group:
                        spcInd=self.spcButtons.index(btn)
                        break
                if not spcInd==None:
                    col=self.spcColors[spcInd]
                else:
                    col=[255,  0,  0]
                boxCoords=QRect(int(origin_x),int(origin_y),int(width),int(height))
                boxObj = imageObj.addPolygon(boxCoords,color=col, thickness=self.guiSettings['BoxLineThickness'], selectable=True,
                        selectThickness=4.0, selectColor=self.selColor)

                self.boxMarks.update({boxObj:[int(target_number),  imageObj]})
                #  and add a label - polygon labels are attached to the vertices and the first
                #  argument is the index of the vertex you want to attach the label to. For
                #  rubber band boxes, the verts are always ordered clockwise from the upper left
                spcLabel=''
                if self.guiSettings['LabelSpeciesParam']>0:
                    spcLabel=species_group
                    if len(spcLabel)>self.guiSettings['LabelSpeciesParam']:
                        spcLabel=spcLabel[0:self.guiSettings['LabelSpeciesParam']]
                boxObj.addLabel(0, target_number+" "+spcLabel, color=col, size=self.guiSettings['LabelTextSize'])

        else:
            # get frame level annotator
            query = self.dataDB.dbQuery("SELECT annotator FROM FRAMES WHERE frame_number="+self.frameBox.text()+" AND deployment_id='"+self.deployment+"'")
            current_tators, =query.first()
            if current_tators==None:
                current_tators=''
            tators=current_tators.split('|')
            if not self.annotator in tators:
                # add our tator
                if len(current_tators)>0:
                    current_tators=current_tators+"|"+self.annotator
                else:
                    current_tators=self.annotator
            self.annotatorLabel.setText(current_tators)
            # draw targets
            self.activeLine[self.gvLeft]=None
            self.activeLine[self.gvRight]=None
            query = self.dataDB.dbQuery("SELECT target_number, species_group, LX, LY, RX, RY, Range, Error, Length, LHX,LHY, LTX, LTY, RHX, RHY, RTX, RTY FROM targets WHERE frame_number="+
            self.frameBox.text()+" AND deployment_id='"+self.deployment+"'", self.dataDB)
            targetToDelete=[]
            for target_number, species_group, LX, LY, RX, RY, Range, Error, Length, LHX,LHY, LTX, LTY, RHX, RHY, RTX, RTY in query:
                spcLabel=''
                if self.guiSettings['LabelSpeciesParam']>0:
                    spcLabel=species_group
                    if len(spcLabel)>self.guiSettings['LabelSpeciesParam']:
                        spcLabel=spcLabel[0:self.guiSettings['LabelSpeciesParam']]
                # find out the class and appropriate color
                if species_group in ['SceneRange',  'SceneMeasurement']:
                    col=self.guiSettings['SceneColor']
                    style='d'
                else:
                    spcInd=None
                    for btn in self.spcButtons:
                        if btn.text()==species_group:
                            spcInd=self.spcButtons.index(btn)
                            break
                    if not spcInd==None:
                        col=self.spcColors[spcInd]
                        style='o'
                    else:
                        col=self.guiSettings['SceneColor']
                        style='o'
                if RX==None and LX!=None:# this is in the left image only target
                    marker = self.gvLeft.addMark(QPointF(float(LX), float(LY)), style='+', color=col,
                                                  size=1.0, thickness=1.0, alpha=255, selectThickness=self.selThickness,  selectColor=self.selColor)

                    self.pointMarks.update({marker:[int(target_number),  self.gvLeft]})

                    marker.addLabel(target_number+" "+spcLabel, color=col,  size=self.guiSettings['LabelTextSize'], offset=self.textOffset, name='tnumber')
                    if not self.labelCheck.isChecked():
                        marker.hideLabels(None)

                elif LX==None and RX!=None:# this is in the right image only target
                    marker = self.gvRight.addMark(QPointF(float(RX), float(RY)), style='+', color=col,
                                                  size=1.0, thickness=1.0, alpha=255, selectThickness=self.selThickness,  selectColor=self.selColor)
                    
                    marker.addLabel(target_number+" "+spcLabel , color=col,  size=self.guiSettings['LabelTextSize'], offset=self.textOffset, name='tnumber')
                    self.pointMarks.update({marker:[int(target_number),  self.gvRight]})
                    if not self.labelCheck.isChecked():
                        marker.hideLabels(None)
                elif RX!=None and LX!=None:# this is a stereo target

                    marker = self.gvRight.addMark(QPointF(float(RX), float(RY)), style=style, color=col,
                                                  size=1.0, thickness=1.0, alpha=255, selectThickness=self.selThickness,  selectColor=self.selColor)
                    self.pointMarks.update({marker:[int(target_number),  self.gvRight]})
                    marker.addLabel(target_number+" "+spcLabel , color=col,  size=self.guiSettings['LabelTextSize'], offset=self.textOffset, name='tnumber')
                    if not self.labelCheck.isChecked():
                        marker.hideLabels(None)
                    marker = self.gvLeft.addMark(QPointF(float(LX), float(LY)), style=style, color=col,
                                                  size=1.0, thickness=1.0, alpha=255, selectThickness=self.selThickness,  selectColor=self.selColor)
                    self.pointMarks.update({marker:[int(target_number),  self.gvLeft]})
                    targetLabel=target_number +" r = "+str(round(float(Range), 2))+"  e = "+str(round(float(Error), 2))
                    if self.guiSettings['ShowClassOnLabel']=='true':
                        targetLabel=targetLabel+' '+species_group
                    marker.addLabel(targetLabel+" "+spcLabel, color=col,size=self.guiSettings['LabelTextSize'], offset=self.textOffset, name='tnumber')
                    if not self.labelCheck.isChecked():
                        marker.hideLabels(None)
                # put on measurements as well
                if not LHX==None: #line
                    if species_group == 'SceneMeasurement':  #this is a line only object
                        col=self.guiSettings['SceneColor']
                    else:# this is a measurement line associated with a target
                        col=self.guiSettings['TargetLineColor']
    #                print(query.value(2).toString())
                    stPoint=QPointF(float(LHX), float(LHY))
                    endPoint=QPointF(float(LTX), float(LTY))
                    if stPoint==endPoint:# this will be prevented in the future!
                        QMessageBox.warning(self, "ERROR", "This Target has a dimension line that starts and ends at the same point, which is an Error.  The target will be deleted.")
                        targetToDelete.append(target_number)
                        continue
                    lineObjsL=self.gvLeft.addDimensionLine(stPoint,endPoint, taillength=self.guiSettings['MeasureLineTailLength'], thickness=self.guiSettings['MeasureLineWidth'],  color=col)
                    self.lineMarks.update({lineObjsL:[int(target_number),  self.gvLeft]})
                    # right image
                    stPoint=QPointF(float(RHX), float(RHY))
                    endPoint=QPointF(float(RTX), float(RTY))
                    if stPoint==endPoint:# this will be prevented in the future!
                        QMessageBox.warning(self, "ERROR", "This Target has a dimension line that starts and ends at the same point, which is an Error.  The target will be deleted.")
                        targetToDelete.append(target_number)
                        continue
                    lineObjs=self.gvRight.addDimensionLine(stPoint,endPoint, taillength=self.guiSettings['MeasureLineTailLength'], thickness=self.guiSettings['MeasureLineWidth'], color=col)
                    self.lineMarks.update({lineObjs:[int(target_number),  self.gvRight]})
                    lineObjsL.addLabel(QPointF(float(LHX), float(LHY)), "l = "+str(round(float(Length), 2))+" e = "+str(round(float(Error), 2)), color=col,  size=self.guiSettings['LabelTextSize'])
                    if not self.labelCheck.isChecked():
                        lineObjsL.hideLabels(None)
                        

                    
            # delete bad target (temporary)
            for t in targetToDelete:
                self.dataDB.dbExec("DELETE FROM targets WHERE frame_number="+self.frameBox.text()+" AND target_number="+t+"  AND deployment_ID='"+self.deployment+"'", self.dataDB)
            # relod frame metadata
            if self.settings['CollectMetadata'].lower()=='true' or self.settings['CollectMetadata'].lower()=='yes':
                if 'ExclusiveRadioBox1' in self.metadataTypesDict:
                    query = self.dataDB.dbQuery("SELECT metadata_tag, metadata_value FROM FRAME_METADATA WHERE frame_number="+
                    self.frameBox.text()+" AND metadata_group='"+self.metadataGroup+"' AND metadata_type='"+self.metadataTypesDict['ExclusiveRadioBox1']+"' AND deployment_id='"+self.deployment+"'", self.dataDB)
                    # this should be only one
                    radioBtnTag1,  val=query.first()
                    if radioBtnTag1:
                        for tag in self.radioBtnTags1:
                            if tag.text()==radioBtnTag1:
                                tag.setChecked(True)
                                
                if 'ExclusiveRadioBox2' in self.metadataTypesDict:
                    query = self.dataDB.dbQuery("SELECT metadata_tag, metadata_value FROM FRAME_METADATA WHERE frame_number="+
                    self.frameBox.text()+" AND metadata_group='"+self.metadataGroup+"' AND metadata_type='"+self.metadataTypesDict['ExclusiveRadioBox2']+"' AND deployment_id='"+self.deployment+"'", self.dataDB)
                    # this should be only one
                    radioBtnTag2,  val=query.first()
                    if radioBtnTag2:
                        for tag in self.radioBtnTags2:
                            if tag.text()==radioBtnTag2:
                                tag.setChecked(True)
                                
                if 'ExclusiveRadioBox3' in self.metadataTypesDict:
                    query = self.dataDB.dbQuery("SELECT metadata_tag, metadata_value FROM FRAME_METADATA WHERE frame_number="+
                    self.frameBox.text()+" AND metadata_group='"+self.metadataGroup+"' AND metadata_type='"+self.metadataTypesDict['ExclusiveRadioBox3']+"' AND deployment_id='"+self.deployment+"'", self.dataDB)
                    # this should be only one
                    radioBtnTag3,  val=query.first()
                    if radioBtnTag3:
                        for tag in self.radioBtnTags3:
                            if tag.text()==radioBtnTag3:
                                tag.setChecked(True)
                                
                if 'LineEdit' in self.metadataTypesDict:
                    query = self.dataDB.dbQuery("SELECT metadata_tag, metadata_value FROM FRAME_METADATA WHERE frame_number="+
                    self.frameBox.text()+" AND metadata_group='"+self.metadataGroup+"' AND metadata_type='"+self.metadataTypesDict['LineEdit']+"' AND deployment_id='"+self.deployment+"'", self.dataDB)
                    for lineEditTag,  val in query:
                        if lineEditTag:
                            for i in list(range(len(self.metadataLineEditLabels))):
                                if self.metadataLineEditLabels[i].text()==lineEditTag:
                                    self.metadataLineEdits[i].setText(val)
                                    
                if 'CheckBox' in self.metadataTypesDict:
                    query = self.dataDB.dbQuery("SELECT metadata_tag, metadata_value FROM FRAME_METADATA WHERE frame_number="+
                    self.frameBox.text()+" AND metadata_group='"+self.metadataGroup+"' AND metadata_type='"+self.metadataTypesDict['CheckBox']+"' AND deployment_id='"+self.deployment+"'", self.dataDB)
                    for checkBoxTag,  val in query:
                        if checkBoxTag:
                            for i in list(range(len(self.metadataLineEditLabels))):
                                if self.metadataCheckBoxes[i].text()==checkBoxTag:
                                    if val=='Checked':
                                        self.metadataCheckBoxes[i].setChecked(True)
                                    else:
                                        self.metadataCheckBoxes[i].setChecked(False)
                if self.frameCommentDlg!= None:
                    frame=self.leftImageFrames[self.imageSlider.value()]
                    self.frameCommentDlg.showComment(str(frame))
        
    def clearAutoExclusiveRadioBtnBoxes(self):
        for rad in self.radioBtnTags1:
            rad.setAutoExclusive(False)
            rad.setChecked(False)
            rad.setAutoExclusive(True)
        for rad in self.radioBtnTags2:
            rad.setAutoExclusive(False)
            rad.setChecked(False)
            rad.setAutoExclusive(True)
        for rad in self.radioBtnTags3:
            rad.setAutoExclusive(False)
            rad.setChecked(False)
            rad.setAutoExclusive(True)


    def clearMarks(self):
        self.gvLeft.removeAllItems()
        self.gvRight.removeAllItems()
        self.lineMarks={}
        self.pointMarks={}
        self.boxMarks={}

    def copyImg(self):
        dirDlg = QFileDialog(self)
        self.deploymentPath = dirDlg.getExistingDirectory(self, 'Select Copy Location', self.__copyImageDir,
                                              QFileDialog.ShowDirsOnly)
        if self.deploymentPath !='':
            self.__copyImageDir=self.deploymentPath
            f=self.RFile.split('/')
            QFile(self.RFile).copy(self.deploymentPath+'/'+f[-1])
            f=self.LFile.split('/')
            QFile(self.LFile).copy(self.deploymentPath+'/'+f[-1])

    def changeActiveTarget(self,  target,  frame,  zoom):
        if int(frame)!=self.imageSlider.value():
            self.imageSlider.setValue(int(frame))
            self.resizeEvent(None)
        for items in self.__selectedItems:
            items.setSelected(False)
        self.__selectedItems=[]
        self.activeMark [self.gvRight]=None
        self.activeMark [self.gvLeft]=None
        for item, info in self.pointMarks.items():
            if info[0]==int(target):
                item.setSelected(True)
                self.__selectedItems.append(item)
                if info[1]==self.gvLeft:
                    self.activeMark [self.gvLeft]=item
                else:
                    self.activeMark [self.gvRight]=item
        if self.activeMark[self.gvLeft]:
            self.gvLeft.zoomToMark(self.activeMark[self.gvLeft], int(zoom))
        if self.activeMark[self.gvRight]:
            self.gvRight.zoomToMark(self.activeMark[self.gvRight], int(zoom))

#
#    def toggleClass(self, species):
#        for btn in self.spcButtons:
#            if btn.text()==species:
#                btn.setChecked(True)
#            else:
#                btn.setChecked(False)

    def calculate(self, what):
        unit=10
        if what=='point':
            xL=ny.array([[self.targetPosition[0].x()],[self.targetPosition[0].y()]])
            xR=ny.array([[self.targetPosition[1].x()],[self.targetPosition[1].y()]])
            (XL, XR)=self.stereoComp.triangulatePoint(xL, xR)
            lx=XL[0, 0]/unit
            ly=XL[2, 0]/unit
            lz=-XL[1, 0]/unit
            xLp=self.stereoComp.projectPoint(XL, 'L')
            xRp=self.stereoComp.projectPoint(XR, 'R')
            width=max(self.gvLeft.imgPixmap.width(), self.gvRight.imgPixmap.width())
            error=self.stereoComp.computeError(xL,xLp,xR,xRp)
            error=error/width*10000

            Range=round(sqrt(lx**2+ly**2+lz**2), len(str(unit)))
            self.targetStereoData=[Range, error,  lx, ly, lz]
        elif what=='line':
            lineL=self.activeLine[self.gvLeft].getLine()
            lineR=self.activeLine[self.gvRight].getLine()
            LHX=lineL.x1()
            LHY=lineL.y1()
            LTX=lineL.x2()
            LTY=lineL.y2()
            RHX=lineR.x1()
            RHY=lineR.y1()
            RTX=lineR.x2()
            RTY=lineR.y2()
            xL=ny.array([[LHX,LTX],[LHY,LTY]])
            xR=ny.array([[RHX,RTX],[RHY,RTY]])

            (XL, XR)=self.stereoComp.triangulatePoint(xL, xR)
            xLp=self.stereoComp.projectPoint(XL, 'L')
            xRp=self.stereoComp.projectPoint(XR, 'R')

            width=max(self.gvLeft.imgPixmap.width(), self.gvRight.imgPixmap.width())
            error=self.stereoComp.computeError(xL,xLp,xR,xRp)
            #error=(error/width)*10000
            lhx=XL[0, 0]/unit
            lhy=XL[2, 0]/unit
            lhz=-XL[1, 0]/unit
            ltx=XL[0, 1]/unit
            lty=XL[2, 1]/unit
            ltz=-XL[1, 1]/unit
            rhx=XR[0, 0]/unit
            rhy=XR[2, 0]/unit
            rhz=-XR[1, 0]/unit
            rtx=XR[0, 1]/unit
            rty=XR[2, 1]/unit
            rtz=-XR[1, 1]/unit
            length=round((sqrt((lhx-ltx)**2+(lhy-lty)**2+(lhz-ltz)**2)+sqrt((rhx-rtx)**2+(rhy-rty)**2+(rhz-rtz)**2))/2, len(str(unit)))
            Range=round(sqrt(((lhx+ltx/2))**2+((lhy+lty)/2)**2+((lhz+ltz)/2)**2), len(str(unit)))# range from left camera
            self.targetStereoData=[length, Range, error,  LHX, LHY,LTX,LTY, RHX, RHY,RTX,RTY,lhx, lhy, lhz,ltx,lty, ltz]

    def recompute3D(self):
        sql=("SELECT deployment_id, frame_number, target_number, LX, LY, RX, RY, LHX, LHY, LTX, LTY,  RHX, RHY, RTX, RTY FROM targets")
        try:
            self.targetPosition=[None,  None]
            from QImageViewer import QIVDimensionLine
            query = self.dataDB.dbQuery(sql)
            for deployment, frame_number, target_number, LX, LY, RX, RY, LHX, LHY, LTX, LTY,  RHX, RHY, RTX, RTY in query:
                print(frame_number,  target_number)

                if LTX==None:
                    if not LX==None and not RX==None:#stereo data only
                        self.targetPosition[0]=QPointF(float(LX), float(LY))
                        self.targetPosition[1]=QPointF(float(RX), float(RY))
                        self.calculate('point')
                        #self.targetStereoData=[range, error,  lx, ly, lz]
                        sql=("UPDATE targets SET Range = "+str(self.targetStereoData[0])+",  Error = "+str(self.targetStereoData[1])+",  hx = "+
                        str(self.targetStereoData[2])+",  hy = "+str(self.targetStereoData[3])+",  hz = "+str(self.targetStereoData[4])+" WHERE frame_number = "+
                        frame_number+" AND target_number="+target_number)
                        self.dataDB.dbExec(sql)
                else:
                    dimLine = QIVDimensionLine.QIVDimensionLine(startPoint=QPointF(float(LHX), float(LHY)), endPoint=QPointF(float(LTX), float(LTY)), color=self.guiSettings['TargetLineColor'],
                                        thickness=self.guiSettings['MeasureLineWidth'], alpha=255, linestyle='-',
                                        taillength=self.guiSettings['MeasureLineTailLength'], view=self.gvLeft)
                    self.activeLine[self.gvLeft] = dimLine
                    dimLine = QIVDimensionLine.QIVDimensionLine(startPoint=QPointF(float(RHX), float(RHY)), endPoint=QPointF(float(RTX), float(RTY)), color=self.guiSettings['TargetLineColor'],
                                        thickness=self.guiSettings['MeasureLineWidth'], alpha=255, linestyle='-',
                                        taillength=self.guiSettings['MeasureLineTailLength'], view=self.gvRight)
                    self.activeLine[self.gvRight] = dimLine
                    self.calculate('line')
                    #self.targetStereoData=[length, range, error,  LHX, LHY,LTX,LTY, RHX, RHY,RTX,RTY,lhx, lhy, lhz,ltx,lty, ltz]
                    self.dataDB.dbExec("UPDATE targets SET Length = "+str(self.targetStereoData[0])+", Range = "+str(self.targetStereoData[1])+",  Error = "+str(self.targetStereoData[2])+",  hx = "+
                    str(self.targetStereoData[11])+",  hy = "+str(self.targetStereoData[12])+",  hz = "+str(self.targetStereoData[13])+", tx = "+
                    str(self.targetStereoData[14])+", ty = "+str(self.targetStereoData[15])+", tz = "+str(self.targetStereoData[16])+" WHERE frame_number = "+
                    frame_number+" AND target_number="+target_number)
            QMessageBox.warning(self, "INFO", "Positions have been recalculated :-)")
            self.__changeImage()
        except:
            self.showError()
            
    def checkBoxAction(self):
        if self.sender()==self.closeupCheck:
            if self.closeupCheck.isChecked():
                position = self.appSettings.value('zoomwinposition', QPoint(10,10))
                #self.closeup.move(position)
                self.closeup.show()
            else:
                self.appSettings.setValue('zoomwinposition', self.closeup.pos())
                self.closeup.hide()
        elif self.sender()==self.showDataCheck:
            if self.showDataCheck.isChecked():
                position = self.appSettings.value('datawinposition', QPoint(10,10))
                #self.datadlg.move(position)
                self.datadlg.show()
                self.datadlg.refreshView()
            else:
                self.appSettings.setValue('datawinposition', self.datadlg.pos())
                self.datadlg.hide()
        elif self.sender()==self.labelCheck:
            if self.labelCheck.isChecked():
                for mark,  x in self.pointMarks.items():
                    mark.showLabels(None)
                for line,  x in self.lineMarks.items():
                    line.showLabels(None)

            else:
                for mark,  x in self.pointMarks.items():
                    mark.hideLabels(None)
                for line,  x in self.lineMarks.items():
                    line.hideLabels(None)
                    
    def gridBoxAction(self):

        if self.gridCheck.isChecked(): # we are adding grid
            self.showGrid()
        else:
            self.clearGridAndSave()
            
    def showGrid(self):
        if self.activeGV=='Right':# figure out which gv is up
            gvObj=self.gvRight
        else:
            gvObj=self.gvLeft
        # check to see if we already have data with a grid here
        query=self.dataDB.dbQuery("SELECT metadata_value FROM FRAME_METADATA WHERE frame_number="+self.frameBox.text()+\
        " AND metadata_group='CountingGridInformation' AND metadata_tag='1' AND metadata_type='GridSize' AND deployment_id='"+self.deployment+"'")
        gridsize=query.first()[0]# we may have an existing grid we collected data with
        if not gridsize:# first grid in this frame
            self.randomCell=None
            self.gridCount=1
            gridsize=self.gridSetup['GridSize']
        else: # get random square previously used
            if gridsize==self.gridSetup['GridSize']:# if grid size is same, reload previous grid
                query=self.dataDB.dbQuery("SELECT metadata_value FROM FRAME_METADATA WHERE frame_number="+self.frameBox.text()+\
                " AND metadata_group='CountingGridInformation' AND metadata_tag='1' AND metadata_type='RandomCell' AND deployment_id='"+self.deployment+"'")
                if query.first()[0]=='None':
                    self.randomCell=None
                else:
                    self.randomCell=int(query.first()[0])
                query=self.dataDB.dbQuery("SELECT metadata_tag FROM FRAME_METADATA WHERE frame_number="+self.frameBox.text()+\
                " AND metadata_group='CountingGridInformation' AND metadata_type='GridSize' AND metadata_value='"+gridsize+"' AND deployment_id='"+self.deployment+"'")
                self.gridCount=int(query.first()[0])
            else:
                # this is a new grid with a different size!
                self.randomCell=None
                query=self.dataDB.dbQuery("SELECT metadata_tag FROM FRAME_METADATA WHERE frame_number="+self.frameBox.text()+\
                " AND metadata_group='CountingGridInformation' AND deployment_id='"+self.deployment+"' GROUP BY metadata_tag")
                grids=[]
                for grid,  in query:
                    grids.append(int(grid))
                self.gridCount=max(grids)+1
                gridsize=self.gridSetup['GridSize']
                self.speciesInGrid=set()
                
        x=gvObj.imgPixmap.width()
        y=gvObj.imgPixmap.height()
        if gridsize=='1x2':# vertical slip in two
            vLine1 = gvObj.addDimensionLine(QPointF(x/2, 0), QPointF(x/2, y), color=self.gridSetup['GridLineColor'],
                                thickness=self.gridSetup['GridLineThickness'], alpha=255, linestyle=self.gridSetup['GridLineStyle'], taillength=0)

            self.gridLines[gvObj] = [vLine1]

        elif gridsize=='2x2':# vertical & horizontal slip in two
            vLine1 = gvObj.addDimensionLine(QPointF(x/2, 0), QPointF(x/2, y), color=self.gridSetup['GridLineColor'],
                                thickness=self.gridSetup['GridLineThickness'], alpha=255, linestyle=self.gridSetup['GridLineStyle'], taillength=0)
            hLine1 = gvObj.addDimensionLine(QPointF(0, y/2), QPointF(x, y/2), color=self.gridSetup['GridLineColor'],
                                thickness=self.gridSetup['GridLineThickness'], alpha=255, linestyle=self.gridSetup['GridLineStyle'], taillength=0)

            self.gridLines[gvObj] = [vLine1, hLine1]
        elif gridsize=='2x3':# same as previous vertical slip in three
            vLine1 = gvObj.addDimensionLine(QPointF(x/3, 0), QPointF(x/3, y), color=self.gridSetup['GridLineColor'],
                                thickness=self.gridSetup['GridLineThickness'], alpha=255, linestyle=self.gridSetup['GridLineStyle'], taillength=0)
            vLine2 = gvObj.addDimensionLine(QPointF(2*x/3, 0), QPointF(2*x/3, y), color=self.gridSetup['GridLineColor'],
                                thickness=self.gridSetup['GridLineThickness'], alpha=255, linestyle=self.gridSetup['GridLineStyle'], taillength=0)
            hLine1 = gvObj.addDimensionLine(QPointF(0, y/2), QPointF(x, y/2), color=self.gridSetup['GridLineColor'],
                                thickness=self.gridSetup['GridLineThickness'], alpha=255, linestyle=self.gridSetup['GridLineStyle'], taillength=0)

            self.gridLines[gvObj] = [vLine1, vLine2,  hLine1]
        elif gridsize=='3x3':# horizontal and vertical slip in three
            vLine1 = gvObj.addDimensionLine(QPointF(x/3, 0), QPointF(x/3, y), color=self.gridSetup['GridLineColor'],
                                thickness=self.gridSetup['GridLineThickness'], alpha=255, linestyle=self.gridSetup['GridLineStyle'], taillength=0)
            vLine2 = gvObj.addDimensionLine(QPointF(2*x/3, 0), QPointF(2*x/3, y), color=self.gridSetup['GridLineColor'],
                                thickness=self.gridSetup['GridLineThickness'], alpha=255, linestyle=self.gridSetup['GridLineStyle'], taillength=0)
            hLine1 = gvObj.addDimensionLine(QPointF(0, y/3), QPointF(x, y/3), color=self.gridSetup['GridLineColor'],
                                thickness=self.gridSetup['GridLineThickness'], alpha=255, linestyle=self.gridSetup['GridLineStyle'], taillength=0)
            hLine2 = gvObj.addDimensionLine(QPointF(0, 2*y/3), QPointF(x, 2*y/3), color=self.gridSetup['GridLineColor'],
                                thickness=self.gridSetup['GridLineThickness'], alpha=255, linestyle=self.gridSetup['GridLineStyle'], taillength=0)

            self.gridLines[gvObj] = [vLine1, vLine2,  hLine1,  hLine2]
        if self.gridSetup['RandomizeCell']:
            self.lightupRandomCell(gridsize)
        else:
            self.randomCellLines[gvObj]=None
            self.randomCell=None
                
    def clearGridAndSave(self):
        if self.activeGV=='Right':# figure out which gv is up
            gvObj=self.gvRight
        else:
            gvObj=self.gvLeft
        # write data, if any
        if len(self.speciesInGrid)>0:
            self.writeGridDetailsToMetadata()
            self.speciesInGrid=set()
        # remove lines
        for lineObj in self.gridLines[gvObj]:
            gvObj.removeItem(lineObj)
        if self.randomCellLines[gvObj]:
            gvObj.removeItem(self.randomCellLines[gvObj])
            self.randomCell=None
            
    def lightupRandomCell(self,  gridsize):
        if self.activeGV=='Right':# figure out which gv is up
            gvObj=self.gvRight
        else:
            gvObj=self.gvLeft
        # delete any prevuious random grid
        gvObj.removeItem(self.randomCellLines[gvObj])
        x=gvObj.imgPixmap.width()
        y=gvObj.imgPixmap.height()
        self.randomCellBounds=[0, x, 0, y]
        if gridsize=='1x2':# vertical slip in two
            # get a random box
            if not self.randomCell:
                self.randomCell=random.randrange(2)
            if self.randomCell==0:#clockwise from top left
                verts=[QPointF(0, y), QPointF(0, 0), QPointF(x/2, 0), QPointF(x/2, y)]
                self.randomCellBounds=[0, x/2, 0, y]
            else:
                verts=[QPointF(x/2, 0), QPointF(x/2, y), QPointF(x, y), QPointF(x, 0)]
                self.randomCellBounds=[x/2, x,  0, y]
                
        elif gridsize=='2x2':# vertical & horizontal slip in two\
            # get a random self.randomCell
            if not self.randomCell:
                self.randomCell=random.randrange(4)
            if self.randomCell==0:#row order from top left
                verts=[QPointF(0, y/2), QPointF(0, 0), QPointF(x/2, 0), QPointF(x/2, y/2)]
                self.randomCellBounds=[0, x/2, 0, y/2]
            elif self.randomCell==1:
                verts=[QPointF(x/2, y/2), QPointF(x/2, 0), QPointF(x, 0), QPointF(x, y/2)]
                self.randomCellBounds=[x/2, x, 0, y/2]
            elif self.randomCell==2:
                verts=[QPointF(0, y/2), QPointF(0, y), QPointF(x/2, y), QPointF(x/2, y/2)]
                self.randomCellBounds=[0, x/2, y/2, y ]
            else:
                verts=[QPointF(x/2, y/2), QPointF(x/2, y), QPointF(x, y), QPointF(x, y/2)]
                self.randomCellBounds=[x/2, x, y/2,  y]
                
        elif gridsize=='2x3':# same as previous vertical slip in three
            # get a random self.randomCell
            if not self.randomCell:
                self.randomCell=random.randrange(6)
            if self.randomCell==0:#row order from top left
                verts=[QPointF(0, y/2), QPointF(0, 0), QPointF(x/3, 0), QPointF(x/3, y/2)]
                self.randomCellBounds=[0, x/3, 0, y/2]
            elif self.randomCell==1:
                verts=[QPointF(x/3, y/2), QPointF(x/3, 0), QPointF(2*x/3, 0), QPointF(2*x/3, y/2)]
                self.randomCellBounds=[x/3, 2*x/3, 0, y/2]
            elif self.randomCell==2:
                verts=[QPointF(2*x/3, y/2), QPointF(2*x/3, 0), QPointF(x, 0), QPointF(x,  y/2)]
                self.randomCellBounds=[2*x/3, x, 0, y/2]
            elif self.randomCell==3:
                verts=[QPointF(0, y), QPointF(0, y/2), QPointF(x/3, y/2), QPointF(x/3, y)]
                self.randomCellBounds=[0, x/3, y/2, y]
            elif self.randomCell==4:
                verts=[QPointF(x/3, y), QPointF(x/3,  y/2), QPointF(2*x/3,  y/2), QPointF(2*x/3, y)]
                self.randomCellBounds=[x/3,2*x/3,  y/2, y]
            elif self.randomCell==5:
                verts=[QPointF(2*x/3, y), QPointF(2*x/3,  y/2), QPointF(x,  y/2), QPointF(x,  y)]
                self.randomCellBounds=[2*x/3,x,  y/2, y]
                
        elif gridsize=='3x3':# same as previous vertical slip in three
            # get a random self.randomCell
            if not self.randomCell:
                self.randomCell=random.randrange(9)
            if self.randomCell==0:#clockwise from top left
                verts=[QPointF(0, y/3), QPointF(0, 0), QPointF(x/3, 0), QPointF(x/3, y/3)]
                self.randomCellBounds=[0,x/3, 0,  y/3]
            elif self.randomCell==1:
                verts=[QPointF(x/3, y/3), QPointF(x/3, 0), QPointF(2*x/3, 0), QPointF(2*x/3, y/3)]
                self.randomCellBounds=[x/3, 2*x/3,  0,  y/3]
            elif self.randomCell==2:
                verts=[QPointF(2*x/3, y/3), QPointF(2*x/3, 0), QPointF(x, 0), QPointF(x, y/3)]
                self.randomCellBounds=[2*x/3, x,  0,  y/3]
            elif self.randomCell==3:
                verts=[QPointF(0, 2*y/3), QPointF(0, y/3), QPointF(x/3, y/3), QPointF(x/3, 2*y/3)]
                self.randomCellBounds=[0,x/3, y/3, 2*y/3]
            elif self.randomCell==4:
                verts=[QPointF(x/3, 2*y/3), QPointF(x/3, y/3), QPointF(2*x/3, y/3), QPointF(2*x/3, 2*y/3)]
                self.randomCellBounds=[x/3,2*x/3,  y/3, 2*y/3]
            elif self.randomCell==5:
                verts=[QPointF(2*x/3, 2*y/3), QPointF(2*x/3, y/3), QPointF(x, y/3), QPointF(x, 2*y/3)]
                self.randomCellBounds=[2*x/3, x,  y/3, 2*y/3]
            elif self.randomCell==6:
                verts=[QPointF(0, y), QPointF(0, 2*y/3), QPointF(x/3, 2*y/3), QPointF(x/3,y)]
                self.randomCellBounds=[0, x/3,  2*y/3, y]
            elif self.randomCell==7:
                verts=[QPointF(x/3, y), QPointF(x/3, 2*y/3), QPointF(2*x/3, 2*y/3), QPointF(2*x/3, y)]
                self.randomCellBounds=[x/3, 2*x/3,  2*y/3, y]
            else:
                verts=[QPointF(2*x/3, y), QPointF(2*x/3, 2*y/3), QPointF(x, 2*y/3), QPointF(x, y)]
                self.randomCellBounds=[2*x/3, x, 2*y/3, y]
                
        randBoxObj = gvObj.addPolygon(verts, color=self.gridSetup['CellLineColor'],
                                thickness=self.gridSetup['GridLineThickness']*2, alpha=255, linestyle='_')
        self.randomCellLines[gvObj] = randBoxObj
        
    def writeGridDetailsToMetadata(self):
        # check to see if this size grid is already in
        query=self.dataDB.dbQuery("SELECT metadata_value FROM FRAME_METADATA WHERE frame_number="+self.frameBox.text()+\
        " AND metadata_group='CountingGridInformation' AND metadata_tag='1' AND metadata_type='GridSize' AND deployment_id='"+self.deployment+"'")
        gridsize=query.first()[0]# we may have an existing grid we collected data with
        if gridsize==self.gridSetup['GridSize']:# this size grid already exists for this frame, update species list?
            query=self.dataDB.dbQuery("SELECT metadata_value FROM FRAME_METADATA WHERE frame_number="+self.frameBox.text()+\
            " AND metadata_group='CountingGridInformation' AND metadata_tag='1' AND metadata_type='SpeciesInGrid' AND deployment_id='"+self.deployment+"'")
            spc_list=query.first()[0].split(";")# we may have an existing grid we collected data with
            for spc in spc_list:
                self.speciesInGrid.add(spc)
            # update species list if user added more counts
            self.dataDB.dbExec("UPDATE FRAME_METADATA SET metadata_value = '"+";".join(self.speciesInGrid)+"' WHERE frame_number="+self.frameBox.text()+\
            " AND metadata_group = 'CountingGridInformation'"+
             "AND metadata_type='SpeciesInGrid' AND metadata_tag='"+str(self.gridCount)+"' AND deployment_id='"+self.deployment+"'")
        else: # new grid, need to write everything
            self.dataDB.dbExec("INSERT INTO FRAME_METADATA (project,deployment_ID, frame_number, metadata_group, metadata_tag, metadata_type, metadata_value, annotator)"+
                                " VALUES('"+self.activeProject+"','"+self.deployment+"',"+self.frameBox.text()+",'CountingGridInformation','"+str(self.gridCount)+"','GridSize','"+
                                self.gridSetup['GridSize']+"','"+self.annotator+"')")
            self.dataDB.dbExec("INSERT INTO FRAME_METADATA (project,deployment_ID, frame_number, metadata_group, metadata_tag, metadata_type, metadata_value, annotator)"+
                                " VALUES('"+self.activeProject+"','"+self.deployment+"',"+self.frameBox.text()+",'CountingGridInformation','"+str(self.gridCount)+"','SpeciesInGrid','"+
                                ";".join(self.speciesInGrid)+"','"+self.annotator+"')")
            self.dataDB.dbExec("INSERT INTO FRAME_METADATA (project,deployment_ID, frame_number, metadata_group, metadata_tag, metadata_type, metadata_value, annotator)"+
                                " VALUES('"+self.activeProject+"','"+self.deployment+"',"+self.frameBox.text()+",'CountingGridInformation','"+str(self.gridCount)+"','RandomCell','"+
                                str(self.randomCell)+"','"+self.annotator+"')")
            self.dataDB.dbExec("INSERT INTO FRAME_METADATA (project,deployment_ID, frame_number, metadata_group, metadata_tag, metadata_type, metadata_value, annotator)"+
                                " VALUES('"+self.activeProject+"','"+self.deployment+"',"+self.frameBox.text()+",'CountingGridInformation','"+str(self.gridCount)+"','CameraUsed','"+
                                self.activeGV+"','"+self.annotator+"')")
            vals=self.gridSetup['GridSize'].split('x')
            self.dataDB.dbExec("INSERT INTO FRAME_METADATA (project, deployment_ID, frame_number, metadata_group, metadata_tag, metadata_type, metadata_value, annotator)"+
                                " VALUES('"+self.activeProject+"','"+self.deployment+"',"+self.frameBox.text()+",'CountingGridInformation','"+str(self.gridCount)+"','ScalingFactor','"+
                                str(int(vals[0])*int(vals[1]))+"','"+self.annotator+"')")

    def clearGridData(self):
        reply=QMessageBox.warning(self, "WARNING", "Sure you want to delete the grid data for this frame?",  QMessageBox.Yes, QMessageBox.No)
        if reply==QMessageBox.Yes:
            self.gridCheck.setChecked(False)
            self.dataDB.dbExec("DELETE FROM FRAME_METADATA WHERE frame_number="+self.frameBox.text()+" AND deployment_ID='"+self.deployment+"' AND metadata_group='CountingGridInformation'")
            self.gridBoxAction()

    def writeDatatoCSV(self):
        if not self.dataDB:
            return
        import pandas as pd
        import sqlite3
        try:
            conn = sqlite3.connect(self.dataPath + self.activeProject+'_' + self.deployment+'.db', isolation_level=None,detect_types=sqlite3.PARSE_COLNAMES)
            db_df = pd.read_sql_query("SELECT * FROM frames WHERE  deployment_id='"+self.deployment+"'", conn)
            filename=str(self.sourcePath.path() + '/' + self.deployment + '/' + "data" + '/' + self.activeProject+'_' + self.deployment+'_frames.csv')
            db_df.to_csv(filename, index=False)
            db_df = pd.read_sql_query("SELECT * FROM targets WHERE  deployment_id='"+self.deployment+"'", conn)
            filename=str(self.sourcePath.path() + '/' + self.deployment + '/' + "data" + '/' + self.activeProject+'_' + self.deployment+'_targets.csv')
            db_df.to_csv(filename, index=False)
            db_df = pd.read_sql_query("SELECT * FROM bounding_boxes WHERE  deployment_id='"+self.deployment+"'", conn)
            filename=str(self.sourcePath.path() + '/' + self.deployment + '/' + "data" + '/' + self.activeProject+'_' + self.deployment+'_bounding_boxes.csv')
            db_df.to_csv(filename, index=False)
            db_df = pd.read_sql_query("SELECT * FROM frame_metadata WHERE  deployment_id='"+self.deployment+"'", conn)
            filename=str(self.sourcePath.path() + '/' + self.deployment + '/' + "data" + '/' + self.activeProject+'_'+ self.deployment+'_frame_metadata.csv')
            db_df.to_csv(filename, index=False)
            # write out image adjustments as well
            self.leftAdjustmentParms=self.gvLeft.adjustmentDialog.getState()
            self.rightAdjustmentParms=self.gvRight.adjustmentDialog.getState()
            imageadjustments={'left':self.leftAdjustmentParms, 'right':self.rightAdjustmentParms}
            ny.save(self.sourcePath.path() + '/' + self.deployment + '/' + "data" + '/' + self.deployment+'_image_adjustments', imageadjustments)
        except:
            self.showError()
           

    def rgbStr2Lists(self,  rgbstr):
        try:
            vals=rgbstr.split(',')
            rgblist=[int(vals[0]), int(vals[1]), int(vals[2])]
            return(rgblist)
        except:
            self.showError()
            
    def closeEvent(self, event):
        self.closeup.hide()
        if (self.datadlg):
            try:
                self.datadlg.hide()
                self.appSettings.value('datawinposition', self.datadlg.pos())
            except:
                self.showError()

        #  shut down the fetchers and accept
        self.appSettings.setValue('winposition', self.pos())
        self.appSettings.setValue('winsize', self.size())
        self.appSettings.setValue('samplerate', self.sampleRateEdit.text())
        self.appSettings.setValue('zoomwinposition', self.closeup.pos())
        self.appSettings.setValue('copyimagedir', self.__copyImageDir)
        # stash gui settings
        self.appSettings.setValue('MeasureLineTailLength',self.guiSettings['MeasureLineTailLength'])
        colstr=str(self.guiSettings['TargetLineColor'][0])+","+str(self.guiSettings['TargetLineColor'][1])+","+str(self.guiSettings['TargetLineColor'][2])
        self.appSettings.setValue('TargetLineColor', colstr)
        colstr=str(self.guiSettings['SceneColor'][0])+","+str(self.guiSettings['SceneColor'][1])+","+str(self.guiSettings['SceneColor'][2])
        self.appSettings.setValue('SceneColor', colstr)
        self.appSettings.setValue('BoxLineThickness', self.guiSettings['BoxLineThickness'])
        self.appSettings.setValue('LabelTextSize', self.guiSettings['LabelTextSize'])
        self.appSettings.setValue('LabelSpeciesParam', self.guiSettings['LabelSpeciesParam'])
        self.appSettings.setValue('ShowClassOnLabel', self.guiSettings['ShowClassOnLabel'])
        self.appSettings.setValue('DefaultMetadataSelection', self.guiSettings['DefaultMetadataSelection'])
        self.appSettings.setValue('RetainSpeciesSelection', self.guiSettings['RetainSpeciesSelection'])
        self.appSettings.setValue('PlaybackSpeedAdjust', self.guiSettings['PlaybackSpeedAdjust'])
        # stash grid settings
        self.appSettings.setValue('GridSize',self.gridSetup['GridSize'])
        colstr=str(self.gridSetup['GridLineColor'][0])+","+str(self.gridSetup['GridLineColor'][1])+","+str(self.gridSetup['GridLineColor'][2])
        self.appSettings.setValue('GridLineColor', colstr)
        colstr=str(self.gridSetup['CellLineColor'][0])+","+str(self.gridSetup['CellLineColor'][1])+","+str(self.gridSetup['CellLineColor'][2])
        self.appSettings.setValue('CellLineColor', colstr)
        self.appSettings.setValue('RandomizeCell', str(self.gridSetup['RandomizeCell']))
        self.appSettings.setValue('PersistentGrid', str(self.gridSetup['PersistentGrid']))
        self.appSettings.setValue('CellBoundary', str(self.gridSetup['CellBoundary']))
        self.appSettings.setValue('GridLineStyle', self.gridSetup['GridLineStyle'])
        self.appSettings.setValue('GridLineThickness', str(self.gridSetup['GridLineThickness']))

        # write out excel file from db
        if self.appDB:
            self.appDB.dbClose()
        if self.dataDB:
            self.writeFrameData()
            self.dataDB.dbClose()
            self.writeDatatoCSV()
        event.accept()


class textBoxFilter(QObject):
    '''
    textBoxFilter is a simple Qt Event filter that diverts Left and Right arrow key presses
    and passes them onto a different event handler as specified in "action".
    '''
    def __init__(self, action, parent=None):
        super(textBoxFilter, self).__init__(parent)
        self.action = action

    def eventFilter(self, obj, event):
        if (event.type() == QEvent.KeyPress) and ((event.key()==Qt.Key_Left) or (event.key()==Qt.Key_Right)):
            #  eat the enter key press
            self.action(None, event)
            return True
        else:
            # not an enter key press - pass along
            return QObject.eventFilter(self, obj, event)


if __name__ == "__main__":

    app = QApplication(sys.argv)
    form = SEBASTES()
    form.show()
    app.exec_()


