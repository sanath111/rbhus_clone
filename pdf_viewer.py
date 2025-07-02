#!/usr/bin/python3
# *-* coding: utf-8 *-*

import os
import sys
from PyQt5 import QtGui, QtWidgets, QtCore, uic, QtWebEngineWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import setproctitle
import argparse
import debug

projDir = os.sep.join(os.path.abspath(__file__).split(os.sep)[:-1])
sys.path.append(projDir)

os.environ['QT_LOGGING_RULES'] = "qt5ct.debug=false"
os.environ['QT_SCALE_FACTOR'] = '1'

ui_main = os.path.join(projDir, "ui_files", "pdf_viewer.ui")
pdfjs_path = os.path.join(projDir, "pdfjs", "web", "viewer.html")

parser = argparse.ArgumentParser(description="Utility to view pdfs")
parser.add_argument("-f","--file",dest="file",help="pdf file path")
args = parser.parse_args()

def main_func(ui):
    pdf_path = args.file
    ui.setWindowTitle(pdf_path.split(os.sep)[-1])
    pdf_url = QtCore.QUrl.fromLocalFile(os.path.abspath(pdf_path)).toString()
    full_url = QtCore.QUrl.fromLocalFile(pdfjs_path).toString() + f"?file={pdf_url}"

    ui.viewer.load(QtCore.QUrl(full_url))
    ui.showMaximized()

if __name__ == '__main__':
    setproctitle.setproctitle("PDF_VIEWER")
    app = QtWidgets.QApplication(sys.argv)
    ui = uic.loadUi(ui_main)
    main_func(ui)
    os._exit(app.exec_())

