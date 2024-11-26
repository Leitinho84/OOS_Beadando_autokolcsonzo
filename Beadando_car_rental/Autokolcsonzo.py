class Autokolcsonzo:
    def __init__(self, name):
        self._name = name
        self._cars = []

    @property
    def name(self):
        return self._name

    @property
    def cars(self):
        for car in self._cars:
            print(f" Rendszám: {car.number_plate}, Típus: {car.model}, Ár: {car.price}, Státusz: {car.is_rented}")

    @cars.setter
    def cars(self, new_car):
        self._cars.append(new_car)

    def rent_car_by_number_plate(self, number_plate):
        for car in self._cars:
            if car.number_plate == number_plate:
                car.rent_car()

    def un_rent_car_by_number_plate(self, number_plate):
        for car in self._cars:
            if car.number_plate == number_plate:
                car.unrent_car()