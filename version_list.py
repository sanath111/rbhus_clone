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
import argparse

from PyQt5 import QtCore, uic, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QTreeView, QFileSystemModel, QVBoxLayout, QWidget, QHBoxLayout, QListView
from PyQt5.QtWidgets import QListWidgetItem, QShortcut
from PyQt5.QtGui import QKeySequence
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


projDir = os.sep.join(os.path.abspath(__file__).split(os.sep)[:-1])
sys.path.append(projDir)

main_ui_file = os.path.join(projDir, "ui_files", "version_list.ui")
file_thumbs_ui = os.path.join(projDir, "ui_files", "file_thumbs.ui")

# root_folder = "/home/sanath.shetty/Documents/rbhus_clone_root/"

text_formats = ["docx"]
audio_formats = ["mp3"]

os.environ['QT_LOGGING_RULES'] = "qt5ct.debug=false"

parser = argparse.ArgumentParser(description="Utility to manage versions")
parser.add_argument("-f","--filepath",dest="filepath",help="file path")
parser.add_argument("-a","--asset",dest="asset",help="asset name")
args = parser.parse_args()


class versionList():
    db = rbhus_clone_db.db()
    def __init__(self):
       
        self.main_ui = uic.loadUi(main_ui_file)
        self.main_ui.setWindowTitle("VERSION LIST")

        self.folder = args.filepath
        self.asset = args.asset
        self.projName = self.asset.split(" : ")[0]
        self.assetName = self.asset.split(" : ")[1]
        debug.info(self.folder)
        debug.info(self.asset)
        debug.info(self.projName)
        debug.info(self.assetName)

        self.loadVersions()
        self.main_ui.versionList.itemClicked.connect(lambda x : self.updateFileList())
        self.main_ui.filesList.itemClicked.connect(lambda x, : self.showFileName(x))
        # self.main_ui.openButt.clicked.connect(lambda x : self.openFile())
        self.main_ui.commitButt.clicked.connect(lambda x : self.commitChanges())
        self.main_ui.pushButt.clicked.connect(lambda x : self.pushChanges())
        
        self.main_ui.assetName.setText(self.asset)
        
        #Show Window
        self.main_ui.show()
        self.main_ui.update()

        qtRectangle = self.main_ui.frameGeometry()
        centerPoint = QtWidgets.QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.main_ui.move(qtRectangle.topLeft())

    def loadVersions(self):
        self.main_ui.versionList.clear()

        try:
            # commits = subprocess.check_output(["git", "log", "--pretty=oneline"], cwd=self.folder).decode("utf-8").splitlines()
            commits = subprocess.check_output(["git", "log", "--pretty=format:%h - %cd", "--date=format:%a, %d %b %Y %I:%M %p"], cwd=self.folder).decode("utf-8").splitlines()
            debug.info(commits)

            # Add each commit to the QListWidget
            for commit in commits:
                list_item = QListWidgetItem(commit, self.main_ui.versionList)
                self.main_ui.versionList.addItem(list_item)
                
        except:
            debug.info(str(sys.exc_info()))
        # files = subprocess.check_output(["git", "ls-tree", "-r", "--name-only", "HEAD"], cwd=folder).decode("utf-8").splitlines()
        # debug.info(files)
        
        # for file in files:
        #     list_item = QListWidgetItem(file, self.main_ui.versionList)
        #     self.main_ui.versionList.addItem(list_item)

    def updateFileList(self):
        self.main_ui.filesList.clear()
        selected_item = self.main_ui.versionList.currentItem()
        if selected_item is not None:
            text = selected_item.text()
            debug.info(text)
            commit_hash = text.split()[0]

            files = subprocess.check_output(["git", "ls-tree", "-r", "--name-only", commit_hash], cwd=self.folder).decode("utf-8").splitlines()
            debug.info(files)
            
            for file in files:
                if file.split('.')[-1] in text_formats:
                    file_icon = QtGui.QPixmap(os.path.join(projDir, "image_files", "text_icon.svg"))
                elif file.split('.')[-1] in audio_formats:
                    file_icon = QtGui.QPixmap(os.path.join(projDir, "image_files", "audio_icon.svg"))
                item_widget = fileThumbsClass()
                item_widget.labelFileName.setText(file)
                item_widget.labelIcon.setPixmap(file_icon)

                item_widget.customContextMenuRequested.connect(lambda x, ui=item_widget: self.fileContextMenu(ui,pos=x))

                item = QListWidgetItemSort()
                item.setSizeHint(item_widget.sizeHint())

                self.main_ui.filesList.addItem(item)
                self.main_ui.filesList.setItemWidget(item, item_widget)

    def showFileName(self, item):
        item_widget = self.main_ui.filesList.itemWidget(item)
        filename = item_widget.labelFileName.text()
        self.main_ui.messageLabel.clear()
        self.main_ui.messageLabel.setText(filename)

    def fileContextMenu(self, ui, pos):
        debug.info("File clicked")

        menu = QtWidgets.QMenu()
        openAction = menu.addAction("Open")

        action = menu.exec_(ui.mapToGlobal(pos))

        if (action == openAction):
            debug.info("Open clicked")
            filename = ui.labelFileName.text()
            filepath = self.folder+os.sep+filename
            debug.info(filepath)
            self.openFile(filepath)


    def openFile(self, filepath):
        # selected_file = self.main_ui.filesList.currentItem()
        # if selected_file is not None:
        selected_commit = self.main_ui.versionList.currentItem()
        if selected_commit is not None:
            commit_text = selected_commit.text()
            commit_hash = commit_text.split()[0]
        
            subprocess.run(["git", "checkout", commit_hash, "--", self.folder], cwd=self.folder)

            # text = selected_file.text()
            
            openCmd = "xdg-open {0}".format(filepath)
            subprocess.Popen(shlex.split(openCmd))
    
    def commitChanges(self):
        try:
            self.main_ui.filesList.clear()
            subprocess.run(["git", "add", "."], cwd=self.folder)
            p = subprocess.Popen(["git", "commit", "-m", "new_commit"], cwd=self.folder , stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
            for line in p.stdout:
                debug.info(line)
                if "nothing to commit" in line:
                    self.main_ui.messageLabel.setText("Nothing to Commit")
                    break
                else:
                    self.main_ui.messageLabel.setText("Commit Success")
            self.loadVersions()
        except:
            debug.info(str(sys.exc_info()))

    def pushChanges(self):
        debug.info("Push clicked")
        # if self.assetName == "draft":
            # copyCmd = "rsync -azHXW --info=progress2 \"{0}\" \"{1}\" ".format(audio_file, folder_path)



class fileThumbsClass(QtWidgets.QWidget):
  def __init__(self,parent=None):
    super(fileThumbsClass, self).__init__(parent)
    uic.loadUi(file_thumbs_ui,baseinstance=self)


class QListWidgetItemSort(QtWidgets.QListWidgetItem):
  def __lt__(self, other):
    return self.data(QtCore.Qt.UserRole) < other.data(QtCore.Qt.UserRole)

  def __ge__(self, other):
    return self.data(QtCore.Qt.UserRole) > other.data(QtCore.Qt.UserRole)



if __name__ == '__main__':
    setproctitle.setproctitle("VERSION_LIST")
    app = QtWidgets.QApplication(sys.argv)
    file = QFile(os.path.join(projDir, "stylesheet.qss"))
    file.open(QFile.ReadOnly | QFile.Text)
    stream = QTextStream(file)
    app.setStyleSheet(stream.readAll())
    window = versionList()
    sys.exit(app.exec_())
