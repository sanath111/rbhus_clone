# import subprocess
# import win32con
# import win32gui
# import win32process
# import ctypes
# from ctypes import wintypes

# class EmbeddedWindow:
#     def __init__(self, hwnd):
#         self.hwnd = hwnd
#         self.parent = None
#         self.prev_style = None
#         self.prev_ex_style = None

#     def embed(self, app_path):
#         startupinfo = subprocess.STARTUPINFO()
#         startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
#         startupinfo.wShowWindow = win32con.SW_HIDE

#         # Launch the external application
#         self.process = subprocess.Popen([app_path], startupinfo=startupinfo)

#         # Get the HWND of the external application
#         app_hwnd = None
#         while not app_hwnd:
#             app_hwnd = win32gui.FindWindow(None, "Application Window Title")

#         # Set the parent of the external application's window
#         self.parent = win32gui.GetParent(app_hwnd)
#         win32gui.SetParent(app_hwnd, self.hwnd)

#         # Adjust the style of the external application's window
#         self.prev_style = win32gui.GetWindowLong(app_hwnd, win32con.GWL_STYLE)
#         self.prev_ex_style = win32gui.GetWindowLong(app_hwnd, win32con.GWL_EXSTYLE)
#         win32gui.SetWindowLong(app_hwnd, win32con.GWL_STYLE, win32con.WS_CHILD | win32con.WS_VISIBLE)
#         win32gui.SetWindowLong(app_hwnd, win32con.GWL_EXSTYLE, win32con.WS_EX_CONTROLPARENT)

#     def cleanup(self):
#         # Restore the original style and parent of the embedded window
#         if self.parent:
#             win32gui.SetWindowLong(self.hwnd, win32con.GWL_STYLE, self.prev_style)
#             win32gui.SetWindowLong(self.hwnd, win32con.GWL_EXSTYLE, self.prev_ex_style)
#             win32gui.SetParent(self.hwnd, self.parent)

#         # Terminate the external application
#         if self.process and self.process.poll() is None:
#             self.process.terminate()
#             self.process.wait()

# # Usage example
# import tkinter as tk

# root = tk.Tk()

# # Create a frame to embed the application
# frame = tk.Frame(root, width=500, height=500)
# frame.pack()

# # Create an instance of the EmbeddedWindow class
# embedded_window = EmbeddedWindow(frame.winfo_id())

# # Embed the application by providing its executable path
# embedded_window.embed("C:\Program Files\LibreOffice\program\soffice.exe")

# # Call the cleanup method when you want to remove the embedded application
# # embedded_window.cleanup()

# root.mainloop()


# import tkinter as tk
# import win32con
# import win32gui
# import win32process

# class EmbeddedWindow:
#     def __init__(self, hwnd):
#         self.hwnd = hwnd
#         self.prev_style = None
#         self.prev_ex_style = None

#     def embed(self, app_path):
#         # Launch the external application
#         self.process = win32process.CreateProcess(
#             app_path, None, None, None, 0,
#             win32process.CREATE_NO_WINDOW, None, None,
#             win32process.STARTUPINFO())

#         # Get the HWND of the external application
#         app_hwnd = None
#         while not app_hwnd:
#             app_hwnd = win32gui.FindWindow(None, "Application Window Title")

#         # Set the parent of the external application's window
#         win32gui.SetParent(app_hwnd, self.hwnd)

#         # Adjust the style of the external application's window
#         self.prev_style = win32gui.GetWindowLong(app_hwnd, win32con.GWL_STYLE)
#         self.prev_ex_style = win32gui.GetWindowLong(app_hwnd, win32con.GWL_EXSTYLE)
#         win32gui.SetWindowLong(app_hwnd, win32con.GWL_STYLE, win32con.WS_CHILD | win32con.WS_VISIBLE)
#         win32gui.SetWindowLong(app_hwnd, win32con.GWL_EXSTYLE, win32con.WS_EX_CONTROLPARENT)

#     def cleanup(self):
#         # Restore the original style of the embedded window
#         if self.prev_style is not None:
#             win32gui.SetWindowLong(self.hwnd, win32con.GWL_STYLE, self.prev_style)
#             win32gui.SetWindowLong(self.hwnd, win32con.GWL_EXSTYLE, self.prev_ex_style)

#         # Terminate the external application
#         if self.process is not None:
#             win32process.TerminateProcess(self.process[0], 0)

# # Usage example
# root = tk.Tk()

