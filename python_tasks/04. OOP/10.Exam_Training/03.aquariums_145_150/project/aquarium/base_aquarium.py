from abc import ABC, abstractmethod


class BaseAquarium(ABC):
    DEFAULT_NAME_ERROR_MESSAGE = 'Aquarium name cannot be an empty string.'
    POSSIBLE_FISH_TYPE = ['FreshwaterFish', 'SaltwaterFish']

    @abstractmethod
    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.decorations = []
        self.fish = []


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value == '':
            raise ValueError(self.DEFAULT_NAME_ERROR_MESSAGE)

        self.__name = value

    def calculate_comfort(self):
        return sum([d.comfort for d in self.decorations])

    def add_fish(self, fish: object):
        fish_type = fish.__class__.__name__
        if self.capacity <= len(self.fish):
            return 'Not enough capacity.'
        if fish_type == 'SaltwaterFish' and self.__class__.__name__ != 'SaltwaterAquarium'\
                or fish_type == 'FreshwaterFish' and self.__class__.__name__ != 'FreshwaterAquarium':
            return 'Water not suitable.'

        if fish_type in self.POSSIBLE_FISH_TYPE:
            self.fish.append(fish)
            return f'Successfully added {fish_type} to {self.name}.'

    def remove_fish(self, fish: object):
        # TODO: check for validation
        self.fish.remove(fish)

    def add_decoration(self, decoration: object):
        self.decorations.append(decoration)

    def feed(self):
        [f.eat() for f in self.fish]

    def calculate_prices(self):
        fish_price = sum([f.price for f in self.fish])
        decoration_price = sum([d.price for d in self.decorations])
        return f'The value of Aquarium {self.name} is {fish_price + decoration_price:.2f}.'

    def __str__(self):
        return f"{self.name}:\n" \
               f"Fish: {', '.join([f.name for f in self.fish]) if self.fish else 'none'}\n" \
               f"Decorations: {len(self.decorations)}\n" \
               f"Comfort: {self.calculate_comfort()}"
