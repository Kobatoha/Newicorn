from PyQt6.QtWidgets import QLineEdit, QCheckBox
from PyQt6.QtGui import QFont
from PyQt6.QtCore import QRect
# from pynput.keyboard import Controller
from functions import functions, state, geometry


def create_keyboard(parent):
    font_check_box = QFont()
    font_check_box.setBold(True)
    font_check_box.setWeight(75)

    # keyboard = Controller()

    key_with_toggle = {
        'f1': [functions.toggle_f1, state.pressed_f1, geometry.place_1],
        'f2': [functions.toggle_f2, state.pressed_f2, geometry.place_2],
        'f3': [functions.toggle_f3, state.pressed_f3, geometry.place_3],
        'f4': [functions.toggle_f4, state.pressed_f4, geometry.place_4],
        'f5': [functions.toggle_f5, state.pressed_f5, geometry.place_5],
        'q': [functions.toggle_q, state.pressed_q, geometry.place_6],
        'w': [functions.toggle_w, state.pressed_w, geometry.place_7],
        'e': [functions.toggle_e, state.pressed_e, geometry.place_8],
        'r': [functions.toggle_r, state.pressed_r, geometry.place_9],
        't': [functions.toggle_t, state.pressed_t, geometry.place_10],
        '1': [functions.toggle_1, state.pressed_1, geometry.place_11],
        '2': [functions.toggle_2, state.pressed_2, geometry.place_12],
        '3': [functions.toggle_3, state.pressed_3, geometry.place_13],
        '4': [functions.toggle_4, state.pressed_4, geometry.place_14],
        '5': [functions.toggle_5, state.pressed_5, geometry.place_15],
        '6': [functions.toggle_6, state.pressed_6, geometry.place_16],
        '7': [functions.toggle_7, state.pressed_7, geometry.place_17],
        '8': [functions.toggle_8, state.pressed_8, geometry.place_18],
        '9': [functions.toggle_9, state.pressed_9, geometry.place_19],
        '`': [functions.toggle_tilda, state.pressed_tilda, geometry.place_20]
    }

    default_keys = ['f1', 'f2', 'f3', 'f4', 'f5',
                    'q', 'w', 'e', 'r', 't',
                    '1', '2', '3', '4', '5',
                    '6', '7', '8', '9', '`']

    for i in default_keys:
        x = key_with_toggle[i][2][0]
        y = key_with_toggle[i][2][1]
        line_edit = QLineEdit(parent)
        line_edit.setGeometry(QRect(x[0], x[1], x[2], x[3]))
        line_edit.setObjectName(f"{i}_line_edit")

        check_box = QCheckBox(parent)
        check_box.setGeometry(QRect(y[0], y[1], y[2], y[3]))
        check_box.setText(f"{i.upper()}")
        check_box.setFont(font_check_box)
        check_box.setObjectName(f"{i}_check_box")
        check_box.setStyleSheet("background: none;")
        check_box.stateChanged.connect(key_with_toggle[i][0])

        key_with_toggle[i][1] = False
