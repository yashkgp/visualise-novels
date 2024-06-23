import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QIcon
from ui.main_window import MainWindow
from clipboard_monitor import ClipboardMonitor


class App:
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.main_window = MainWindow()
        self.clipboard_monitor = ClipboardMonitor(self.main_window)

    def run(self):
        self.app.setWindowIcon(QIcon("resources/icon.webp"))
        self.main_window.show()
        sys.exit(self.app.exec_())


if __name__ == "__main__":
    App().run()
