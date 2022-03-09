from abc import ABC, abstractmethod


class IModel(ABC):
    @abstractmethod
    def train_per_epoch(self, data):
        pass

    @abstractmethod
    def predict(self, data):
        pass

    @abstractmethod
    def get_lines(self):
        pass
