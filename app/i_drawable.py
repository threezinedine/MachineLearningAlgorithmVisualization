from abc import ABC, abstractmethod


class IDrawable(ABC):
    @abstractmethod
    def draw(self, graph):
        raise NotImplementedError("You must impliment draw method.")
