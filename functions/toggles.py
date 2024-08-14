import time
from PyQt6.QtCore import Qt, QTimer
from functions import configuration, state
import threading
import win32con
import win32gui
import win32api


def toggle_key(key, check_box, line_edit):
    state_box = check_box.checkState()
    print(key, state_box, line_edit.text())

    if state_box == Qt.CheckState.Checked:
        if state.start:
            print('State start:', state.start)
            state.state_press[key] = True
            # press_key(key, line_edit)
            threading.Thread(target=press_key(line_edit=line_edit, key=key)).start()
    else:
        state.state_press[key] = False
    print(f'press toggle_{key}')


def press_key(line_edit=None, key=None):
    if key and line_edit:
        while state.state_press[key]:
            interval = int(line_edit.text())
            print(key, configuration.down, configuration.keys_num[key], 0)
            time.sleep(interval / 1000)
            print(key, configuration.up, configuration.keys_num[key], 0)
            QTimer.singleShot(interval, press_key)


def toggle_res(state):
    print('press toggle_res')
