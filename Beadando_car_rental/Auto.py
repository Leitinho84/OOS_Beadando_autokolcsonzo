from abc import ABC, abstractmethod

class Auto(ABC):
    def __init__(self, number_plate, model, price):
        self._number_plate = number_plate
        self._model = model
        self._price = price

    @property
    @abstractmethod
    def number_plate(self):
        pass

    @property
    @abstractmethod
    def model(self):
        pass

    @property
    @abstractmethod
    def price(self):
        pass
