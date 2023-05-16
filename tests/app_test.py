# from PyQt5.QtCore import *
# from PyQt5.QtWidgets import *
# from PyQt5.QtGui import *

# import sys
# from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout
# from PyQt5.QtCore import Qt, QUrl
# from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
# from PyQt5.QtMultimediaWidgets import QVideoWidget

# class MainWindow(QMainWindow):
#     def __init__(self, file_path, parent=None):
#         super(MainWindow, self).__init__(parent)
#         self.setWindowTitle("VLC Player")
#         self.setGeometry(100, 100, 800, 600)

#         # Create a QMediaPlayer instance
#         self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)

#         # Create a QVideoWidget to hold the video output
#         self.videoWidget = QVideoWidget(self)
#         self.setCentralWidget(self.videoWidget)

#         # Create a QVBoxLayout to manage the layout
#         self.layout = QVBoxLayout()
#         self.videoWidget.setLayout(self.layout)

#         # Set the video widget as the output for the media player
#         self.mediaPlayer.setVideoOutput(self.videoWidget)

#         # Load and play the specified file
#         self.play(file_path)

#     def play(self, file_path):
#         # Load the media file
#         media_content = QMediaContent(QUrl.fromLocalFile(file_path))
#         self.mediaPlayer.setMedia(media_content)

#         # Play the media
#         self.mediaPlayer.play()

# if __name__ == '__main__':
#     app = QApplication(sys.argv)

#     # Provide the file path here
#     file_path = r"C:\Users\Dell\Documents\rbhus_clone_root\template\test_video.mp4"

#     mainWindow = MainWindow(file_path)
#     mainWindow.show()

#     sys.exit(app.exec_())


# import sys
# from PyQt5.QtWidgets import QApplication, QMainWindow
# from PyQt5.QtCore import Qt
# import vlc

# class MainWindow(QMainWindow):
#     def __init__(self, file_path, parent=None):
#         super(MainWindow, self).__init__(parent)
#         self.setWindowTitle("VLC Player")
#         self.setGeometry(100, 100, 800, 600)

#         # Create a VLC instance
#         self.vlcInstance = vlc.Instance("--no-xlib")

#         # Create a VLC media player
#         self.mediaPlayer = self.vlcInstance.media_player_new()

#         # Create a QWidget to hold the video output
#         self.videoWidget = self.mediaPlayer.get_xwindow()

#         # Set the window handle for video output
#         if sys.platform.startswith('linux'):  # Linux
#             self.videoWidget.setProperty("X11Display", str(self.videoWidget.display()))
#             self.videoWidget.setProperty("X11Window", str(self.videoWidget.winId()))
#         elif sys.platform == "win32":  # Windows
#             self.videoWidget.set_hwnd(self.videoWidget.winId())
#         elif sys.platform == "darwin":  # macOS
#             self.videoWidget.setProperty("macosx-video-handler", str(self.videoWidget.winId()))

#         # Load and play the specified file
#         self.play(file_path)

#     def play(self, file_path):
#         # Create a VLC media
#         media = self.vlcInstance.media_new(file_path)

#         # Set the media to the player
#         self.mediaPlayer.set_media(media)

#         # Play the media
#         self.mediaPlayer.play()

# if __name__ == '__main__':
#     app = QApplication(sys.argv)

#     # Provide the file path here
#     file_path = r"C:\Users\Dell\Documents\rbhus_clone_root\template\test_video.mp4"

#     mainWindow = MainWindow(file_path)
#     mainWindow.show()

#     sys.exit(app.exec_())


# import sys
# from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
# from PyQt5.QtCore import Qt
# import vlc

# class MainWindow(QMainWindow):
#     def __init__(self, file_path, parent=None):
#         super(MainWindow, self).__init__(parent)
#         self.setWindowTitle("VLC Player")
#         self.setGeometry(100, 100, 800, 600)

#         # Create a VLC instance
#         self.vlcInstance = vlc.Instance()

#         # Create a VLC media player
#         self.mediaPlayer = self.vlcInstance.media_player_new()

#         # Create a QWidget to hold the video output
#         self.videoFrame = QWidget(self)
#         self.videoFrame.setGeometry(0, 0, 800, 600)
#         self.layout = QVBoxLayout()
#         self.layout.addWidget(self.videoFrame)

#         # Set the layout of the main window
#         centralWidget = QWidget(self)
#         centralWidget.setLayout(self.layout)
#         self.setCentralWidget(centralWidget)

#         # Load and play the specified file
#         self.play(file_path)

#     def play(self, file_path):
#         # Create a VLC media
#         media = self.vlcInstance.media_new(file_path)

#         # Set the media to the player
#         self.mediaPlayer.set_media(media)

#         # Get the window handle of the video frame
#         if sys.platform == "win32":
#             self.mediaPlayer.set_hwnd(self.videoFrame.winId())
#         else:
#             self.mediaPlayer.set_xwindow(self.videoFrame.winId())

#         # Play the media
#         self.mediaPlayer.play()

# if __name__ == '__main__':
#     app = QApplication(sys.argv)

#     # Provide the file path here
#     file_path = r"C:\Users\Dell\Documents\rbhus_clone_root\template\test_video.mp4"

#     mainWindow = MainWindow(file_path)
#     mainWindow.show()

#     sys.exit(app.exec_())


# import sys
# from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
# from PyQt5.QtCore import Qt
# import vlc

# class MainWindow(QMainWindow):
#     def __init__(self, file_path, parent=None):
#         super(MainWindow, self).__init__(parent)
#         self.setWindowTitle("VLC Player")
#         self.setGeometry(100, 100, 800, 600)

#         # Create a VLC instance
#         self.vlcInstance = vlc.Instance("--no-xlib")

#         # Create a VLC media player
#         self.mediaPlayer = self.vlcInstance.media_player_new()

#         # Create a QWidget to hold the video output
#         self.videoFrame = QWidget(self)

#         # Create a QWidget to hold the VLC player UI controls
#         self.controlFrame = QWidget(self)

#         # Set the layouts for video and controls
#         self.layout = QVBoxLayout()
#         self.layout.addWidget(self.videoFrame)
#         self.layout.addWidget(self.controlFrame)

#         # Set the layout of the main window
#         centralWidget = QWidget(self)
#         centralWidget.setLayout(self.layout)
#         self.setCentralWidget(centralWidget)

#         # Load and play the specified file
#         self.play(file_path)

#     def play(self, file_path):
#         # Create a VLC media
#         media = self.vlcInstance.media_new(file_path)

#         # Set the media to the player
#         self.mediaPlayer.set_media(media)

