from PyQt6.QtWidgets import QPushButton
from PyQt6.QtGui import QFont
from PyQt6.QtCore import QRect
from functions import functions


def create_save_load(parent):
    font_button = QFont()
    font_button.setPointSize(8)
    font_button.setBold(True)
    font_button.setWeight(75)

    save_button = QPushButton(parent)
    save_button.setGeometry(QRect(170, 510, 51, 31))
    save_button.setStyleSheet("background-color: rgb(255, 239, 220);")
    save_button.setFont(font_button)
    save_button.setObjectName("save_button")
    save_button.setText('save')
    save_button.clicked.connect(functions.save_settings)

    load_button = QPushButton(parent)
    load_button.setGeometry(QRect(230, 510, 51, 31))
    load_button.setStyleSheet("background-color: rgb(255, 239, 220);")
    load_button.setFont(font_button)
    load_button.setObjectName("load_button")
    load_button.setText('load')
    load_button.clicked.connect(functions.load_settings)

    functions.load_settings()
