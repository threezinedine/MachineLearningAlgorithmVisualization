from abc import ABC, abstractmethod
    def __init__(self):{


class IActivation(ABC):
    @abstractmethod
    def call(self, input_vect):
        pass 

    @abstractmethod
    def grad(self, input_vect):
        pass
