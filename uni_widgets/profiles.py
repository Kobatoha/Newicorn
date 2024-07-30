from PyQt6.QtWidgets import QPushButton, QLabel, QFrame
from PyQt6.QtGui import QPixmap, QFont
from PyQt6.QtCore import QRect, QSize, Qt
from functions import functions


def create_profile(parent):
    font_title_icons = QFont()
    font_title_icons.setBold(True)
    font_title_icons.setWeight(630)

    font_button = QFont()
    font_button.setPointSize(8)
    font_button.setBold(True)
    font_button.setWeight(75)

    profiles_title = QLabel(parent)
    profiles_title.setGeometry(QRect(170, 390, 111, 16))
    profiles_title.setObjectName("profiles_title")
    profiles_title.setFont(font_title_icons)
    profiles_title.setText('Profiles')
    profiles_title.setStyleSheet("background: none;")

    profile1_button = QPushButton(parent)
    profile1_button.setGeometry(QRect(170, 420, 111, 21))
    profile1_button.setStyleSheet("background-color: rgb(255, 239, 220);")
    profile1_button.setObjectName("pushButton_profile1")
    profile1_button.setFont(font_button)
    profile1_button.setText('profile 1')
    profile1_button.clicked.connect(functions.profile1)

    profile2_button = QPushButton(parent)
    profile2_button.setGeometry(QRect(170, 450, 111, 21))
    profile2_button.setStyleSheet("background-color: rgb(255, 239, 220);")
    profile2_button.setObjectName("profile2_button")
    profile2_button.setFont(font_button)
    profile2_button.setText('profile 2')
    profile2_button.clicked.connect(functions.profile2)

    profile3_button = QPushButton(parent)
    profile3_button.setGeometry(QRect(170, 480, 111, 21))
    profile3_button.setStyleSheet("background-color: rgb(255, 239, 220);")
    profile3_button.setObjectName("pushButton_profile3")
    profile3_button.setFont(font_button)
    profile3_button.setText('profile 3')
    profile3_button.clicked.connect(functions.profile3)

    lines_profile = QFrame(parent)
    lines_profile.setGeometry(QRect(220, 390, 61, 20))
    lines_profile.setFrameShape(QFrame.Shape.HLine)
    lines_profile.setFrameShadow(QFrame.Shadow.Sunken)
    lines_profile.setObjectName("line_profiles")
    lines_profile.setStyleSheet("background: none;")
