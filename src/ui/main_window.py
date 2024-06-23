from PyQt5.QtWidgets import QMainWindow, QLabel, QVBoxLayout, QWidget
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from .loading_screen import LoadingScreen
import requests


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Text to Image")
        self.setGeometry(100, 100, 400, 400)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout(self.central_widget)

        self.image_label = QLabel(self)
        self.image_label.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.image_label)

        self.loading_screen = LoadingScreen(self)

    def show_loading_screen(self):
        self.loading_screen.show()

    def update_image(self, image_url):
        self.loading_screen.hide()
        if image_url:
            pixmap = QPixmap()
            image_data = requests.get(image_url).content
            pixmap.loadFromData(image_data)
            self.image_label.setPixmap(
                pixmap.scaled(380, 380, Qt.KeepAspectRatio, Qt.SmoothTransformation)
            )
        else:
            self.image_label.setText("Failed to load image")
