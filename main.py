import sys
from PySide6.QtWidgets import QApplication
from logic import mainWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    screen = mainWindow()
    screen.show()
    sys.exit(app.exec())