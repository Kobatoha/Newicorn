from PyQt6.QtWidgets import QLineEdit, QCheckBox
from PyQt6.QtGui import QFont
from PyQt6.QtCore import QRect
# from pynput.keyboard import Controller
from functions import functions, state, geometry


def create_keys(parent):
    font_check_box = QFont()
    font_check_box.setBold(True)
    font_check_box.setWeight(75)

    # keyboard = Controller()

    key_with_toggle = {
        'f1': [functions.toggle_f1, state.pressed_f1],
        'f2': [functions.toggle_f2, state.pressed_f2],
        'f3': [functions.toggle_f3, state.pressed_f3],
        'f4': [functions.toggle_f4, state.pressed_f4],
        'f5': [functions.toggle_f5, state.pressed_f5],
        'q': [functions.toggle_q, state.pressed_q],
        'w': [functions.toggle_w, state.pressed_w],
        'e': [functions.toggle_e, state.pressed_e],
        'r': [functions.toggle_r, state.pressed_r],
        't': [functions.toggle_t, state.pressed_t],
        '1': [functions.toggle_1, state.pressed_1],
        '2': [functions.toggle_2, state.pressed_2],
        '3': [functions.toggle_3, state.pressed_3],
        '4': [functions.toggle_4, state.pressed_4],
        '5': [functions.toggle_5, state.pressed_5],
        '6': [functions.toggle_6, state.pressed_6],
        '7': [functions.toggle_7, state.pressed_7],
        '8': [functions.toggle_8, state.pressed_8],
        '9': [functions.toggle_9, state.pressed_9],
        '`': [functions.toggle_tilda, state.pressed_tilda]
    }

    default_keys = ['f1', 'f2', 'f3', 'f4', 'f5',
                    'q', 'w', 'e', 'r', 't',
                    '1', '2', '3', '4', '5',
                    '6', '7', '8', '9', '`']

    place = 0

    for i in default_keys:
        x = geometry.line_edits_and_check_boxs[place][0]
        y = geometry.line_edits_and_check_boxs[place][1]

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
        place += 1
