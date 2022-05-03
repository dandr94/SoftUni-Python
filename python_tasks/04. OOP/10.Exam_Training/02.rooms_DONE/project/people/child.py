class Child:
    DAYS_IN_A_MONTH = 30

    def __init__(self, food_cost: int, *toys_cost):
        self.cost = food_cost + sum(toys_cost)

    def get_monthly_expense(self):
        return self.cost * self.DAYS_IN_A_MONTH
