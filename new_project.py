#!/usr/bin/python3
# *-* coding: utf-8 *-*

import os
import sys
import setproctitle
import uuid
import subprocess
import shlex

from PyQt5 import QtCore, uic, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QTreeView, QFileSystemModel, QVBoxLayout, QWidget, QHBoxLayout, QListView
from PyQt5.QtWidgets import QListWidgetItem, QShortcut
from PyQt5.QtGui import QKeySequence
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

import rbhus_clone_db
import debug

projDir = os.sep.join(os.path.abspath(__file__).split(os.sep)[:-1])
sys.path.append(projDir)

main_ui_file = os.path.join(projDir, "new_project.ui")

root_folder = "/home/sanath.shetty/Documents/rbhus_clone_root/"
template_folder = root_folder+"template/"


class newProject():
    db = rbhus_clone_db.db()
    def __init__(self):
       
        self.main_ui = uic.loadUi(main_ui_file)
        self.main_ui.setWindowTitle("NEW PROJECT")

        self.setUsers()
        self.main_ui.draftBox.stateChanged.connect(lambda x : self.updateAssetsBox())
        self.main_ui.correctionsBox.stateChanged.connect(lambda x : self.updateAssetsBox())
        self.main_ui.finalBox.stateChanged.connect(lambda x : self.updateAssetsBox())
        self.main_ui.saveButt.clicked.connect(lambda x : self.createProject())

        #Show Window
        self.main_ui.show()
        self.main_ui.update()

        qtRectangle = self.main_ui.frameGeometry()
        centerPoint = QtWidgets.QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.main_ui.move(qtRectangle.topLeft())

    def setUsers(self):
        queryUsers = "select * from users"
        assets = self.db.execute(queryUsers,dictionary=True)
        users = [x['name'] for x in assets]
        debug.info(users)
        self.main_ui.userBox.addItems(users)

    def updateAssetsBox(self):
        text = ''
        if self.main_ui.draftBox.isChecked():
            text += self.main_ui.draftBox.text() + ','
        if self.main_ui.correctionsBox.isChecked():
            text += self.main_ui.correctionsBox.text() + ','
        if self.main_ui.finalBox.isChecked():
            text += self.main_ui.finalBox.text() + ','
        self.main_ui.assetsBox.setText(text.strip())

    def createProject(self):
        projName = self.main_ui.nameBox.text()
        debug.info(projName)
        if projName:
            assetNames = [ass for ass in self.main_ui.assetsBox.text().split(',') if ass]
            debug.info(assetNames)
            if assetNames:
                user = self.main_ui.userBox.currentText()
                debug.info(user)
                if user:
                    projUpdateQuery = "insert into projects (projName) values (\"{0}\") ".format(projName)
                    updateProjList = self.db.execute(projUpdateQuery)
                    if updateProjList == 1:
                        debug.info("Updated proj list")
                        for ass in assetNames:
                            assID = str(uuid.uuid4())
                            debug.info(assID)
                            folder_path = root_folder+projName+os.sep+ass
                            debug.info(folder_path)
                            createAssetQuery = "insert into assets (assID, projName, assetName, path, assignedUser) values (\"{0}\",\"{1}\",\"{2}\",\"{3}\",\"{4}\") ".format(assID, projName, ass, folder_path, user)
                            debug.info(createAssetQuery)
                            updateAssList = self.db.execute(createAssetQuery)
                            if updateAssList == 1:
                                os.makedirs(folder_path, exist_ok=True)
                                if ass == "draft":
                                    pasteCmd = "rsync -azHXW --info=progress2 \"{0}\" \"{1}\" ".format(template_folder+"draft.docx",folder_path)
                                    subprocess.run(shlex.split(pasteCmd))
                        self.main_ui.close()
                    else:
                        debug.info("Project not created")          
                else:
                    debug.info("Please select an user")
            else:
                debug.info("Please select an asset")
        else:
            debug.info("Please provide a project name")

if __name__ == '__main__':
    setproctitle.setproctitle("RBHUS_CLONE")
    app = QtWidgets.QApplication(sys.argv)
    window = newProject()
    sys.exit(app.exec_())
