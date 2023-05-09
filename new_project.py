#!/usr/bin/python3
# *-* coding: utf-8 *-*

import os
import sys
import setproctitle
import uuid
import subprocess
import shlex
import rbhus_clone_db
import debug

from PyQt5 import QtCore, uic, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QTreeView, QFileSystemModel, QVBoxLayout, QWidget, QHBoxLayout, QListView
from PyQt5.QtWidgets import QListWidgetItem, QShortcut
from PyQt5.QtGui import QKeySequence
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


projDir = os.sep.join(os.path.abspath(__file__).split(os.sep)[:-1])
sys.path.append(projDir)

main_ui_file = os.path.join(projDir,  "ui_files", "new_project_new.ui")

# root_folder = r"Z:\share\sanath\rbhus_clone_root"
root_folder = r"C:\Users\Dell\Documents\rbhus_clone_root"
template_folder = root_folder+os.sep+"template"

text_formats = ["docx"]
audio_formats = ["*.mp3"]

asset_and_user = {}

os.environ['QT_LOGGING_RULES'] = "qt5ct.debug=false"


class newProject():
    db = rbhus_clone_db.db()
    def __init__(self):
       
        self.main_ui = uic.loadUi(main_ui_file)
        self.main_ui.setWindowTitle("NEW PROJECT")

        self.setAssAndUser()
        # self.setUsers()
        # self.main_ui.draftBox.stateChanged.connect(lambda x : self.updateAssetsBox())
        # self.main_ui.correctionsBox.stateChanged.connect(lambda x : self.updateAssetsBox())
        # self.main_ui.finalBox.stateChanged.connect(lambda x : self.updateAssetsBox())
        self.main_ui.selectAudioButt.clicked.connect(lambda x : self.showFileDialog())
        self.main_ui.createButt.clicked.connect(lambda x : self.createProject())

        #Show Window
        self.main_ui.show()
        self.main_ui.update()

        qtRectangle = self.main_ui.frameGeometry()
        centerPoint = QtWidgets.QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.main_ui.move(qtRectangle.topLeft())

    def setAssAndUser(self):
        vLayout = QVBoxLayout(self.main_ui.assetFrame)
        
        queryAssetNames = "select * from asset_names"
        aN = self.db.execute(queryAssetNames,dictionary=True)
        asset_names = [x['name'] for x in aN]
        debug.info(asset_names)

        queryUsers = "select * from users"
        assets = self.db.execute(queryUsers,dictionary=True)
        users = [x['name'] for x in assets]
        debug.info(users)

        for ass_name in asset_names:
            frame = QFrame()
            hlayout = QHBoxLayout(frame)
            chBox = QCheckBox(ass_name, frame)
            coBox = QComboBox(frame)
            coBox.addItems(users)
            chBox.stateChanged.connect(lambda x, chBox=chBox, coBox=coBox: self.updateAssAndUserDict(chBox, coBox))
            coBox.currentIndexChanged.connect(lambda x, chBox=chBox, coBox=coBox: self.updateAssAndUserDict(chBox, coBox))
            hlayout.addWidget(chBox)
            hlayout.addWidget(coBox)

            frame.setLayout(hlayout)
            vLayout.addWidget(frame)

        self.main_ui.assetFrame.setLayout(vLayout)

    def updateAssAndUserDict(self, chBox, coBox):
        if chBox.isChecked():
            asset_and_user[chBox.text()] = coBox.currentText()
        else:
            try:
                asset_and_user.pop(chBox.text())
            except:
                debug.info(str(sys.exc_info()))
        
        debug.info(asset_and_user)

    # def setUsers(self):
    #     queryUsers = "select * from users"
    #     assets = self.db.execute(queryUsers,dictionary=True)
    #     users = [x['name'] for x in assets]
    #     debug.info(users)
    #     self.main_ui.userBox.addItems(users)

    # def updateAssetsBox(self):
    #     text = ''
    #     if self.main_ui.draftBox.isChecked():
    #         text += self.main_ui.draftBox.text() + ','
    #     if self.main_ui.correctionsBox.isChecked():
    #         text += self.main_ui.correctionsBox.text() + ','
    #     if self.main_ui.finalBox.isChecked():
    #         text += self.main_ui.finalBox.text() + ','
    #     self.main_ui.assetsBox.setText(text.strip())

    def showFileDialog(self):
        file_dialog = QFileDialog()
        file_dialog.setDirectory(root_folder)
        file_dialog.setNameFilters(audio_formats)
        file_dialog.exec_()
        file_paths = file_dialog.selectedFiles()
        debug.info(file_paths)
        self.main_ui.audioFileBox.clear()
        self.main_ui.audioFileBox.setText(file_paths[0].replace('/','\\'))

    def createProject(self):
        projName = self.main_ui.nameBox.text()
        debug.info(projName)

        gitConfigCmd = "git config --global user.email \"{0}\" & git config --global user.name \"{1}\" ".format("sanathshetty111@gmail.com","sanath111")
        debug.info(gitConfigCmd)
        subprocess.run(gitConfigCmd, shell=True)
        
        if projName:
            # assetNames = [ass for ass in self.main_ui.assetsBox.text().split(',') if ass]
            # debug.info(assetNames)
            # if assetNames:
            audio_file = self.main_ui.audioFileBox.text()
            debug.info(audio_file)
            if audio_file:
                # user = self.main_ui.userBox.currentText()
                # debug.info(user)
                # if user:
                if asset_and_user:
                    try:
                        projUpdateQuery = "insert into projects (projName) values (\"{0}\") ".format(projName)
                        updateProjList = self.db.execute(projUpdateQuery)
                        if updateProjList == 1:
                            debug.info("Updated proj list")
                        for aNU in asset_and_user:
                            asset = aNU
                            user = asset_and_user[aNU]
                            debug.info(asset)
                            debug.info(user)
                            # for ass in assetNames:
                            assID = str(uuid.uuid4())
                            debug.info(assID)
                            # folder_path = root_folder+os.sep+projName+os.sep+asset
                            folder_path = os.path.join(root_folder, projName, asset)
                            debug.info(folder_path)
                            createAssetQuery = "insert into assets (assID, projName, assetName, path, assignedUser) values (\"{0}\",\"{1}\",\"{2}\",\"{3}\",\"{4}\") ".format(assID, projName, asset, folder_path, user)
                            debug.info(createAssetQuery)
                            updateAssList = self.db.execute(createAssetQuery)
                            if updateAssList == 1:
                                os.makedirs(folder_path, exist_ok=True)
                                if asset == "draft":
                                    # pasteAudioCmd = "rsync -azHXW --info=progress2 \"{0}\" \"{1}\" ".format(audio_file, folder_path)
                                    # pasteDocCmd = "rsync -azHXW --info=progress2 \"{0}\" \"{1}\" ".format(template_folder+"draft.docx",folder_path+os.sep+projName+"_draft.docx")
                                    pasteAudioCmd = "copy {0} {1} ".format(audio_file, folder_path)
                                    debug.info(pasteAudioCmd)
                                    subprocess.run(pasteAudioCmd, shell=True)
                                    pasteDocCmd = "copy {0} {1} ".format(template_folder+os.sep+"draft.docx",folder_path)
                                    debug.info(pasteDocCmd)
                                    subprocess.run(pasteDocCmd, shell=True)
                                    renameDocCmd = "ren {0} {1} ".format(folder_path+os.sep+"draft.docx", projName+"_draft.docx")
                                    debug.info(renameDocCmd)
                                    subprocess.run(renameDocCmd, shell=True)

                                    # gitInitCmd = "git init {0}".format(folder_path)
                                    # debug.info(gitInitCmd)
                                    # subprocess.run(gitInitCmd, shell=True)
                                    # gitAddCmd = "cd {0} & git add . ".format(folder_path)
                                    # debug.info(gitAddCmd)
                                    # subprocess.run(gitAddCmd, shell=True)
                                    # gitCommitCmd = "cd {0} & git commit -m 'first_commit' ".format(folder_path)
                                    # debug.info(gitCommitCmd)
                                    # subprocess.run(gitCommitCmd, shell=True)

                                    initGitCmd = "cd {0} & git init & git add . & git commit -m 'first_commit' ".format(folder_path)
                                    debug.info(initGitCmd)
                                    subprocess.run(initGitCmd, shell=True)

                                    # subprocess.run("git init {0}".format(folder_path))
                                    # subprocess.run("cd {0} & git add . ".format(folder_path))
                                    # subprocess.run("cd {0} & git commit -m 'first_commit' ".format(folder_path))
                        self.main_ui.close()
                    except:
                        err_mess = str(sys.exc_info())
                        debug.info(err_mess)
                        if "Duplicate entry" in err_mess:
                            debug.info("Duplicate entry")
                            self.main_ui.messageLabel.setText("Project already exists")
                else:
                    debug.info("No asset selected")
                    self.main_ui.messageLabel.setText("Please select an asset")
            else:
                debug.info("No audio file selected")
                self.main_ui.messageLabel.setText("Please select an audio file")
            # else:
            #     debug.info("No asset selected")
            #     self.main_ui.messageLabel.setText("Please select an asset")
        else:
            debug.info("No Project name given")
            self.main_ui.messageLabel.setText("Please provide a project name")



if __name__ == '__main__':
    setproctitle.setproctitle("NEW_PROJECT")
    app = QtWidgets.QApplication(sys.argv)
    file = QFile(os.path.join(projDir, "stylesheet.qss"))
    file.open(QFile.ReadOnly | QFile.Text)
    stream = QTextStream(file)
    app.setStyleSheet(stream.readAll())
    window = newProject()
    sys.exit(app.exec_())
