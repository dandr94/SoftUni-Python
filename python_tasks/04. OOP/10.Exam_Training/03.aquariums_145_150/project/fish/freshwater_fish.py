from project.fish.base_fish import BaseFish


class FreshwaterFish(BaseFish):
    DEFAULT_EAT_SIZE_INCREASE = 3

    def __init__(self, name: str, species: str, price: float):
        super().__init__(name, species, self.DEFAULT_EAT_SIZE_INCREASE, price)

    def eat(self):
        self.size += self.DEFAULT_EAT_SIZE_INCREASE
