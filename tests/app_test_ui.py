# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\Repos\rbhus_clone\tests\app_test.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(709, 994)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.scrollArea = QtWidgets.QScrollArea(Form)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 689, 860))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.textFrame = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.textFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.textFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.textFrame.setObjectName("textFrame")
        self.gridLayout_2.addWidget(self.textFrame, 0, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 0, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 0, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 1, 0, 1, 1)
        self.audioFrame = QtWidgets.QFrame(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.audioFrame.sizePolicy().hasHeightForWidth())
        self.audioFrame.setSizePolicy(sizePolicy)
        self.audioFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.audioFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.audioFrame.setObjectName("audioFrame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.audioFrame)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.playButton = QtWidgets.QPushButton(self.audioFrame)
        self.playButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.playButton.setObjectName("playButton")
        self.horizontalLayout_2.addWidget(self.playButton)
        self.slider = QtWidgets.QSlider(self.audioFrame)
        self.slider.setFocusPolicy(QtCore.Qt.NoFocus)
        self.slider.setOrientation(QtCore.Qt.Horizontal)
        self.slider.setObjectName("slider")
        self.horizontalLayout_2.addWidget(self.slider)
        self.backwardButt = QtWidgets.QPushButton(self.audioFrame)
        self.backwardButt.setFocusPolicy(QtCore.Qt.NoFocus)
        self.backwardButt.setText("")
        self.backwardButt.setObjectName("backwardButt")
        self.horizontalLayout_2.addWidget(self.backwardButt)
        self.forwardButt = QtWidgets.QPushButton(self.audioFrame)
        self.forwardButt.setFocusPolicy(QtCore.Qt.NoFocus)
        self.forwardButt.setText("")
        self.forwardButt.setObjectName("forwardButt")
        self.horizontalLayout_2.addWidget(self.forwardButt)
        self.volumeSlider = QtWidgets.QSlider(self.audioFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.volumeSlider.sizePolicy().hasHeightForWidth())
        self.volumeSlider.setSizePolicy(sizePolicy)
        self.volumeSlider.setFocusPolicy(QtCore.Qt.NoFocus)
        self.volumeSlider.setOrientation(QtCore.Qt.Horizontal)
        self.volumeSlider.setObjectName("volumeSlider")
        self.horizontalLayout_2.addWidget(self.volumeSlider)
        self.gridLayout.addWidget(self.audioFrame, 3, 0, 1, 1)
        self.videoFrame = QtWidgets.QFrame(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.videoFrame.sizePolicy().hasHeightForWidth())
        self.videoFrame.setSizePolicy(sizePolicy)
        self.videoFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.videoFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.videoFrame.setObjectName("videoFrame")
        self.gridLayout.addWidget(self.videoFrame, 2, 0, 1, 1)
        self.toolsFrame = QtWidgets.QFrame(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolsFrame.sizePolicy().hasHeightForWidth())
        self.toolsFrame.setSizePolicy(sizePolicy)
        self.toolsFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.toolsFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.toolsFrame.setObjectName("toolsFrame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.toolsFrame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.saveButt = QtWidgets.QPushButton(self.toolsFrame)
        self.saveButt.setObjectName("saveButt")
        self.horizontalLayout.addWidget(self.saveButt)
        self.printButt = QtWidgets.QPushButton(self.toolsFrame)
        self.printButt.setObjectName("printButt")
        self.horizontalLayout.addWidget(self.printButt)
        self.fontBox = QtWidgets.QFontComboBox(self.toolsFrame)
        self.fontBox.setObjectName("fontBox")
        self.horizontalLayout.addWidget(self.fontBox)
        self.fontSizeBox = QtWidgets.QComboBox(self.toolsFrame)
        self.fontSizeBox.setObjectName("fontSizeBox")
        self.horizontalLayout.addWidget(self.fontSizeBox)
        self.boldButt = QtWidgets.QPushButton(self.toolsFrame)
        self.boldButt.setText("")
        self.boldButt.setCheckable(True)
        self.boldButt.setObjectName("boldButt")
        self.horizontalLayout.addWidget(self.boldButt)
        self.italicButt = QtWidgets.QPushButton(self.toolsFrame)
        self.italicButt.setText("")
        self.italicButt.setCheckable(True)
        self.italicButt.setObjectName("italicButt")
        self.horizontalLayout.addWidget(self.italicButt)
        self.underlineButt = QtWidgets.QPushButton(self.toolsFrame)
        self.underlineButt.setText("")
        self.underlineButt.setCheckable(True)
        self.underlineButt.setObjectName("underlineButt")
        self.horizontalLayout.addWidget(self.underlineButt)
        self.leftAlignButt = QtWidgets.QPushButton(self.toolsFrame)
        self.leftAlignButt.setText("")
        self.leftAlignButt.setObjectName("leftAlignButt")
        self.horizontalLayout.addWidget(self.leftAlignButt)
        self.centerAlignButt = QtWidgets.QPushButton(self.toolsFrame)
        self.centerAlignButt.setText("")
        self.centerAlignButt.setObjectName("centerAlignButt")
        self.horizontalLayout.addWidget(self.centerAlignButt)
        self.rightAlignButt = QtWidgets.QPushButton(self.toolsFrame)
        self.rightAlignButt.setText("")
        self.rightAlignButt.setObjectName("rightAlignButt")
        self.horizontalLayout.addWidget(self.rightAlignButt)
        self.justifyButt = QtWidgets.QPushButton(self.toolsFrame)
        self.justifyButt.setText("")
        self.justifyButt.setObjectName("justifyButt")
        self.horizontalLayout.addWidget(self.justifyButt)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.gridLayout.addWidget(self.toolsFrame, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.saveButt.setText(_translate("Form", "Save"))
        self.printButt.setText(_translate("Form", "Print"))
        self.fontBox.setCurrentText(_translate("Form", "Arial"))
