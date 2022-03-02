import unittest
import numpy as np
from app.model.activations import Sigmoid


class SigmoidTest(unittest.TestCase):
    def sigmoi_func(self, x):
        return 1/(1 + np.exp(-x))

    def test_call(self):
        sigmoid = Sigmoid()
        # test with a number
        self.assertAlmostEqual(sigmoid.call(0), np.array([[0.5]]))

        a = 0.2
        b = 0.1 
        result = np.array([[self.sigmoi_func(a)], [self.sigmoi_func(b)]])

        # test with a numpy array 
        self.assertAlmostEqual(sigmoid.call(np.array([[a], [b]])).all(), result.all())
