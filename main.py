from qt.QtClass import *
from PySide6.QtWidgets import QApplication
import sys


def main() -> None:
    app = QApplication(sys.argv)

    window = MyWidget()
    window.show()

    sys.exit(app.exec())

if __name__ == "__main__":
    main()
