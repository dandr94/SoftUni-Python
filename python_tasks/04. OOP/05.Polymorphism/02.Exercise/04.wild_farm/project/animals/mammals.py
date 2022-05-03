from project.animals.animal import Mammal


class Mouse(Mammal):
    ALLOWED_FOOD = ['Vegetable', 'Fruit']
    WEIGHT_MULTIPLIER = 0.1

    def __init__(self, name: str, weight: float, living_region: str):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return 'Squeak'


class Cat(Mammal):
    ALLOWED_FOOD = ['Vegetable', 'Meat']
    WEIGHT_MULTIPLIER = 0.3

    def __init__(self, name: str, weight: float, living_region: str):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return 'Meow'


class Dog(Mammal):
    ALLOWED_FOOD = ['Meat']
    WEIGHT_MULTIPLIER = 0.4

    def __init__(self, name: str, weight: float, living_region: str):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return 'Woof!'


class Tiger(Mammal):
    ALLOWED_FOOD = ['Meat']
    WEIGHT_MULTIPLIER = 1

    def __init__(self, name: str, weight: float, living_region: str):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return 'ROAR!!!'
