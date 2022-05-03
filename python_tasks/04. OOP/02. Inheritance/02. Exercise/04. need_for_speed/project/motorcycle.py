from project.vehicle import Vehicle


class Motorcycle(Vehicle):
    DEFAULT_FUEL_CONSUMPTION = 1.25

    def __init__(self, fuel, horse_power):
        super().__init__(fuel, horse_power)
        self.fuel_consumption = 1.25


    def drive(self, kilometers):
        if self.fuel >= kilometers * self.DEFAULT_FUEL_CONSUMPTION:
            self.fuel -= kilometers * self.DEFAULT_FUEL_CONSUMPTION
