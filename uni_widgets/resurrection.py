from PyQt6.QtWidgets import QCheckBox, QLabel
from PyQt6.QtGui import QFont
from PyQt6.QtCore import QRect, Qt
from functions import toggles


def create_resurrection(parent):
    font_check_box = QFont()
    font_check_box.setBold(True)
    font_check_box.setWeight(75)

    check_box_res = QCheckBox(parent)
    check_box_res.setGeometry(QRect(250, 320, 40, 20))
    check_box_res.setFont(font_check_box)
    check_box_res.setObjectName("check_box_res")
    check_box_res.setText("res")
    check_box_res.setStyleSheet("background: none;")
    check_box_res.stateChanged.connect(toggles.toggle_res)

    pressed_res = False