#         # Set the video output window handle
#         if sys.platform == "win32":
#             self.mediaPlayer.set_hwnd(self.videoFrame.winId())
#         else:
#             self.mediaPlayer.set_xwindow(self.videoFrame.winId())

#         # Get the VLC player UI widget
#         vlcWidget = self.mediaPlayer.get_full_title()

#         # Set the layout for the control frame
#         controlLayout = QVBoxLayout()
#         controlLayout.addWidget(vlcWidget)

#         # Set the layout for the control frame widget
#         self.controlFrame.setLayout(controlLayout)

#         # Play the media
#         self.mediaPlayer.play()

# if __name__ == '__main__':
#     app = QApplication(sys.argv)

#     # Provide the file path here
#     file_path = r"C:\Users\Dell\Documents\rbhus_clone_root\template\test_video.mp4"

#     mainWindow = MainWindow(file_path)
#     mainWindow.show()

#     sys.exit(app.exec_())


# import sys
# from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
# from PyQt5.QtCore import Qt, QUrl
# from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
# from PyQt5.QtMultimediaWidgets import QVideoWidget

# class MainWindow(QMainWindow):
#     def __init__(self, file_path, parent=None):
#         super(MainWindow, self).__init__(parent)
#         self.setWindowTitle("VLC Player")
#         self.setGeometry(100, 100, 800, 600)

#         # Create a QMediaPlayer instance
#         self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)

#         # Create a QVideoWidget to hold the video output
#         self.videoWidget = QVideoWidget(self)

#         # Create a QWidget to hold the VLC player UI controls
#         self.controlWidget = QWidget(self)

#         # Set the layout for the main window
#         self.layout = QVBoxLayout()
#         self.layout.addWidget(self.videoWidget)
#         self.layout.addWidget(self.controlWidget)

#         # Set the layout of the main window
#         centralWidget = QWidget(self)
#         centralWidget.setLayout(self.layout)
#         self.setCentralWidget(centralWidget)

#         # Set the video widget as the output for the media player
#         self.mediaPlayer.setVideoOutput(self.videoWidget)

#         # Load and play the specified file
#         self.play(file_path)

#     def play(self, file_path):
#         # Load the media file
#         media_content = QMediaContent(QUrl.fromLocalFile(file_path))
#         self.mediaPlayer.setMedia(media_content)

#         # Create the media player UI controls
#         media_player_ui = self.mediaPlayer.mediaObject().requestControl("org.qtproject.qt.mediaplayercontrol")

#         # Set the layout for the control widget
#         controlLayout = QVBoxLayout()
#         controlLayout.addWidget(media_player_ui)

#         # Set the layout for the control widget
#         self.controlWidget.setLayout(controlLayout)

#         # Play the media
#         self.mediaPlayer.play()

# if __name__ == '__main__':
#     app = QApplication(sys.argv)

#     # Provide the file path here
#     file_path = r"C:\Users\Dell\Documents\rbhus_clone_root\template\test_video.mp4"

#     mainWindow = MainWindow(file_path)
#     mainWindow.show()

#     sys.exit(app.exec_())


# import sys
# from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
# from PyQt5.QtCore import Qt, QUrl
# from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
# from PyQt5.QtMultimediaWidgets import QVideoWidget

# class MainWindow(QMainWindow):
#     def __init__(self, file_path, parent=None):
#         super(MainWindow, self).__init__(parent)
#         self.setWindowTitle("VLC Player")
#         self.setGeometry(100, 100, 800, 600)

#         # Create a QMediaPlayer instance
#         self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)

#         # Create a QVideoWidget to hold the video output
#         self.videoWidget = QVideoWidget(self)

#         # Create a QWidget to hold the VLC player UI controls
#         self.controlWidget = QWidget(self)

#         # Set the layout for the main window
#         self.layout = QVBoxLayout()
#         self.layout.addWidget(self.videoWidget)
#         self.layout.addWidget(self.controlWidget)

#         # Set the layout of the main window
#         centralWidget = QWidget(self)
#         centralWidget.setLayout(self.layout)
#         self.setCentralWidget(centralWidget)

#         # Set the video widget as the output for the media player
#         self.mediaPlayer.setVideoOutput(self.videoWidget)

#         # Load and play the specified file
#         self.play(file_path)

#     def play(self, file_path):
#         # Load the media file
#         media_content = QMediaContent(QUrl.fromLocalFile(file_path))
#         self.mediaPlayer.setMedia(media_content)

#         # Set the layout for the control widget
#         controlLayout = QVBoxLayout()
#         controlLayout.addWidget(self.mediaPlayer)

#         # Set the layout for the control widget
#         self.controlWidget.setLayout(controlLayout)

#         # Play the media
#         self.mediaPlayer.play()

# if __name__ == '__main__':
#     app = QApplication(sys.argv)

#     # Provide the file path here
#     file_path = r"C:\Users\Dell\Documents\rbhus_clone_root\template\test_video.mp4"

#     mainWindow = MainWindow(file_path)
#     mainWindow.show()

#     sys.exit(app.exec_())


# import sys
# from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
# from PyQt5.QtCore import Qt
# import vlc

# class MainWindow(QMainWindow):
#     def __init__(self, file_path, parent=None):
#         super(MainWindow, self).__init__(parent)
#         self.setWindowTitle("VLC Player")
#         self.setGeometry(100, 100, 800, 600)

#         # Create a QWidget to hold the VLC player
#         self.videoFrame = QFrame(self)
#         self.videoFrame.setFrameShape(QFrame.Box)

#         # Set the layout for the main window
#         self.layout = QVBoxLayout()
#         self.layout.addWidget(self.videoFrame)

#         # Set the layout of the main window
#         centralWidget = QWidget(self)
#         centralWidget.setLayout(self.layout)
#         self.setCentralWidget(centralWidget)

#         # Create a VLC instance
#         self.vlcInstance = vlc.Instance()

#         # Create a VLC media player
#         self.mediaPlayer = self.vlcInstance.media_player_new()

#         # Set the video output window handle
#         if sys.platform == "win32":
#             self.mediaPlayer.set_hwnd(self.videoFrame.winId())
#         else:
#             self.mediaPlayer.set_xwindow(self.videoFrame.winId())

#         # Load and play the specified file
#         self.play(file_path)

#     def play(self, file_path):
#         # Create a VLC media
#         media = self.vlcInstance.media_new(file_path)

#         # Set the media to the player
#         self.mediaPlayer.set_media(media)

#         # Play the media
#         self.mediaPlayer.play()

# if __name__ == '__main__':
#     app = QApplication(sys.argv)

