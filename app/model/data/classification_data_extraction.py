from .i_data_extraction import IDataExtraction
import numpy as np


class ClassificationDataExtraction(IDataExtraction):
    def sparse(data):
        X = []
        y = []
        for point in data.points:
            if point.coor != (None, None): 
                X.append(point.coor)
                y.append([point.label.label])

        return np.concatenate([np.array(X), np.array(y)], axis=1)
