import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QTextEdit, QAction, QFileDialog, QMessageBox,
    QVBoxLayout, QWidget, QToolBar, QFontComboBox, QSpinBox
)
from PyQt5.QtGui import QTextCursor, QTextDocumentWriter, QTextDocument
from PyQt5.QtCore import Qt


class WordEditor(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Main editor area
        self.textEdit = QTextEdit(self)
        self.textEdit.setAcceptRichText(True)
        self.textEdit.setAlignment(Qt.AlignTop)

        # Setting layout for multiple pages
        document = self.textEdit.document()
        document.setPageSize(self.sizeHint())  # Adjusts for multi-page view

        self.setCentralWidget(self.textEdit)

        # Create toolbar
        self.createToolBar()

        self.setGeometry(100, 100, 800, 600)
        self.setWindowTitle('Word Editor')
        self.show()

    def createToolBar(self):
        toolbar = QToolBar(self)
        self.addToolBar(toolbar)

        # Font selector
        fontBox = QFontComboBox(self)
        fontBox.currentFontChanged.connect(self.setFont)
        toolbar.addWidget(fontBox)

        # Font size selector
        fontSizeBox = QSpinBox(self)
        fontSizeBox.setRange(1, 72)
        fontSizeBox.valueChanged.connect(self.setFontSize)
        toolbar.addWidget(fontSizeBox)

        # Actions
        openFileAction = QAction('Open', self)
        openFileAction.triggered.connect(self.openFile)
        toolbar.addAction(openFileAction)

        saveFileAction = QAction('Save', self)
        saveFileAction.triggered.connect(self.saveFile)
        toolbar.addAction(saveFileAction)

        # Bold, Italic, Underline
        boldAction = QAction('Bold', self)
        boldAction.setCheckable(True)
        boldAction.triggered.connect(self.toggleBold)
        toolbar.addAction(boldAction)

        italicAction = QAction('Italic', self)
        italicAction.setCheckable(True)
        italicAction.triggered.connect(self.toggleItalic)
        toolbar.addAction(italicAction)

        underlineAction = QAction('Underline', self)
        underlineAction.setCheckable(True)
        underlineAction.triggered.connect(self.toggleUnderline)
        toolbar.addAction(underlineAction)

    def setFont(self, font):
        self.textEdit.setCurrentFont(font)

    def setFontSize(self, size):
        self.textEdit.setFontPointSize(size)

    def toggleBold(self):
        fmt = self.textEdit.currentCharFormat()
        fmt.setFontWeight(Qt.Bold if not fmt.fontWeight() == Qt.Bold else Qt.Normal)
        self.textEdit.setCurrentCharFormat(fmt)

    def toggleItalic(self):
        fmt = self.textEdit.currentCharFormat()
        fmt.setFontItalic(not fmt.fontItalic())
        self.textEdit.setCurrentCharFormat(fmt)

    def toggleUnderline(self):
        fmt = self.textEdit.currentCharFormat()
        fmt.setFontUnderline(not fmt.fontUnderline())
        self.textEdit.setCurrentCharFormat(fmt)

    def openFile(self):
        fname, _ = QFileDialog.getOpenFileName(self, 'Open File', '', 'Text Files (*.txt);;All Files (*)')
        if fname:
            with open(fname, 'r', encoding='utf-8') as file:
                self.textEdit.setPlainText(file.read())

    def saveFile(self):
        fname, _ = QFileDialog.getSaveFileName(self, 'Save File', '', 'Text Files (*.txt);;All Files (*)')
        if fname:
            with open(fname, 'w', encoding='utf-8') as file:
                file.write(self.textEdit.toPlainText())
            QMessageBox.information(self, "Success", "File saved successfully.")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    editor = WordEditor()
    sys.exit(app.exec_())
