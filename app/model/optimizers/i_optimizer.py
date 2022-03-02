from abc import ABC, abstractmethod


class IOptimizer(ABC):
    @abstractmethod
    def update(self, variables, gradients):
        pass 
