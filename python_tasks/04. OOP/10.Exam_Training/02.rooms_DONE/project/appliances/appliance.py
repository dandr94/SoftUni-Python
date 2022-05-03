class Appliance:
    DAYS_IN_A_MONTH = 30

    def __init__(self, cost: float):
        self.cost = cost  # for single day

    def get_monthly_expense(self):
        return self.cost * self.DAYS_IN_A_MONTH
