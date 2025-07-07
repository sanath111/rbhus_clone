#!/usr/bin/python3
# *-* coding: utf-8 *-*

import os
import sys
import setproctitle
import uuid
import subprocess
import shlex
# import rbhus_clone_db
# import rbhus_clone_db_sqlite
import debug
import bcrypt
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

main_ui_file = os.path.join(projDir,  "ui_files", "login_prompt.ui")

rbhus_clone = os.path.join(projDir, "rbhus_clone.py")

os.environ['QT_LOGGING_RULES'] = "qt5ct.debug=false"
os.environ['QT_SCALE_FACTOR'] = '1.4'

class loginPrompt():
    # db = rbhus_clone_db.db()
    # db = rbhus_clone_db_sqlite.db()
    def __init__(self):
    
        self.main_ui = uic.loadUi(main_ui_file)
        self.main_ui.setWindowTitle("LOGIN PROMPT")

        self.main_ui.username.clear()
        users = utils.getUsers()
        debug.info(users)
        self.main_ui.username.addItems(users)

        self.main_ui.toggle_button.setCheckable(True)
        self.main_ui.toggle_button.setFixedWidth(60)
        self.main_ui.toggle_button.toggled.connect(self.toggle_password_visibility)

        self.main_ui.loginButton.clicked.connect(lambda x : self.login())
        self.main_ui.loginButton.setShortcut(Qt.Key_Return)

        #Show Window
        self.main_ui.show()
        self.main_ui.showFullScreen()
        self.main_ui.update()

        # qtRectangle = self.main_ui.frameGeometry()
        # centerPoint = QtWidgets.QDesktopWidget().availableGeometry().center()
        # qtRectangle.moveCenter(centerPoint)
        # self.main_ui.move(qtRectangle.topLeft())

    def toggle_password_visibility(self, checked):
        if checked:
            self.main_ui.password.setEchoMode(QtWidgets.QLineEdit.EchoMode.Normal)
            self.main_ui.toggle_button.setText("Hide")
        else:
            self.main_ui.password.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
            self.main_ui.toggle_button.setText("Show")

    def login(self):
        username = self.main_ui.username.currentText().strip()
        password = self.main_ui.password.text().strip()
        debug.info(username)
        debug.info(password)

        # queryAllUsers = "SELECT name FROM users"
        # all_users = self.db.execute(queryAllUsers,dictionary=True)
        # all_users = self.db.execute(queryAllUsers, dictionary=True)
        # debug.info(all_users)
        # users = [x['name'] for x in all_users]
        users = utils.getUsers()
        debug.info(users)
        if username in users:
            # queryPassword = "SELECT * FROM users WHERE name='{0}' ".format(username)
            # passDets = self.db.execute(queryPassword,dictionary=True)
            # passDets = self.db.execute(queryPassword, dictionary=True)
            passDets = utils.getPassword(username)
            if passDets:
                # debug.info(passDets)
                storedPass = passDets.encode('utf-8')
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
    # Enable high-DPI scaling
    QtWidgets.QApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)
    QtWidgets.QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps, True)
    app = QtWidgets.QApplication(sys.argv)
    # file = QFile(os.path.join(projDir, "stylesheet.qss"))
    # file.open(QFile.ReadOnly | QFile.Text)
    # stream = QTextStream(file)
    # app.setStyleSheet(stream.readAll())
    window = loginPrompt()
    sys.exit(app.exec_())
