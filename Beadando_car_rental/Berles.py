from abc import ABC
from Auto import Auto

class Berles:
    def __init__(self, number_plate, date, price):
        self.number_plate = number_plate
        self.date = date
        self.price = price

    def __str__(self):
        return f"Rendszám: {self.number_plate}, Dátum: {self.date}, Ár: {self.price} Ft"
