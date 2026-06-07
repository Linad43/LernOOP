from abc import ABC, abstractmethod


class BaseProduct(ABC):
    @property
    @abstractmethod
    def price(self) -> float:
        pass
