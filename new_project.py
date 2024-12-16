#!/usr/bin/python3
# *-* coding: utf-8 *-*

import os
import sys
import setproctitle
import uuid
import subprocess
import shlex
# import rbhus_clone_db
import debug
import argparse
from pathlib import Path
import utils


from PyQt5 import QtCore, uic, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QTreeView, QFileSystemModel, QVBoxLayout, QWidget, QHBoxLayout, QListView
from PyQt5.QtWidgets import QListWidgetItem, QShortcut
from PyQt5.QtGui import QKeySequence
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

import constants

projDir = os.sep.join(os.path.abspath(__file__).split(os.sep)[:-1])
sys.path.append(projDir)

main_ui_file = os.path.join(projDir,  "ui_files", "new_project_new.ui")

# root_folder = r"Z:\share\sanath\rbhus_clone_root"
# root_folder = r"C:\Users\aum\Documents\rbhus_clone_root"
root_folder = constants.root_folder
# template_folder = root_folder+os.sep+"template"
template_folder = constants.template_folder

text_formats = ["docx"]
audio_formats = ["*.mp3"]

stage_and_user = {}

os.environ['QT_LOGGING_RULES'] = "qt5ct.debug=false"

parser = argparse.ArgumentParser(description="Utility to manage assets")
parser.add_argument("-u","--user",dest="user",help="user")
args = parser.parse_args()

