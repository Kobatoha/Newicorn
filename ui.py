import sys
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QVBoxLayout
from PyQt6.QtWidgets import QWidget, QPushButton, QVBoxLayout, QMainWindow, QProgressBar, QLineEdit, QLabel, QMenuBar
from PyQt6.QtGui import QIcon, QPixmap, QFont
from PyQt6.QtCore import QRect, QSize, Qt
from uni_widgets import start_stop, lock_window, save_load, status_bar, keys


class Unicorn(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Unicorn')
        self.setWindowIcon(QIcon("images/unicorn.png"))
        self.resize(300, 600)
        self.setMinimumSize(QSize(165, 360))
        self.setMaximumSize(QSize(300, 600))
        self.setBaseSize(QSize(300, 600))
        self.setStyleSheet("background-image: url('images/bg_image.jpg');")

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        start_stop.create_start_stop(central_widget)
        lock_window.create_lock_window(central_widget)
        save_load.create_save_load(central_widget)
        status_bar.create_status_bar(central_widget)
        keys.create_keys(central_widget)





