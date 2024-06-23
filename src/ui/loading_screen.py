from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import Qt

class LoadingScreen(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowFlags(Qt.Window | Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        
        layout = QVBoxLayout()
        self.label = QLabel("Loading...", self)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setStyleSheet("font-size: 24px; color: white;")
        layout.addWidget(self.label)
        
        self.setLayout(layout)
        self.setStyleSheet("background-color: rgba(0, 0, 0, 150);")

    def show(self):
        if self.parentWidget():
            self.setGeometry(self.parentWidget().rect())
        super().show()