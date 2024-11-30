#!/usr/bin/python3
# *-* coding: utf-8 *-*

import os
import sys
import setproctitle
import subprocess
# import rbhus_clone_db
# import rbhus_clone_db_sqlite
import debug
import argparse
import getpass
from pathlib import Path

from PyQt5 import QtCore, uic, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QTreeView, QFileSystemModel, QVBoxLayout, QWidget, QHBoxLayout, QListView
from PyQt5.QtWidgets import QListWidgetItem, QShortcut
from PyQt5.QtGui import QKeySequence
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

import constants
import utils

projDir = os.sep.join(os.path.abspath(__file__).split(os.sep)[:-1])
sys.path.append(projDir)

main_ui_file = os.path.join(projDir, "ui_files", "rbhus_clone.ui")
asset_details_ui = os.path.join(projDir, "ui_files", "asset_details_row.ui")

# root_folder = r"Z:\share\sanath\rbhus_clone_root"
# root_folder = r"C:\Users\aum\Documents\rbhus_clone_root"
root_folder = constants.root_folder

new_project = os.path.join(projDir, "new_project.py")
admin_tools = os.path.join(projDir, "admin_tools.py")
version_list = os.path.join(projDir, "version_list.py")
edit_asset = os.path.join(projDir, "edit_asset.py")
login_prompt = os.path.join(projDir, "login_prompt.py")
processes = []

os.environ['QT_LOGGING_RULES'] = "qt5ct.debug=false"

# user = os.environ['USER']
system_user = getpass.getuser()
debug.info(system_user)

parser = argparse.ArgumentParser(description="Utility to manage assets")
parser.add_argument("-u","--user",dest="user",help="user")
args = parser.parse_args()


