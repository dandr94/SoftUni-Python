from project.appliances.appliance import Appliance


class Stove(Appliance):
    APPLIANCE_COST = 0.7

    def __init__(self):
        super().__init__(self.APPLIANCE_COST)
