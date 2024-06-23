import logging
from PyQt5.QtCore import QObject, QTimer
from PyQt5.QtGui import QGuiApplication
from server_communication import GetVisualization
import requests

# Configure logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


class ClipboardMonitor(QObject):
    def __init__(self, main_window):
        super().__init__()
        self.clipboard = QGuiApplication.clipboard()
        self.text_to_image = GetVisualization()
        self.main_window = main_window
        self.last_text = ""

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.check_clipboard)
        self.timer.start(500)  # Check every second

    def check_clipboard(self):
        text = self.clipboard.text()
        if text != self.last_text:
            self.last_text = text
            self.main_window.show_loading_screen()
            logging.info(f"Clipboard text changed: {text}")
            image_url = self.text_to_image.send_text_get_image(text=text)
            if image_url:
                image_data = requests.get(image_url).content
            self.main_window.update_image(image_data)
