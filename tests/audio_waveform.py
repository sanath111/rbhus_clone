import sys
import numpy as np
import soundfile as sf
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtCore import QUrl
import pyqtgraph as pg


class WaveformWidget(pg.PlotWidget):
    def __init__(self, audio_data, sample_rate, media_player, parent=None):
        super().__init__(parent)
        self.audio_data = audio_data
        self.sample_rate = sample_rate
        self.media_player = media_player
        self.plot_waveform()
        self.setMouseEnabled(x=True, y=False)  # Allow horizontal panning only

    def plot_waveform(self):
        # Downsample for performance
        downsample_factor = 100
        downsampled_data = self.audio_data[::downsample_factor]
        time = np.arange(len(downsampled_data)) * downsample_factor / self.sample_rate
        self.plot(time, downsampled_data, pen='c')  # Cyan line for waveform

    def mousePressEvent(self, event):
        # Map click position to time
        pos = self.plotItem.vb.mapSceneToView(event.pos())
        time_pos = pos.x()
        # Convert to milliseconds and seek
        seek_pos = int(time_pos * 1000)
        self.media_player.setPosition(seek_pos)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # Load audio data (replace 'audio_file.wav' with your file path)
        self.audio_data, self.sample_rate = sf.read('audio_file.wav')

        # Set up media player
        self.media_player = QMediaPlayer()
        self.media_player.setMedia(QMediaContent(QUrl.fromLocalFile('audio_file.wav')))

        # Create and set waveform widget
        self.waveform_widget = WaveformWidget(self.audio_data, self.sample_rate, self.media_player)
        self.setCentralWidget(self.waveform_widget)

        # Window settings
        self.setWindowTitle("Audio Waveform Viewer")
        self.setGeometry(100, 100, 800, 400)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())