#!/usr/bin/python3
# *-* coding: utf-8 *-*

import os
import sys
import setproctitle
import subprocess
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

main_ui_file = os.path.join(projDir, "rbhus_clone.ui")
asset_details_ui = os.path.join(projDir,"asset_details_row.ui")

root_folder = "/home/sanath.shetty/Documents/rbhus_clone_root/"

new_project = os.path.join(projDir, "new_project.py")
admin_tools = os.path.join(projDir, "admin_tools.py")
version_list = os.path.join(projDir, "version_list.py")

processes = []

os.environ['QT_LOGGING_RULES'] = "qt5ct.debug=false"

### TODO: REMOVE LATER ###
parser = argparse.ArgumentParser(description="Utility to manage assets")
parser.add_argument("-u","--user",dest="user",help="user")
args = parser.parse_args()


class rbhusClone():
    db = rbhus_clone_db.db()
    def __init__(self):
       
        self.main_ui = uic.loadUi(main_ui_file)
        self.main_ui.setWindowTitle("RBHUS CLONE")
        # self.main_ui.setWindowIcon(QtGui.QIcon(os.path.join(projDir, "imageFiles", "new_icons" , "folder.svg")))


        self.main_ui.newProjectButt.clicked.connect(lambda x : self.newProject())
        self.main_ui.adminToolsButt.clicked.connect(lambda x : self.adminTools())
        
        self.main_ui.listWidgetProjs.itemClicked.connect(lambda x : self.updateAssetsList())

        self.main_ui.radioMineAss.clicked.connect(lambda x : self.updateAssetsList())
        self.main_ui.radioAllAss.clicked.connect(lambda x : self.updateAssetsList())

        self.authorize()
        self.updateProjectsList()

        #Show Window
        # self.main_ui.showMaximized()
        self.main_ui.show()
        self.main_ui.update()

        qtRectangle = self.main_ui.frameGeometry()
        centerPoint = QtWidgets.QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.main_ui.move(qtRectangle.topLeft())

    def authorize(self):
        getAdmins = "SELECT * FROM admins"
        aU = self.db.execute(getAdmins, dictionary=True)
        admins = [x['name'] for x in aU]
        debug.info(admins)
        user = args.user
        if user:
            debug.info(user)
            if user in admins:
                self.main_ui.adminBox.setEnabled(True)
                self.main_ui.radioAllAss.setEnabled(True)
            else:
                self.main_ui.adminBox.setEnabled(False)
                self.main_ui.radioAllAss.setEnabled(False)

    def updateProjectsList(self):
        self.main_ui.listWidgetProjs.clear()
        queryProj = "select projName from projects"
        projects = self.db.execute(queryProj,dictionary=True)
        if projects:
            for x in projects:
                item = QtWidgets.QListWidgetItem()
                item.setText(x['projName'])
                
                self.main_ui.listWidgetProjs.addItem(item)

    def updateAssetsList(self):
        self.main_ui.listWidgetAssets.clear()
        selected_item = self.main_ui.listWidgetProjs.currentItem()
        if selected_item is not None:
            text = selected_item.text()
            debug.info(text)
            queryAss = ""
            if self.main_ui.radioMineAss.isChecked():
                queryAss = "select * from assets where projName='{0}' and assignedUser='{1}' order by assetName".format(text,args.user)
            else:
                queryAss = "select * from assets where projName='{0}' order by assetName".format(text)
            assets = self.db.execute(queryAss,dictionary=True)
            debug.info(assets)
            if assets:
                for x in assets:
                    item_widget = assetDetailRowClass()
                    item_widget.labelUser.setText(x['assignedUser'])
                    item_widget.labelAsset.setText(x['projName']+" : "+x['assetName'])

                    item_widget.customContextMenuRequested.connect(lambda x, ui=item_widget: self.assContextMenu(ui,pos=x))

                    item = QListWidgetItemSort()
                    item.setSizeHint(item_widget.sizeHint())

                    self.main_ui.listWidgetAssets.addItem(item)
                    self.main_ui.listWidgetAssets.setItemWidget(item, item_widget)
            
            # self.main_ui.listWidgetAssets.itemClicked.connect(lambda x : self.assClicked())
            # self.main_ui.listWidgetAssets.customContextMenuRequested.connect(self.assContextMenu)
    
    def assContextMenu(self, ui, pos):
        debug.info("Asset clicked")
        # selected_item = self.main_ui.listWidgetAssets.currentItem()
        # if selected_item is not None:
        #     itemWidget = self.main_ui.listWidgetAssets.itemWidget(selected_item)
        #     text = itemWidget.labelAsset.text()
        #     debug.info(text)

        menu = QtWidgets.QMenu()
        openAction = menu.addAction("Open")
        toolsAction = menu.addAction("Tools")

        # action = menu.exec_(self.main_ui.listWidgetAssets.mapToGlobal(pos))
        action = menu.exec_(ui.mapToGlobal(pos))

        if (action == openAction):
            # self.tab_open_doubleclick()
            debug.info("Open clicked")
            assText = ui.labelAsset.text()
            debug.info(assText)
            filepath = root_folder + assText.replace(" : ", "/")
            debug.info(filepath)
            self.versionList(filepath)

        if (action == toolsAction):
            debug.info("Tools clicked")
            # currTabIndex = self.main_ui.tabWidget.currentIndex()
            # self.close_current_tab(currTabIndex)

    def versionList(self, filepath):
        debug.info("Opening version list")
        p = QProcess(parent=self.main_ui)
        processes.append(p)
        debug.info(processes)
        # p.started.connect(self.disableNewProjButt)
        p.readyReadStandardOutput.connect(self.read_out)
        p.readyReadStandardError.connect(self.read_err)
        # p.finished.connect(self.enableNewProjButt)
        # p.start(sys.executable, version_list.split())
        p.start(sys.executable + " " + version_list + " --filepath " + filepath)

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
    
    def adminTools(self):
        debug.info("Opening admin tools")
        p = QProcess(parent=self.main_ui)
        processes.append(p)
        debug.info(processes)
        p.started.connect(self.disableAdminToolsButt)
        p.readyReadStandardOutput.connect(self.read_out)
        p.readyReadStandardError.connect(self.read_err)
        p.finished.connect(self.enableAdminTooolsButt)
        p.start(sys.executable, admin_tools.split())

    def disableAdminToolsButt(self):
        self.main_ui.adminToolsButt.setEnabled(False)

    def enableAdminTooolsButt(self):
        self.updateProjectsList()
        self.main_ui.adminToolsButt.setEnabled(True)

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
    uic.loadUi(asset_details_ui,baseinstance=self)


# class FSM(QtWidgets.QFileSystemModel):
#     def __init__(self,**kwargs):
#         super(FSM, self).__init__(**kwargs)


class QListWidgetItemSort(QtWidgets.QListWidgetItem):
  def __lt__(self, other):
    return self.data(QtCore.Qt.UserRole) < other.data(QtCore.Qt.UserRole)

  def __ge__(self, other):
    return self.data(QtCore.Qt.UserRole) > other.data(QtCore.Qt.UserRole)



if __name__ == '__main__':
    setproctitle.setproctitle("RBHUS_CLONE")
    app = QtWidgets.QApplication(sys.argv)
    file = QFile(os.path.join(projDir, "stylesheet.qss"))
    file.open(QFile.ReadOnly | QFile.Text)
    stream = QTextStream(file)
    app.setStyleSheet(stream.readAll())
    window = rbhusClone()
    sys.exit(app.exec_())
