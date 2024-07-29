from PyQt6.QtWidgets import QPushButton, QLabel, QLineEdit
from PyQt6.QtGui import QIcon, QFont
from PyQt6.QtCore import QRect, QSize, Qt
from functions import functions


def create_lock_window(parent):
    font_button = QFont()
    font_button.setPointSize(8)
    font_button.setBold(False)
    font_button.setWeight(50)

    lock_window_button = QPushButton(parent)
    lock_window_button.setGeometry(QRect(30, 490, 41, 41))
    lock_window_button.setStyleSheet("background-color: rgb(255, 239, 220);")
    lock_window_button.setFont(font_button)
    lock_window_button.setObjectName("pushButton_located")
    lock_window_button.setIcon(QIcon('images/target_off.png'))
    lock_window_button.setIconSize(QSize(40, 40))
    lock_window_button.clicked.connect(functions.lock_window)

    msg_box_active = False

    font_label = QFont()
    font_label.setPointSize(7)
    font_label.setItalic(False)
    font_label.setUnderline(False)
    font_label.setStrikeOut(False)
    font_label.setKerning(True)

    hwnd_label = QLabel(parent)
    hwnd_label.setGeometry(QRect(25, 530, 50, 21))

    hwnd_label.setFont(font_label)
    hwnd_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
    hwnd_label.setObjectName("hwnd_label")
    hwnd_label.setText("F11")
    hwnd_label.setStyleSheet("background: none;")

    hwnd_line_edit = QLineEdit(parent)
    hwnd_line_edit.setGeometry(QRect(40, 460, 90, 20))
    hwnd_line_edit.setObjectName("hwnd_line_edit")
    hwnd_line_edit.setStyleSheet("background-color: rgb(239, 239, 239);")
    hwnd_line_edit.setText('hwnd')
    hwnd_line_edit.setAlignment(Qt.AlignmentFlag.AlignCenter | Qt.AlignmentFlag.AlignHCenter)
