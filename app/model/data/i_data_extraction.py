from abc import ABC, abstractstaticmethod


class IDataExtraction(ABC):
    @abstractstaticmethod
    def sparse(data):
        pass
