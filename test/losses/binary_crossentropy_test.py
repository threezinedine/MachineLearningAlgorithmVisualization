from app.model.losses import BinaryCrossentropy
import unittest
import numpy as np


class BinaryCrossentropyTest(unittest.TestCase):
    def test_call(self):
        a = 0.2
        a_t = 0

        b = 0.8
        b_t = 1

        loss_func = BinaryCrossentropy()

        # call 
        self.assertEqual(loss_func.call(np.array([[a_t], [b_t]]), np.array([[a], [b]])), - (np.log(1 - a) + np.log(b))/2)


    def test_grad(self):
        a = 0.2
        a_t = 0

        b = 0.8
        b_t = 1

        loss_func = BinaryCrossentropy()

        # call 
        self.assertEqual(loss_func.grad(np.array([[a_t], [b_t]]), np.array([[a], [b]])).shape, (2, 1))
