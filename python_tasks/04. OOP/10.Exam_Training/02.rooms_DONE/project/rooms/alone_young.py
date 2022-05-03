from project.appliances.tv import TV
from project.rooms.room import Room


class AloneYoung(Room):
    DEFAULT_ROOM_COST = 10
    DEFAULT_MEMBERS_COUNT = 1
    DEFAULT_APPLIANCES = [TV()]

    def __init__(self, family_name: str, salary: float):
        super().__init__(family_name, salary, self.DEFAULT_MEMBERS_COUNT)
        self.room_cost = self.DEFAULT_ROOM_COST
        self.appliances = self.DEFAULT_APPLIANCES
        self.calculate_expenses(self.DEFAULT_APPLIANCES)
