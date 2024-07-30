from PyQt6.QtWidgets import QLabel, QLineEdit, QCheckBox
from PyQt6.QtCore import Qt
from functions import configuration, state


def start_stop(button, ui_elements):
    info_label = ui_elements[0]
    check_boxes = ui_elements[1]
    if button.text() == 'Start':
        print('start')
        state.start = True
        button.setText('Stop')
        info_label.setText("Started clicker")
        for check_box in check_boxes:
            key = check_box.text().lower()
            box_state = check_box.checkState()
            if box_state == Qt.CheckState.Checked:
                state.state_press[key] = True

    else:
        print('stop')
        button.setText('Start')
        state.start = False
        info_label.setText('Stopped clicker')
        for check_box in check_boxes:
            key = check_box.text().lower()
            state.state_press[key] = False


def lock_window():
    print('press lock_window')


def save_settings():
    print('press save_settings')
    status_bar_message('save_settings')


def load_settings():
    print('press load_settings')


def status_bar_message(message):
    if message:
        return message
    return 'status_bar_message'


def profile1():
    print('press profile1')


def profile2():
    print('press profile2')


def profile3():
    print('press profile3')
