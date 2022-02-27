from .point import Point


class Data:
    """
        Class stores all data points for training process.

        Parameters
        ----------
            num_classes: int
                The number of classes that the problem has.

            points: Point[]
                The points of the problem.
    """
    def __init__(self, num_classes):
        self.__points = []
        self.__num_classes = num_classes

    @property
    def num_classes(self):
        return self.__num_classes

    @num_classes.setter
    def num_classes(self, new_num_classes):
        if (isinstance(new_num_classes, int)):
            self.__num_classes = new_num_classes
        else:
            raise TypeError("num_classes must be a integer.")

    @property
    def points(self):
        return self.__points

    def add_point(self, new_point):
        if (isinstance(new_point, Point)):
            self.__points.append(new_point)
        else:
            raise TypeError("add_point must receive Point object.")
