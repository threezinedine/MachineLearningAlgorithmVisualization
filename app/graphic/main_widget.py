from PyQt5.QtWidgets import QWidget, QFrame, QVBoxLayout, QRadioButton, QLineEdit, QPushButton
from PyQt5.QtCore import QTimer
from ..graph import Graph
from ..label import Label
from ..type_color import Color
from PyQt5 import uic
from threading import Thread


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
        self.setGeometry(100, 100, 1000, 900)

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
        self.training_mode_button.clicked.connect(self.training_mode_thread)

        self.clear_button = self.findChild(QPushButton, 'clear_button')
        self.clear_button.clicked.connect(self.clear_data)

    def clear_data(self):
        self.controller.data
        self.graph.axes.clear()
        self.graph.update_scale(self.graph.x_scale, self.graph.y_scale)
        self.graph.draw()
        self.controller.data.reset()
        self.controller.history.reset()

    def _check_label(self):
        colors = [Color.RED, Color.BLUE, Color.YELLOW, Color.GREEN]
        for index, label in enumerate(self.labels):
            if label.isChecked():
                self.graph.label = Label(index, colors[index])
                break

    def training_mode_thread(self):
        thread = Thread(target=self._clicked_training_mode)
        thread.start()

    def _clicked_training_mode(self):
        params = self.get_params()
        self.controller.update_params(params)
        self.controller.training_mode(params['iteration'], self.graph)

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

        learning_speed_line = self.findChild(QLineEdit, 'learning_speed_line')
        try:
            params['learning_speed'] = float(self.learning_speed_line.text())
        except:
            params['learning_speed'] = 0

        num_steps_line = self.findChild(QLineEdit, 'num_steps_line')
        try:
            params['num_steps'] = int(self.num_steps_line.text())
        except:
            params['num_steps'] = 0


        return params