# # Create a frame to embed the application
# frame = tk.Frame(root, width=500, height=500)
# frame.pack()

# # Create an instance of the EmbeddedWindow class
# embedded_window = EmbeddedWindow(frame.winfo_id())

# # Embed the application by providing its executable path
# embedded_window.embed(r"C:\Program Files\LibreOffice\program\soffice.exe")

# # Call the cleanup method when you want to remove the embedded application
# # embedded_window.cleanup()

# root.mainloop()

# import tkinter as tk
# from tkinterdnd2 import DND_FILES, TkinterDnD

# root = TkinterDnD.Tk()

# # Create a frame to embed the application
# frame = tk.Frame(root, width=500, height=500)
# frame.pack()

# # Set up drag-and-drop support for the frame
# frame.drop_target_register(DND_FILES)
# frame.dnd_bind('<<Drop>>', lambda event: handle_drop(event, frame))

# def handle_drop(event, frame):
#     # Get the path of the dropped file
#     filepath = event.data

#     # Embed the application using the file's path
#     embed_application(frame, filepath)

# def embed_application(frame, filepath):
#     pass
#     # TODO: Implement embedding logic for the specific application
#     # You will need to use platform-specific APIs or external libraries
#     # to achieve the embedding of the application within the frame

# # Call the embed_application function with the path of the application you want to embed
# # embed_application(frame, "path_to_your_application.exe")

# root.mainloop()




# import tkinter as tk
# import win32gui
# import win32con
# import win32process

# class EmbeddedWindow:
#     def __init__(self, hwnd):
#         self.hwnd = hwnd
#         self.processes = {}

#     def embed(self, app_name, app_path):
#         process_info = win32process.CreateProcess(
#             app_path, None, None, None, 0,
#             win32process.CREATE_NO_WINDOW, None, None,
#             win32process.STARTUPINFO())

#         handle = process_info[0].handle
#         win32gui.SetWindowLongPtr(handle, win32con.GWL_STYLE, win32con.WS_CHILD | win32con.WS_VISIBLE)
#         win32gui.SetWindowLongPtr(handle, win32con.GWL_EXSTYLE, win32con.WS_EX_CONTROLPARENT)
#         win32gui.SetParent(handle, self.hwnd)

#         prev_style = win32gui.GetWindowLongPtr(handle, win32con.GWL_STYLE)
#         prev_ex_style = win32gui.GetWindowLongPtr(handle, win32con.GWL_EXSTYLE)

#         self.processes[app_name] = {
#             'handle': handle,
#             'prev_style': prev_style,
#             'prev_ex_style': prev_ex_style
#         }

#     def cleanup(self):
#         for app_name, app_data in self.processes.items():
#             handle = app_data['handle']
#             prev_style = app_data['prev_style']
#             prev_ex_style = app_data['prev_ex_style']
#             win32gui.SetWindowLongPtr(handle, win32con.GWL_STYLE, prev_style)
#             win32gui.SetWindowLongPtr(handle, win32con.GWL_EXSTYLE, prev_ex_style)

#             win32process.TerminateProcess(handle, 0)

# # Usage example
# root = tk.Tk()

# frame = tk.Frame(root, width=800, height=600)
# frame.pack()

# embedded_window = EmbeddedWindow(int(frame.winfo_id()))  # Convert winfo_id() to int

# libreoffice_path = r"C:\Program Files\LibreOffice\program\soffice.exe"
# embedded_window.embed("LibreOffice", libreoffice_path)

# vlc_path = r"C:\Program Files\VideoLAN\VLC\vlc.exe"
# embedded_window.embed("VLC", vlc_path)

# root.mainloop()


# import sys

# from PyQt5.QtCore import *
# from PyQt5.QtWidgets import *
# from PyQt5.QtGui import *

# from PyQt5.QtWidgets import (
#     QApplication,
#     QMainWindow,
#     QPlainTextEdit,
#     QMenuBar,
#     QMenu,
#     QAction,
#     QToolBar,
# )


# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()

#         self.text_editor = QPlainTextEdit()
#         self.text_editor.setBaseSize(595, 842)
#         self.setCentralWidget(self.text_editor)

#         self.menu_bar = QMenuBar()
#         self.file_menu = QMenu("File", self.menu_bar)
#         self.save_action = QAction("Save", self.file_menu)
#         self.save_as_action = QAction("Save As", self.file_menu)
#         self.file_menu.addAction(self.save_action)
#         self.file_menu.addAction(self.save_as_action)
#         self.menu_bar.addMenu(self.file_menu)

