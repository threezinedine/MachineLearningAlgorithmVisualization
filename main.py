import sys
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QApplication 
from PyQt5.QtCore import QTimer
from app.graph import Graph


class MyWidget(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        
        layout = QVBoxLayout()
        self.graph = Graph(3, 4) 
        layout.addWidget(self.graph)
        self.setLayout(layout)

        self._data = 0.5

#        myTime = QTimer(self)
#        myTime.timeout.connect(self._update_graph)
#        myTime.start(100)

#    def _update_graph(self):
#        print("Test Update")
#        self.graph.axes.scatter(self._data, self._data)
#        self._data += 0.1
#        self.graph.draw()


def main():
    app = QApplication(sys.argv)
    win = MyWidget()
    win.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
