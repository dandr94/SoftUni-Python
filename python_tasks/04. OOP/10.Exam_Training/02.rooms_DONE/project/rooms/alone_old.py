from project.rooms.room import Room


class AloneOld(Room):
    DEFAULT_ROOM_COST = 10
    DEFAULT_MEMBERS_COUNT = 1

    def __init__(self, family_name: str, pension: float):
        super().__init__(family_name, pension, self.DEFAULT_MEMBERS_COUNT)
        self.room_cost = self.DEFAULT_ROOM_COST