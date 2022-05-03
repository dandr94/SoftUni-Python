from project.appliances.fridge import Fridge
from project.appliances.stove import Stove
from project.appliances.tv import TV
from project.rooms.room import Room


class OldCouple(Room):
    DEFAULT_ROOM_COST = 15
    DEFAULT_MEMBERS_COUNT = 2
    DEFAULT_APPLIANCES = [TV(), TV(), Fridge(), Fridge(), Stove(), Stove()]

    def __init__(self, family_name: str, pension_one: float, pension_two: float):
        super().__init__(family_name, pension_one + pension_two, self.DEFAULT_MEMBERS_COUNT)
        self.appliances = self.DEFAULT_APPLIANCES
        self.room_cost = self.DEFAULT_ROOM_COST
        self.calculate_expenses(self.DEFAULT_APPLIANCES)
