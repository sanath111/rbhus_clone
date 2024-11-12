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

main_ui_file = os.path.join(projDir,  "ui_files", "admin_tools.ui")

# root_folder = "/home/sanath.shetty/Documents/rbhus_clone_root/"

os.environ['QT_LOGGING_RULES'] = "qt5ct.debug=false"


class adminTools():
    db = rbhus_clone_db.db()
    def __init__(self):
       
        self.main_ui = uic.loadUi(main_ui_file)
        self.main_ui.setWindowTitle("ADMIN TOOLS")

        self.setUsers()
        self.setRoles()
        
        self.main_ui.addUserButt.clicked.connect(lambda x : self.addUser())
        self.main_ui.changePasswordButt.clicked.connect(lambda x : self.changePassword())
        self.main_ui.chanageRoleButt.clicked.connect(lambda x : self.changeRole())
        self.main_ui.userList_chrole.currentIndexChanged.connect(lambda x : self.updateRole())

        #Show Window
        self.main_ui.show()
        self.main_ui.update()

        qtRectangle = self.main_ui.frameGeometry()
        centerPoint = QtWidgets.QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.main_ui.move(qtRectangle.topLeft())

    def setUsers(self):
        self.main_ui.userList_chpwd.clear()
        self.main_ui.userList_chrole.clear()
        queryUsers = "select * from users"
        assets = self.db.execute(queryUsers,dictionary=True)
        users = [x['name'] for x in assets]
        debug.info(users)
        self.main_ui.userList_chpwd.addItems(users)
        self.main_ui.userList_chrole.addItems(users)

    def setRoles(self):
        self.main_ui.roleList_adusr.clear()
        self.main_ui.roleList_chrole.clear()
        queryRoles = "select * from roles"
        assets = self.db.execute(queryRoles,dictionary=True)
        roles = [x['role'] for x in assets]
        debug.info(roles)
        self.main_ui.roleList_adusr.addItems(roles)
        self.main_ui.roleList_chrole.addItems(roles)

    def addUser(self):
        username = self.main_ui.usernameBox.text()
        password = self.main_ui.passwordBox.text()
        role = self.main_ui.roleList_adusr.currentText()

        if username:
            if password:
                debug.info(username)
                debug.info(password)
                debug.info(role)
                try:
                    password = password.encode('utf-8')
                    salt = bcrypt.gensalt()
                    hashed_password = bcrypt.hashpw(password, salt)
                    hashed_password = hashed_password.decode('utf-8')
                    debug.info(hashed_password)
                    userUpdateQuery = "insert into users (name,password,role) values (\"{0}\",\"{1}\",\"{2}\") ".format(username, hashed_password,role)
                    debug.info(userUpdateQuery)
                    try:
                        reply = QMessageBox.question(self.main_ui, 'Confirmation',
                                                     'Are you sure you want to create user?',
                                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
                        if reply == QMessageBox.Yes:
                            updateUserList = self.db.execute(userUpdateQuery)
                            debug.info(updateUserList)
                            if updateUserList == 1:
                                debug.info("User created")
                                self.main_ui.messageLabel.setText("User Created")
                                self.setUsers()
                            elif "Duplicate entry" in updateUserList:
                                self.main_ui.messageLabel.setText("User already exists")
                        else:
                            return
                    except:
                        debug.info(str(sys.exc_info()))
                except:
                    debug.info(str(sys.exc_info()))
            else:
                debug.info("No password")
                self.main_ui.messageLabel.setText("Please provide a password")
        else:
            debug.info("No username")
            self.main_ui.messageLabel.setText("Please provide a valid username")

    def changePassword(self):
        username = self.main_ui.userList_chpwd.currentText()
        old_password = self.main_ui.oldPasswordBox.text()
        new_password = self.main_ui.newPasswordBox.text()
        if username:
            queryAllUsers = "select name from users"
            all_users = self.db.execute(queryAllUsers,dictionary=True)
            users = [x['name'] for x in all_users]
            debug.info(users)
            if username in users:
                if old_password:
                    queryPassword = "select * from users where name='{0}' ".format(username)
                    passDets = self.db.execute(queryPassword,dictionary=True)
                    if passDets:
                        storedPass = passDets[0]['password'].encode('utf-8')
                        debug.info(storedPass)
                        if bcrypt.checkpw(old_password.encode('utf-8'), storedPass):
                            debug.info("Password matched")
                            if new_password:
                                if new_password == old_password:
                                    debug.info("Same Password")
                                    self.main_ui.messageLabel.setText("Please provide different passwords")
                                else:
                                    try:
                                        new_password = new_password.encode('utf-8')
                                        salt = bcrypt.gensalt()
                                        hashed_password = bcrypt.hashpw(new_password, salt)
                                        hashed_password = hashed_password.decode('utf-8')
                                        debug.info(hashed_password)
                                        passwordUpdateQuery = "update users set password='{0}' where name='{1}' ".format(hashed_password, username)
                                        debug.info(passwordUpdateQuery)
                                        try:
                                            reply = QMessageBox.question(self.main_ui, 'Confirmation',
                                                                         'Are you sure you want to update password?',
                                                                         QMessageBox.Yes | QMessageBox.No,
                                                                         QMessageBox.No)
                                            if reply == QMessageBox.Yes:
                                                updatePassword = self.db.execute(passwordUpdateQuery)
                                                debug.info(updatePassword)
                                                if updatePassword == 1:
                                                    debug.info("Password Updated")
                                                    self.main_ui.messageLabel.setText("Password Updated")
                                            else:
                                                return
                                        except:
                                            debug.info(str(sys.exc_info()))
                                    except:
                                        err_mess = str(sys.exc_info())
                                        debug.info(err_mess)
                                        self.main_ui.messageLabel.setText("Password not changed")
                            else:
                                debug.info("No password")
                                self.main_ui.messageLabel.setText("Please provide new password")
                        else:
                            debug.info("Password did not match")
                            self.main_ui.messageLabel.setText("Wrong password")
                else:
                    debug.info("No password")
                    self.main_ui.messageLabel.setText("Please provide old password")
            else:
                debug.info("User does not exists")
                self.main_ui.messageLabel.setText("User does not exists")
        else:
            debug.info("No username")
            self.main_ui.messageLabel.setText("Please provide a valid username")

    def updateRole(self):
        user = self.main_ui.userList_chrole.currentText()
        getRoleQuery = "select role from users where name='{0}' ".format(user)
        debug.info(getRoleQuery)
        try:
            assets = self.db.execute(getRoleQuery, dictionary=True)
            role = assets[0]['role']
            debug.info(role)
            self.main_ui.roleList_chrole.setCurrentText(role)
        except:
            debug.info(str(sys.exc_info()))

    def changeRole(self):
        user = self.main_ui.userList_chrole.currentText()
        role = self.main_ui.roleList_chrole.currentText()
        debug.info(user)
        if user:
            try:
                userUpdateQuery = "update users set role='{0}' where name='{1}' ".format(role,user)
                debug.info(userUpdateQuery)
                reply = QMessageBox.question(self.main_ui, 'Confirmation',
                                             'Are you sure you want to update role?',
                                             QMessageBox.Yes | QMessageBox.No,
                                             QMessageBox.No)
                if reply == QMessageBox.Yes:
                    updateUserList = self.db.execute(userUpdateQuery)
                    debug.info(updateUserList)
                    if updateUserList == 1:
                        debug.info("User role updated")
                        self.main_ui.messageLabel.setText("User role updated")
                else:
                    return
            except:
                err_mess = str(sys.exc_info())
                debug.info(err_mess)
                if "Duplicate entry" in err_mess:
                    debug.info("Duplicate entry")
                    self.main_ui.messageLabel.setText("User role already exists")
        else:
            debug.info("Please select an user")
            self.main_ui.messageLabel.setText("Please select an user")


if __name__ == '__main__':
    setproctitle.setproctitle("ADMIN_TOOLS")
    app = QtWidgets.QApplication(sys.argv)
    # file = QFile(os.path.join(projDir, "stylesheet.qss"))
    # file.open(QFile.ReadOnly | QFile.Text)
    # stream = QTextStream(file)
    # app.setStyleSheet(stream.readAll())
    window = adminTools()
    sys.exit(app.exec_())
