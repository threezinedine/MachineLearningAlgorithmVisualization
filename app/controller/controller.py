from ..data import Data
from ..line import Line
from ..model.data import ClassificationDataExtraction


class Controller:
    def __init__(self, data, model):
        self.__data = data
        self.__lines = []
        self.__model = model

    @property
    def data(self):
        return self.__data

#    @data.setter
#    def data(self, new_data):
#        self.__data = new_data

    @property
    def lines(self):
        return self.__lines

    @lines.setter
    def lines(self, new_lines):
        self.__lines = new_lines

    @property
    def model(self):
        return self.__model

    def update_params(self, new_param):
        new_points = new_param['data point']
        for point in new_points:
            self.data.add_point(point)

        self.model.learning_rate = new_param['learning_rate']

    def training_mode(self, iteration):
        data = ClassificationDataExtraction.sparse(self.data)
        for index in range(iteration):
            self.model.train_per_epoch(data)

        print(self.model.weights)

    def draw(self, graph):
        for point in self.data.points:
            point.draw(graph)

        for line in self.lines:
            line.draw(graph)
