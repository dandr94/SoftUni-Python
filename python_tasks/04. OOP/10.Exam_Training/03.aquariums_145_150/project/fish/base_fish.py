from abc import ABC, abstractmethod


class BaseFish(ABC):
    DEFAULT_NAME_ERROR_MESSAGE = 'Fish name cannot be an empty string.'
    DEFAULT_SPECIES_ERROR_MESSAGE = 'Fish species cannot be an empty string.'
    DEFAULT_PRICE_ERROR_MESSAGE = 'Price cannot be equal to or below zero.'
    DEFAULT_EAT_SIZE_INCREASE = 5

    @abstractmethod
    def __init__(self, name: str, species: str, size: int, price: float):
        self.name = name
        self.species = species
        self.size = size
        self.price = price

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value == '':
            raise ValueError(self.DEFAULT_NAME_ERROR_MESSAGE)

        self.__name = value

    @property
    def species(self):
        return self.__species

    @species.setter
    def species(self, value):
        if value == '':
            raise ValueError(self.DEFAULT_SPECIES_ERROR_MESSAGE)

        self.__species = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value <= 0:
            raise ValueError(self.DEFAULT_PRICE_ERROR_MESSAGE)

        self.__price = value

    def eat(self):
        self.size += self.DEFAULT_EAT_SIZE_INCREASE
