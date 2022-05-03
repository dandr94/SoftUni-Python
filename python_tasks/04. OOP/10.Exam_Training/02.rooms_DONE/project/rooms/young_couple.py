from project.appliances.fridge import Fridge
from project.appliances.laptop import Laptop
from project.appliances.tv import TV
from project.rooms.room import Room


class YoungCouple(Room):
    DEFAULT_ROOM_COST = 20
    DEFAULT_MEMBERS_COUNT = 2
    DEFAULT_APPLIANCES = [TV(), TV(), Fridge(), Fridge(), Laptop(), Laptop()]

    def __init__(self, family_name: str, salary_one: float, salary_two: float):
        super().__init__(family_name, salary_one + salary_two, self.DEFAULT_MEMBERS_COUNT)
        self.room_cost = self.DEFAULT_ROOM_COST
        self.appliances = self.DEFAULT_APPLIANCES
        self.calculate_expenses(self.DEFAULT_APPLIANCES)
