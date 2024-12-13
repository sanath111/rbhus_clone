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

main_ui_file = os.path.join(projDir, "ui_files", "edit_asset.ui")

# root_folder = "/home/sanath.shetty/Documents/rbhus_clone_root/"

os.environ['QT_LOGGING_RULES'] = "qt5ct.debug=false"

parser = argparse.ArgumentParser(description="Utility to manage versions")
# parser.add_argument("-a","--asset",dest="asset",help="asset name")
parser.add_argument("-a","--ass_id",dest="ass_id",help="asset id")
parser.add_argument("-u","--user",dest="user",help="user")
args = parser.parse_args()

class editAsset():
    # db = rbhus_clone_db.db()
    def __init__(self):
       
        self.main_ui = uic.loadUi(main_ui_file)
        self.main_ui.setWindowTitle("EDIT ASSET")

        # self.asset = args.asset
        # self.projName = self.asset.split(" : ")[0]
        # self.stage = self.asset.split(" : ")[1]
        # debug.info(self.asset)
        # debug.info(self.projName)
        # debug.info(self.stage)

        self.ass_id = args.ass_id
        self.ass_dets = utils.getAssDetsByAssId(self.ass_id)
        debug.info(self.ass_dets)
        self.ass_path = self.ass_dets['path']
        self.proj_name = self.ass_dets['projName']
        self.stage_name = self.ass_dets['stage']
        self.ass_user = self.ass_dets['assignedUser']


        self.fillDetails()
        self.setUsers()
        
        self.main_ui.assignButt.clicked.connect(lambda x : self.assignAsset())

        #Show Window
        self.main_ui.show()
        self.main_ui.showMaximized()
        self.main_ui.update()

        qtRectangle = self.main_ui.frameGeometry()
        centerPoint = QtWidgets.QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.main_ui.move(qtRectangle.topLeft())

    def fillDetails(self):
        self.main_ui.assetBox.setText(" : ".join([self.proj_name, self.stage_name]))
        # queryGetUser = "select assignedUser from assets where projName='{0}' and stage='{1}'".format(self.proj_name,self.stage_name)
        # debug.info(queryGetUser)
        # assets = self.db.execute(queryGetUser,dictionary=True)
        # assignedUser = str(assets[0]["assignedUser"])
        assignedUser = utils.getAssUser(self.ass_id)
        debug.info(assignedUser)
        self.main_ui.currUserBox.setText(assignedUser)

    def setUsers(self):
        # queryUsers = "select * from users"
        # assets = self.db.execute(queryUsers,dictionary=True)
        # users = [x['name'] for x in assets]
        users = utils.getUsers()
        debug.info(users)
        self.main_ui.newUserBox.addItems(users)

    def assignAsset(self):
        new_user = self.main_ui.newUserBox.currentText().strip()
        debug.info(new_user)
        if new_user:
            try:
                # updateUserQuery = "update assets set assignedUser='{0}' where projName='{1}' and stage='{2}'".format(user,self.proj_name,self.stage_name)
                # updateAssignedUser = self.db.execute(updateUserQuery)
                update_ass_user_result = utils.updateAssUser(self.proj_name, self.stage_name, new_user)
                debug.info(update_ass_user_result)
                if update_ass_user_result == 1:
                    debug.info("Assigned user updated")
                    self.fillDetails()
                    self.main_ui.messageLabel.setText("Assigned user updated")
            except:
                debug.info(str(sys.exc_info()))
        else:
            debug.info("Please select an user")
            self.main_ui.messageLabel.setText("Please select an user")


if __name__ == '__main__':
    setproctitle.setproctitle("EDIT_ASSET")
    app = QtWidgets.QApplication(sys.argv)
    # file = QFile(os.path.join(projDir, "stylesheet.qss"))
    # file.open(QFile.ReadOnly | QFile.Text)
    # stream = QTextStream(file)
    # app.setStyleSheet(stream.readAll())
    window = editAsset()
    sys.exit(app.exec_())
