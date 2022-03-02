from abc import ABC, abstractmethod


class ILoss(ABC):
    @abstractmethod
    def call(self, y_true, y_pred):
        pass 

    @abstractmethod
    def grad(self, y_true, y_pred):
        pass 