#         self.toolbar = QToolBar()
#         self.save_button = QAction("Save", self.toolbar)
#         self.save_as_button = QAction("Save As", self.toolbar)
#         self.toolbar.addAction(self.save_button)
#         self.toolbar.addAction(self.save_as_button)

#         self.status_bar = QStatusBar()
#         self.setStatusBar(self.status_bar)

#         self.save_action.triggered.connect(self.save_file)
#         self.save_as_action.triggered.connect(self.save_file_as)
#         self.save_button.triggered.connect(self.save_file)
#         self.save_as_button.triggered.connect(self.save_file_as)

#         self.status_bar.showMessage("Ready")

#     def save_file(self):
#         file_name, _ = QFileDialog.getSaveFileName(
#             self, "Save File", "", "Text Files (*.txt);;All Files (*)"
#         )
#         if file_name:
#             with open(file_name, "w") as f:
#                 f.write(self.text_editor.toPlainText())
#             self.status_bar.showMessage("File saved")

#     def save_file_as(self):
#         file_name, _ = QFileDialog.getSaveFileName(
#             self, "Save File As", "", "Text Files (*.txt);;All Files (*)"
#         )
#         if file_name:
#             with open(file_name, "w") as f:
#                 f.write(self.text_editor.toPlainText())
#             self.status_bar.showMessage("File saved as")


# if __name__ == "__main__":
#     app = QApplication(sys.argv)

#     main_window = MainWindow()
#     main_window.show()

#     sys.exit(app.exec_())


# import sys
# from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit

# class TextEditor(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.text_editors = []  # List to store created QTextEdit widgets

#         self.create_text_edit()  # Initial QTextEdit widget

#     def create_text_edit(self):
#         text_edit = QTextEdit()
#         text_edit.textChanged.connect(self.handle_text_changed)
#         self.text_editors.append(text_edit)

#         if len(self.text_editors) > 1:
#             # Set the new QTextEdit as the central widget if it's not the first one
#             self.setCentralWidget(text_edit)

#     def handle_text_changed(self):
#         current_text_edit = self.text_editors[-1]  # Get the current QTextEdit widget
#         document_height = current_text_edit.document().size().height()
#         visible_height = current_text_edit.viewport().height()

#         if document_height > visible_height:
#             self.create_text_edit()

# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     window = TextEditor()
#     window.setGeometry(100, 100, 595, 842)  # Set the desired window size
#     window.show()
#     sys.exit(app.exec_())


# import sys
# from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QVBoxLayout, QWidget

# class TextEditor(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.text_editors = []  # List to store created QTextEdit widgets

#         self.create_text_edit()  # Initial QTextEdit widget

#         main_widget = QWidget(self)
#         layout = QVBoxLayout(main_widget)
#         layout.addWidget(self.text_editors[0])
#         self.setCentralWidget(main_widget)

#     def create_text_edit(self):
#         text_edit = QTextEdit()
#         text_edit.textChanged.connect(self.handle_text_changed)
#         self.text_editors.append(text_edit)

#     def handle_text_changed(self):
#         current_text_edit = self.text_editors[-1]  # Get the current QTextEdit widget
#         document_height = current_text_edit.document().size().height()
#         visible_height = current_text_edit.viewport().height()

#         if document_height > visible_height:
#             self.create_text_edit()
#             main_widget = self.centralWidget()
#             layout = main_widget.layout()
#             layout.addWidget(self.text_editors[-1])

# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     window = TextEditor()
#     window.setGeometry(100, 100, 595, 842)  # Set the desired window size
#     window.show()
#     sys.exit(app.exec_())


""" Docx

author: ashraf minhaj
mail  : ashraf_minhaj@yahoo.com
"""

"""
install -
$ pip install pyqt5
$ pip install docx2txt
"""

import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtPrintSupport import *
import docx2txt


