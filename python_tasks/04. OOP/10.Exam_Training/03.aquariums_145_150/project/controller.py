from project.aquarium.freshwater_aquarium import FreshwaterAquarium
from project.aquarium.saltwater_aquarium import SaltwaterAquarium
from project.decoration.decoration_repository import DecorationRepository
from project.decoration.ornament import Ornament
from project.decoration.plant import Plant
from project.fish.freshwater_fish import FreshwaterFish
from project.fish.saltwater_fish import SaltwaterFish


class Controller:
    def __init__(self):
        self.decorations = DecorationRepository()
        self.aquariums = []

    def add_aquarium(self, aquarium_type: str, aquarium_name: str):
        if aquarium_type == 'FreshwaterAquarium':
            self.aquariums.append(FreshwaterAquarium(aquarium_name))
        elif aquarium_type == 'SaltwaterAquarium':
            self.aquariums.append(SaltwaterAquarium(aquarium_name))
        else:
            return 'Invalid aquarium type.'

        return f'Successfully added {aquarium_type}.'

    def add_decoration(self, decoration_type: str):
        if decoration_type == 'Ornament':
            self.decorations.add(Ornament())
        elif decoration_type == 'Plant':
            self.decorations.add(Plant())
        else:
            return 'Invalid decoration type.'

        return f'Successfully added {decoration_type}.'

    def insert_decoration(self, aquarium_name: str, decoration_type: str):
        aquarium = self.find_aquarium(aquarium_name)
        decoration = self.decorations.find_by_type(decoration_type)

        if aquarium and decoration and decoration != 'None':
            aquarium.add_decoration(decoration)
            self.decorations.remove(decoration)
            return f'Successfully added {decoration_type} to {aquarium_name}.'

        return f'There isn\'t a decoration of type {decoration_type}.'

    def add_fish(self,
                 aquarium_name: str,
                 fish_type: str,
                 fish_name: str,
                 fish_species: str,
                 price: float):
        aquarium = self.find_aquarium(aquarium_name)
        fish = self.create_fish(fish_type, fish_name, fish_species, price)

        if aquarium and fish:
            return aquarium.add_fish(fish)

    def feed_fish(self, aquarium_name: str):
        aquarium = self.find_aquarium(aquarium_name)
        aquarium.feed()
        return f'Fish fed: {len(aquarium.fish)}'

    def calculate_value(self, aquarium_name: str):
        aquarium = self.find_aquarium(aquarium_name)
        return aquarium.calculate_prices()

    def report(self):
        return "\n".join(str(x) for x in self.aquariums)

    def find_aquarium(self, aquarium_name):
        for aquarium in self.aquariums:
            if aquarium.name == aquarium_name:
                return aquarium

        return None

    @staticmethod
    def create_fish(fish_type, name, species, price):
        if fish_type == 'SaltwaterFish':
            return SaltwaterFish(name, species, price)
        if fish_type == 'FreshwaterFish':
            return FreshwaterFish(name, species, price)

        return None
