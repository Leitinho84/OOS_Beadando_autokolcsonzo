from Autokolcsonzo import Autokolcsonzo
from Szemelyauto import Szemelyauto
from Teherauto import Teherauto
from datetime import datetime

class RentalSystem:

    def __init__(self):
        self._autokolcsonzo = Autokolcsonzo("EviszHertzisz")
        self._init_data()

    def _init_data(self):
        self._autokolcsonzo.cars = Szemelyauto("AAA-000", "Crossland", 10000)
        self._autokolcsonzo.cars = Szemelyauto("BAA-001", "Q3", 20000)
        self._autokolcsonzo.cars = Teherauto("TBA-011", "Transit", 17000)
        self._autokolcsonzo.rent_car_by_number_plate("AAA-000", datetime(2024, 12, 20).date())
        self._autokolcsonzo.rent_car_by_number_plate("BAA-001", datetime(2024, 12, 14).date())
        self._autokolcsonzo.rent_car_by_number_plate("TBA-011", datetime(2024, 12, 15).date())
        self._autokolcsonzo.rent_car_by_number_plate("TBA-011", datetime(2024, 12, 19).date())

    def user_interaction(self):
        while True:
            print(f"--- {self._autokolcsonzo.name} Autókölcsönző Rendszer ---")
            print("1. Autók listázása")
            print("2. Bérlések listázása")
            print("3. Autó kölcsönzése")
            print("4. Kölcsönzés visszamondása")
            print("5. Kilépés")

            menu = input("Válassz a lehetőségek közül: ")

            if menu == "1":
                self._autokolcsonzo.cars
            elif menu == "2":
                self._autokolcsonzo.rentals
            elif menu == "3":
                number_plate = input("Add meg az autó rendszámát: ")
                date = input("Add meg a bérlés dátumát (YYYY-MM-DD): ")
                try:
                    valid_date = datetime.strptime(date, "%Y-%m-%d").date()
                    self._autokolcsonzo.rent_car_by_number_plate(number_plate, valid_date)
                except ValueError:
                    print("Hiba: Érvénytelen dátum formátum.")
            elif menu == "4":
                number_plate = input("Add meg az autó rendszámát: ")
                date = input("Add meg a visszamondás dátumát (YYYY-MM-DD): ")
                try:
                    valid_date = datetime.strptime(date, "%Y-%m-%d").date()
                    self._autokolcsonzo.un_rent_car_by_number_plate(number_plate, valid_date)
                except ValueError:
                    print("Hiba: Érvénytelen dátum formátum.")
            elif menu == "5":
                print("Kilépés...")
                break
            else:
                print("Hiba: Érvénytelen választás.")

rental_system = RentalSystem()
rental_system.user_interaction()
