class Room:
    DEFAULT_EXPENSES_ERROR_MESSAGE = 'Expenses cannot be negative'
    DEFAULT_ROOM_COST = 0

    def __init__(self, name: str, budget: float, members_count: int):
        self.family_name = name
        self.budget = budget
        self.members_count = members_count
        self.children = []
        self.expenses = 0

    @property
    def expenses(self):
        return self.__expenses

    @expenses.setter
    def expenses(self, value):
        if value < 0:
            raise ValueError(self.DEFAULT_EXPENSES_ERROR_MESSAGE)
        self.__expenses = value

    def calculate_expenses(self, *args):
        result = 0
        for item in args:
            for k in item:
                result += k.get_monthly_expense()

        self.expenses = result




