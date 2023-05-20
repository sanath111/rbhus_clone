import sys
import os

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

# class TextEditor(QMainWindow):

#     def __init__(self):
#         super().__init__()

#         self.text_edit = QPlainTextEdit()
#         self.text_edit.setFont(QFont("Arial", 12))

#         self.bold_action = QAction("Bold", self)
#         self.bold_action.setShortcut("Ctrl+B")
#         self.bold_action.triggered.connect(self.bold)

#         self.italic_action = QAction("Italic", self)
#         self.italic_action.setShortcut("Ctrl+I")
#         self.italic_action.triggered.connect(self.italic)

#         self.underline_action = QAction("Underline", self)
#         self.underline_action.setShortcut("Ctrl+U")
#         self.underline_action.triggered.connect(self.underline)

#         self.font_family_combo = QComboBox()
#         self.font_family_combo.addItems(["Arial", "Times New Roman", "Verdana"])
#         self.font_family_combo.activated.connect(self.set_font_family)

#         self.font_size_combo = QComboBox()
#         self.font_size_combo.addItems(["10", "12", "14", "16", "18"])
#         self.font_size_combo.activated.connect(self.set_font_size)

#         self.toolbar = QToolBar()
#         self.toolbar.addAction(self.bold_action)
#         self.toolbar.addAction(self.italic_action)
#         self.toolbar.addAction(self.underline_action)
#         self.toolbar.addWidget(self.font_family_combo)
#         self.toolbar.addWidget(self.font_size_combo)

#         self.statusbar = QStatusBar()
#         self.statusbar.showMessage("Ready")

#         self.central_widget = QWidget()
#         self.layout = QVBoxLayout()
#         self.layout.addWidget(self.text_edit)
#         self.central_widget.setLayout(self.layout)

#         self.setCentralWidget(self.central_widget)
#         self.setGeometry(500, 100, 500, 500)
#         self.setWindowTitle("Text Editor")
#         self.show()

#     def bold(self):
#         if self.text_edit.isBold():
#             self.text_edit.setBold(False)
#         else:
#             self.text_edit.setBold(True)

#     def italic(self):
#         if self.text_edit.isItalic():
#             self.text_edit.setItalic(False)
#         else:
#             self.text_edit.setItalic(True)

#     def underline(self):
#         if self.text_edit.isUnderline():
#             self.text_edit.setUnderline(False)
#         else:
#             self.text_edit.setUnderline(True)

#     def set_font_family(self, font_family):
#         self.text_edit.setFont(QFont(font_family, self.text_edit.font().pointSize()))

#     def set_font_size(self, font_size):
#         self.text_edit.setFont(QFont(self.text_edit.font().family(), font_size))

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     text_editor = TextEditor()
#     sys.exit(app.exec_())


# class TextEditor(QMainWindow):

#     def __init__(self):
#         super().__init__()

#         self.text_edit = QPlainTextEdit()
#         self.text_edit.setFont(QFont("Arial", 12))

#         self.bold_button = QPushButton("Bold")
#         self.bold_button.setShortcut("Ctrl+B")
#         self.bold_button.clicked.connect(self.bold)

#         self.italic_button = QPushButton("Italic")
#         self.italic_button.setShortcut("Ctrl+I")
#         self.italic_button.clicked.connect(self.italic)

#         self.underline_button = QPushButton("Underline")
#         self.underline_button.setShortcut("Ctrl+U")
#         self.underline_button.clicked.connect(self.underline)

#         self.font_family_combo = QComboBox()
#         self.font_family_combo.addItems(["Arial", "Times New Roman", "Verdana"])
#         self.font_family_combo.activated.connect(self.set_font_family)

#         self.font_size_combo = QComboBox()
#         self.font_size_combo.addItems(["10", "12", "14", "16", "18"])
#         self.font_size_combo.activated.connect(self.set_font_size)

#         self.toolbar = QToolBar()
#         self.toolbar.addWidget(self.bold_button)
#         self.toolbar.addWidget(self.italic_button)
#         self.toolbar.addWidget(self.underline_button)
#         self.toolbar.addWidget(self.font_family_combo)
#         self.toolbar.addWidget(self.font_size_combo)

#         self.statusbar = QStatusBar()
#         self.statusbar.showMessage("Ready")

#         self.central_widget = QWidget()
#         self.layout = QVBoxLayout()
#         self.layout.addWidget(self.text_edit)
#         self.central_widget.setLayout(self.layout)

#         self.setCentralWidget(self.central_widget)
#         self.setGeometry(500, 100, 500, 500)
#         self.setWindowTitle("Text Editor")
#         self.show()

#     def bold(self):
#         if self.text_edit.isBold():
#             self.text_edit.setBold(False)
#         else:
#             self.text_edit.setBold(True)

