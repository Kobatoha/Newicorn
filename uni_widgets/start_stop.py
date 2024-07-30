from PyQt6.QtWidgets import QPushButton, QLabel
from PyQt6.QtGui import QFont
from PyQt6.QtCore import QRect, Qt
from functions import functions


def create_start_stop(parent, ui_elements):
    font_button = QFont()
    font_button.setPointSize(10)
    font_button.setBold(True)
    font_button.setWeight(75)

    font_label = QFont()
    font_label.setPointSize(7)
    font_label.setItalic(False)
    font_label.setUnderline(False)
    font_label.setStrikeOut(False)
    font_label.setKerning(True)

    start_stop_button = QPushButton(parent)
    start_stop_button.setGeometry(QRect(100, 490, 40, 40))
    start_stop_button.setStyleSheet("background-color: rgb(255, 239, 220);")
    start_stop_button.setFont(font_button)
    start_stop_button.setObjectName("start_stop_button")
    start_stop_button.setText('Start')

    start_stop_label = QLabel(parent)
    start_stop_label.setGeometry(QRect(95, 530, 50, 21))
    start_stop_label.setFont(font_label)
    start_stop_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
    start_stop_label.setObjectName("start_stop_label")
    start_stop_label.setText('INSERT')
    start_stop_label.setStyleSheet("background: none;")

    start_stop_button.clicked.connect(lambda: functions.start_stop(start_stop_button, ui_elements))

    return start_stop_button
