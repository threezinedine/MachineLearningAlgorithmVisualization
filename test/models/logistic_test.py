from app.model.models import LogisticRegression
import unittest
from app.model.activations import Sigmoid
import numpy as np
from app.model.losses import BinaryCrossentropy



class LogisticTest(unittest.TestCase):
    def test_train(self):
        sigmoid = Sigmoid()
        loss_func = BinaryCrossentropy()
        model = LogisticRegression(activation_func=sigmoid, loss_func=loss_func)

        data = np.array([[0.2, 0.3, 1], [1, 1, 0]])

        print(model.weights)
        print(loss_func.call(model.predict(data[:, :-1]), data[:, -1:]))
        model.train_per_epoch(data)
        print(loss_func.call(model.predict(data[:, :-1]), data[:, -1:]))
        print(model.weights)


        