#     # Provide the file path here
#     file_path = r"C:\Users\Dell\Documents\rbhus_clone_root\template\test_video.mp3"

#     mainWindow = MainWindow(file_path)
#     mainWindow.show()

#     sys.exit(app.exec_())


# import sys
# from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QSlider, QHBoxLayout, QPushButton
# from PyQt5.QtCore import Qt, QUrl, QTimer
# from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
# from PyQt5.QtMultimediaWidgets import QVideoWidget

# class MainWindow(QMainWindow):
#     def __init__(self, file_path, parent=None):
#         super(MainWindow, self).__init__(parent)
#         self.setWindowTitle("VLC Player")
#         self.setGeometry(100, 100, 800, 600)

#         # Create a QMediaPlayer instance
#         self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)

#         # Create a QVideoWidget to hold the video output
#         self.videoWidget = QVideoWidget(self)

#         # Create a QWidget to hold the VLC player UI controls
#         self.controlWidget = QWidget(self)

#         # Create a QSlider for the timeline
#         self.slider = QSlider(Qt.Horizontal)

#         # Create a QPushButton for play/pause
#         self.playButton = QPushButton("Play")

#         # Set the layout for the main window
#         self.layout = QVBoxLayout()
#         self.layout.addWidget(self.videoWidget)
#         self.layout.addWidget(self.controlWidget)

#         # Set the layout of the main window
#         centralWidget = QWidget(self)
#         centralWidget.setLayout(self.layout)
#         self.setCentralWidget(centralWidget)

#         # Set the video widget as the output for the media player
#         self.mediaPlayer.setVideoOutput(self.videoWidget)

#         # Load and play the specified file
#         self.play(file_path)

#         # Connect signals and slots
#         self.slider.sliderMoved.connect(self.setSliderPosition)
#         self.playButton.clicked.connect(self.togglePlay)

#         # Timer to update the slider position
#         self.timer = QTimer(self)
#         self.timer.setInterval(100)
#         self.timer.timeout.connect(self.updateSlider)
#         self.timer.start()

#     def play(self, file_path):
#         # Load the media file
#         media_content = QMediaContent(QUrl.fromLocalFile(file_path))
#         self.mediaPlayer.setMedia(media_content)

#         # Set the layout for the control widget
#         controlLayout = QHBoxLayout()
#         controlLayout.addWidget(self.slider)
#         controlLayout.addWidget(self.playButton)

#         # Set the layout for the control widget
#         self.controlWidget.setLayout(controlLayout)

#         # Play the media
#         self.mediaPlayer.play()

#     def setSliderPosition(self, position):
#         self.mediaPlayer.setPosition(position)

#     def togglePlay(self):
#         if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
#             self.mediaPlayer.pause()
#             self.playButton.setText("Play")
#         else:
#             self.mediaPlayer.play()
#             self.playButton.setText("Pause")

#     def updateSlider(self):
#         position = self.mediaPlayer.position()
#         duration = self.mediaPlayer.duration()
#         self.slider.setMaximum(duration)
#         self.slider.setValue(position)

# if __name__ == '__main__':
#     app = QApplication(sys.argv)

#     # Provide the file path here
#     file_path = r"C:\Users\Dell\Documents\rbhus_clone_root\template\test_video.mp3"

#     mainWindow = MainWindow(file_path)
#     mainWindow.show()

#     sys.exit(app.exec_())


# import sys
# from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QSlider, QHBoxLayout, QPushButton
# from PyQt5.QtCore import Qt, QUrl, QTimer
# from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
# from PyQt5.QtMultimediaWidgets import QVideoWidget

# class MainWindow(QMainWindow):
#     def __init__(self, file_path, parent=None):
#         super(MainWindow, self).__init__(parent)
#         self.setWindowTitle("VLC Player")
#         self.setGeometry(100, 100, 800, 600)

#         # Create a QMediaPlayer instance
#         self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)

#         # Create a QVideoWidget to hold the video output
#         self.videoWidget = QVideoWidget(self)

#         # Create a QWidget to hold the VLC player UI controls
#         self.controlWidget = QWidget(self)

#         # Create a QSlider for the timeline
#         self.slider = QSlider(Qt.Horizontal)

#         # Create a QPushButton for play/pause
#         self.playButton = QPushButton("Play")

#         # Set the layout for the main window
#         self.layout = QVBoxLayout()
#         self.layout.addWidget(self.videoWidget)
#         self.layout.addWidget(self.controlWidget)

#         # Set the layout of the main window
#         centralWidget = QWidget(self)
#         centralWidget.setLayout(self.layout)
#         self.setCentralWidget(centralWidget)

#         # Set the video widget as the output for the media player
#         self.mediaPlayer.setVideoOutput(self.videoWidget)

#         # Load and play the specified file
#         self.play(file_path)

#         # Connect signals and slots
#         self.slider.sliderMoved.connect(self.setSliderPosition)
#         self.playButton.clicked.connect(self.togglePlay)

#         # Timer to update the slider position
#         self.timer = QTimer(self)
#         self.timer.setInterval(100)
#         self.timer.timeout.connect(self.updateSlider)
#         self.timer.start()

#     def play(self, file_path):
#         # Load the media file
#         media_content = QMediaContent(QUrl.fromLocalFile(file_path))
#         self.mediaPlayer.setMedia(media_content)

#         # Set the layout for the control widget
#         controlLayout = QHBoxLayout()
#         controlLayout.addWidget(self.slider)
#         controlLayout.addWidget(self.playButton)

#         # Set the layout for the control widget
#         self.controlWidget.setLayout(controlLayout)

#         # Play the media
#         self.mediaPlayer.play()

#     def setSliderPosition(self, position):
#         self.mediaPlayer.setPosition(position)
#         if self.mediaPlayer.state() != QMediaPlayer.PlayingState:
#             self.mediaPlayer.play()
#             self.playButton.setText("Pause")

#     def togglePlay(self):
#         if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
#             self.mediaPlayer.pause()
#             self.playButton.setText("Play")
#         else:
#             self.mediaPlayer.play()
#             self.playButton.setText("Pause")

#     def updateSlider(self):
#         position = self.mediaPlayer.position()
#         duration = self.mediaPlayer.duration()
#         self.slider.setMaximum(duration)
#         self.slider.setValue(position)

# if __name__ == '__main__':
#     app = QApplication(sys.argv)

#     # Provide the file path here
#     file_path = r"C:\Users\Dell\Documents\rbhus_clone_root\template\test_video.mp3"

#     mainWindow = MainWindow(file_path)
#     mainWindow.show()

