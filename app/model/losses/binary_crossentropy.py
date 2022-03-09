from .i_loss import ILoss
import numpy as np


class BinaryCrossentropy(ILoss):
    """
        BinaryCrossentroy function class and its gradient.
    """
    def __check(self, param_string, param):
        if isinstance(param, np.ndarray):
            if len(param.shape) == 1:
                return param.reshape(-1, 1)
            elif len(param.shape) >= 3:
                raise ValueError(f"{param_string} shape must have less than 3 dimensions.")
            elif param.shape[1] != 1: 
                raise ValueError(f"{param_string} shape must have the shape (n, 1), but find {param.shape}")
        else:
            raise TypeError(f"{param_string} must be a numpy array.")

        return param

    def call(self, y_true, y_pred):
        """
            Calculate the Binary Crossentropy result.

            Parameters
            ----------
                y_true: ndarray of shape (n, 1) or (n, )
                    The true labels, each element must be 1 or 0.

                y_pred: ndarray of shape (n, 1) or (n, )
                    The predict probabilites, the value of each element must be in range [0, 1]

            Return
            ------
                result: float 
                    The result of the functions that be a scalar.
        """
        # handle y_true
        y_true = self.__check("y_true", y_true)

        # handle y_pred
        y_pred = self.__check("y_pred", y_pred)

        nums = y_true.shape[0]
        result = - 1 / nums * np.sum(y_true * np.log(y_pred) + (1 - y_true) * np.log(1 - y_pred))
        return result

    def grad(self, y_true, y_pred):
        """
            Calculate the Binary Crossentropy gradient.

            Parameters
            ----------
                y_true: ndarray of shape (n, 1) or (n, )
                    The true labels, each element must be 1 or 0.

                y_pred: ndarray of shape (n, 1) or (n, )
                    The predict probabilites, the value of each element must be in range [0, 1]

            Return
            ------
                result: ndarray of shape (n, 1) 
                    The result of the functions that has the shape (n, 1) where n is the number of y_true
        """
        # handle y_true
        y_true = self.__check("y_true", y_true)

        # handle y_pred
        y_pred = self.__check("y_pred", y_pred)

        for index in range(y_pred.shape[0]):
            if y_pred[index, 0] == 0 or y_pred[index, 0] == 1:
                y_pred[index, 0] == 0.5

        result = (y_pred - y_true)/(y_pred * (1 - y_pred))
        return result
