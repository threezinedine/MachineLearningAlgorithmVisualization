from time import time, sleep


class History:
    def __init__(self):
        self.__lines = []

    @property
    def lines(self):
        return self.__lines

    def __len__(self):
        return len(self.__lines)

    def add_step_lines(self, step_lines):
        self.__lines.append(step_lines)

    def draw(self, graph, num_steps, speed):
        len_history = len(self) - 1
        for i in range(num_steps):
            index = len_history - i * (len_history // num_steps)
            for line in self.lines[index]:
                line.draw(graph)
            sleep(speed)
            if i != num_steps - 1:
                for line in graph.axes.lines:
                    line.remove()

    def reset(self):
        self.__lines = []
