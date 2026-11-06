#!/usr/bin/env python
# Copyright (c) 2007-8 Qtrac Ltd. All rights reserved.
# This program or module is free software: you can redistribute it and/or
# modify it under the terms of the GNU General Public License as published
# by the Free Software Foundation, either version 2 of the License, or
# version 3 of the License, or (at your option) any later version. It is
# provided for educational purposes and is distributed in the hope that
# it will be useful, but WITHOUT ANY WARRANTY; without even the implied
# warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See
# the GNU General Public License for more details.

import os
import platform
import stat
import sys

from PySide6.QtGui import *
from PySide6.QtCore import *
from PySide6.QtWidgets import *


__version__ = "3.0.0"


class OptionsForm(QDialog):

    def __init__(self, parent=None):
        super(OptionsForm, self).__init__(parent)

        settings = QSettings('afsc.noaa.gov','makepySide6')
        pyuic6Label = QLabel("pyuic6")
        self.pyuic6Label = QLabel(settings.value("pyuic6", PYUIC6))
        self.pyuic6Label.setFrameStyle(QFrame.Shape.StyledPanel|QFrame.Shadow.Sunken)
        pyuic6Button = QPushButton("py&uic6...")
        pylupdate6Label = QLabel("pylupdate6")
        self.pylupdate6Label = QLabel(settings.value("pylupdate6",PYLUPDATE6))
        self.pylupdate6Label.setFrameStyle(QFrame.Shape.StyledPanel|QFrame.Shadow.Sunken)
        pylupdate6Button = QPushButton("py&lupdate6...")
        lreleaseLabel = QLabel("lrelease")
        self.lreleaseLabel = QLabel(settings.value("lrelease","lrelease"))
        self.lreleaseLabel.setFrameStyle(QFrame.Shape.StyledPanel|QFrame.Shadow.Sunken)
        lreleaseButton = QPushButton("l&release...")

        buttonBox = QDialogButtonBox(QDialogButtonBox.StandardButton.Ok|
                                     QDialogButtonBox.StandardButton.Cancel)

        layout = QGridLayout()
        layout.addWidget(pyuic6Label, 0, 0)
        layout.addWidget(self.pyuic6Label, 0, 1)
        layout.addWidget(pyuic6Button, 0, 2)
        layout.addWidget(pylupdate6Label, 2, 0)
        layout.addWidget(self.pylupdate6Label, 2, 1)
        layout.addWidget(pylupdate6Button, 2, 2)
        layout.addWidget(lreleaseLabel, 3, 0)
        layout.addWidget(self.lreleaseLabel, 3, 1)
        layout.addWidget(lreleaseButton, 3, 2)
        layout.addWidget(buttonBox, 4, 0, 1, 3)
        self.setLayout(layout)

        pyuic6Button.clicked.connect(lambda: self.setPath("pyuic6"))
        pylupdate6Button.clicked.connect(lambda: self.setPath("pylupdate6"))
        lreleaseButton.clicked.connect(lambda: self.setPath("lrelease"))
        buttonBox.accepted.connect(self.accept)
        buttonBox.rejected.connect(self.reject)

        self.setWindowTitle("Make PyQt - Tool Paths")


    def accept(self):
        settings = QSettings('afsc.noaa.gov','makepySide6')
        settings.setValue("pyuic6", self.pyuic6Label.text())
        settings.setValue("pylupdate6",self.pylupdate6Label.text())
        settings.setValue("lrelease", self.lreleaseLabel.text())
        QDialog.accept(self)


    def setPath(self, tool):
        if tool == "pyuic6":
            label = self.pyuic6Label
        elif tool == "pylupdate6":
            label = self.pylupdate6Label
        elif tool == "lrelease":
            label = self.lreleaseLabel
        path = QFileDialog.getOpenFileName(self, "Make PyQt - Set Tool Path", label.text())
        if path:
            label.setText(QDir.toNativeSeparators(path[0]))


