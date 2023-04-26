#!/usr/bin/python3
# *-* coding: utf-8 *-*

import os
import sys
import setproctitle

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

main_ui_file = os.path.join(projDir, "rbhus_clone.ui")
ui_asset_details = os.path.join(projDir,"assetDetailsRow.ui")

root_folder = "/home/sanath.shetty/Documents/rbhus_clone_root/"

new_project = os.path.join(projDir, "new_project.py")

processes = []

class rbhusClone():
    db = rbhus_clone_db.db()
    def __init__(self):
       
        self.main_ui = uic.loadUi(main_ui_file)
        self.main_ui.setWindowTitle("RBHUS CLONE")

        # project_list= self.main_ui.listWidgetProjs
        # asset_list = self.main_ui.listWidgetAssets

        # model_projs = FSM(parent=self.main_ui)

        # project_list.setModel(model_projs)
        # model_projs.setRootPath(root_folder)

        # model_projs.setFilter(QtCore.QDir.Dirs | QtCore.QDir.NoDotAndDotDot)

        self.main_ui.newProjectButt.clicked.connect(lambda x : self.newProject())
        
        self.main_ui.listWidgetProjs.itemClicked.connect(lambda x : self.updateAssetsList())
        self.updateProjectsList()

        #Show Window
        # self.main_ui.showMaximized()
        self.main_ui.show()
        self.main_ui.update()

        qtRectangle = self.main_ui.frameGeometry()
        centerPoint = QtWidgets.QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.main_ui.move(qtRectangle.topLeft())

    def updateProjectsList(self):
        self.main_ui.listWidgetProjs.clear()
        queryProj = "select projName from projects"
        projects = self.db.execute(queryProj,dictionary=True)
        # maxlen = 0
        if projects:
            for x in projects:
                item = QtWidgets.QListWidgetItem()
                item.setText(x['projName'])
                # mylen = len(x['projName'])
                # if(mylen >= maxlen):
                #     maxlen = mylen
                self.main_ui.listWidgetProjs.addItem(item)
            # return(maxlen)

    def updateAssetsList(self):
        self.main_ui.listWidgetAssets.clear()
        selected_item = self.main_ui.listWidgetProjs.currentItem()
        if selected_item is not None:
            text = selected_item.text()
            debug.info(text)
            queryAss = "select * from assets where projName='{0}'".format(text)
            assets = self.db.execute(queryAss,dictionary=True)
            debug.info(assets)
            for x in assets:
                # item = QtWidgets.QListWidgetItem()
                item_widget = assetDetailRowClass()
                # item.setSizeHint(item_widget.sizeHint())
                item_widget.labelUser.setText(x['assignedUser'])
                item_widget.labelAsset.setText(x['assetName'])
                # item.setWidget(item_widget)
                # item.setText(x['assetName']+" "+x['assignedUser'])
                # self.main_ui.listWidgetAssets.addItem(item)



                item = QListWidgetItemSort()
                item.setSizeHint(item_widget.sizeHint())

                self.main_ui.listWidgetAssets.addItem(item)
                self.main_ui.listWidgetAssets.setItemWidget(item, item_widget)

    def newProject(self):
        debug.info("Opening new project")
        p = QProcess(parent=self.main_ui)
        processes.append(p)
        debug.info(processes)
        p.started.connect(self.disableNewProjButt)
        p.readyReadStandardOutput.connect(self.read_out)
        p.readyReadStandardError.connect(self.read_err)
        p.finished.connect(self.enableNewProjButt)
        p.start(sys.executable, new_project.split())

    def disableNewProjButt(self):
        self.main_ui.newProjectButt.setEnabled(False)

    def enableNewProjButt(self):
        self.updateProjectsList()
        self.main_ui.newProjectButt.setEnabled(True)

    
    def read_out(self):
        if processes:
            for process in processes:
                print ('stdout:', str(process.readAllStandardOutput()).strip())

    def read_err(self):
        if processes:
            for process in processes:
                print ('stderr:', str(process.readAllStandardError()).strip())


class assetDetailRowClass(QtWidgets.QWidget):
  def __init__(self,parent=None):
    super(assetDetailRowClass, self).__init__(parent)
    uic.loadUi(ui_asset_details,baseinstance=self)


class FSM(QtWidgets.QFileSystemModel):
    def __init__(self,**kwargs):
        super(FSM, self).__init__(**kwargs)


class QListWidgetItemSort(QtWidgets.QListWidgetItem):
  def __lt__(self, other):
    return self.data(QtCore.Qt.UserRole) < other.data(QtCore.Qt.UserRole)

  def __ge__(self, other):
    return self.data(QtCore.Qt.UserRole) > other.data(QtCore.Qt.UserRole)



if __name__ == '__main__':
    setproctitle.setproctitle("RBHUS_CLONE")
    app = QtWidgets.QApplication(sys.argv)
    window = rbhusClone()
    sys.exit(app.exec_())
