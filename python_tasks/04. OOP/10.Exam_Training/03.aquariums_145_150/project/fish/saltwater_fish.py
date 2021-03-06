from project.fish.base_fish import BaseFish


class SaltwaterFish(BaseFish):
    DEFAULT_EAT_SIZE_INCREASE = 2

    def __init__(self, name: str, species: str, price: float):
        super().__init__(name, species, self.DEFAULT_EAT_SIZE_INCREASE, price)
