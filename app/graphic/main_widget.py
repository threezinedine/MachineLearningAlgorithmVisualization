from PyQt5.QtWidgets import QWidget, QFrame, QVBoxLayout, QRadioButton, QLineEdit, QPushButton
from PyQt5.QtCore import QTimer
from ..graph import Graph
from ..label import Label
from ..type_color import Color
from PyQt5 import uic


class MyWidget(QWidget):
    def __init__(self, controller):
        QWidget.__init__(self)
        self.init()
        
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update)
        self.timer.start(100)

        self.controller = controller

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

        self.training_mode_button = self.findChild(QPushButton, 'training_mode')
        self.training_mode_button.clicked.connect(self._clicked_training_mode)

    def _check_label(self):
        colors = [Color.RED, Color.BLUE, Color.YELLOW, Color.GREEN]
        for index, label in enumerate(self.labels):
            if label.isChecked():
                self.graph.label = Label(index, colors[index])
                break

    def _clicked_training_mode(self):
        self.graph.axes.clear()
        self.controller.draw(self.graph)
        params = self.get_params()
        self.controller.update_params(params)
        self.controller.training_mode(params['iteration'])

    def update(self):
        self._check_label() 
        self.controller.update_params(self.get_params())

    def get_params(self):
        params = {"data point": self.graph.stack_points}
        
        # learning rate param
        learning_rate_line = self.findChild(QLineEdit, 'learning_rate_line')
        try:
            params['learning_rate'] = float(learning_rate_line.text())
        except:
            params['learning_rate'] = 0.0

        # iteration param
        iteration_line = self.findChild(QLineEdit, 'iteration_line')
        try: 
            params['iteration'] = int(iteration_line.text())
        except:
            params['iteration'] = 0

        return params
