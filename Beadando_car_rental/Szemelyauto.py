from Auto import Car

class Szemelyauto(Car):

    def __init__(self, number_plate, model, price):
        super().__init__(number_plate, model, price)

    @property
    def number_plate(self):
        return self._number_plate

    @property
    def model(self):
        return self._model

    @property
    def price(self):
        return self._price

    @property
    def is_rented(self):
        return self._is_rented

    def rent_car(self):
        if not self._is_rented:
            self._is_rented = True
            print(f"Foglalás sikeres, Ára: {self._price}")
        else:
            print("Hiba. Az autó már ki van kölcsönözve.")

    def unrent_car(self):
        if self._is_rented:
            self._is_rented = False
            print(f"Foglalás sikeresen lemondva, Rendszám: {self._number_plate}")
        else:
            print("Hiba. Az autó nincs kikölcsönözve")