class rbhusClone():
    # db = rbhus_clone_db.db()
    # db = rbhus_clone_db_sqlite.db()
    def __init__(self):
       
        self.main_ui = uic.loadUi(main_ui_file)
        self.main_ui.setWindowTitle("RBHUS CLONE")
        # self.main_ui.setWindowIcon(QtGui.QIcon(os.path.join(projDir, "imageFiles", "new_icons" , "folder.svg")))


        self.main_ui.newProjectButt.clicked.connect(lambda x : self.newProject())
        self.main_ui.adminToolsButt.clicked.connect(lambda x : self.adminTools())
        
        self.main_ui.listWidgetProjs.itemClicked.connect(lambda x : self.updateAssetsList())
        self.main_ui.listWidgetAssets.itemClicked.connect(self.updateStatusLabel)

        self.main_ui.radioMineAss.clicked.connect(lambda x : self.updateAssetsList())
        self.main_ui.radioAllAss.clicked.connect(lambda x : self.updateAssetsList())

        self.main_ui.logoutButton.clicked.connect(lambda x : self.logout())

        # self.master_admin = []
        # self.admins = []
        self.master_admin, self.admins = utils.getAdmins()
        self.user = "nobody"
        self.role = "none"
        try:
            if args.user:
                self.user = args.user
                # get_role_cmd = f"SELECT role FROM users WHERE name='{self.user}'"
                # role = self.db.execute(get_role_cmd, dictionary=True)
                # self.role = role[0]['role']
                self.role = utils.getRole(self.user)
            else:
                self.user = system_user
        except:
            pass

        self.main_ui.usernameLabel.setText(self.user)

        # self.getAdmins()
        self.authorize()
        self.updateProjectsList()

        if self.user not in self.admins:
            self.main_ui.radioMineAss.setChecked(True)
            # self.main_ui.radioAllAss.setChecked(True)

        #Show Window
        self.main_ui.show()
        # self.main_ui.showMaximized()
        # self.main_ui.showFullScreen()
        self.main_ui.update()

        qtRectangle = self.main_ui.frameGeometry()
        centerPoint = QtWidgets.QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.main_ui.move(qtRectangle.topLeft())

    # def getAdmins(self):
    #     # get_master_admin = "SELECT * FROM master_admin"
    #     get_user_details = "SELECT * FROM users"
    #     user_dets = self.db.execute(get_user_details, dictionary=True)
    #     self.master_admin = [x['name'] for x in user_dets if x['role'] == "master_admin"]
    #     debug.info(self.master_admin)
    #
    #     # get_admins = "SELECT * FROM admins"
    #     # aU = self.db.execute(get_admins, dictionary=True)
    #     self.admins = [x['name'] for x in user_dets if  x['role'] == "admin" or x['role'] == "master_admin"]
    #     debug.info(self.admins)

    def authorize(self):
        """
        Decide who has access to what
        """
        # get_master_admin = "SELECT * FROM master_admin"
        # mAU = self.db.execute(get_master_admin, dictionary=True)
        # master_admin = [x['name'] for x in mAU]
        # debug.info(master_admin)

        # get_admins = "SELECT * FROM admins"
        # aU = self.db.execute(get_admins, dictionary=True)
        # admins = [x['name'] for x in aU]
        # debug.info(admins)

        user = self.user
        if user:
            debug.info(user)
            if user in self.master_admin:
                self.main_ui.radioAllAss.setEnabled(True)
                self.main_ui.adminBox.setEnabled(True)
                self.main_ui.newProjectButt.setEnabled(True)
                self.main_ui.adminToolsButt.setEnabled(True)
            elif user in self.admins:
                self.main_ui.radioAllAss.setEnabled(True)
                self.main_ui.adminBox.setEnabled(True)
                self.main_ui.newProjectButt.setEnabled(True)
                self.main_ui.adminToolsButt.setEnabled(False)
            else:
                self.main_ui.adminBox.setEnabled(False)
                self.main_ui.radioAllAss.setEnabled(False)
                self.main_ui.newProjectButt.setEnabled(False)
                self.main_ui.adminToolsButt.setEnabled(False)

        # gitConfigCmd = "git config --global user.email \"{0}\" & git config --global user.name \"{1}\" ".format("sanathshetty111@gmail.com","sanath111")
        # debug.info(gitConfigCmd)
        # subprocess.run(gitConfigCmd, shell=True)


    def updateProjectsList(self):
        self.main_ui.listWidgetProjs.clear()
        # queryProj = "select projName from projects"
        # projects = self.db.execute(queryProj,dictionary=True)
        projects = utils.getProjNames()
        debug.info(projects)
        if projects:
            for x in projects:
                item = QtWidgets.QListWidgetItem()
                item.setText(x['projName'])
                
                self.main_ui.listWidgetProjs.addItem(item)

    def updateAssetsList(self):
        self.main_ui.listWidgetAssets.clear()
        selected_item = self.main_ui.listWidgetProjs.currentItem()
        if selected_item is not None:
            proj_text = selected_item.text()
            debug.info(proj_text)
            proj_status = utils.getProjStatus(proj_text)
            debug.info(proj_status)
            proj_status_stage = utils.getStageName(proj_status)
            self.main_ui.statusLabel.setText(f"Project Status: In {proj_status_stage}")

            # queryAss = ""
            if self.main_ui.radioMineAss.isChecked():
                assets = utils.getAssDetsByProjName(proj_text, ass_user=self.user)
                # queryAss = "select * from assets where projName='{0}' and assignedUser='{1}' order by stage".format(proj_text,self.user)
            else:
                assets = utils.getAssDetsByProjName(proj_text)
            #     queryAss = "select * from assets where projName='{0}' order by stage".format(proj_text)
            # assets = self.db.execute(queryAss,dictionary=True)
            debug.info(assets)
            if assets:
                for x in assets:
                    item_widget = assetDetailRowClass()
                    item_widget.labelUser.setText(x['assignedUser'])
                    # item_widget.labelAsset.setText(x['projName']+" : "+x['stage'])
                    item_widget.labelProject.setText(x['projName'])
                    item_widget.labelStage.setText(x['stage'])

                    item_widget.customContextMenuRequested.connect(lambda x, ui=item_widget: self.assContextMenu(ui,pos=x))

                    item = QListWidgetItemSort()
                    item.setSizeHint(item_widget.sizeHint())

                    self.main_ui.listWidgetAssets.addItem(item)
                    self.main_ui.listWidgetAssets.setItemWidget(item, item_widget)
            
            # self.main_ui.listWidgetAssets.itemClicked.connect(lambda x : self.assClicked())
            # self.main_ui.listWidgetAssets.customContextMenuRequested.connect(self.assContextMenu)

    def updateStatusLabel(self):
        selected_item = self.main_ui.listWidgetProjs.currentItem()
        if selected_item is not None:
            proj_text = selected_item.text()
            proj_status = utils.getProjStatus(proj_text)
            proj_status_stage = utils.getStageName(proj_status)
            self.main_ui.statusLabel.setText(f"Project Status: In {proj_status_stage}")

    def assContextMenu(self, ui, pos):
        debug.info("Asset clicked")
        cur_proj = ui.labelProject.text()
        cur_stage = ui.labelStage.text()
        # selected_item = self.main_ui.listWidgetAssets.currentItem()
        # if selected_item is not None:
        #     itemWidget = self.main_ui.listWidgetAssets.itemWidget(selected_item)
        #     text = itemWidget.labelAsset.text()
        #     debug.info(text)

        menu = QtWidgets.QMenu()
        menuTools = QtWidgets.QMenu()
        # menuPush = QtWidgets.QMenu()

        menuTools.setTitle("Tools")
        # menuPush.setTitle("Send To")
        openAction = menu.addAction("Open")
        editAction = menuTools.addAction("Edit")

        # sub_action_dict = {}
        #
        # get_stages_cmd = "select stage from assets where projName='{0}'".format(cur_proj)
        # stages = self.db.execute(get_stages_cmd, dictionary=True)
        # for x in stages:
        #     if not x['stage'] == cur_stage:
        #         get_access_cmd = "select access from stages where name='{0}'".format(x['stage'])
        #         accesses = self.db.execute(get_access_cmd, dictionary=True)
        #         if self.role in accesses[0]['access']:
        #             sub_action = menuPush.addAction(x['stage'])
        #             sub_action_dict[x['stage']] = sub_action

        if self.user in self.admins:
            menu.addMenu(menuTools)
        # if self.user == ui.labelUser.text():
        #     menu.addMenu(menuPush)

        action = menu.exec_(ui.mapToGlobal(pos))

        # for x in sub_action_dict:
        #     if action == sub_action_dict[x]:
        #         debug.info("Push to "+x+" clicked")
        #         self.pushAsset(x, cur_proj, cur_stage)

        if action == openAction:
            debug.info("Open clicked")
            # filepath = os.path.join(root_folder, cur_proj, cur_stage)
            # assText = " : ".join([cur_proj, cur_stage])
            # debug.info(filepath)
            ass_id = utils.getAssID(proj_name=cur_proj, stage_name=cur_stage)
            debug.info(ass_id)
            self.versionList(ass_id)

        if action == editAction:
            debug.info("Edit clicked")
            # ass_name = " : ".join([cur_proj, cur_stage])
            # debug.info(ass_name)
            # self.editAsset(ass_name)
            ass_id = utils.getAssID(proj_name=cur_proj, stage_name=cur_stage)
            debug.info(ass_id)
            self.editAsset(ass_id)

    # def pushAsset(self, stage, cur_proj, cur_stage):
    #     source_path = os.path.join(root_folder, cur_proj, cur_stage)
    #     dest_path = os.path.join(root_folder, cur_proj, stage)
    #     if os.name == 'nt':
    #         paste_audio_cmd = f"cmd /c copy \"{os.path.join(source_path, cur_proj + '_source.mp3')}\" \"{dest_path}\" /Y"
    #         paste_doc_cmd = f"cmd /c copy \"{os.path.join(source_path, cur_proj + '_'+cur_stage+'.docx')}\" \"{os.path.join(dest_path, cur_proj + '_'+stage+'.docx')}\" /Y "
    #     else:
    #         paste_audio_cmd = f"rsync -azHXW --info=progress2 \"{os.path.join(source_path, cur_proj + '_source.mp3')}\" \"{os.path.join(dest_path, cur_proj + '_source.mp3')}\""
    #         paste_doc_cmd = f"rsync -azHXW --info=progress2 \"{os.path.join(source_path, cur_proj + '_'+cur_stage+'.docx')}\" \"{os.path.join(dest_path, cur_proj + '_'+stage+'.docx')}\""
    #
    #     self.run_command(paste_audio_cmd)
    #     self.run_command(paste_doc_cmd)
    #     self.commitChanges(dest_path)
    #
    # def commitChanges(self, dest_path):
    #     cmd_separator = '&' if os.name == 'nt' else '&&'
    #
    #     init_hg_cmd = (
    #         f"hg add --cwd \"{dest_path}\" . {cmd_separator} "
    #         f"hg commit --cwd \"{dest_path}\" -m  \"new_commit\" --user {self.user}"
    #     )
    #
    #     self.run_command(init_hg_cmd)
    #
    # def run_command(self, cmd):
    #     debug.info(cmd)
    #     try:
    #         result = subprocess.run(cmd, shell=True, check=True, text=True,
    #                                 stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    #         debug.info(result.stdout.strip())
    #     except subprocess.CalledProcessError as e:
    #         debug.info(f"Command failed with error: {e.stderr}")

    def versionList(self, ass_id):
        debug.info("Opening version list")
        p = QProcess(parent=self.main_ui)
        processes.append(p)
        debug.info(processes)
        # p.started.connect(self.disableNewProjButt)
        # p.readyReadStandardOutput.connect(self.read_out)
        # p.readyReadStandardError.connect(self.read_err)
        p.readyReadStandardOutput.connect(lambda: debug.info(p.readAllStandardOutput().data().decode()))
        p.readyReadStandardError.connect(lambda: debug.info(p.readAllStandardError().data().decode()))
        # p.finished.connect(self.enableNewProjButt)
        p.start(sys.executable, [version_list, "--ass_id", ass_id, "--user", self.user])

    def editAsset(self, ass_id):
        debug.info("Opening edit asset")
        p = QProcess(parent=self.main_ui)
        processes.append(p)
        debug.info(processes)
        # p.readyReadStandardOutput.connect(self.read_out)
        # p.readyReadStandardError.connect(self.read_err)
        p.readyReadStandardOutput.connect(lambda: debug.info(p.readAllStandardOutput().data().decode()))
        p.readyReadStandardError.connect(lambda: debug.info(p.readAllStandardError().data().decode()))
        p.finished.connect(self.updateAssetsList)
        # p.start(sys.executable + " " + edit_asset + " --asset " + "\""+ass_name+"\"")
        p.start(sys.executable, [edit_asset, "--ass_id", ass_id, "--user", self.user])

    def newProject(self):
        debug.info("Opening new project")
        p = QProcess(parent=self.main_ui)
        processes.append(p)
        debug.info(processes)
        p.started.connect(self.disableNewProjButt)
        # p.readyReadStandardOutput.connect(self.read_out)
        # p.readyReadStandardError.connect(self.read_err)
        p.readyReadStandardOutput.connect(lambda: debug.info(p.readAllStandardOutput().data().decode()))
        p.readyReadStandardError.connect(lambda: debug.info(p.readAllStandardError().data().decode()))
        p.finished.connect(self.enableNewProjButt)
        p.start(sys.executable, [new_project, "--user", self.user])

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
        # p.readyReadStandardOutput.connect(self.read_out)
        # p.readyReadStandardError.connect(self.read_err)
        p.readyReadStandardOutput.connect(lambda: debug.info(p.readAllStandardOutput().data().decode()))
        p.readyReadStandardError.connect(lambda: debug.info(p.readAllStandardError().data().decode()))
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

    def logout(self):
        self.main_ui.close()
        debug.info("Opening login prompt")
        subprocess.run(sys.executable + " " + login_prompt, shell=True)


class assetDetailRowClass(QtWidgets.QWidget):
  def __init__(self,parent=None):
    super(assetDetailRowClass, self).__init__(parent)
    uic.loadUi(asset_details_ui,baseinstance=self)

    # sS = open(os.path.join(projDir, "stylesheet.qss"), "r")
    # details_ui.setStyleSheet(sS.read())
    # sS.close()

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
    # file = QFile(os.path.join(projDir, "stylesheet.qss"))
    # file.open(QFile.ReadOnly | QFile.Text)
    # stream = QTextStream(file)
    # app.setStyleSheet(stream.readAll())
    window = rbhusClone()
    sys.exit(app.exec_())

