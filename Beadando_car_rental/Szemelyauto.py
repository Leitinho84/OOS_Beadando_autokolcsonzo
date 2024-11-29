from Auto import Auto

class Szemelyauto(Auto):
    @property
    def number_plate(self):
        return self._number_plate

    @property
    def model(self):
        return self._model

    @property
    def price(self):
        return self._price