#     sys.exit(app.exec_())


# import sys
# from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QSlider, QHBoxLayout, QPushButton
# from PyQt5.QtCore import Qt, QUrl, QTimer
# from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
# from PyQt5.QtMultimediaWidgets import QVideoWidget

# class MainWindow(QMainWindow):
#     def __init__(self, file_path, parent=None):
#         super(MainWindow, self).__init__(parent)
#         self.setWindowTitle("VLC Player")
#         self.setGeometry(100, 100, 800, 600)

#         # Create a QMediaPlayer instance
#         self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)

#         # Create a QVideoWidget to hold the video output
#         self.videoWidget = QVideoWidget(self)

#         # Create a QWidget to hold the VLC player UI controls
#         self.controlWidget = QWidget(self)

#         # Create a QSlider for the timeline
#         self.slider = QSlider(Qt.Horizontal)

#         # Create a QPushButton for play/pause
#         self.playButton = QPushButton("Play")

#         # Set the layout for the main window
#         self.layout = QVBoxLayout()
#         self.layout.addWidget(self.videoWidget)
#         self.layout.addWidget(self.controlWidget)

#         # Set the layout of the main window
#         centralWidget = QWidget(self)
#         centralWidget.setLayout(self.layout)
#         self.setCentralWidget(centralWidget)

#         # Set the video widget as the output for the media player
#         self.mediaPlayer.setVideoOutput(self.videoWidget)

#         # Load and play the specified file
#         self.play(file_path)

#         # Connect signals and slots
#         self.slider.sliderPressed.connect(self.sliderPressedEvent)
#         self.slider.sliderReleased.connect(self.sliderReleasedEvent)
#         self.playButton.clicked.connect(self.togglePlay)

#         # Timer to update the slider position
#         self.timer = QTimer(self)
#         self.timer.setInterval(100)
#         self.timer.timeout.connect(self.updateSlider)
#         self.timer.start()

#     def play(self, file_path):
#         # Load the media file
#         media_content = QMediaContent(QUrl.fromLocalFile(file_path))
#         self.mediaPlayer.setMedia(media_content)

#         # Set the layout for the control widget
#         controlLayout = QHBoxLayout()
#         controlLayout.addWidget(self.slider)
#         controlLayout.addWidget(self.playButton)

#         # Set the layout for the control widget
#         self.controlWidget.setLayout(controlLayout)

#         # Play the media
#         self.mediaPlayer.play()

#     def sliderPressedEvent(self):
#         self.mediaPlayer.pause()

#     def sliderReleasedEvent(self):
#         self.mediaPlayer.setPosition(self.slider.value())
#         self.mediaPlayer.play()

#     def togglePlay(self):
#         if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
#             self.mediaPlayer.pause()
#             self.playButton.setText("Play")
#         else:
#             self.mediaPlayer.play()
#             self.playButton.setText("Pause")

#     def updateSlider(self):
#         position = self.mediaPlayer.position()
#         duration = self.mediaPlayer.duration()
#         self.slider.setMaximum(duration)
#         self.slider.setValue(position)

# if __name__ == '__main__':
#     app = QApplication(sys.argv)

#     # Provide the file path here
#     file_path = r"C:\Users\Dell\Documents\rbhus_clone_root\template\test_video.mp3"

#     mainWindow = MainWindow(file_path)
#     mainWindow.show()

#     sys.exit(app.exec_())


# import sys
# from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QSlider, QHBoxLayout, QPushButton, QScrollBar
# from PyQt5.QtCore import Qt, QUrl, QTimer
# from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
# from PyQt5.QtMultimediaWidgets import QVideoWidget

# class MainWindow(QMainWindow):
#     def __init__(self, file_path, parent=None):
#         super(MainWindow, self).__init__(parent)
#         self.setWindowTitle("VLC Player")
#         self.setGeometry(100, 100, 800, 600)

#         # Create a QMediaPlayer instance
#         self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)

#         # Create a QVideoWidget to hold the video output
#         self.videoWidget = QVideoWidget(self)

#         # Create a QWidget to hold the VLC player UI controls
#         self.controlWidget = QWidget(self)

#         # Create a QSlider for the timeline
#         self.timelineSlider = QSlider(Qt.Horizontal)

#         # Create a QScrollBar for fine-grained seeking
#         self.seekScrollBar = QScrollBar(Qt.Horizontal)
#         self.seekScrollBar.setPageStep(10000)  # Set the page step size
#         self.seekScrollBar.setSingleStep(1000)  # Set the single step size
#         self.seekScrollBar.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
#         self.seekScrollBar.setMaximumWidth(200)  # Adjust the width as needed

#         # Create a QPushButton for play/pause
#         self.playButton = QPushButton("Play")

#         # Set the layout for the main window
#         self.layout = QVBoxLayout()
#         self.layout.addWidget(self.videoWidget)
#         self.layout.addWidget(self.controlWidget)

#         # Set the layout of the main window
#         centralWidget = QWidget(self)
#         centralWidget.setLayout(self.layout)
#         self.setCentralWidget(centralWidget)

#         # Set the video widget as the output for the media player
#         self.mediaPlayer.setVideoOutput(self.videoWidget)

#         # Load and play the specified file
#         self.play(file_path)

#         # Connect signals and slots
#         self.timelineSlider.sliderPressed.connect(self.sliderPressedEvent)
#         self.timelineSlider.sliderReleased.connect(self.sliderReleasedEvent)
#         self.timelineSlider.valueChanged.connect(self.sliderValueChangedEvent)
#         self.seekScrollBar.valueChanged.connect(self.scrollBarValueChangedEvent)
#         self.playButton.clicked.connect(self.togglePlay)

#         # Timer to update the slider position
#         self.timer = QTimer(self)
#         self.timer.setInterval(100)
#         self.timer.timeout.connect(self.updateSlider)
#         self.timer.start()

#     def play(self, file_path):
#         # Load the media file
#         media_content = QMediaContent(QUrl.fromLocalFile(file_path))
#         self.mediaPlayer.setMedia(media_content)

#         # Set the layout for the control widget
#         controlLayout = QHBoxLayout()
#         controlLayout.addWidget(self.timelineSlider)
#         controlLayout.addWidget(self.seekScrollBar)
#         controlLayout.addWidget(self.playButton)

#         # Set the layout for the control widget
#         self.controlWidget.setLayout(controlLayout)

#         # Play the media
#         self.mediaPlayer.play()

#     def sliderPressedEvent(self):
#         self.mediaPlayer.pause()

