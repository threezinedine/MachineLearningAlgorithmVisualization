import sys
from PyQt5.QtWidgets import QApplication
from app.graphic import MyWidget
from app.controller import Controller
from app import Data, Line
from app.model.models import LogisticRegression
from app.model.activations import Sigmoid
from app.model.losses import BinaryCrossentropy


def main():
    model = LogisticRegression(Sigmoid(), BinaryCrossentropy()) 
    data = Data(2)
    controller = Controller(data, model)
    app = QApplication(sys.argv)
    win = MyWidget(controller)
    win.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
