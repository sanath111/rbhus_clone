#!/usr/bin/python3
# *-* coding: utf-8 *-*

import os
import sys
# from sys import exc_info, exception

import setproctitle
import uuid
import subprocess
import shlex
import rbhus_clone_db
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


projDir = os.sep.join(os.path.abspath(__file__).split(os.sep)[:-1])
sys.path.append(projDir)

main_ui_file = os.path.join(projDir, "ui_files", "version_list_new.ui")
file_thumbs_ui = os.path.join(projDir, "ui_files", "file_thumbs.ui")
version_details_ui = os.path.join(projDir, "ui_files", "version_details_row.ui")

# app_test = os.path.join(projDir, "tests", "app_test.py")
text_editor = os.path.join(projDir, "text_editor.py")
processes = []

text_formats = ["docx", "txt"]
audio_formats = ["mp3"]



os.environ['QT_LOGGING_RULES'] = "qt5ct.debug=false"

parser = argparse.ArgumentParser(description="Utility to manage versions")
# parser.add_argument("-f","--filepath",dest="filepath",help="file path")
# parser.add_argument("-a","--asset",dest="asset",help="asset name")
parser.add_argument("-a","--ass_id",dest="ass_id",help="asset id")
parser.add_argument("-u","--user",dest="user",help="user")
args = parser.parse_args()


