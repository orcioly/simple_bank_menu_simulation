from abc import ABC, abstractmethod

class Transaction(ABC):
    @property
    @abstractmethod
    def value(self):
        pass

    @classmethod
    @abstractmethod
    def register(cls, account):
        pass