#     def italic(self):
#         if self.text_edit.isItalic():
#             self.text_edit.setItalic(False)
#         else:
#             self.text_edit.setItalic(True)

#     def underline(self):
#         if self.text_edit.isUnderline():
#             self.text_edit.setUnderline(False)
#         else:
#             self.text_edit.setUnderline(True)

#     def set_font_family(self, font_family):
#         self.text_edit.setFont(QFont(font_family, self.text_edit.font().pointSize()))

#     def set_font_size(self, font_size):
#         self.text_edit.setFont(QFont(self.text_edit.font().family(), font_size))

#     def select_text(self):
#         self.text_edit.setSelectionMode(QPlainTextEdit.ExtendedSelection)

#     def apply_style(self, style):
#         if style == "bold":
#             self.text_edit.setBold(True)
#         elif style == "italic":
#             self.text_edit.setItalic(True)
#         elif style == "underline":
#             self.text_edit.setUnderline(True)

#     def mousePressEvent(self, event):
#         if event.button() == Qt.LeftButton:
#             self.select_text()

#     def keyPressEvent(self, event):
#         if event.key() == Qt.Key_B:
#             self.apply_style("bold")
#         elif event.key() == Qt.Key_I:
#             self.apply_style("italic")
#         elif event.key() == Qt.Key_U:
#             self.apply_style("underline")

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     text_editor = TextEditor()
#     sys.exit(app.exec_())




import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QAction, QFontComboBox, QComboBox
from PyQt5.QtGui import QFont, QTextCharFormat
from PyQt5.QtCore import Qt


class TextEditor(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.text_edit = QTextEdit(self)
        self.setCentralWidget(self.text_edit)

        self.create_toolbars()
        self.create_actions()

        self.setGeometry(100, 100, 800, 600)
        self.setWindowTitle('Text Editor')
        self.show()

    def create_toolbars(self):
        toolbar = self.addToolBar('Formatting')

        font_combo = QFontComboBox(self)
        font_combo.currentFontChanged.connect(self.set_font)

        font_size_combo = QComboBox(self)
        font_size_combo.setEditable(True)
        font_size_combo.setMinimumContentsLength(3)
        font_size_combo.activated.connect(self.set_font_size)

        sizes = ["8", "9", "10", "11", "12", "14", "16", "18", "20", "22", "24", "26", "28", "32", "36", "48", "72"]
        font_size_combo.addItems(sizes)

        toolbar.addWidget(font_combo)
        toolbar.addWidget(font_size_combo)
        toolbar.addSeparator()

        self.bold_action = QAction('Bold', self)
        self.bold_action.setShortcut('Ctrl+B')
        self.bold_action.setCheckable(True)
        self.bold_action.triggered.connect(self.set_bold)
        toolbar.addAction(self.bold_action)

        self.italic_action = QAction('Italic', self)
        self.italic_action.setShortcut('Ctrl+I')
        self.italic_action.setCheckable(True)
        self.italic_action.triggered.connect(self.set_italic)
        toolbar.addAction(self.italic_action)

        self.underline_action = QAction('Underline', self)
        self.underline_action.setShortcut('Ctrl+U')
        self.underline_action.setCheckable(True)
        self.underline_action.triggered.connect(self.set_underline)
        toolbar.addAction(self.underline_action)

    def create_actions(self):
        self.exit_action = QAction('Exit', self)
        self.exit_action.setShortcut('Ctrl+Q')
        self.exit_action.triggered.connect(self.close)

    def set_font(self, font):
        self.text_edit.setCurrentFont(font)

    def set_font_size(self, size):
        self.text_edit.setFontPointSize(int(size))

    def set_bold(self, checked):
        text_format = self.text_edit.currentCharFormat()
        font = text_format.font()
        font.setBold(checked)
        text_format.setFont(font)
        self.merge_format_on_word_or_selection(text_format)

    def set_italic(self, checked):
        text_format = self.text_edit.currentCharFormat()
        font = text_format.font()
        font.setItalic(checked)
        text_format.setFont(font)
        self.merge_format_on_word_or_selection(text_format)

    def set_underline(self, checked):
        text_format = self.text_edit.currentCharFormat()
        font = text_format.font()
        font.setUnderline(checked)
        text_format.setFont(font)
        self.merge_format_on_word_or_selection(text_format)

    def merge_format_on_word_or_selection(self, format):
        cursor = self.text_edit.textCursor()
        if not cursor.hasSelection():
            cursor.select(QTextCursor.WordUnderCursor)
        cursor.mergeCharFormat(format)
        self.text_edit.mergeCurrentCharFormat

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Exit', 'Are you sure you want to exit?', QMessageBox.Yes | QMessageBox.No,
                                    QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    text_editor = TextEditor()
    sys.exit(app.exec_())