class newProject():
    # db = rbhus_clone_db.db()
    def __init__(self):
       
        self.main_ui = uic.loadUi(main_ui_file)
        self.main_ui.setWindowTitle("NEW PROJECT")

        self.user = args.user

        self.setStageAndUser()
        # self.setUsers()
        # self.main_ui.draftBox.stateChanged.connect(lambda x : self.updateAssetsBox())
        # self.main_ui.correctionsBox.stateChanged.connect(lambda x : self.updateAssetsBox())
        # self.main_ui.finalBox.stateChanged.connect(lambda x : self.updateAssetsBox())
        self.main_ui.selectAudioButt.clicked.connect(lambda x : self.showFileDialog())
        self.main_ui.createButt.clicked.connect(lambda x : self.createProject())

        #Show Window
        # self.main_ui.show()
        self.main_ui.showMaximized()
        self.main_ui.update()

        # qtRectangle = self.main_ui.frameGeometry()
        # centerPoint = QtWidgets.QDesktopWidget().availableGeometry().center()
        # qtRectangle.moveCenter(centerPoint)
        # self.main_ui.move(qtRectangle.topLeft())


    def setStageAndUser(self):
        v_layout = QVBoxLayout(self.main_ui.assetFrame)
        
        # query_stage_names = "select * from stages"
        # stage_names = self.db.execute(query_stage_names,dictionary=True)
        stage_names = utils.getStageDets()
        stage_names = [x['name'] for x in stage_names]
        debug.info(stage_names)

        # query_users = "select * from users"
        # users = self.db.execute(query_users,dictionary=True)
        # users = [x['name'] for x in users]
        users = utils.getUsers()
        debug.info(users)

        for stage_name in stage_names:
            frame = QFrame()
            h_layout = QHBoxLayout(frame)
            ch_box = QCheckBox(stage_name, frame)
            co_box = QComboBox(frame)
            co_box.addItems(users)
            ch_box.stateChanged.connect(lambda x, ch_box=ch_box, co_box=co_box: self.updateStageAndUserDict(ch_box, co_box))
            co_box.currentIndexChanged.connect(lambda x, ch_box=ch_box, co_box=co_box: self.updateStageAndUserDict(ch_box, co_box))
            ch_box.setChecked(True)
            h_layout.addWidget(ch_box)
            h_layout.addWidget(co_box)

            frame.setLayout(h_layout)
            v_layout.addWidget(frame)

        self.main_ui.assetFrame.setLayout(v_layout)


    def updateStageAndUserDict(self, ch_box, co_box):
        if ch_box.isChecked():
            stage_and_user[ch_box.text()] = co_box.currentText()
        else:
            try:
                stage_and_user.pop(ch_box.text())
            except:
                debug.info(str(sys.exc_info()))
        
        debug.info(stage_and_user)

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
        file_dialog.setDirectory(template_folder)
        file_dialog.setNameFilters(audio_formats)
        file_dialog.exec_()
        file_paths = file_dialog.selectedFiles()
        debug.info(file_paths)
        self.main_ui.audioFileBox.clear()
        if os.name == 'nt':
            self.main_ui.audioFileBox.setText(file_paths[0].replace('/','\\'))
        else:
            self.main_ui.audioFileBox.setText(file_paths[0])


    def setupProject(self, audio_file, folder_path, proj_name, stage):
        if os.name == 'nt':
            paste_audio_cmd = f"cmd /c copy \"{audio_file}\" \"{os.path.join(folder_path, proj_name + '_source.mp3')}\" /Y"
            paste_doc_cmd = f"cmd /c copy \"{os.path.join(template_folder, 'draft.docx')}\" \"{os.path.join(folder_path, proj_name+'_'+stage+'.docx')}\" /Y"
            # audio_filename = audio_file.split(os.sep)[-1]
            # rename_audio_cmd = f"ren \"{os.path.join(folder_path, audio_filename)}\" \"{proj_name}_source.mp3\""
            # rename_doc_cmd = f"ren \"{os.path.join(folder_path, 'draft.docx')}\" \"{proj_name}_{stage}.docx\""
        else:
            paste_audio_cmd = f"rsync -azHXW --info=progress2 \"{audio_file}\" \"{os.path.join(folder_path, proj_name + '_source.mp3')}\""
            paste_doc_cmd = f"rsync -azHXW --info=progress2 \"{os.path.join(template_folder, 'draft.docx')}\" \"{os.path.join(folder_path, proj_name+'_'+stage+'.docx')}\""
            # rename_audio_cmd = ""
            # rename_doc_cmd = ""

        utils.run_command(paste_audio_cmd)
        utils.run_command(paste_doc_cmd)
        # if rename_audio_cmd:
        #     utils.run_command(rename_audio_cmd)
        # if rename_doc_cmd:
        #     utils.run_command(rename_doc_cmd)


    def setupVersioning(self, folder_path):
        if os.name == 'nt':
            folder_path = folder_path.replace("\\\\", "\\")
        cmd_separator = '&' if os.name == 'nt' else '&&'

        # init_hg_cmd = (
        #     f"hg init --cwd \"{folder_path}\" {cmd_separator} "
        #     f"hg add --cwd \"{folder_path}\" . {cmd_separator} "
        #     f"hg commit --cwd \"{folder_path}\" -m 'first commit' --user {self.user}"
        # )

        # self.run_command(init_hg_cmd)

        hg_init_cmd = f"hg init --cwd \"{folder_path}\""
        hg_add_cmd = f"hg add --cwd \"{folder_path}\" . "
        hg_commit_cmd = f"hg commit --cwd \"{folder_path}\" -m 'first commit' --user {self.user}"

        utils.run_command(hg_init_cmd)
        utils.run_command(hg_add_cmd)
        utils.run_command(hg_commit_cmd)

    # def run_command(self, cmd):
    #     debug.info(cmd)
    #     try:
    #         result = subprocess.run(cmd, shell=True, check=True, text=True,
    #                                 stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    #         debug.info(result.stdout.strip())
    #     except subprocess.CalledProcessError as e:
    #         debug.info(f"Command failed with error: {e.stderr}")


    def createProject(self):
        projName = self.main_ui.nameBox.text().strip()
        debug.info(projName)

        # gitConfigCmd = "git config --global user.email \"{0}\" & git config --global user.name \"{1}\" ".format("sanathshetty111@gmail.com","sanath111")
        # debug.info(gitConfigCmd)
        # subprocess.run(gitConfigCmd, shell=True)
        
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
                if stage_and_user:
                    reply = QMessageBox.question(self.main_ui, 'Confirmation',
                                                 'Are you sure you want to create this project?',
                                                 QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
                    if reply == QMessageBox.Yes:
                        self.main_ui.messageLabel.setText("Creating Project ... ")
                        try:
                            # projPath = os.path.join(root_folder, projName)
                            if os.name == 'nt':
                                projPath = os.path.join(root_folder, projName).replace("\\", "\\\\")
                            else:
                                projPath = os.path.normpath(os.path.join(root_folder, projName))
                            # projUpdateQuery = "INSERT INTO projects (projName, path, status) VALUES (\"{0}\",\"{1}\",\"{2}\") ".format(projName, projPath, 0)
                            # debug.info(projUpdateQuery)
                            # updateProjList = self.db.execute(projUpdateQuery)
                            create_proj_result = utils.createNewProject(projName, projPath, proj_status=0)
                            if create_proj_result == 1:
                                debug.info("Updated proj list")
                                for aNU in stage_and_user:
                                    stage = aNU
                                    user = stage_and_user[aNU]
                                    debug.info(stage)
                                    debug.info(user)
                                    # for ass in assetNames:
                                    assID = str(uuid.uuid4())
                                    debug.info(assID)
                                    # folder_path = root_folder+os.sep+projName+os.sep+asset
                                    # folder_path = os.path.join(root_folder, projName, stage)
                                    if os.name == 'nt':
                                        folder_path = os.path.join(root_folder, projName, stage).replace("\\", "\\\\")
                                    else:
                                        folder_path = os.path.normpath(os.path.join(root_folder, projName, stage))
                                    debug.info(folder_path)
                                    # createAssetQuery = "insert into assets (assetID, projName, stage, path, assignedUser) values (\"{0}\",\"{1}\",\"{2}\",\"{3}\",\"{4}\") ".format(assID, projName, stage, folder_path, user)
                                    # debug.info(createAssetQuery)
                                    # updateAssList = self.db.execute(createAssetQuery)
                                    create_ass_result = utils.createNewAsset(assID, projName, stage, folder_path, user)
                                    if create_ass_result == 1:
                                        os.makedirs(folder_path, exist_ok=True)
                                        self.setupProject(audio_file, folder_path, projName, stage)
                                        self.setupVersioning(folder_path)
                                    elif "Duplicate entry" in create_ass_result:
                                        self.main_ui.messageLabel.setText("Asset already exists")
                                    elif "UNIQUE constraint failed" in create_ass_result:
                                        self.main_ui.messageLabel.setText("Asset already exists")
                                self.main_ui.close()
                            elif "Duplicate entry" in create_proj_result:
                                self.main_ui.messageLabel.setText("Project already exists")
                            elif "UNIQUE constraint failed" in create_proj_result:
                                self.main_ui.messageLabel.setText("Project already exists")

                        except:
                            debug.info(str(sys.exc_info()))
                    else:
                        return
                else:
                    debug.info("No stages selected")
                    self.main_ui.messageLabel.setText("Please select a stage")
            else:
                debug.info("No audio file selected")
                self.main_ui.messageLabel.setText("Please select an audio file")
        else:
            debug.info("No Project name given")
            self.main_ui.messageLabel.setText("Please provide a project name")



if __name__ == '__main__':
    setproctitle.setproctitle("NEW_PROJECT")
    app = QtWidgets.QApplication(sys.argv)
    # file = QFile(os.path.join(projDir, "stylesheet.qss"))
    # file.open(QFile.ReadOnly | QFile.Text)
    # stream = QTextStream(file)
    # app.setStyleSheet(stream.readAll())
    window = newProject()
    sys.exit(app.exec_())