#     def sliderReleasedEvent(self):
#         self.mediaPlayer.setPosition(self.timelineSlider.value())
#         self.mediaPlayer.play()

#     def sliderValueChangedEvent(self, value):
#         self.mediaPlayer.setPosition(value)

#     def scrollBarValueChangedEvent(self, value):
#         self.timelineSlider.setValue(value)

#     def togglePlay(self):
#         if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
#             self.mediaPlayer.pause()
#             self.playButton.setText("Play")
#         else:
#             self.mediaPlayer.play()
#             self.playButton.setText("Pause")

#     def updateSlider(self):
#         position = self.mediaPlayer.position()
#         duration = self.mediaPlayer.duration()

#         # Update the timeline slider and scroll bar
#         self.timelineSlider.setMaximum(duration)
#         self.timelineSlider.setValue(position)

#         self.seekScrollBar.setMaximum(duration - self.timelineSlider.pageStep())
#         self.seekScrollBar.setValue(position)


# if __name__ == '__main__':
#     app = QApplication(sys.argv)

#     # Provide the file path here
#     file_path = r"C:\Users\Dell\Documents\rbhus_clone_root\template\test_video.mp3"

#     mainWindow = MainWindow(file_path)
#     mainWindow.show()

#     sys.exit(app.exec_())


# import os
# import sys

# dllFolder = os.path.abspath(__file__)
# sys.path.append(dllFolder)

# os.environ["PATH"] = os.path.dirname(__file__)

# from PyQt5.QtWidgets import *
# from PyQt5.QtCore import *

# import mpv
# from mpv import MPV


# class MainWindow(QMainWindow):
#     def __init__(self, media_file_path):
#         super().__init__()

#         self.container = QWidget(self)
#         self.setCentralWidget(self.container)
#         self.container.setAttribute(Qt.WA_DontCreateNativeAncestors)
#         self.container.setAttribute(Qt.WA_NativeWindow)

#         self.player = MPV(wid=str(int(self.container.winId())), input_default_bindings=True, input_vo_keyboard=True, osd="yes")
#         self.player.play(media_file_path)

#     def closeEvent(self, event):
#         self.player.quit()
#         event.accept()


# if __name__ == "__main__":
#     media_file_path = r"C:\Users\Dell\Documents\rbhus_clone_root\template\test_video.mp4"

#     app = QApplication(sys.argv)
#     win = MainWindow(media_file_path)
#     win.show()
#     sys.exit(app.exec_())



# import sys
# import os
# from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout
# from PyQt5.QtCore import Qt

# dllFolder = os.path.abspath(__file__)
# sys.path.append(dllFolder)
# os.environ["PATH"] = os.path.dirname(__file__)

# import mpv

# class MPVWidget(QWidget):
#     def __init__(self, parent=None):
#         super(MPVWidget, self).__init__(parent)
#         self.setAttribute(Qt.WA_NativeWindow)
#         self.mpv = mpv.MPV(wid=str(int(self.winId())))

#     def keyPressEvent(self, event):
#         self.mpv.command('keypress', event.text())
#         event.accept()

#     def mousePressEvent(self, event):
#         if event.button() == Qt.LeftButton:
#             self.mpv.command('mouse', '0')
#         elif event.button() == Qt.RightButton:
#             self.mpv.command('mouse', '2')
#         event.accept()

#     def mouseMoveEvent(self, event):
#         self.mpv.command('mouse_move', event.x(), self.height() - event.y())

#     def resizeEvent(self, event):
#         self.mpv.command('osd-bar', 'yes')
#         event.accept()

# class MainWindow(QMainWindow):
#     def __init__(self):
#         super(MainWindow, self).__init__()
#         self.setWindowTitle('MPV Player')
#         self.setGeometry(100, 100, 800, 600)
#         central_widget = QWidget(self)
#         self.setCentralWidget(central_widget)
#         layout = QVBoxLayout(central_widget)
#         self.mpv_widget = MPVWidget(self)  # Make sure you are using MPVWidget
#         layout.addWidget(self.mpv_widget)

# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     main_window = MainWindow()
#     main_window.show()
#     sys.exit(app.exec_())


# import sys
# from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QSlider, QHBoxLayout, QPushButton, QScrollBar
# from PyQt5.QtCore import Qt, QUrl, QTimer
# from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
# from PyQt5.QtMultimediaWidgets import QVideoWidget

# class MainWindow(QMainWindow):
#     def __init__(self, file_path, parent=None):
#         super(MainWindow, self).__init__(parent)
#         self.setWindowTitle("VLC Player")
#         self.setGeometry(100, 100, 800, 600)

#         # Create a QMediaPlayer instance
#         self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)

#         # Create a QVideoWidget to hold the video output
#         self.videoWidget = QVideoWidget(self)

#         # Create a QWidget to hold the VLC player UI controls
#         self.controlWidget = QWidget(self)

#         # Create a QSlider for the timeline
#         self.timelineSlider = QSlider(Qt.Horizontal)

#         # Create a QScrollBar for fine-grained seeking
#         self.seekScrollBar = QScrollBar(Qt.Horizontal)
#         self.seekScrollBar.setPageStep(10000)  # Set the page step size
#         self.seekScrollBar.setSingleStep(1000)  # Set the single step size
#         self.seekScrollBar.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
#         self.seekScrollBar.setMaximumWidth(200)  # Adjust the width as needed

#         # Create a QPushButton for play/pause
#         self.playButton = QPushButton("Play")

#         # Set the layout for the main window
#         self.layout = QVBoxLayout()
#         self.layout.addWidget(self.videoWidget)
#         self.layout.addWidget(self.controlWidget)

#         # Set the layout of the main window
#         centralWidget = QWidget(self)
#         centralWidget.setLayout(self.layout)
#         self.setCentralWidget(centralWidget)

#         # Set the video widget as the output for the media player
#         self.mediaPlayer.setVideoOutput(self.videoWidget)

#         # Load and play the specified file
#         self.play(file_path)

#         # Connect signals and slots
#         self.timelineSlider.sliderPressed.connect(self.sliderPressedEvent)
#         self.timelineSlider.sliderReleased.connect(self.sliderReleasedEvent)
#         self.timelineSlider.valueChanged.connect(self.sliderValueChangedEvent)
#         self.seekScrollBar.valueChanged.connect(self.scrollBarValueChangedEvent)
#         self.playButton.clicked.connect(self.togglePlay)

#         # Timer to update the slider position
#         self.timer = QTimer(self)
#         self.timer.setInterval(100)
#         self.timer.timeout.connect(self.updateSlider)
#         self.timer.start()

