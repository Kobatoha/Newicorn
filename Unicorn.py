import sys
from PyQt6.QtWidgets import QApplication
from ui import Unicorn
import threading
import keyboard


def hotkey_listener(window):
    """Функция, обрабатывающая нажатие клавиши Insert."""
    while True:
        keyboard.wait('insert')
        window.toggle_start_stop()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Unicorn()

    listener_thread = threading.Thread(target=hotkey_listener, args=(window,))
    listener_thread.daemon = True
    listener_thread.start()

    window.show()
    sys.exit(app.exec())
