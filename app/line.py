from .i_drawable import IDrawable
import numpy as np


NUM_POINTS = 100


class Line(IDrawable):
    """
        The line represents parameter of the IModel
        
        Parameter
        ---------
            function: a pointer of a function(x)
                The function that represents this line
    """
    def __init__(self, func):
        self.__func = func

    def draw(self, graph):
        """
            Draws this line on the graph

            Parameter
            ---------
                graph: FigureCanvasQTAgg object 
                    The graph in which this line is drawn
        """

        try: 
            x_range = np.linspace(*graph.x_scale, NUM_POINTS)
            y_range = self.__func(x_range)  

            indexes = []
            y_min, y_max = graph.y_scale
            for index, y in enumerate(y_range):
                if not y_min <= y <= y_max:
                    continue
                indexes.append(index)
            graph.axes.plot(x_range[indexes], y_range[indexes])
            graph.draw()
        except Exception as error:
            print(error)