#     def play(self, file_path):
#         # Load the media file
#         media_content = QMediaContent(QUrl.fromLocalFile(file_path))
#         self.mediaPlayer.setMedia(media_content)

#         # Set the layout for the control widget
#         controlLayout = QHBoxLayout()
#         controlLayout.addWidget(self.timelineSlider)
#         controlLayout.addWidget(self.seekScrollBar)
#         controlLayout.addWidget(self.playButton)

#         # Set the layout for the control widget
#         self.controlWidget.setLayout(controlLayout)

#         # Play the media
#         self.mediaPlayer.play()

#     def sliderPressedEvent(self):
#         self.mediaPlayer.pause()

#     def sliderReleasedEvent(self):
#         self.mediaPlayer.setPosition(self.timelineSlider.value())
#         self.mediaPlayer.play()

#     def sliderValueChangedEvent(self, value):
#         self.mediaPlayer.setPosition(value)

#     def scrollBarValueChangedEvent(self, value):
#         self.timelineSlider.setValue(value)

#     def togglePlay(self):
#         if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
#             self.mediaPlayer.pause()
#             self.playButton.setText("Play")
#         else:
#             self.mediaPlayer.play()
#             self.playButton.setText("Pause")

#     def updateSlider(self):
#         position = self.mediaPlayer.position()
#         duration = self.mediaPlayer.duration()

#         # Update the timeline slider and scroll bar
#         self.timelineSlider.setMaximum(duration)
#         self.timelineSlider.setValue(position)

#         self.seekScrollBar.setMaximum(duration - self.timelineSlider.pageStep())
#         self.seekScrollBar.setValue(position)


# if __name__ == '__main__':
#     app = QApplication(sys.argv)

#     # Provide the file path here
#     file_path = r"C:\Users\Dell\Documents\rbhus_clone_root\template\test_video.mp3"

#     mainWindow = MainWindow(file_path)
#     mainWindow.show()

#     sys.exit(app.exec_())



# import sys
# from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QSlider, QHBoxLayout, QPushButton
# from PyQt5.QtCore import Qt, QUrl, QTimer
# from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent, QAudioOutput
# from PyQt5.QtMultimediaWidgets import QVideoWidget

# class MainWindow(QMainWindow):
#     def __init__(self, file_path, parent=None):
#         super(MainWindow, self).__init__(parent)
#         self.setWindowTitle("VLC Player")
#         self.setGeometry(100, 100, 800, 600)

#         # Create a QMediaPlayer instance
#         self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)

#         # Create a QVideoWidget to hold the video output
#         self.videoWidget = QVideoWidget(self)

#         # Create a QWidget to hold the VLC player UI controls
#         self.controlWidget = QWidget(self)

#         # Create a QSlider for the timeline
#         self.timelineSlider = QSlider(Qt.Horizontal)

#         # Create a QPushButton for play/pause
#         self.playButton = QPushButton("Play")

#         # Set the layout for the main window
#         self.layout = QVBoxLayout()
#         self.layout.addWidget(self.videoWidget)
#         self.layout.addWidget(self.controlWidget)

#         # Set the layout of the main window
#         centralWidget = QWidget(self)
#         centralWidget.setLayout(self.layout)
#         self.setCentralWidget(centralWidget)

#         # Set the video widget as the output for the media player
#         self.mediaPlayer.setVideoOutput(self.videoWidget)

#         # Load and play the specified file
#         self.play(file_path)

#         # Connect signals and slots
#         self.timelineSlider.sliderPressed.connect(self.sliderPressedEvent)
#         self.timelineSlider.sliderReleased.connect(self.sliderReleasedEvent)
#         self.timelineSlider.valueChanged.connect(self.sliderValueChangedEvent)
#         self.playButton.clicked.connect(self.togglePlay)

#         # Timer to update the slider position
#         self.timer = QTimer(self)
#         self.timer.setInterval(100)
#         self.timer.timeout.connect(self.updateSlider)
#         self.timer.start()

#     def play(self, file_path):
#         # Load the media file
#         media_content = QMediaContent(QUrl.fromLocalFile(file_path))
#         self.mediaPlayer.setMedia(media_content)

#         # Set the layout for the control widget
#         controlLayout = QHBoxLayout()
#         controlLayout.addWidget(self.timelineSlider)
#         controlLayout.addWidget(self.playButton)

#         # Set the layout for the control widget
#         self.controlWidget.setLayout(controlLayout)

#         # Play the media
#         self.mediaPlayer.play()

#     def sliderPressedEvent(self):
#         self.mediaPlayer.pause()

#     def sliderReleasedEvent(self):
#         self.mediaPlayer.setPosition(self.timelineSlider.value())
#         self.mediaPlayer.play()

#     def sliderValueChangedEvent(self, value):
#         self.mediaPlayer.setPosition(value)

#     def togglePlay(self):
#         if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
#             self.mediaPlayer.pause()
#             self.playButton.setText("Play")
#         else:
#             self.mediaPlayer.play()
#             self.playButton.setText("Pause")

#     def updateSlider(self):
#         position = self.mediaPlayer.position()
#         duration = self.mediaPlayer.duration()

#         if duration > 0:
#             self.timelineSlider.setMaximum(duration)
#             self.timelineSlider.setValue(position)

# app = QApplication(sys.argv)
# window = MainWindow(r"C:\Users\Dell\Documents\rbhus_clone_root\template\test_video.mp3")
# window.show()
# sys.exit(app.exec_())



# import sys
# from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QHBoxLayout, QPushButton, QScrollBar
# from PyQt5.QtCore import Qt, QUrl, QTimer
# from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
# from PyQt5.QtMultimediaWidgets import QVideoWidget

# class MainWindow(QMainWindow):
#     def __init__(self, file_path, parent=None):
#         super(MainWindow, self).__init__(parent)
#         self.setWindowTitle("VLC Player")
#         self.setGeometry(100, 100, 800, 600)

#         # Create a QMediaPlayer instance
#         self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)

#         # Create a QVideoWidget to hold the video output
#         self.videoWidget = QVideoWidget(self)

#         # Create a QWidget to hold the VLC player UI controls
#         self.controlWidget = QWidget(self)

#         # Create a QScrollBar for the timeline
#         self.timelineScrollBar = QScrollBar(Qt.Horizontal)
#         self.timelineScrollBar.setPageStep(10000)  # Set the page step size
#         self.timelineScrollBar.setSingleStep(1000)  # Set the single step size

#         # Create a QPushButton for play/pause
#         self.playButton = QPushButton("Play")

