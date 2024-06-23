import sys
from PyQt5.QtWidgets import (QMainWindow, QLabel, QVBoxLayout, QWidget, QAction, 
                             QMenuBar, QStatusBar, QFileDialog, QSystemTrayIcon, QMenu)
from PyQt5.QtGui import QPixmap, QIcon, QFont
from PyQt5.QtCore import Qt, QSize
from .loading_screen import LoadingScreen

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Text to Image Converter")
        self.setGeometry(100, 100, 500, 600)
        self.setStyleSheet("""
            QMainWindow {
                background-color: #f0f0f0;
            }
            QLabel {
                color: #333333;
            }
            QStatusBar {
                background-color: #e0e0e0;
            }
        """)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout(self.central_widget)
        
        self.title_label = QLabel("Text to Image Converter", self)
        self.title_label.setAlignment(Qt.AlignCenter)
        self.title_label.setFont(QFont("Arial", 18, QFont.Bold))
        self.layout.addWidget(self.title_label)

        self.instruction_label = QLabel("Select text anywhere to convert it to an image", self)
        self.instruction_label.setAlignment(Qt.AlignCenter)
        self.instruction_label.setFont(QFont("Arial", 12))
        self.layout.addWidget(self.instruction_label)

        self.image_label = QLabel(self)
        self.image_label.setAlignment(Qt.AlignCenter)
        self.image_label.setMinimumSize(400, 400)
        self.image_label.setStyleSheet("""
            QLabel {
                background-color: white;
                border: 2px solid #cccccc;
                border-radius: 10px;
            }
        """)
        self.layout.addWidget(self.image_label)

        self.loading_screen = LoadingScreen(self)

        self.create_menu_bar()
        self.create_status_bar()
        self.create_system_tray()

    def create_menu_bar(self):
        menu_bar = QMenuBar(self)
        self.setMenuBar(menu_bar)

        file_menu = menu_bar.addMenu("File")
        
        save_action = QAction("Save Image", self)
        save_action.setShortcut("Ctrl+S")
        save_action.triggered.connect(self.save_image)
        file_menu.addAction(save_action)

        exit_action = QAction("Exit", self)
        exit_action.setShortcut("Ctrl+Q")
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)

    def create_status_bar(self):
        status_bar = QStatusBar()
        self.setStatusBar(status_bar)
        status_bar.showMessage("Ready")

    def create_system_tray(self):
        self.tray_icon = QSystemTrayIcon(self)
        self.tray_icon.setIcon(QIcon("resources/icon.png"))
        
        tray_menu = QMenu()
        show_action = QAction("Show", self)
        quit_action = QAction("Exit", self)
        show_action.triggered.connect(self.show)
        quit_action.triggered.connect(sys.exit)
        
        tray_menu.addAction(show_action)
        tray_menu.addAction(quit_action)
        self.tray_icon.setContextMenu(tray_menu)
        self.tray_icon.show()

    def show_loading_screen(self):
        self.loading_screen.show()
        self.statusBar().showMessage("Converting text to image...")

    def update_image(self, image_data):
        self.loading_screen.hide()
        if image_data:
            pixmap = QPixmap()
            pixmap.loadFromData(image_data)
            scaled_pixmap = pixmap.scaled(380, 380, Qt.KeepAspectRatio, Qt.SmoothTransformation)
            self.image_label.setPixmap(scaled_pixmap)
            self.statusBar().showMessage("Image received successfully")
        else:
            self.image_label.setText("Failed to load image")
            self.statusBar().showMessage("Failed to receive image")

    def save_image(self):
        if self.image_label.pixmap():
            file_path, _ = QFileDialog.getSaveFileName(self, "Save Image", "", "PNG Files (*.png);;All Files (*)")
            if file_path:
                self.image_label.pixmap().save(file_path)
                self.statusBar().showMessage(f"Image saved to {file_path}")
        else:
            self.statusBar().showMessage("No image to save")

    def closeEvent(self, event):
        event.ignore()
        self.hide()
        self.tray_icon.showMessage(
            "Text to Image Converter",
            "The app is still running in the system tray.",
            QSystemTrayIcon.Information,
            2000
        )