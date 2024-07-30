from PyQt6.QtCore import Qt
from functions import configuration
import threading


def toggle_f1(button, state):
    if state == Qt.CheckState.Checked:
        if button.text() == 'Stop':
            configuration.key_with_toggle['f1'][1] = True
            # self.press_1()
            threading.Thread(target=press_f1).start()
    else:
        configuration.key_with_toggle['f1'][1] = False
    print('press toggle_f1')


def toggle_f2(state):
    print('press toggle_f2')


def toggle_f3(state):
    print('press toggle_f3')


def toggle_f4(state):
    print('press toggle_f4')


def toggle_f5(state):
    print('press toggle_f5')


def toggle_f6(state):
    print('press toggle_f6')


def toggle_f7(state):
    print('press toggle_f7')


def toggle_f8(state):
    if state == 'Checked':
        print('Checked, click')
    else:
        print('Unchecked toggle_f8')


def toggle_f9(state):
    print('press toggle_f9')


def toggle_f10(state):
    print('press toggle_f10')


def toggle_q(state):
    print('press toggle_q')


def toggle_w(state):
    print('press toggle_w')


def toggle_e(state):
    print('press toggle_e')


def toggle_r(state):
    print('press toggle_r')


def toggle_t(state):
    print('press toggle_t')


def toggle_y(state):
    print('press toggle_y')


def toggle_u(state):
    print('press toggle_u')


def toggle_i(state):
    print('press toggle_i')


def toggle_o(state):
    print('press toggle_o')


def toggle_p(state):
    print('press toggle_p')


def toggle_1(state):
    print('press toggle_1')


def toggle_2(state):
    print('press toggle_2')


def toggle_3(state):
    print('press toggle_3')


def toggle_4(state):
    print('press toggle_4')


def toggle_5(state):
    print('press toggle_5')


def toggle_6(state):
    print('press toggle_6')


def toggle_7(state):
    print('press toggle_7')


def toggle_8(state):
    print('press toggle_8')


def toggle_9(state):
    print('press toggle_9')


def toggle_tilda(state):
    print('press toggle_tilda')


def toggle_res(state):
    print('press toggle_res')