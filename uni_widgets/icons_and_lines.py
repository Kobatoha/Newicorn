from PyQt6.QtWidgets import QFrame, QLabel
from PyQt6.QtGui import QPixmap, QFont
from PyQt6.QtCore import QRect, Qt


def create_icons_and_lines(parent):
    font_title_icons = QFont()
    font_title_icons.setBold(True)
    font_title_icons.setWeight(630)

    font_label = QFont()
    font_label.setPointSize(7)
    font_label.setUnderline(False)
    font_label.setStrikeOut(False)
    font_label.setKerning(True)

    icons_title = QLabel(parent)
    icons_title.setGeometry(QRect(10, 370, 41, 16))
    icons_title.setFont(font_title_icons)
    icons_title.setAlignment(Qt.AlignmentFlag.AlignCenter)
    icons_title.setObjectName("icons_title")
    icons_title.setText("Icons")
    icons_title.setStyleSheet("background: none;")

    line_icons_left = QFrame(parent)
    line_icons_left.setGeometry(QRect(50, 370, 101, 20))
    line_icons_left.setFrameShape(QFrame.Shape.HLine)
    line_icons_left.setFrameShadow(QFrame.Shadow.Sunken)
    line_icons_left.setObjectName("line_icons_left")
    line_icons_left.setStyleSheet("background: none;")

    line_icons_right = QFrame(parent)
    line_icons_right.setGeometry(QRect(170, 370, 111, 20))
    line_icons_right.setFrameShape(QFrame.Shape.HLine)
    line_icons_right.setFrameShadow(QFrame.Shadow.Sunken)
    line_icons_right.setObjectName("line_icons_right")
    line_icons_right.setStyleSheet("background: none;")

    hot_time_icon = QLabel(parent)
    hot_time_icon.setGeometry(QRect(20, 390, 31, 31))
    hot_time_icon.setPixmap(QPixmap("images/hot_time_off.png"))
    hot_time_icon.setScaledContents(True)
    hot_time_icon.setAlignment(Qt.AlignmentFlag.AlignCenter)
    hot_time_icon.setObjectName("label_hottime")
    hot_time_icon.setStyleSheet("background: none;")

    hot_time_title = QLabel(parent)
    hot_time_title.setGeometry(QRect(10, 420, 51, 16))
    hot_time_title.setFont(font_label)
    hot_time_title.setAlignment(Qt.AlignmentFlag.AlignCenter)
    hot_time_title.setObjectName("label_hottime")
    hot_time_title.setText("Hot Time")
    hot_time_title.setStyleSheet("background: none;")

    window_title = QLabel(parent)
    window_title.setGeometry(QRect(10, 440, 60, 20))
    window_title.setFont(font_title_icons)
    window_title.setAlignment(Qt.AlignmentFlag.AlignCenter)
    window_title.setObjectName("label_window")
    window_title.setText("Window id")
    window_title.setStyleSheet("background: none;")

    line_window = QFrame(parent)
    line_window.setGeometry(QRect(80, 440, 70, 20))
    line_window.setFrameShape(QFrame.Shape.HLine)
    line_window.setFrameShadow(QFrame.Shadow.Sunken)
    line_window.setObjectName("line_window")
    line_window.setStyleSheet("background: none;")
