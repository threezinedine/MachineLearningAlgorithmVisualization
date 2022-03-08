from PyQt5.QtCore import Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas 
from .point import Point
from .type_color import Color
from matplotlib.figure import Figure
from .label import Label
from .line import Line


class Graph(FigureCanvas):
    def __init__(self, width=5, height=4):
        fig = Figure(figsize=(width, height))
        FigureCanvas.__init__(self, fig)
        self.axes = fig.subplots(1)
        self.mpl_connect("button_press_event", self.click)
        self.x_scale = (-5, 5)
        self.y_scale = (-5, 5)
        self.axes.set_xlim(self.x_scale)
        self.axes.set_ylim(self.y_scale)

        self.label = None
        self.__stack_points = []

    def update_scale(self, x_scale, y_scale):
        self.x_scale = x_scale
        self.y_scale = y_scale
        self.axes.set_xlim(self.x_scale)
        self.axes.set_ylim(self.y_scale)

    def _test_draw(self):
        self.axes.plot([0, 0.5], [0.5, 1])
        self.draw()

    @property
    def stack_points(self):
        points = self.__stack_points.copy()
        self.__stack_points = []
        return points

    def click(self, event):
        if self.label is not None:
            point = Point((event.xdata, event.ydata), self.label)
            point.draw(self)
            self.__stack_points.append(point)