class versionList():
    db = rbhus_clone_db.db()
    def __init__(self):

        self.main_ui = uic.loadUi(main_ui_file)
        self.main_ui.setWindowTitle("VERSION LIST")

        self.user = args.user
        self.role = utils.getRole(self.user)

        self.current_files = []

        self.ass_dets = utils.getAssDets(args.ass_id)
        debug.info(self.ass_dets)
        self.ass_path = self.ass_dets['path']
        self.proj_name = self.ass_dets['projName']
        self.stage_name = self.ass_dets['stage']
        self.ass_user = self.ass_dets['assignedUser']

        stage_dets = utils.getStageDets()
        self.stage_dets_dict = {item['name']: {'index': item['index'], 'access': item['access']} for item in stage_dets}
        debug.info(self.stage_dets_dict)

        self.stage_index = self.stage_dets_dict[self.stage_name]['index']

        self.commit_dets_dict = {}

        self.loadingVersions = False
        self.pushingAssets = False
        self.buttsVisibility()

        self.loadVersions()
        self.main_ui.versionTable.itemSelectionChanged.connect(self.updateFileList)
        # self.main_ui.versionList.itemClicked.connect(lambda x : self.updateFileList())
        # self.main_ui.filesList.itemClicked.connect(lambda x, : self.showFileName(x))
        self.main_ui.openButt.clicked.connect(lambda x: self.openFile())
        self.main_ui.commitButt.clicked.connect(lambda x, path=self.ass_path: self.commitChanges(path, "regular commit"))
        # self.main_ui.pushButt.clicked.connect(lambda x : self.pushChanges())
        menu = self.popupToolButton()
        if menu:
            self.main_ui.pushButt.setMenu(menu)
            self.main_ui.pushButt.triggered.connect(self.popupToolButtonTriggered)
        else:
            self.main_ui.pushButt.setMenu(None)
            self.main_ui.pushButt.clicked.connect(lambda x: self.popupToolButtonClicked())

        proj_status = utils.getProjStatus(self.proj_name)
        proj_status_stage = next((key for key, value in self.stage_dets_dict.items() if value['index'] == proj_status), None)
        self.main_ui.assetName.setText(" : ".join(['Asset', self.stage_name]))
        self.main_ui.projStatus.setText(" : ".join(['Status', 'In '+proj_status_stage]))

        #Show Window
        self.main_ui.show()
        self.main_ui.update()

        qtRectangle = self.main_ui.frameGeometry()
        centerPoint = QtWidgets.QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.main_ui.move(qtRectangle.topLeft())

    # def loadVersions(self):
    #     try:
    #         get_commits_cmd = ["hg", "log", "--cwd", self.ass_path, "--template", "{node|short}\n"]
    #         debug.info(get_commits_cmd)
    #         commits = subprocess.check_output(get_commits_cmd).decode("utf-8").splitlines()
    #         debug.info(commits)
    #
    #         self.main_ui.versionTable.setColumnCount(4)
    #         self.main_ui.versionTable.setHorizontalHeaderLabels(["Revision", "Author", "Date", "Description"])
    #         self.main_ui.versionTable.setRowCount(len(commits))
    #
    #         for row, commit_hash in enumerate(commits):
    #             commit_dets_cmd = ["hg", "log", "--cwd", self.ass_path, "--rev", commit_hash, "--template", "{rev+1}\n{author}\n{date(date, '%d-%m-%Y %I:%M %p')}\n{desc}"]
    #             commit_dets = subprocess.check_output(commit_dets_cmd).decode("utf-8").splitlines()
    #
    #             for col, detail in enumerate(commit_dets):
    #                 cell_item = QTableWidgetItem(detail)
    #                 if col == 0:
    #                     cell_item.setData(Qt.UserRole, commit_hash)
    #                 self.main_ui.versionTable.setItem(row, col, cell_item)
    #                 if col == 3:
    #                     self.main_ui.versionTable.horizontalHeader().setSectionResizeMode(col, QtWidgets.QHeaderView.Stretch)
    #                 else:
    #                     self.main_ui.versionTable.horizontalHeader().setSectionResizeMode(col, QtWidgets.QHeaderView.ResizeToContents)
    #
    #         if len(commits) > 0:
    #             self.main_ui.versionTable.selectRow(0)
    #
    #         self.updateFileList()
    #     except:
    #         debug.info(str(sys.exc_info()))

    def loadVersions(self):
        # Initialize the table
        # Clear the table before loading new data
        self.loadingVersions = True
        self.buttsVisibility()
        self.main_ui.versionTable.clear()
        self.main_ui.versionTable.setRowCount(0)  # Reset the row count
        self.main_ui.versionTable.setColumnCount(4)
        self.main_ui.versionTable.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.main_ui.versionTable.setHorizontalHeaderLabels(["Revision", "Author", "Date", "Description"])
        # self.main_ui.versionTable.setRowCount(0)

        # Start the thread
        self.load_versions_thread = LoadVersionsThread(self.ass_path)
        self.load_versions_thread.row_loaded.connect(self.addRow)
        self.load_versions_thread.error_occurred.connect(self.onError)
        self.load_versions_thread.finished.connect(self.onThreadFinished)
        self.load_versions_thread.start()

    def addRow(self, row, details):
        # Increment row count as rows are added dynamically
        self.main_ui.versionTable.setRowCount(row + 1)

        commit_hash = details[0]
        for col, detail in enumerate(details[1:]):
            cell_item = QTableWidgetItem(detail)
            if col == 0:
                cell_item.setData(Qt.UserRole, commit_hash)
            self.main_ui.versionTable.setItem(row, col, cell_item)
            if col == 3:
                self.main_ui.versionTable.horizontalHeader().setSectionResizeMode(col, QHeaderView.Stretch)
            else:
                self.main_ui.versionTable.horizontalHeader().setSectionResizeMode(col, QHeaderView.ResizeToContents)

        # Select the first row once it's added
        if row == 0:
            self.main_ui.versionTable.selectRow(0)

        self.commit_dets_dict[row] = details

    def onError(self, error_msg):
        debug.info(f"Error: {error_msg}")

    def onThreadFinished(self):
        debug.info("Data loading completed!")
        self.load_versions_thread.row_loaded.disconnect()
        self.load_versions_thread.finished.disconnect()
        self.load_versions_thread = None
        self.updateFileList()
        self.loadingVersions = False
        self.buttsVisibility()

    def updateFileList(self):
        # self.main_ui.filesList.clear()
        # selected_item = self.main_ui.versionList.currentItem()
        selected_items = self.main_ui.versionTable.selectedItems()
        # if selected_item is not None:
        if selected_items:
            selected_row = selected_items[0].row()
            commit_hash = self.main_ui.versionTable.item(selected_row, 0).data(Qt.UserRole)
            # text = selected_item.text()
            debug.info(commit_hash)
            # commit_hash = selected_item.data(3)
            # commit_hash = text.split()[0]

            # files = subprocess.check_output(["git", "ls-tree", "-r", "--name-only", commit_hash], cwd=self.folder).decode("utf-8").splitlines()
            files = subprocess.check_output(["hg", "manifest", "-r", commit_hash, "--cwd", self.ass_path]).decode("utf-8").splitlines()
            debug.info(files)
            # debug.info(type(files))
            self.current_files = files

    def buttsVisibility(self):
        proj_status = utils.getProjStatus(self.proj_name)
        debug.info(proj_status)

        if (self.user != self.ass_user or
            self.stage_name == 'final' or
            self.loadingVersions or
            self.pushingAssets or
            self.stage_index != proj_status):
            self.main_ui.pushButt.setEnabled(False)
        else:
            self.main_ui.pushButt.setEnabled(True)

    def openFile(self):
        # selected_file = self.main_ui.filesList.currentItem()
        # if selected_file is not None:
        # selected_commit = self.main_ui.versionList.currentItem()
        selected_items = self.main_ui.versionTable.selectedItems()
        # if selected_commit is not None:
        if selected_items:
            # commit_text = selected_commit.text()
            # commit_hash = commit_text.split()[0]
            # commit_hash = selected_commit.data(3)
            selected_row = selected_items[0].row()
            commit_hash = self.main_ui.versionTable.item(selected_row, 0).data(Qt.UserRole)
            debug.info(commit_hash)
            # subprocess.run(["git", "checkout", commit_hash, "--", self.folder], cwd=self.folder)
            subprocess.run(["hg", "update", "-r", commit_hash, "--cwd", self.ass_path])

            # text = selected_file.text()

            # openCmd = "start {0}".format(filepath)
            # # subprocess.Popen(shlex.split(openCmd))
            # subprocess.run(openCmd, shell=True)
            text_file = ""
            audio_file = ""
            for file in self.current_files:
                if file.endswith("docx"):
                    text_file = self.ass_path+os.sep+file
                if file.endswith("mp3"):
                    audio_file = self.ass_path+os.sep+file

            debug.info("Opening file")
            try:
                p = QProcess(parent=self.main_ui)
                processes.append(p)
                debug.info(processes)
                # p.readyReadStandardOutput.connect(self.read_out)
                # p.readyReadStandardError.connect(self.read_err)
                p.readyReadStandardOutput.connect(lambda: debug.info(p.readAllStandardOutput().data().decode()))
                p.readyReadStandardError.connect(lambda: debug.info(p.readAllStandardError().data().decode()))
                # p.start(sys.executable, edit_asset.split())
                # p.start(sys.executable + " " + text_editor + " --text " + "\""+text_file+"\"" + " --audio " + "\""+audio_file+"\"")
                p.start(sys.executable, [text_editor, "--text", text_file, "--audio", audio_file, "--user", self.user])
            except Exception as e:
                debug.info(f"Error: {e}")

    def read_out(self):
        if processes:
            for process in processes:
                debug.info ('stdout:', str(process.readAllStandardOutput()).strip())

    def read_err(self):
        if processes:
            for process in processes:
                debug.info ('stderr:', str(process.readAllStandardError()).strip())

    def commitChanges(self, path, message):
        self.main_ui.messageLabel.clear()
        try:
            if not self.user == self.ass_user:
                self.main_ui.messageLabel.setText("Asset not assigned to you.")
                return

            # self.main_ui.filesList.clear()
            # subprocess.run(["hg", "add", "--cwd", self.folder, "."], shell=True)
            # p = subprocess.Popen(["hg", "commit", "--cwd", self.folder, "-m" , "new_commit", "--user", self.user], stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)

            hg_add_cmd =f"hg add --cwd \"{path}\" . "
            hg_commit_cmd = f"hg commit --cwd \"{path}\" -m  \"{message}\" --user {self.user}"

            add_result = utils.run_command(hg_add_cmd)
            commit_result = utils.run_command(hg_commit_cmd)
            if add_result == 'success':
                if commit_result:
                    self.main_ui.messageLabel.setText(commit_result)
            else:
                self.main_ui.messageLabel.setText(add_result)
            self.loadVersions()

        except Exception as ex :
            debug.info("An unexpected error occurred: ", ex)
            debug.info(str(sys.exc_info()))

    def popupToolButton(self):
        if self.user != self.ass_user:
            self.main_ui.messageLabel.setText("Asset not assigned to you.")
            return None
        if self.stage_name == 'final':
            return None
        if self.stage_name == 'draft':
            return None

        menu = QtWidgets.QMenu()

        sub_action_dict = {}
        stages = utils.getAllStages(self.proj_name)

        for x in stages:
            if not x['stage'] == self.stage_name:
                stage_details = self.stage_dets_dict[x['stage']]
                current_stage_details = self.stage_dets_dict[self.stage_name]
                # TODO: check for availability of the stage which can push to final
                if self.role in stage_details['access']:
                    if stage_details['index'] == current_stage_details['index'] + 1 or stage_details['index'] <= current_stage_details['index']:
                        sub_action = menu.addAction(x['stage'])
                        sub_action_dict[x['stage']] = sub_action

        return menu

    def popupToolButtonTriggered(self, action):
        if not action:
            return
        dest_stage = action.text().strip()
        debug.info(f"Push to {dest_stage} clicked")
        self.main_ui.messageLabel.clear()
        self.pushAsset(dest_stage)

    def popupToolButtonClicked(self):
        debug.info(f"Push to clicked")
        debug.info(self.commit_dets_dict)
        dest_stage = ""
        if self.stage_name == 'draft':
            for key, value in self.commit_dets_dict.items():
                if 'from' in value[-1]:
                    debug.info(f"extracting dest_stage using commits: {value[-1]}")
                    dest_stage = value[-1].lstrip('from').strip()
                    break
            if not dest_stage:
                draft_index = self.stage_dets_dict['draft']['index']
                debug.info(f"extracting dest_stage using db: {draft_index}")
                dest_stage = next((key for key, value in self.stage_dets_dict.items() if value['index'] == draft_index+1), None)

        debug.info(dest_stage)
        self.pushAsset(dest_stage)

    def pushAsset(self, dest_stage):
        self.main_ui.messageLabel.clear()
        self.pushingAssets = True
        self.buttsVisibility()
        source_path = self.ass_path
        dest_path = utils.getAssPath(proj_name=self.proj_name,stage_name=dest_stage)
        if os.name == 'nt':
            paste_audio_cmd = f"cmd /c copy \"{os.path.join(source_path, self.proj_name + '_source.mp3')}\" \"{dest_path}\" /Y"
            paste_doc_cmd = f"cmd /c copy \"{os.path.join(source_path, self.proj_name + '_'+self.stage_name+'.docx')}\" \"{os.path.join(dest_path, self.proj_name + '_'+dest_stage+'.docx')}\" /Y "
        else:
            paste_audio_cmd = f"rsync -azHXW --info=progress2 \"{os.path.join(source_path, self.proj_name + '_source.mp3')}\" \"{os.path.join(dest_path, self.proj_name + '_source.mp3')}\""
            paste_doc_cmd = f"rsync -azHXW --info=progress2 \"{os.path.join(source_path, self.proj_name + '_'+self.stage_name+'.docx')}\" \"{os.path.join(dest_path, self.proj_name + '_'+dest_stage+'.docx')}\""

        paste_audio_result = utils.run_command(paste_audio_cmd)
        paste_doc_result = utils.run_command(paste_doc_cmd)
        self.commitChanges(dest_path, f"from {self.stage_name}")
        utils.setProjStatus(self.proj_name, self.stage_dets_dict[dest_stage]['index'])
        proj_status = utils.getProjStatus(self.proj_name)
        proj_status_stage = next((key for key, value in self.stage_dets_dict.items() if value['index'] == proj_status), None)
        self.main_ui.projStatus.setText(" : ".join(['Status', 'In '+proj_status_stage]))
        self.pushingAssets = False
        self.buttsVisibility()


