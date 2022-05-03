from project.appliances.appliance import Appliance


class Laptop(Appliance):
    APPLIANCE_COST = 1

    def __init__(self):
        super().__init__(self.APPLIANCE_COST)
