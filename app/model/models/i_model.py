from abc import ABC, abstractmethod


class IModel(ABC):
    @abstractmethod
    def train_per_epoch(self, data):
        pass

    @abstractmethod
    def predict(self, point):
        pass
