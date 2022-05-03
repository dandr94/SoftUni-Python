from project.astronaut.astronaut import Astronaut
from project.astronaut.astronaut_repository import AstronautRepository
from project.astronaut.biologist import Biologist
from project.astronaut.geodesist import Geodesist
from project.astronaut.meteorologist import Meteorologist
from project.planet.planet import Planet
from project.planet.planet_repository import PlanetRepository


class SpaceStation:
    successful_missions = 0
    unsuccessful_missions = 0

    def __init__(self):
        self.astronaut_repository = AstronautRepository()
        self.planet_repository = PlanetRepository()

    def add_astronaut(self, astronaut_type: str, name: str):
        astronaut = self.return_astronaut(astronaut_type, name)

        if astronaut is None:
            raise Exception('Astronaut type is not valid!')
        if self.astronaut_repository.find_by_name(name):
            return f'{name} is already added.'

        self.astronaut_repository.astronauts.append(astronaut)
        return f'Successfully added {astronaut_type}: {name}.'

    def add_planet(self, name: str, items: str):
        if self.planet_repository.find_by_name(name):
            return f'{name} is already added.'

        planet = Planet(name)
        [planet.items.append(x) for x in items.split(', ')]
        self.planet_repository.planets.append(planet)
        return f'Successfully added Planet: {name}.'

    def retire_astronaut(self, name: str):
        astronaut = self.astronaut_repository.find_by_name(name)

        if astronaut is None:
            raise Exception(f"Astronaut {name} doesn't exist!")

        self.astronaut_repository.remove(astronaut)
        return f'Astronaut {name} was retired!'

    def recharge_oxygen(self):
        for astronaut in self.astronaut_repository.astronauts:
            astronaut.increase_oxygen(10)

    def send_on_mission(self, planet_name: str):
        planet = self.planet_repository.find_by_name(planet_name)

        if planet is None:
            raise Exception('Invalid planet name!')

        suitable_astronauts = sorted([x for x in self.astronaut_repository.astronauts if x.oxygen > 30],
                                     key=lambda x: -x.oxygen)[0:5]

        if not suitable_astronauts:
            raise Exception('You need at least one astronaut to explore the planet!')

        astronaut_participated = 0
        for astronaut in suitable_astronauts:
            if len(planet.items) == 0:
                break
            while astronaut.oxygen > 0 and len(planet.items) > 0:
                astronaut.backpack.append(planet.items.pop())
                astronaut.breathe()
            astronaut_participated += 1

        if len(planet.items) > 0:
            self.unsuccessful_missions += 1
            return 'Mission is not completed.'
        self.successful_missions += 1
        return f'Planet: {planet_name} was explored. ' \
               f'{astronaut_participated} astronauts participated in collecting items.'

    def report(self):
        result = ''
        result += f"{self.successful_missions} successful missions!\n"
        result += f'{self.unsuccessful_missions} missions were not completed!\n'
        result += "Astronauts' info:\n"
        for astronaut in self.astronaut_repository.astronauts:
            result += str(astronaut) + '\n'

        return result.strip()

    @staticmethod
    def return_astronaut(astronaut_type, name):
        if astronaut_type == 'Biologist':
            return Biologist(name)
        if astronaut_type == 'Geodesist':
            return Geodesist(name)
        if astronaut_type == 'Meteorologist':
            return Meteorologist(name)
        return None
