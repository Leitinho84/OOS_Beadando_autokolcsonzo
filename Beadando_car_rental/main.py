from Autokolcsonzo import Autokolcsonzo
from Szemelyauto import Szemelyauto
from Teherauto import Teherauto

class RentalSystem:

    def __init__(self):
        self._autokolcsonzo = Autokolcsonzo("Eevisz")
        self._init_data()

    def _init_data(self):
        self._autokolcsonzo.cars = Szemelyauto("AAA-000", "Crossland", 10000)
        self._autokolcsonzo.cars = Szemelyauto("BAA-001", "Q3", 20000)
        self._autokolcsonzo.cars = Teherauto("TBA-011", "Transit", 17000)

    def user_interaction(self):
        while True:
            print("1. Elérhető autók listázása")
            print("2. Autó kölcsönzése")
            print("3. Kölcsönzés visszamondása")
            print("4. Kilépés")

            menu = input("Válassz a lehetőségek közül: ")

            if menu == "1":
                self._autokolcsonzo.cars
            elif menu == "2":
                number_plate = input("Add meg a rendszámot!")
                self._autokolcsonzo.rent_car_by_number_plate(number_plate)
            elif menu == "3":
                number_plate = input("Add meg a rendszámot!")
                self._autokolcsonzo.un_rent_car_by_number_plate(number_plate)
            elif menu == "4":
                break

rental_system = RentalSystem()
rental_system.user_interaction()
