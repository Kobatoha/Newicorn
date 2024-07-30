from PyQt6.QtWidgets import QStatusBar, QLabel
from PyQt6.QtGui import QFont
from PyQt6.QtCore import QRect, Qt


def create_status_bar(parent):
    status_bar = QStatusBar(parent)
    status_bar.setObjectName("status_bar")
    status_bar.setFixedHeight(20)
    status_bar.setFixedWidth(300)
    status_bar.setStyleSheet("background: none;")
    status_bar.showMessage('')

    font_label = QFont()
    font_label.setPointSize(7)

    info_label = QLabel(parent)
    info_label.setGeometry(QRect(50, 550, 201, 16))
    info_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
    info_label.setFont(font_label)
    info_label.setObjectName("info_label")
    info_label.setStyleSheet("background: none;")

    return info_label
