from project.appliances.appliance import Appliance


class TV(Appliance):
    APPLIANCE_COST = 1.5

    def __init__(self):
        super().__init__(self.APPLIANCE_COST)
