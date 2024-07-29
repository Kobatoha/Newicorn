import sys
from PyQt6.QtWidgets import QApplication
from ui import Unicorn


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Unicorn()
    window.show()
    sys.exit(app.exec())
