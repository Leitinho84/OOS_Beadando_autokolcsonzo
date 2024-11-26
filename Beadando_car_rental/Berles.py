from abc import ABC, abstractmethod

class Berles:
    def __init__(self, rented_number_plate, date):
        self._rented_number_plate = rented_number_plate
        self._date = date

    @abstractmethod
    def rent_car(self):
        pass

    @abstractmethod
    def unrent_car(self):
        pass