class MainApp(QMainWindow):
    """ the main class of our app """
    def __init__(self):
        """ init things here """
        super().__init__()                         # parent class initializer

        # window title
        self.title = "Google Doc Clone"
        self.setWindowTitle(self.title)
        
        # editor section
        self.editor = QTextEdit(self) 
        self.setCentralWidget(self.editor)

        # create menubar and toolbar first
        self.create_menu_bar()
        self.create_toolbar()

        # after craeting toolabr we can call and select font size
        font = QFont('Times', 12)
        self.editor.setFont(font)
        self.editor.setFontPointSize(12)

        # stores path
        self.path = ''

    def create_menu_bar(self):
        menuBar = QMenuBar(self)

        """ add elements to the menubar """
        # App icon will go here
        app_icon = menuBar.addMenu(QIcon("doc_icon.png"), "icon")

        # file menu **
        file_menu = QMenu("File", self)
        menuBar.addMenu(file_menu)

        save_action = QAction('Save', self)
        save_action.triggered.connect(self.file_save)
        file_menu.addAction(save_action)

        open_action = QAction('Open', self)
        open_action.triggered.connect(self.file_open)
        file_menu.addAction(open_action)

        rename_action = QAction('Rename', self)
        rename_action.triggered.connect(self.file_saveas)
        file_menu.addAction(rename_action)

        pdf_action = QAction("Save as PDF", self)
        pdf_action.triggered.connect(self.save_pdf)
        file_menu.addAction(pdf_action)
        

        # edit menu **
        edit_menu = QMenu("Edit", self)
        menuBar.addMenu(edit_menu)

        # paste
        paste_action = QAction('Paste', self)
        paste_action.triggered.connect(self.editor.paste)
        edit_menu.addAction(paste_action)

        # clear 
        clear_action = QAction('Clear', self)
        clear_action.triggered.connect(self.editor.clear)
        edit_menu.addAction(clear_action)

        # select all
        select_action = QAction('Select All', self)
        select_action.triggered.connect(self.editor.selectAll)
        edit_menu.addAction(select_action)

        # view menu **
        view_menu = QMenu("View", self)
        menuBar.addMenu(view_menu)

        # fullscreen
        fullscr_action = QAction('Full Screen View', self)
        fullscr_action.triggered.connect(lambda : self.showFullScreen())
        view_menu.addAction(fullscr_action)

        # normal screen
        normscr_action = QAction('Normal View', self)
        normscr_action.triggered.connect(lambda : self.showNormal())
        view_menu.addAction(normscr_action)

        # minimize
        minscr_action = QAction('Minimize', self)
        minscr_action.triggered.connect(lambda : self.showMinimized())
        view_menu.addAction(minscr_action)

        self.setMenuBar(menuBar)

    def create_toolbar(self):
        # Using a title
        ToolBar = QToolBar("Tools", self)

        # undo
        undo_action = QAction(QIcon("undo.png"), 'Undo', self)
        undo_action.triggered.connect(self.editor.undo)
        ToolBar.addAction(undo_action)

        # redo
        redo_action = QAction(QIcon("redo.png"), 'Redo', self)
        redo_action.triggered.connect(self.editor.redo)
        ToolBar.addAction(redo_action)

        # adding separator
        ToolBar.addSeparator()

        # copy
        copy_action = QAction(QIcon("copy.png"), 'Copy', self)
        copy_action.triggered.connect(self.editor.copy)
        ToolBar.addAction(copy_action)

        # cut 
        cut_action = QAction(QIcon("cut.png"), 'Cut', self)
        cut_action.triggered.connect(self.editor.cut)
        ToolBar.addAction(cut_action)

        # paste
        paste_action = QAction(QIcon("paste.png"), 'Paste', self)
        paste_action.triggered.connect(self.editor.paste)
        ToolBar.addAction(paste_action)

        # adding separator
        ToolBar.addSeparator()
        ToolBar.addSeparator()

        # fonts
        self.font_combo = QComboBox(self)
        self.font_combo.addItems(["Courier Std", "Hellentic Typewriter Regular", "Helvetica", "Arial", "SansSerif", "Helvetica", "Times", "Monospace"])
        self.font_combo.activated.connect(self.set_font)      # connect with function
        ToolBar.addWidget(self.font_combo) 

        # font size
        self.font_size = QSpinBox(self)   
        self.font_size.setValue(12)  
        self.font_size.valueChanged.connect(self.set_font_size)      # connect with funcion
        ToolBar.addWidget(self.font_size)

        # separator
        ToolBar.addSeparator()

        # bold
        bold_action = QAction(QIcon("bold.png"), 'Bold', self)
        bold_action.triggered.connect(self.bold_text)
        ToolBar.addAction(bold_action)

        # underline
        underline_action = QAction(QIcon("underline.png"), 'Underline', self)
        underline_action.triggered.connect(self.underline_text)
        ToolBar.addAction(underline_action)

        # italic
        italic_action = QAction(QIcon("italic.png"), 'Italic', self)
        italic_action.triggered.connect(self.italic_text)
        ToolBar.addAction(italic_action)

        # separator
        ToolBar.addSeparator()

        # text alignment
        right_alignment_action = QAction(QIcon("right-align.png"), 'Align Right', self)
        right_alignment_action.triggered.connect(lambda : self.editor.setAlignment(Qt.AlignRight))
        ToolBar.addAction(right_alignment_action)

        left_alignment_action = QAction(QIcon("left-align.png"), 'Align Left', self)
        left_alignment_action.triggered.connect(lambda : self.editor.setAlignment(Qt.AlignLeft))
        ToolBar.addAction(left_alignment_action)

        justification_action = QAction(QIcon("justification.png"), 'Center/Justify', self)
        justification_action.triggered.connect(lambda : self.editor.setAlignment(Qt.AlignCenter))
        ToolBar.addAction(justification_action)

        # separator
        ToolBar.addSeparator()

        # zoom in
        zoom_in_action = QAction(QIcon("zoom-in.png"), 'Zoom in', self)
        zoom_in_action.triggered.connect(self.editor.zoomIn)
        ToolBar.addAction(zoom_in_action)

        # zoom out
        zoom_out_action = QAction(QIcon("zoom-out.png"), 'Zoom out', self)
        zoom_out_action.triggered.connect(self.editor.zoomOut)
        ToolBar.addAction(zoom_out_action)


        # separator
        ToolBar.addSeparator()
        
        self.addToolBar(ToolBar)

    def italic_text(self):
        # if already italic, change into normal, else italic
        state = self.editor.fontItalic()
        self.editor.setFontItalic(not(state))

    def underline_text(self):
        # if already underlined, change into normal, else underlined
        state = self.editor.fontUnderline()
        self.editor.setFontUnderline(not(state))

    def bold_text(self):
        # if already bold, make normal, else make bold
        if self.editor.fontWeight() != QFont.Bold:
            self.editor.setFontWeight(QFont.Bold)
            return
        self.editor.setFontWeight(QFont.Normal)

    def set_font(self):
        font = self.font_combo.currentText()
        self.editor.setCurrentFont(QFont(font))

    def set_font_size(self):
        value = self.font_size.value()
        self.editor.setFontPointSize(value)

        # we can also make it one liner without writing such function.
        # by using lamba function -
        # self.font_size.valueChanged.connect(self.editor.setFontPointSize(self.font_size.value()))  


    def file_open(self):
        self.path, _ = QFileDialog.getOpenFileName(self, "Open file", "", "Text documents (*.text);Text documents (*.txt);All files (*.*)")

        try:
            #with open(self.path, 'r') as f:
            #    text = f.read()
            text = docx2txt.process(self.path) # docx2txt
            #doc = Document(self.path)         # if using docx
            #text = ''
            #for line in doc.paragraphs:
            #    text += line.text
        except Exception as e:
            print(e)
        else:
            self.editor.setText(text)
            self.update_title()

    def file_save(self):
        print(self.path)
        if self.path == '':
            # If we do not have a path, we need to use Save As.
            self.file_saveas()

        text = self.editor.toPlainText()

        try:
            with open(self.path, 'w') as f:
                f.write(text)
                self.update_title()
        except Exception as e:
            print(e)

    def file_saveas(self):
        self.path, _ = QFileDialog.getSaveFileName(self, "Save file", "", "text documents (*.text);Text documents (*.txt);All files (*.*)")

        if self.path == '':
            return   # If dialog is cancelled, will return ''

        text = self.editor.toPlainText()

        try:
            with open(path, 'w') as f:
                f.write(text)
                self.update_title()
        except Exception as e:
            print(e)

    def update_title(self):
        self.setWindowTitle(self.title + ' ' + self.path)

    def save_pdf(self):
        f_name, _ = QFileDialog.getSaveFileName(self, "Export PDF", None, "PDF files (.pdf);;All files()")
        print(f_name)

        if f_name != '':  # if name not empty
           printer = QPrinter(QPrinter.HighResolution)
           printer.setOutputFormat(QPrinter.PdfFormat)
           printer.setOutputFileName(f_name)
           self.editor.document().print_(printer)
    

app = QApplication(sys.argv)
window = MainApp()
window.show()
sys.exit(app.exec_())