#         # Set the layout for the main window
#         self.layout = QVBoxLayout()
#         self.layout.addWidget(self.videoWidget)
#         self.layout.addWidget(self.controlWidget)

#         # Set the layout of the main window
#         centralWidget = QWidget(self)
#         centralWidget.setLayout(self.layout)
#         self.setCentralWidget(centralWidget)

#         # Set the video widget as the output for the media player
#         self.mediaPlayer.setVideoOutput(self.videoWidget)

#         # Load and play the specified file
#         self.play(file_path)

#         # Connect signals and slots
#         self.timelineScrollBar.sliderPressed.connect(self.sliderPressedEvent)
#         self.timelineScrollBar.sliderReleased.connect(self.sliderReleasedEvent)
#         self.timelineScrollBar.valueChanged.connect(self.sliderValueChangedEvent)
#         self.playButton.clicked.connect(self.togglePlay)

#         # Timer to update the slider position
#         self.timer = QTimer(self)
#         self.timer.setInterval(100)
#         self.timer.timeout.connect(self.updateSlider)
#         self.timer.start()

#     def play(self, file_path):
#         # Load the media file
#         media_content = QMediaContent(QUrl.fromLocalFile(file_path))
#         self.mediaPlayer.setMedia(media_content)

#         # Set the layout for the control widget
#         controlLayout = QHBoxLayout()
#         controlLayout.addWidget(self.timelineScrollBar)
#         controlLayout.addWidget(self.playButton)

#         # Set the layout for the control widget
#         self.controlWidget.setLayout(controlLayout)

#         # Play the media
#         self.mediaPlayer.play()

#     def sliderPressedEvent(self):
#         self.mediaPlayer.pause()

#     def sliderReleasedEvent(self):
#         self.mediaPlayer.setPosition(self.timelineScrollBar.value())
#         self.mediaPlayer.play()

#     def sliderValueChangedEvent(self, value):
#         self.mediaPlayer.setPosition(value)

#     def togglePlay(self):
#         if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
#             self.mediaPlayer.pause()
#             self.playButton.setText("Play")
#         else:
#             self.mediaPlayer.play()
#             self.playButton.setText("Pause")

#     def updateSlider(self):
#         position = self.mediaPlayer.position()
#         duration = self.mediaPlayer.duration()

#         if duration > 0:
#             self.timelineScrollBar.setMaximum(duration)
#             self.timelineScrollBar.setValue(position)

# app = QApplication(sys.argv)
# window = MainWindow(r"C:\Users\Dell\Documents\rbhus_clone_root\template\test_video.mp3")
# window.show()
# sys.exit(app.exec_())



# import sys
# from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QScrollBar, QHBoxLayout, QPushButton
# from PyQt5.QtCore import Qt, QUrl, QTimer
# from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent, QAudioOutput
# from PyQt5.QtMultimediaWidgets import QVideoWidget

# class MainWindow(QMainWindow):
#     def __init__(self, file_path, parent=None):
#         super(MainWindow, self).__init__(parent)
#         self.setWindowTitle("VLC Player")
#         self.setGeometry(100, 100, 800, 600)

#         # Create a QMediaPlayer instance
#         self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)

#         # Create a QVideoWidget to hold the video output
#         self.videoWidget = QVideoWidget(self)

#         # Create a QWidget to hold the VLC player UI controls
#         self.controlWidget = QWidget(self)

#         # Create a QScrollBar for the timeline
#         self.scrollBar = QScrollBar(Qt.Horizontal)

#         # Create a QPushButton for play/pause
#         self.playButton = QPushButton("Play")

#         # Set the layout for the main window
#         self.layout = QVBoxLayout()
#         self.layout.addWidget(self.videoWidget)
#         self.layout.addWidget(self.controlWidget)

#         # Set the layout of the main window
#         centralWidget = QWidget(self)
#         centralWidget.setLayout(self.layout)
#         self.setCentralWidget(centralWidget)

#         # Set the video widget as the output for the media player
#         self.mediaPlayer.setVideoOutput(self.videoWidget)

        
#         # Load and play the specified file
#         self.play(file_path)

#         # Connect signals and slots
#         self.scrollBar.sliderPressed.connect(self.sliderPressedEvent)
#         self.scrollBar.sliderReleased.connect(self.sliderReleasedEvent)
#         self.scrollBar.valueChanged.connect(self.sliderValueChangedEvent)
#         self.playButton.clicked.connect(self.togglePlay)

#         # Timer to update the slider position
#         self.timer = QTimer(self)
#         self.timer.setInterval(100000)
#         self.timer.timeout.connect(self.updateSlider)
#         self.timer.start()

#     def play(self, file_path):
#         # Load the media file
#         media_content = QMediaContent(QUrl.fromLocalFile(file_path))
#         self.mediaPlayer.setMedia(media_content)

#         # Set the layout for the control widget
#         controlLayout = QHBoxLayout()
#         controlLayout.addWidget(self.scrollBar)
#         controlLayout.addWidget(self.playButton)

#         # Set the layout for the control widget
#         self.controlWidget.setLayout(controlLayout)

#         # Play the media
#         self.mediaPlayer.play()

#     def sliderPressedEvent(self):
#         self.mediaPlayer.pause()

#     def sliderReleasedEvent(self):
#         self.mediaPlayer.setPosition(self.scrollBar.value())
#         self.mediaPlayer.play()

#     def sliderValueChangedEvent(self, value):
#         self.mediaPlayer.setPosition(value)

#     def togglePlay(self):
#         if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
#             self.mediaPlayer.pause()
#             self.playButton.setText("Play")
#         else:
#             self.mediaPlayer.play()
#             self.playButton.setText("Pause")

#     def updateSlider(self):
#         position = self.mediaPlayer.position()
#         duration = self.mediaPlayer.duration()

#         if duration > 0:
#             self.scrollBar.setMaximum(duration)
#             self.scrollBar.setValue(position)

# app = QApplication(sys.argv)
# window = MainWindow(r"C:\Users\Dell\Documents\rbhus_clone_root\template\test_video.mp3")
# window.show()
# sys.exit(app.exec_())



# import sys
# from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QFileDialog, QStyle, QVBoxLayout
# from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
# from PyQt5.QtMultimediaWidgets import QVideoWidget
# from PyQt5.QtGui import QIcon

# class VideoPlayer(QWidget):
#     def __init__(self):
#         super().__init__()

