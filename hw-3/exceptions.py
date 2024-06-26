"""
Объявите следующие исключения:
- LowFuelError
- NotEnoughFuel
- CargoOverload
"""


class VehicleExeption(Exception):
    pass

class LowFuelError(VehicleExeption):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)
        self.add_note('Low fuel')

class NotEnoughFuel(VehicleExeption):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)
        self.message = 'Not enought fuel'

class CargoOverload(VehicleExeption):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)
        self.message = 'Overload'