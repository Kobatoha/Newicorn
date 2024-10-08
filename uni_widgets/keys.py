from PyQt6.QtWidgets import QLineEdit, QCheckBox
from PyQt6.QtGui import QFont
from PyQt6.QtCore import QRect
# from pynput.keyboard import Controller
from functions import configuration, geometry, toggles, state


def create_keys(parent):
    font_check_box = QFont()
    font_check_box.setBold(True)
    font_check_box.setWeight(75)

    # keyboard = Controller()

    # key_with_toggle = configuration.key_with_toggle

    default_keys = ['f1', 'f2', 'f3', 'f4', 'f5',
                    'q', 'w', 'e', 'r', 't',
                    '1', '2', '3', '4', '5',
                    '6', '7', '8', '9', '`']

    check_boxes = []
    line_edits = []

    place = 0

    for key in default_keys:
        x = geometry.line_edits_and_check_boxs[place][0]
        y = geometry.line_edits_and_check_boxs[place][1]

        line_edit = QLineEdit(parent)
        line_edit.setGeometry(QRect(x[0], x[1], x[2], x[3]))
        line_edit.setObjectName(f"{key}_line_edit")

        check_box = QCheckBox(parent)
        check_box.setGeometry(QRect(y[0], y[1], y[2], y[3]))
        check_box.setText(f"{key.upper()}")
        check_box.setFont(font_check_box)
        check_box.setObjectName(f"{key}_check_box")
        check_box.setStyleSheet("background: none;")

        # check_box.stateChanged.connect(lambda: key_with_toggle[i][0]())
        # key_with_toggle[key][1] = False

        def create_state_changed_handler(key, check_box, line_edit):
            return lambda: toggles.toggle_key(key, check_box, line_edit)

        check_box.stateChanged.connect(create_state_changed_handler(key, check_box, line_edit))

        state.state_press[key] = False

        place += 1

        check_boxes.append(check_box)
        line_edits.append(line_edit)

    return check_boxes, line_edits
