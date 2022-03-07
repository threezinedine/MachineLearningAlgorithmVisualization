from PyQt5.QtWidgets import QWidget, QFrame, QVBoxLayout, QRadioButton
from PyQt5.QtCore import QTimer
from ..graph import Graph
from ..label import Label
from ..type_color import Color
from PyQt5 import uic


class MyWidget(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.init()
        
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update)
        self.timer.start(100)

    def init(self):
        # load ui
        uic.loadUi('ui/main.ui', self)
        self.setGeometry(300, 300, 1000, 900)

        # create graph
        layout = QVBoxLayout()
        self.graph = Graph(3, 4) 
        layout.addWidget(self.graph)

        # set graph to frame
        graph_frame = self.findChild(QFrame, 'graph_frame')
        graph_frame.setLayout(layout)

        # get point data
        red_point = self.findChild(QRadioButton, 'red_point')
        blue_point = self.findChild(QRadioButton, 'blue_point')
        yellow_point = self.findChild(QRadioButton, 'yellow_point')
        green_point = self.findChild(QRadioButton, 'green_point')
        self.labels = [red_point, blue_point, yellow_point, green_point]

    def _check_label(self):
        colors = [Color.RED, Color.BLUE, Color.YELLOW, Color.GREEN]
        for index, label in enumerate(self.labels):
            if label.isChecked():
                self.graph.label = Label(index, colors[index])
                break

    def update(self):
        self._check_label() 
