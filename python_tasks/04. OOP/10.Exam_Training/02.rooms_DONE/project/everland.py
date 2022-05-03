from project.rooms.room import Room


class Everland:
    def __init__(self):
        self.rooms = []

    def add_room(self, room: Room):
        self.rooms.append(room)

    def get_monthly_consumptions(self):
        result = sum([r.expenses + r.DEFAULT_ROOM_COST for r in self.rooms])
        return f'Monthly consumption: {result:.2f}$.'

    def pay(self):
        result = ''
        for room in self.rooms:
            if room.budget >= room.expenses:
                room.budget -= room.expenses
                result += f'{room.family_name} paid ' \
                          f'{room.expenses + room.DEFAULT_ROOM_COST:.2f}$ and have ' \
                          f'{room.budget- room.DEFAULT_ROOM_COST:.2f}$ left.\n'
            else:
                result += f'{room.family_name} does not have enough budget and must leave the hotel.\n'
                self.rooms.remove(room)

        return result.strip()

    def status(self):
        result = f'Total population: {sum(r.members_count for r in self.rooms)}\n'

        for room in self.rooms:
            result += f'{room.family_name} with {room.members_count} members. ' \
                      f'Budget: {room.budget - room.DEFAULT_ROOM_COST:.2f}$, Expenses: {room.expenses:.2f}$\n'
            for i, c in enumerate(room.children):
                result += f'--- Child {i + 1} monthly cost: {c.get_monthly_expense():.2f}$\n'
            result += f'--- Appliances monthly cost: {sum(a.get_monthly_expense() for a in room.appliances):.2f}$\n'

        return result.strip()
