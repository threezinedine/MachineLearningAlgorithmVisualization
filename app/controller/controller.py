from ..data import Data
from ..line import Line
from ..model.data import ClassificationDataExtraction
from threading import Thread
from ..history import History
from time import sleep, time


class Controller:
    def __init__(self, data, model):
        self.__data = data
        self.__history = History()
        self.__model = model
        self.__learning_speed = 0
        self.__num_steps = 0

    @property
    def data(self):
        return self.__data

#    @data.setter
#    def data(self, new_data):
#        self.__data = new_data

    @property
    def history(self):
        return self.__history

    @property
    def model(self):
        return self.__model

    def update_params(self, new_param):
        new_points = new_param['data point']
        for point in new_points:
            self.data.add_point(point)

        self.model.learning_rate = new_param['learning_rate']
        self.__learning_speed = new_param['learning_speed']
        self.__num_steps = new_param['num_steps']

    def training_mode(self, iteration, graph):
        data = ClassificationDataExtraction.sparse(self.data)
        for index in range(iteration):
            self.model.train_per_epoch(data)
            self.history.add_step_lines(self.model.get_lines()) 

        self.history.draw(graph, self.__num_steps, self.__learning_speed)

    def draw(self, graph):
        graph.axes.clear() 
        graph.update_scale(graph.x_scale, graph.y_scale)
        for point in self.data.points:
            point.draw(graph)
