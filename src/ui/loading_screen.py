from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QMovie


class LoadingScreen(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowFlags(Qt.Window | Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        layout = QVBoxLayout()
        self.label = QLabel(self)
        self.movie = QMovie("resources/loading.gif")
        self.label.setMovie(self.movie)
        layout.addWidget(self.label)

        self.text_label = QLabel("Converting...", self)
        self.text_label.setAlignment(Qt.AlignCenter)
        self.text_label.setStyleSheet(
            "font-size: 18px; color: white; font-weight: bold;"
        )
        layout.addWidget(self.text_label)

        self.setLayout(layout)
        self.setStyleSheet("background-color: rgba(0, 0, 0, 150);")

    def show(self):
        if self.parentWidget():
            self.setGeometry(self.parentWidget().rect())
        self.movie.start()
        super().show()

    def hide(self):
        self.movie.stop()
        super().hide()
