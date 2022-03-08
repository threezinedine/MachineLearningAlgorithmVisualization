from .i_model import IModel
import numpy as np


class LogisticRegression(IModel):
    """
        Linear regression model.

        Parameters
        ----------
            learning_rate: float 
                The learning rate that represent how fast the gradient updating.

            weights: np.ndarray
                The weights parameters of the model.
    """
    def __init__(self, activation_func, loss_func, learning_rate=0.01):
        self.__weights = None
        self.__learning_rate = learning_rate 
        self.__activation_func = activation_func
        self.__loss_func = loss_func

    @property
    def learning_rate(self):
        return self.__learning_rate

    @learning_rate.setter
    def learning_rate(self, new_learning_rate):
        self.__learning_rate = new_learning_rate

    @property
    def weights(self):
        return self.__weights

    def __random_weights(self, size=3, loc=0.0, scale=0.5):
        self.__weights = np.random.normal(loc=loc, scale=scale, size=(size, 1))

    def __add_dummy(self, X):
        ones = np.ones(shape=(X.shape[0], 1), dtype=np.float32)
        return np.concatenate([ones, X], axis=1)

    def train_per_epoch(self, data):
        """
            Update weights by an iteration.

            Parameters
            ----------
                data: np.ndarray 
                    The data that has 2 data training and their labels (the final column)
        """
        X, y = data[:, :-1], data[:, -1:] 
        if self.weights is None:
            self.__random_weights(size=X.shape[1] + 1)
        y_pred = self.predict(X)
        dummy_X = self.__add_dummy(X)
        grad = self.__loss_func.grad(y, y_pred) * self.__activation_func.grad(np.dot(dummy_X, self.__weights))
        self.__weights = self.__weights - self.__learning_rate * np.dot(dummy_X.T, grad)

    def predict(self, data):
        """
            Predict the results.

            Parameters
            ----------
                data: np.ndarray 
                    The data that has 2 data training and their labels (the final column)

            Return
            ------
                y_pred: np.ndarray
                    The labels of the input data
        """
        dummy_X = self.__add_dummy(data)
        try:
            return self.__activation_func.call(np.dot(dummy_X, self.__weights))
        except:
            self.__random_weights(dummy_X.shape[1])
            return self.__activation_func.call(np.dot(dummy_X, self.__weights))