class LoadVersionsThread(QThread):
    row_loaded = pyqtSignal(int, list)
    error_occurred = pyqtSignal(str)
    def __init__(self, ass_path, parent=None):
        super().__init__(parent)
        self.ass_path = ass_path

    def run(self):
        try:
            get_commits_cmd = ["hg", "log", "--cwd", self.ass_path, "--template", "{node|short}\n"]
            commits = subprocess.check_output(get_commits_cmd).decode("utf-8").splitlines()
            debug.info(commits)
            for row, commit_hash in enumerate(commits):
                commit_dets_cmd = [
                    "hg", "log", "--cwd", self.ass_path, "--rev", commit_hash,
                    "--template", "{rev+1}\n{author}\n{date(date, '%d-%m-%Y %I:%M %p')}\n{desc}"
                ]
                commit_dets = subprocess.check_output(commit_dets_cmd).decode("utf-8").splitlines()
                commit_dets.insert(0, commit_hash)  # Include the hash for later use
                debug.info(commit_dets)
                self.row_loaded.emit(row, commit_dets)  # Emit each row
        except Exception as e:
            debug.info(str(exc_info()))
            self.error_occurred.emit(str(e))


class QListWidgetItemSort(QtWidgets.QListWidgetItem):
  def __lt__(self, other):
    return self.data(QtCore.Qt.UserRole) < other.data(QtCore.Qt.UserRole)

  def __ge__(self, other):
    return self.data(QtCore.Qt.UserRole) > other.data(QtCore.Qt.UserRole)



if __name__ == '__main__':
    setproctitle.setproctitle("VERSION_LIST")
    app = QtWidgets.QApplication(sys.argv)
    # file = QFile(os.path.join(projDir, "stylesheet.qss"))
    # file.open(QFile.ReadOnly | QFile.Text)
    # stream = QTextStream(file)
    # app.setStyleSheet(stream.readAll())
    window = versionList()
    sys.exit(app.exec_())
