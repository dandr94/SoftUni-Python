from project.appliances.appliance import Appliance


class Fridge(Appliance):
    APPLIANCE_COST = 1.2

    def __init__(self):
        super().__init__(self.APPLIANCE_COST)
