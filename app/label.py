from .type_color import Color


class Label:
    """
        Class stores label of the problem.

        Parameter
        ---------
            label: int 
                The label of the class

            color: Color 
                The color in the graph of the label, must be Color Type
    """
    def __init__(self, label, color):
        self.__label = label 
        self.__color = color

    @property
    def label(self):
        return self.__label

    @property
    def color(self):
        return self.__color.value
