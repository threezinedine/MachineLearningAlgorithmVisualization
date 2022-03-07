import sys
from PyQt5.QtWidgets import QApplication
from app.graphic import MyWidget


def main():
    app = QApplication(sys.argv)
    win = MyWidget()
    win.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
