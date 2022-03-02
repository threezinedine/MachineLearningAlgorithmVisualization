from .i_activation import IActivation
import numpy as np


class Sigmoid(IActivation):
    """
        Sigmoid function class and its gradient.
    """

    def __re_format(self, result):
        # convert result to the shape (n, 1)
        if not isinstance(result, np.ndarray):
            if isinstance(result, int) or isinstance(result, float):
                return np.array([[result]])
            else:
                raise TypeError("The input_vect type is not correct.")
        else:
            if len(result.shape) == 1:
                return result.reshape(-1, 1)
            elif len(result.shape) == 2:
                if result.shape[1] != 1:
                    raise ValueError(f"input_vect has an expected shape is (n, 1), but found {result.shape}")
                return result
            else:
                raise ValueError("input_vect shape must be less than 2.")


    def call(self, input_vect):
        """
            Calculate the sigmoid function result.

            Parameters
            ----------
                input_vect: np.ndarray
                    The input of the sigmoid function

            Return
            ------
                result: np.ndarray of shape (n, 1)
                    The output of the sigmoid function that has the format of shape (n, 1)
        """
        # calculate the result by sigmoid formula
        result = 1/(1 + np.exp(-input_vect))
        return self.__re_format(result)
    
    def grad(self, input_vect):
        """
            Calculate the grad of sigmoid funciton with particular input.

            Parameters
            ----------
                input_vect: np.ndarray
                    The input of the sigmoid function

            Return
            ------
                result: np.ndarray of shape (n, 1)
                    The gradient of the sigmoid function that has the format of shape (n, 1)
        """
        result = self.call(input_vect)
        return result * (1 - result)
