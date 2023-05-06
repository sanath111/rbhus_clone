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

main_ui_file = os.path.join(projDir, "edit_asset.ui")

root_folder = "/home/sanath.shetty/Documents/rbhus_clone_root/"

os.environ['QT_LOGGING_RULES'] = "qt5ct.debug=false"

parser = argparse.ArgumentParser(description="Utility to manage versions")
parser.add_argument("-a","--asset",dest="asset",help="asset name")
args = parser.parse_args()

class editAsset():
    db = rbhus_clone_db.db()
    def __init__(self):
       
        self.main_ui = uic.loadUi(main_ui_file)
        self.main_ui.setWindowTitle("EDIT ASSET")

        self.asset = args.asset
        self.projName = self.asset.split(" : ")[0]
        self.assetName = self.asset.split(" : ")[1]
        debug.info(self.asset)
        debug.info(self.projName)
        debug.info(self.assetName)

        self.fillDetails()
        self.setUsers()
        
        self.main_ui.assignButt.clicked.connect(lambda x : self.assignAsset())

        #Show Window
        self.main_ui.show()
        self.main_ui.update()

        qtRectangle = self.main_ui.frameGeometry()
        centerPoint = QtWidgets.QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.main_ui.move(qtRectangle.topLeft())

    def fillDetails(self):
        self.main_ui.assetBox.setText(self.asset)
        queryGetUser = "select assignedUser from assets where projName='{0}' and assetName='{1}'".format(self.projName,self.assetName)
        debug.info(queryGetUser)
        assets = self.db.execute(queryGetUser,dictionary=True)
        assignedUser = str(assets[0]["assignedUser"])
        debug.info(assignedUser)
        self.main_ui.currUserBox.setText(assignedUser)

    def setUsers(self):
        queryUsers = "select * from users"
        assets = self.db.execute(queryUsers,dictionary=True)
        users = [x['name'] for x in assets]
        debug.info(users)
        self.main_ui.newUserBox.addItems(users)

    def assignAsset(self):
        user = self.main_ui.newUserBox.currentText()
        debug.info(user)
        if user:
            try:
                updateUserQuery = "update assets set assignedUser='{0}' where projName='{1}' and assetName='{2}'".format(user,self.projName,self.assetName)
                updateAssignedUser = self.db.execute(updateUserQuery)
                debug.info(updateAssignedUser)
                if updateAssignedUser == 1:
                    debug.info("Assigned user updated")
                    self.main_ui.messageLabel.setText("Assigned user updated")
            except:
                debug.info(str(sys.exc_info()))
        else:
            debug.info("Please select an user")
            self.main_ui.messageLabel.setText("Please select an user")


if __name__ == '__main__':
    setproctitle.setproctitle("EDIT_ASSET")
    app = QtWidgets.QApplication(sys.argv)
    file = QFile(os.path.join(projDir, "stylesheet.qss"))
    file.open(QFile.ReadOnly | QFile.Text)
    stream = QTextStream(file)
    app.setStyleSheet(stream.readAll())
    window = editAsset()
    sys.exit(app.exec_())
