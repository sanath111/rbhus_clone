# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\Repos\rbhus_clone\ui_files\admin_tools.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(332, 206)
        self.gridLayout_2 = QtWidgets.QGridLayout(Form)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.messageLabel = QtWidgets.QLabel(Form)
        self.messageLabel.setText("")
        self.messageLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.messageLabel.setObjectName("messageLabel")
        self.gridLayout_2.addWidget(self.messageLabel, 1, 0, 1, 1)
        self.tabWidget = QtWidgets.QTabWidget(Form)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.tab_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setMaximumSize(QtCore.QSize(80, 16777215))
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.passwordBox = QtWidgets.QLineEdit(self.tab_2)
        self.passwordBox.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwordBox.setObjectName("passwordBox")
        self.horizontalLayout_3.addWidget(self.passwordBox)
        self.gridLayout_3.addLayout(self.horizontalLayout_3, 1, 0, 1, 2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.tab_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMaximumSize(QtCore.QSize(80, 16777215))
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.usernameBox = QtWidgets.QLineEdit(self.tab_2)
        self.usernameBox.setObjectName("usernameBox")
        self.horizontalLayout_2.addWidget(self.usernameBox)
        self.gridLayout_3.addLayout(self.horizontalLayout_2, 0, 0, 1, 2)
        self.addUserButt = QtWidgets.QPushButton(self.tab_2)
        self.addUserButt.setFocusPolicy(QtCore.Qt.NoFocus)
        self.addUserButt.setObjectName("addUserButt")
        self.gridLayout_3.addWidget(self.addUserButt, 2, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(226, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem, 2, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem1, 3, 0, 1, 2)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.tab_3)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_5 = QtWidgets.QLabel(self.tab_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setMaximumSize(QtCore.QSize(100, 16777215))
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_5.addWidget(self.label_5)
        self.username = QtWidgets.QLineEdit(self.tab_3)
        self.username.setObjectName("username")
        self.horizontalLayout_5.addWidget(self.username)
        self.gridLayout_4.addLayout(self.horizontalLayout_5, 0, 0, 1, 4)
        self.changePasswordButt = QtWidgets.QPushButton(self.tab_3)
        self.changePasswordButt.setFocusPolicy(QtCore.Qt.NoFocus)
        self.changePasswordButt.setObjectName("changePasswordButt")
        self.gridLayout_4.addWidget(self.changePasswordButt, 3, 3, 1, 1)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_6 = QtWidgets.QLabel(self.tab_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setMaximumSize(QtCore.QSize(100, 16777215))
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_6.addWidget(self.label_6)
        self.newPasswordBox = QtWidgets.QLineEdit(self.tab_3)
        self.newPasswordBox.setEchoMode(QtWidgets.QLineEdit.Password)
        self.newPasswordBox.setObjectName("newPasswordBox")
        self.horizontalLayout_6.addWidget(self.newPasswordBox)
        self.gridLayout_4.addLayout(self.horizontalLayout_6, 2, 0, 1, 4)
        spacerItem2 = QtWidgets.QSpacerItem(240, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem2, 3, 0, 1, 3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.tab_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setMaximumSize(QtCore.QSize(100, 16777215))
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.oldPasswordBox = QtWidgets.QLineEdit(self.tab_3)
        self.oldPasswordBox.setEchoMode(QtWidgets.QLineEdit.Password)
        self.oldPasswordBox.setObjectName("oldPasswordBox")
        self.horizontalLayout_4.addWidget(self.oldPasswordBox)
        self.gridLayout_4.addLayout(self.horizontalLayout_4, 1, 0, 1, 4)
        spacerItem3 = QtWidgets.QSpacerItem(178, 70, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem3, 5, 1, 1, 1)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout = QtWidgets.QGridLayout(self.tab)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMaximumSize(QtCore.QSize(60, 16777215))
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.userList = QtWidgets.QComboBox(self.tab)
        self.userList.setFocusPolicy(QtCore.Qt.NoFocus)
        self.userList.setObjectName("userList")
        self.horizontalLayout.addWidget(self.userList)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 2)
        spacerItem4 = QtWidgets.QSpacerItem(206, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 1, 0, 1, 1)
        self.makeAdminButt = QtWidgets.QPushButton(self.tab)
        self.makeAdminButt.setFocusPolicy(QtCore.Qt.NoFocus)
        self.makeAdminButt.setObjectName("makeAdminButt")
        self.gridLayout.addWidget(self.makeAdminButt, 1, 1, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(20, 71, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem5, 2, 0, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.gridLayout_2.addWidget(self.tabWidget, 0, 0, 1, 1)

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_3.setText(_translate("Form", "Password:"))
        self.label_2.setText(_translate("Form", "Username:"))
        self.addUserButt.setText(_translate("Form", "Add User"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Form", "Add User"))
        self.label_5.setText(_translate("Form", "Username:"))
        self.changePasswordButt.setText(_translate("Form", "Change Password"))
        self.label_6.setText(_translate("Form", "New Password: "))
        self.label_4.setText(_translate("Form", "Old Password: "))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Form", "Change Password"))
        self.label.setText(_translate("Form", "User:"))
        self.makeAdminButt.setText(_translate("Form", "Make Admin"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", "Make Admin"))
