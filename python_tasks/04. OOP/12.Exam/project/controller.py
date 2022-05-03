from project.car.muscle_car import MuscleCar
from project.car.sports_car import SportsCar
from project.driver import Driver
from project.race import Race


class Controller:
    def __init__(self):
        self.cars = []
        self.drivers = []
        self.races = []

    def create_car(self, car_type: str, model: str, speed_limit: int):
        car = self.provide_car(car_type, model, speed_limit)

        if any([c for c in self.cars if c.model == model]):
            raise Exception(f'Car {model} is already created!')

        if car:
            self.cars.append(car)
            return f"{car_type} {model} is created."

    def create_driver(self, driver_name: str):
        driver = Driver(driver_name)

        if any([d for d in self.drivers if d.name == driver_name]):
            raise Exception(f"Driver {driver_name} is already created!")

        if driver:
            self.drivers.append(driver)
            return f'Driver {driver_name} is created.'

    def create_race(self, race_name: str):
        race = Race(race_name)

        if any([r for r in self.races if r.name == race_name]):
            raise Exception(f'Race {race_name} is already created!')

        if race:
            self.races.append(race)
            return f'Race {race_name} is created.'

    def add_car_to_driver(self, driver_name: str, car_type: str):
        driver = self.find_driver(driver_name)
        car = self.find_car(car_type)

        if driver is None:
            raise Exception(f'Driver {driver_name} could not be found!')

        if car is None:
            raise Exception(f'Car {car_type} could not be found!')

        if driver.car:
            old_model = driver.car  # object
            old_model.is_taken = False
            driver.car = car
            car.is_taken = True
            return f'Driver {driver.name} changed his car from {old_model.model} to {car.model}.'

        driver.car = car
        car.is_taken = True
        return f'Driver {driver_name} chose the car {car.model}.'

    def add_driver_to_race(self, race_name: str, driver_name: str):
        driver = self.find_driver(driver_name)
        race = self.find_race(race_name)

        if race is None:
            raise Exception(f'Race {race_name} could not be found!')

        if driver is None:
            raise Exception(f'Driver {driver_name} could not be found!')

        if driver.car is None:
            raise Exception(f'Driver {driver_name} could not participate in the race!')

        if driver in race.drivers:
            return f'Driver {driver_name} is already added in {race_name} race.'

        race.drivers.append(driver)
        return f'Driver {driver_name} added in {race_name} race.'


    def start_race(self, race_name: str):
        race = self.find_race(race_name)

        if race is None:
            raise Exception(f'Race {race_name} could not be found!')

        if len(race.drivers) < 3:
            raise Exception(f'Race {race_name} cannot start with less than 3 participants!')

        winners = sorted([x for x in race.drivers], key=lambda x: -x.car.speed_limit)[0:3]

        result = ''

        for winner in winners:
            winner.number_of_wins += 1
            result += f'Driver {winner.name} wins the {race_name} race ' \
                      f'with a speed of {winner.car.speed_limit}.\n'

        return result.strip()




    @staticmethod
    def provide_car(car_type, model, speed_limit):
        if car_type == 'MuscleCar':
            return MuscleCar(model, speed_limit)
        if car_type == 'SportsCar':
            return SportsCar(model, speed_limit)
        return None

    def find_driver(self, driver_name):
        for driver in self.drivers:
            if driver.name == driver_name:
                return driver

        return None

    def find_car(self, car_type):
        for car in self.cars[::-1]:
            if car.__class__.__name__ == car_type and not car.is_taken:
                return car

        return None

    def find_race(self, race_name):
        for race in self.races:
            if race.name == race_name:
                return race

        return None