import sys
from PyQt5.QtWidgets import QApplication, QFileSystemModel, QTreeView, QWidget, QVBoxLayout

app = QApplication(sys.argv)

# create the main window
window = QWidget()
window.setWindowTitle('File System Viewer')
layout = QVBoxLayout(window)

# create the file system model and set its root path
model = QFileSystemModel()
model.setRootPath('')

# create the tree view and set its model
tree = QTreeView()
tree.setModel(model)
tree.setRootIndex(model.index(''))

# add the tree view to the main window
layout.addWidget(tree)
window.setLayout(layout)

# show the main window
window.show()

# start the event loop
sys.exit(app.exec_())
