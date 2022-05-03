class Vehicle:
    DEFAULT_FUEL_CONSUMPTION = 1.25

    def __init__(self, fuel, horse_power):
        self.fuel = fuel
        self.horse_power = horse_power
        self.fuel_consumption = 1.25

    def drive(self, kilometers):
        if self.fuel >= kilometers * self.DEFAULT_FUEL_CONSUMPTION:
            self.fuel -= kilometers * self.DEFAULT_FUEL_CONSUMPTION
