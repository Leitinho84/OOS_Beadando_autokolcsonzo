from Berles import Berles

class Autokolcsonzo:
    def __init__(self, name):
        self._name = name
        self._cars = []
        self._rentals = []

    @property
    def name(self):
        return self._name

    @property
    def cars(self):
        for car in self._cars:
            print(f"Rendszám: {car.number_plate}, Típus: {car.model}, Ár: {car.price} Ft")

    @cars.setter
    def cars(self, new_car):
        self._cars.append(new_car)

    @property
    def rentals(self):
        for rental in self._rentals:
            print(rental)

    @rentals.setter
    def rentals(self, new_rental):
        self._rentals.append(new_rental)

    def rent_car_by_number_plate(self, number_plate, date):
        for car in self._cars:
            if car.number_plate == number_plate:
                if not any(r.number_plate == number_plate and r.date == date for r in self._rentals):
                    rental = Berles(number_plate, date, car.price)
                    self._rentals.append(rental)
                    print(f"Sikeres bérlés: {rental}")
                    return
                else:
                    print(f"Hiba: Az autó ({number_plate}) már foglalt {date} napra.")
                    return
        print(f"Hiba: Az autó ({number_plate}) nem található.")

    def un_rent_car_by_number_plate(self, number_plate, date):
        for rental in self._rentals:
            if rental.number_plate == number_plate and rental.date == date:
                self._rentals.remove(rental)
                print(f"Bérlés visszamondva: {rental}")
                return
        print(f"Hiba: Nincs ilyen bérlés ({number_plate}, {date}).")