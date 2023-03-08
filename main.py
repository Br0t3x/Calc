from PySide6.QtWidgets import QApplication
from Application import Application
import sys

if __name__ == '__main__':
    app = QApplication(sys.argv)
    application = Application()
    sys.exit(app.exec())
