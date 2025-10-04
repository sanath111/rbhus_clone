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
from PyQt5.QtWidgets import QListWidgetItem, QShortcut, QGraphicsDropShadowEffect
from PyQt5.QtGui import QKeySequence, QColor
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


projDir = os.sep.join(os.path.abspath(__file__).split(os.sep)[:-1])
sys.path.append(projDir)

main_ui_file = os.path.join(projDir,  "ui_files", "login_prompt_new.ui")
style_sheet_path = os.path.join(projDir,  "stylesheets", "glass.qss")
rbhus_clone = os.path.join(projDir, "rbhus_clone.py")

#Image files
eye_closed = QtGui.QIcon(os.path.join(projDir, "image_files", "eye_closed.svg"))
eye_open = QtGui.QIcon(os.path.join(projDir, "image_files", "eye_open.svg"))
# button_image = QtGui.QIcon(os.path.join(projDir, "image_files", "button.svg"))
button_image = os.path.join(projDir, "image_files", "button.png")
logo_image = os.path.join(projDir, "image_files", "logo.png")
# bg_image = os.path.join(projDir, "image_files", "ui_ref.jpg")
bg_image = os.path.join(projDir, "image_files", "bg.png")

os.environ['QT_LOGGING_RULES'] = "qt5ct.debug=false"
os.environ['QT_SCALE_FACTOR'] = '1.0'


def apply_background_scaled(widget, image_path):
    pixmap = QtGui.QPixmap(image_path).scaled(
        widget.size(),
        QtCore.Qt.KeepAspectRatioByExpanding,
        QtCore.Qt.SmoothTransformation
    )
    palette = widget.palette()
    palette.setBrush(QtGui.QPalette.Window, QtGui.QBrush(pixmap))
    widget.setAutoFillBackground(True)
    widget.setPalette(palette)


class loginPrompt():
    def __init__(self):

        self.main_ui = uic.loadUi(main_ui_file)
        self.main_ui.setWindowTitle("LOGIN PROMPT")

        with open(style_sheet_path, "r") as sS:
            self.main_ui.setStyleSheet(sS.read())

        # Shadow Effect
        shadow_effect = QGraphicsDropShadowEffect()
        shadow_effect.setBlurRadius(30)
        shadow_effect.setXOffset(0)
        shadow_effect.setYOffset(10)
        shadow_effect.setColor(QColor(0, 0, 0, 30))
        self.main_ui.group_box.setGraphicsEffect(shadow_effect)
        # self.main_ui.setAttribute(Qt.WA_TranslucentBackground)

        # Background image
        apply_background_scaled(self.main_ui, bg_image)

        def resizeEvent(event):
            apply_background_scaled(self.main_ui, bg_image)
            QWidget.resizeEvent(self.main_ui, event)
        self.main_ui.resizeEvent = resizeEvent

        # self.main_ui.username.clear()
        # users = utils.getUsers()
        # debug.info(users)
        # self.main_ui.username.addItems(users)

        self.main_ui.username.setPlaceholderText("Username")
        self.main_ui.password.setPlaceholderText("Password")

        # self.main_ui.toggle_button.setCheckable(True)
        # # self.main_ui.toggle_button.setFixedSize(20, 20)
        # self.main_ui.toggle_button.setIcon(eye_closed)
        # # self.main_ui.toggle_button.setIconSize(self.main_ui.toggle_button.size())
        # self.main_ui.toggle_button.toggled.connect(self.toggle_password_visibility)

        self.main_ui.logo_label.setFixedSize(460, 460)
        # self.main_ui.logo_label.setPixmap(QPixmap(logo_image).scaled(460, 460))
        # print(self.main_ui.logo_label.size())
        self.main_ui.logo_label.setPixmap(QPixmap(logo_image).scaled(self.main_ui.logo_label.size()))
        self.main_ui.logo_label.setPixmap(QPixmap(logo_image))

        self.main_ui.login_button.setFixedSize(120, 120)
        self.main_ui.login_button.setIcon(QtGui.QIcon(button_image))
        self.main_ui.login_button.setIconSize(self.main_ui.login_button.size())
        self.main_ui.login_button.clicked.connect(lambda x : self.login())
        self.main_ui.login_button.setShortcut(Qt.Key_Return)

        self.main_ui.group_box.setFixedSize(920, 436)
        self.main_ui.username.setFixedSize(470, 64)
        self.main_ui.password.setFixedSize(470, 64)

        # self.main_ui.main_frame.setStyleSheet(""" QFrame { border: 0px; padding: 0px ; margin: 0px; } """)
        # self.main_ui.logo_frame.setStyleSheet(""" QFrame { border: 0px; padding: 0px ; margin: 0px; } """)
        # self.main_ui.login_frame.setStyleSheet(""" QFrame { border: 0px; padding: 0px ; margin: 0px; } """)
        self.main_ui.logo_label.setStyleSheet(""" QLabel { border: 0px; padding: 0px ; margin: 0px; } """)
        self.main_ui.group_box.setStyleSheet(""" QGroupBox { padding: 0px ; margin: 0px; } """)
        self.main_ui.username.setStyleSheet(""" QLineEdit { padding: 0px ; margin: 0px; } """)
        self.main_ui.password.setStyleSheet(""" QLineEdit { padding: 0px ; margin: 0px; } """)
        self.main_ui.login_button.setStyleSheet(""" QButton { border: 0px; padding: 0px ; margin: 0px; } """)
        self.main_ui.messageLabel.setStyleSheet(""" QLabel { border: 0px; padding: 0px ; margin: 0px; } """)

        # self.main_ui.group_box.setStyleSheet(""" QGroupBox { background: transparent; } """)
        # self.main_ui.username.setStyleSheet(""" QLineEdit { background: transparent; } """)
        # self.main_ui.password.setStyleSheet(""" QLineEdit { background: transparent; } """)

        # self.main_ui.password_frame.setStyleSheet(""" QFrame { background: #ffffff; border: 1.5px solid rgba(0, 0, 0, 0.1); border-radius: 10px; padding: 0px -20px; margin: 0px; } """)
        # self.main_ui.password.setStyleSheet(""" QLineEdit { border: none; padding: 12px 15px; margin: 0px; background: transparent; } """)
        # self.main_ui.toggle_button.setStyleSheet(""" QToolButton { border: none; padding: 12px 15px 12px 5px; margin: 0px; background: transparent; } """)
        #
        # layout = self.main_ui.password_frame.layout()
        # if layout:
        #     layout.setContentsMargins(0, 0, 0, 0)
        #     layout.setSpacing(0)

        # Show Window
        # self.main_ui.show()
        self.main_ui.showFullScreen()
        # self.main_ui.showMaximized()
        self.main_ui.update()

        # qtRectangle = self.main_ui.frameGeometry()
        # centerPoint = QtWidgets.QDesktopWidget().availableGeometry().center()
        # qtRectangle.moveCenter(centerPoint)
        # self.main_ui.move(qtRectangle.topLeft())

    def toggle_password_visibility(self, checked):
        if checked:
            self.main_ui.password.setEchoMode(QtWidgets.QLineEdit.EchoMode.Normal)
            self.main_ui.toggle_button.setIcon(eye_open)
            # self.main_ui.toggle_button.setText("Hide")
        else:
            self.main_ui.password.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
            self.main_ui.toggle_button.setIcon(eye_closed)
            # self.main_ui.toggle_button.setText("Show")

    def login(self):
        # username = self.main_ui.username.currentText().strip()
        username = self.main_ui.username.text().strip()
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
