from project.hardware.hardware import Hardware


class PowerHardware(Hardware):
    hardware_type = 'Power'

    def __init__(self,
                 name: str,
                 capacity: int,
                 memory: int):
        super().__init__(name,
                         self.hardware_type,
                         int(capacity * 0.25),
                         int(memory + (memory * 0.75)))
