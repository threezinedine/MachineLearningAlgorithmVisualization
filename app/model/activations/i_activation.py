from abc import ABC, abstractmethod


class IActivation(ABC):
    @abstractmethod
    def call(self, input_vect):
        pass 

    @abstractmethod
    def grad(self, input_vect):
        pass
