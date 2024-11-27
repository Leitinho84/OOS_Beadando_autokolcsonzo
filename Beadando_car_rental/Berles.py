from abc import ABC

class Rental:
    def __init__(self, rented_number_plate, date):
        self._rented_number_plate = rented_number_plate
        self._date = date

    @property
    def rented_number_plate(self):
        return self._rented_number_plate

    @property
    def date(self):
        return self._date