from abc import ABC, abstractmethod

class Car(ABC):
    def __init__(self, number_plate, model, price):
        self._number_plate = number_plate
        self._model = model
        self._price = price
        self._is_rented = False

    @abstractmethod
    def rent_car(self):
        pass

    @abstractmethod
    def unrent_car(self):
        pass