class Form(QMainWindow):

    def __init__(self):
        super(Form, self).__init__(None)

        pathLabel = QLabel("Path:")
        self.pathLabel = QLabel(sys.argv[1] \
                if len(sys.argv) > 1 and os.access(sys.argv[1], os.F_OK) \
                else os.getcwd())
        self.pathLabel.setFrameStyle(QFrame.Shape.StyledPanel|QFrame.Shadow.Sunken)
        self.pathLabel.setToolTip("The relative path; all actions will "
                "take place here,<br>and in this path's subdirectories "
                "if the Recurse checkbox is checked")
        self.pathButton = QPushButton("&Path...")
        self.pathButton.setToolTip(self.pathLabel.toolTip().replace(
                "The", "Sets the"))
        self.recurseCheckBox = QCheckBox("&Recurse")
        self.recurseCheckBox.setToolTip("Clean or build all the files "
                "in the path directory,<br>and all its subdirectories, "
                "as deep as they go.")
        self.transCheckBox = QCheckBox("&Translate")
        self.transCheckBox.setToolTip("Runs <b>PYLUPDATE6</b> on all "
                "<tt>.py</tt> and <tt>.pyw</tt> files in conjunction "
                "with each <tt>.ts</tt> file.<br>Then runs "
                "<b>lrelease</b> on all <tt>.ts</tt> files to produce "
                "corresponding <tt>.qm</tt> files.<br>The "
                "<tt>.ts</tt> files must have been created initially by "
                "running <b>PYLUPDATE6</b><br>directly on a <tt>.py</tt> "
                "or <tt>.pyw</tt> file using the <tt>-ts</tt> option.")
        self.debugCheckBox = QCheckBox("&Dry Run")
        self.debugCheckBox.setToolTip("Shows the actions that would "
                "take place but does not do them.")
        self.logBrowser = QTextBrowser()
        self.logBrowser.setLineWrapMode(QTextEdit.LineWrapMode.NoWrap)
        self.buttonBox = QDialogButtonBox()
        menu = QMenu(self)
        toolsAction = menu.addAction("&Tool paths...")
        aboutAction = menu.addAction("&About")
        moreButton = self.buttonBox.addButton("&More",
                QDialogButtonBox.ButtonRole.ActionRole)
        moreButton.setMenu(menu)
        moreButton.setToolTip("Use <b>More-&gt;Tool paths</b> to set the "
                "paths to the tools if they are not found by default")
        self.buildButton = self.buttonBox.addButton("&Build",
                QDialogButtonBox.ButtonRole.ActionRole)
        self.buildButton.setToolTip("Runs <b>PYUIC6</b> on all "
                "<tt>.ui</tt> "
                "files "
                "that are out-of-date.<br>Also runs <b>PYLUPDATE6</b> "
                "and <b>lrelease</b> if the Translate checkbox is "
                "checked.")
        self.cleanButton = self.buttonBox.addButton("&Clean",
                QDialogButtonBox.ButtonRole.ActionRole)
        self.cleanButton.setToolTip("Deletes all <tt>.py</tt> files that "
                "were generated from <tt>.ui</tt> and <tt>.qrc</tt> "
                "files,<br>i.e., all files matching <tt>qrc_*.py</tt> "
                " and <tt>ui_*.py.")
        quitButton = self.buttonBox.addButton("&Quit",
                QDialogButtonBox.ButtonRole.RejectRole)

        topLayout = QHBoxLayout()
        topLayout.addWidget(pathLabel)
        topLayout.addWidget(self.pathLabel, 1)
        topLayout.addWidget(self.pathButton)
        bottomLayout = QHBoxLayout()
        bottomLayout.addWidget(self.recurseCheckBox)
        bottomLayout.addWidget(self.transCheckBox)
        bottomLayout.addWidget(self.debugCheckBox)
        bottomLayout.addStretch()
        bottomLayout.addWidget(self.buttonBox)
        layout = QVBoxLayout()
        layout.addLayout(topLayout)
        layout.addWidget(self.logBrowser)
        layout.addLayout(bottomLayout)
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        aboutAction.triggered.connect(self.about)
        toolsAction.triggered.connect(self.setToolPaths)
        self.pathButton.clicked.connect(self.setPath)
        self.buildButton.clicked.connect(self.build)
        self.cleanButton.clicked.connect(self.clean)
        quitButton.clicked.connect(self.close)

        self.setWindowTitle("Make PyQt")


    def about(self):
        QMessageBox.about(self, "About Make PySide6",
                """<b>Make PySide6</b> v %s
                <p>This application, modified to work with PySide6, can be used to build PyQt
                applications.
                It runs pyuic6, pylupdate6, and lrelease as
                required, although pylupdate6 must be run directly to
                create the initial .ts files.
                <p>Python %s - Qt %s - PyQt %s on %s""" % (
                __version__, platform.python_version(),
                Qt.QT_VERSION_STR, Qt.PYQT_VERSION_STR, platform.system()))


    def setPath(self):
        path = QFileDialog.getExistingDirectory(self,
                "Make PySide - Set Path", self.pathLabel.text())
        if path:
            self.pathLabel.setText(QDir.toNativeSeparators(path))


    def setToolPaths(self):
        dlg = OptionsForm(self)
        dlg.exec()


    def build(self):
        self.updateUi(False)
        self.logBrowser.clear()
        recurse = self.recurseCheckBox.isChecked()
        path = self.pathLabel.text()
        self._apply(recurse, self._build, path)
        if self.transCheckBox.isChecked():
            self._apply(recurse, self._translate, path)
        self.updateUi(True)


    def clean(self):
        self.updateUi(False)
        self.logBrowser.clear()
        recurse = self.recurseCheckBox.isChecked()
        path = self.pathLabel.text()
        self._apply(recurse, self._clean, path)
        self.updateUi(True)


    def updateUi(self, enable):
        for widget in (self.buildButton, self.cleanButton,
                self.pathButton, self.recurseCheckBox,
                self.transCheckBox, self.debugCheckBox):
            widget.setEnabled(enable)
        if not enable:
            QApplication.setOverrideCursor(QCursor(Qt.CursorShape.WaitCursor))
        else:
            QApplication.restoreOverrideCursor()
            self.buildButton.setFocus()


    def _apply(self, recurse, function, path):
        if not recurse:
            function(path)
        else:
            for root, dirs, files in os.walk(path):
                for dir in sorted(dirs):
                    function(os.path.join(root, dir))


    def _build(self, path):
        settings = QSettings('afsc.noaa.gov','makepySide6')
        pyuic6 = settings.value("pyuic6", PYUIC6)
        prefix = self.pathLabel.text()
        if not prefix.endswith(os.sep):
            prefix += os.sep
        failed = 0
        process = QProcess()
        for name in os.listdir(path):
            source = os.path.join(path, name)
            target = None
            if source.endswith(".ui"):
                target = os.path.join(path,
                                    "ui_" + name.replace(".ui", ".py"))
                command = pyuic6
            if target is not None:
                if not os.access(target, os.F_OK) or (
                   os.stat(source)[stat.ST_MTIME] > \
                   os.stat(target)[stat.ST_MTIME]):
                    args = ["-o", target, source]
                    msg = "converted <font color=darkblue>" + source + \
                          "</font> to <font color=blue>" + target + \
                          "</font>"
                    if self.debugCheckBox.isChecked():
                        msg = "<font color=green># " + msg + "</font>"
                    else:
                        process.start(command, args)
                        if not process.waitForFinished(2 * 60 * 1000):
                            msg = "<font color=red>FAILED: %s</font>" % \
                                command
                            failed += 1
                    self.logBrowser.append(msg.replace(prefix, ""))
                else:
                    self.logBrowser.append("<font color=green>"
                            "# %s is up-to-date</font>" % \
                            source.replace(prefix, ""))
                QApplication.processEvents()
        if failed:
            QMessageBox.information(self, "Make PySide6 - Failures",
                    "Try manually setting the paths to the tools "
                    "using <b>More-&gt;Tool paths</b>")


    def _clean(self, path):
        prefix = self.pathLabel.text()
        if not prefix.endswith(os.sep):
            prefix += os.sep
        deletelist = []
        for name in os.listdir(path):
            target = os.path.join(path, name)
            source = None
            if target.endswith(".py") or target.endswith(".pyc") or \
               target.endswith(".pyo"):
                if name.startswith("ui_") and not name[-1] in "oc":
                    source = os.path.join(path, name[3:-3] + ".ui")
                elif name.startswith("qrc_"):
                    if target[-1] in "oc":
                        source = os.path.join(path, name[4:-4] + ".qrc")
                    else:
                        source = os.path.join(path, name[4:-3] + ".qrc")
                elif target[-1] in "oc":
                    source = target[:-1]
                if source is not None:
                    if os.access(source, os.F_OK):
                        if self.debugCheckBox.isChecked():
                            self.logBrowser.append("<font color=green>"
                                    "# delete %s</font>" % \
                                    target.replace(prefix, ""))
                        else:
                            deletelist.append(target)
                    else:
                        self.logBrowser.append("<font color=darkred>"
                                "will not remove "
                                "'%s' since `%s' not found</font>" % (
                                target.replace(prefix, ""),
                                source.replace(prefix, "")))
        if not self.debugCheckBox.isChecked():
            for target in deletelist:
                self.logBrowser.append("deleted "
                        "<font color=red>%s</font>" % \
                        target.replace(prefix, ""))
                os.remove(target)
                QApplication.processEvents()


    def _translate(self, path):
        prefix = self.pathLabel.text()
        if not prefix.endswith(os.sep):
            prefix += os.sep
        files = []
        tsfiles = []
        for name in os.listdir(path):
            if name.endswith((".py", ".pyw")):
                files.append(os.path.join(path, name))
            elif name.endswith(".ts"):
                tsfiles.append(os.path.join(path, name))
        if not tsfiles:
            return
        settings = QSettings()
        pylupdate6 = settings.value("pylupdate6", PYLUPDATE6)
        lrelease = settings.value("lrelease", LRELEASE)
        process = QProcess()
        failed = 0
        for ts in tsfiles:
            qm = ts[:-3] + ".qm"
            command1 = pylupdate6
            args1 = files + ["-ts", ts]
            command2 = lrelease
            args2 = ["-silent", ts, "-qm", qm]
            msg = "updated <font color=blue>%s</font>" % \
                    ts.replace(prefix, "")
            if self.debugCheckBox.isChecked():
                msg = "<font color=green># %s</font>" % msg
            else:
                process.start(command1, args1)
                if not process.waitForFinished(2 * 60 * 1000):
                    msg = "<font color=red>FAILED: %s</font>" % command1
                    failed += 1
            self.logBrowser.append(msg)
            msg = "generated <font color=blue>%s</font>" % \
                    qm.replace(prefix, "")
            if self.debugCheckBox.isChecked():
                msg = "<font color=green># %s</font>" % msg
            else:
                process.start(command2, args2)
                if not process.waitForFinished(2 * 60 * 1000):
                    msg = "<font color=red>FAILED: %s</font>" % command2
                    failed += 1
            self.logBrowser.append(msg)
            QApplication.processEvents()
        if failed:
            QMessageBox.information(self, "Make PySide6 - Failures",
                    "Try manually setting the paths to the tools "
                    "using <b>More-&gt;Tool paths</b>")


app = QApplication(sys.argv)
PATH = app.applicationDirPath()
PYUIC6 = os.path.join(PATH, "pyuic6")
PYLUPDATE6 = os.path.join(PATH, "pylupdate6")
LRELEASE = "lrelease"
if platform.system() == "Windows":
    PYUIC6 = PYUIC6.replace("/", "\\") + ".bat"
    PYLUPDATE6 = PYLUPDATE6.replace("/", "\\") + ".exe"
app.setApplicationName("Make PyQt")
form = Form()
form.show()
app.exec()


