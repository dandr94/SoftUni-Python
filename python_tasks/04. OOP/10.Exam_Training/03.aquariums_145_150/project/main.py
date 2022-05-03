from project.aquarium.base_aquarium import BaseAquarium
from project.aquarium.freshwater_aquarium import FreshwaterAquarium
from project.aquarium.saltwater_aquarium import SaltwaterAquarium
from project.controller import Controller
from project.decoration.decoration_repository import DecorationRepository
from project.decoration.ornament import Ornament
from project.decoration.plant import Plant
from project.fish.freshwater_fish import FreshwaterFish
from project.fish.saltwater_fish import SaltwaterFish


controller = Controller()
print(controller.add_aquarium('SaltwaterAquarium', 'Foo'))
print(controller.add_fish('Foo', 'SaltwaterFish', 'Barz', 'SaltwaterFish', 50))
print(controller.add_fish('Foo', 'SaltwaterFish', 'Goraz', 'SaltwaterFish', 50))
print(controller.add_decoration('Plant'))
print(controller.insert_decoration('Foo', 'Plant'))
print(controller.feed_fish('Foo'))
print(controller.calculate_value('Foo'))
print(controller.report())




