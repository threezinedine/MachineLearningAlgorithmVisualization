from .i_drawable import IDrawable
from .label import Label


class Point(IDrawable):
    """
        The class that stores data point and draw it on the Graph interface by matplotlib.
        
        Parameter
        ---------
            coor: tuple(float, float)
                The coordinate of the data point, with the first element stands for x, the second element stands for y.
    """
    def __init__(self, coor, label):
        self.__coor = coor
        self.__label = label

    @property
    def coor(self):
        return self.__coor

    @coor.setter
    def coor(self, new_coor):
        if len(new_coor) != 2:
            raise ValueError("The coor must be array, tuple and has 2 elements.")
        self.__coor = new_coor

    @property
    def label(self):
        return self.__label

    @label.setter
    def color(self, new_label):
        if isinstance(new_label, Label):
            self.__label = new_label
        else:
            raise ValueError("The label argument must be Label class.")

    def draw(self, graph):
        """
            Draw data point on a Matplotlib backends graph.
            
            Parameter
            ---------
                graph: FigureCanvasQTAgg object
                    The graph in which this point is painted. 
        """

        try:
            graph.axes.scatter(self.coor[0], self.coor[1], c=self.label.color)
            graph.draw()
        except Exception as e:
            print(e)