#         self.setWindowTitle("PyQt5 Video Player")
#         self.setGeometry(350, 100, 700, 500)

        # self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)

        # videoWidget = QVideoWidget()

        # fileName = r"C:\Users\Dell\Documents\rbhus_clone_root\template\test_video.mp3"
        # self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile(fileName)))

        # self.playButton = QPushButton()
        # self.playButton.setEnabled(True)
        # self.playButton.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))
        # self.playButton.clicked.connect(self.play_pause)

        # self.positionSlider = QSlider(Qt.Horizontal)
        # self.positionSlider.setRange(0, 0)
        # self.positionSlider.sliderMoved.connect(self.set_position)

        # layout = QVBoxLayout()
        # layout.addWidget(videoWidget)
        # layout.addWidget(self.playButton)
        # layout.addWidget(self.positionSlider)

        # self.setLayout(layout)

        # self.mediaPlayer.setVideoOutput(videoWidget)
        
        # self.mediaPlayer.stateChanged.connect(self.media_state_changed)
        # self.mediaPlayer.positionChanged.connect(self.position_changed)
        # self.mediaPlayer.durationChanged.connect(self.duration_changed)
        # self.mediaPlayer.error.connect(self.handle_error)

    # def play_pause(self):
    #     if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
    #         self.mediaPlayer.pause()
    #     else:
    #         self.mediaPlayer.play()

    # def media_state_changed(self, state):
    #     if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
    #         self.playButton.setIcon(
    #                 self.style().standardIcon(QStyle.SP_MediaPause))
    #     else:
    #         self.playButton.setIcon(
    #                 self.style().standardIcon(QStyle.SP_MediaPlay))

    # def position_changed(self, position):
    #     self.positionSlider.setValue(position)

    # def duration_changed(self, duration):
    #     self.positionSlider.setRange(0, duration)

    # def set_position(self, position):
    #     self.mediaPlayer.setPosition(position)
    #     # self.mediaPlayer.play()

    # def handle_error(self):
    #     self.playButton.setEnabled(False)

# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     player = VideoPlayer()
#     player.show()
#     sys.exit(app.exec_())






#!/usr/bin/python3
# *-* coding: utf-8 *-*

import os
import sys
import setproctitle
import uuid
import subprocess
import shlex
# import rbhus_clone_db
# import debug
import bcrypt


from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

from PyQt5 import QtCore, uic, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QTreeView, QFileSystemModel, QVBoxLayout, QWidget, QHBoxLayout, QListView
from PyQt5.QtWidgets import QListWidgetItem, QShortcut
from PyQt5.QtGui import QKeySequence, QIcon
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtMultimediaWidgets import QVideoWidget



projDir = os.sep.join(os.path.abspath(__file__).split(os.sep)[:-2])
sys.path.append(projDir)

main_ui_file = os.path.join(projDir,  "tests", "app_test.ui")

# root_folder = "/home/sanath.shetty/Documents/rbhus_clone_root/"

os.environ['QT_LOGGING_RULES'] = "qt5ct.debug=false"


class appTest():
    # db = rbhus_clone_db.db()
    def __init__(self):
       
        self.main_ui = uic.loadUi(main_ui_file)
        self.main_ui.setWindowTitle("App TEST")

        self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)

        videoWidget = QVideoWidget()

        fileName = r"C:\Users\Dell\Documents\rbhus_clone_root\template\test_video.mp3"
        self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile(fileName)))

        
        # self.main_ui.playButton.setText("Play")
        self.main_ui.playButton.setIcon(QtGui.QIcon(os.path.join(projDir, "tests", "play.svg")))
        self.main_ui.forwardButt.setIcon(QtGui.QIcon(os.path.join(projDir, "tests", "chevron-right.svg")))
        self.main_ui.backwardButt.setIcon(QtGui.QIcon(os.path.join(projDir, "tests", "chevron-left.svg")))

        self.main_ui.forwardButt.setShortcut(QKeySequence(Qt.Key_Left))
        self.main_ui.backwardButt.setShortcut(QKeySequence(Qt.Key_Left))

        self.main_ui.playButton.clicked.connect(self.play_pause)
        self.main_ui.forwardButt.clicked.connect(self.forward_5_seconds)
        self.main_ui.backwardButt.clicked.connect(self.back_5_seconds)

        self.main_ui.slider.setRange(0, 0)
        self.main_ui.slider.sliderMoved.connect(self.set_position)

        self.main_ui.volumeSlider.setRange(0, 100)
        self.main_ui.volumeSlider.setValue(50)
        self.main_ui.volumeSlider.sliderMoved.connect(self.set_volume)

        layout = QVBoxLayout()
        layout.addWidget(videoWidget)

        self.main_ui.frame.setLayout(layout)

        self.mediaPlayer.setVideoOutput(videoWidget)

        self.mediaPlayer.stateChanged.connect(self.media_state_changed)
        self.mediaPlayer.positionChanged.connect(self.position_changed)
        self.mediaPlayer.durationChanged.connect(self.duration_changed)
        self.mediaPlayer.error.connect(self.handle_error)

        self.main_ui.textFrame.setVisible(False)

        #Show Window
        self.main_ui.show()
        self.main_ui.update()

        qtRectangle = self.main_ui.frameGeometry()
        centerPoint = QtWidgets.QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.main_ui.move(qtRectangle.topLeft())

    def play_pause(self):
        if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
            self.mediaPlayer.pause()
        else:
            self.mediaPlayer.play()
            
    def media_state_changed(self, state):
        if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
            self.main_ui.playButton.setIcon(QtGui.QIcon(os.path.join(projDir, "tests", "pause.svg")))
        else:
            self.main_ui.playButton.setIcon(QtGui.QIcon(os.path.join(projDir, "tests", "play.svg")))

    def position_changed(self, position):
        self.main_ui.slider.setValue(position)

    def duration_changed(self, duration):
        self.main_ui.slider.setRange(0, duration)

    def set_position(self, position):
        self.mediaPlayer.setPosition(position)
        # self.mediaPlayer.play()

    def set_volume(self, volume):
        self.mediaPlayer.setVolume(volume)

    def handle_error(self):
        self.main_ui.playButton.setEnabled(False)

    def forward_5_seconds(self):
        self.mediaPlayer.setPosition(self.mediaPlayer.position() + 5000)

    def back_5_seconds(self):
        self.mediaPlayer.setPosition(self.mediaPlayer.position() - 5000)

if __name__ == '__main__':
    setproctitle.setproctitle("APP_TEST")
    app = QtWidgets.QApplication(sys.argv)
    file = QFile(os.path.join(projDir, "stylesheet.qss"))
    file.open(QFile.ReadOnly | QFile.Text)
    stream = QTextStream(file)
    app.setStyleSheet(stream.readAll())
    window = appTest()
    sys.exit(app.exec_())



