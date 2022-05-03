from project.appliances.fridge import Fridge
from project.appliances.laptop import Laptop
from project.appliances.tv import TV
from project.rooms.room import Room


class YoungCoupleWithChildren(Room):
    DEFAULT_ROOM_COST = 30
    DEFAULT_MEMBERS_COUNT_WITHOUT_CHILDREN = 2

    def __init__(self, family_name: str, salary_one, salary_two, *children):
        super().__init__(family_name, salary_one + salary_two, self.DEFAULT_MEMBERS_COUNT_WITHOUT_CHILDREN)
        self.children = [x for x in children] if children else []
        self.room_cost = self.DEFAULT_ROOM_COST
        self.members_count = len(self.children) + self.DEFAULT_MEMBERS_COUNT_WITHOUT_CHILDREN
        self.appliances = self.return_appliances_for_every_member(self.members_count)
        self.calculate_expenses(self.children + self.appliances)

    @staticmethod
    def return_appliances_for_every_member(members_count):
        result = []

        for _ in range(members_count):
            result.append(TV())
            result.append(Fridge())
            result.append(Laptop())

        return result
