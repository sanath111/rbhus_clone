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
import bcrypt

from PyQt5 import QtCore, uic, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QTreeView, QFileSystemModel, QVBoxLayout, QWidget, QHBoxLayout, QListView
from PyQt5.QtWidgets import QListWidgetItem, QShortcut
from PyQt5.QtGui import QKeySequence
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


projDir = os.sep.join(os.path.abspath(__file__).split(os.sep)[:-1])
sys.path.append(projDir)

main_ui_file = os.path.join(projDir,  "ui_files", "login_prompt.ui")

rbhus_clone = os.path.join(projDir, "rbhus_clone.py")

os.environ['QT_LOGGING_RULES'] = "qt5ct.debug=false"


class loginPrompt():
    db = rbhus_clone_db.db()
    def __init__(self):
    
        self.main_ui = uic.loadUi(main_ui_file)
        self.main_ui.setWindowTitle("LOGIN PROMPT")
        
        self.main_ui.loginButton.clicked.connect(lambda x : self.login())
        self.main_ui.loginButton.setShortcut(Qt.Key_Return)

        #Show Window
        self.main_ui.show()
        self.main_ui.update()

        qtRectangle = self.main_ui.frameGeometry()
        centerPoint = QtWidgets.QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.main_ui.move(qtRectangle.topLeft())

    def login(self):
        username = self.main_ui.username.text()
        password = self.main_ui.password.text()
        debug.info(username)
        debug.info(password)

        queryAllUsers = "select name from users"
        all_users = self.db.execute(queryAllUsers,dictionary=True)
        users = [x['name'] for x in all_users]
        debug.info(users)
        if username in users:
            queryPassword = "select * from users where name='{0}' ".format(username)
            passDets = self.db.execute(queryPassword,dictionary=True)
            if passDets:
                debug.info(passDets)
                storedPass = passDets[0]['password'].encode('utf-8')
                debug.info(storedPass)

                if bcrypt.checkpw(password.encode('utf-8'), storedPass):
                    debug.info("Password matched")
                    self.main_ui.messageLabel.setText("Password matched")
                    self.main_ui.close()
                    subprocess.run(sys.executable + " " + rbhus_clone + " -u " + username, shell=True)
                else:
                    debug.info("Wrong password")
                    self.main_ui.messageLabel.setText("Password does not match")
        else:
            debug.info("User does not exists")
            self.main_ui.messageLabel.setText("User does not exists")


if __name__ == '__main__':
    setproctitle.setproctitle("LOGIN_PROMPT")
    app = QtWidgets.QApplication(sys.argv)
    file = QFile(os.path.join(projDir, "stylesheet.qss"))
    file.open(QFile.ReadOnly | QFile.Text)
    stream = QTextStream(file)
    app.setStyleSheet(stream.readAll())
    window = loginPrompt()
    sys.exit(app.exec_())