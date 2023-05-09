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

main_ui_file = os.path.join(projDir,  "ui_files", "admin_tools.ui")

# root_folder = "/home/sanath.shetty/Documents/rbhus_clone_root/"

os.environ['QT_LOGGING_RULES'] = "qt5ct.debug=false"


class adminTools():
    db = rbhus_clone_db.db()
    def __init__(self):
       
        self.main_ui = uic.loadUi(main_ui_file)
        self.main_ui.setWindowTitle("ADMIN TOOLS")

        self.setUsers()
        
        self.main_ui.makeAdminButt.clicked.connect(lambda x : self.makeAdmin())

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

    def makeAdmin(self):
        user = self.main_ui.userBox.currentText()
        debug.info(user)
        if user:
            try:
                adminUpdateQuery = "insert into admins (name) values (\"{0}\") ".format(user)
                updateAdminList = self.db.execute(adminUpdateQuery)
                debug.info(updateAdminList)
                if updateAdminList == 1:
                    debug.info("User added to admin list")
                    self.main_ui.messageLabel.setText("User added to admin list")
            except:
                err_mess = str(sys.exc_info())
                debug.info(err_mess)
                if "Duplicate entry" in err_mess:
                    debug.info("Duplicate entry")
                    self.main_ui.messageLabel.setText("User is already an admin")
        else:
            debug.info("Please select an user")
            self.main_ui.messageLabel.setText("Please select an user")


if __name__ == '__main__':
    setproctitle.setproctitle("ADMIN_TOOLS")
    app = QtWidgets.QApplication(sys.argv)
    file = QFile(os.path.join(projDir, "stylesheet.qss"))
    file.open(QFile.ReadOnly | QFile.Text)
    stream = QTextStream(file)
    app.setStyleSheet(stream.readAll())
    window = adminTools()
    sys.exit(app.exec_())
