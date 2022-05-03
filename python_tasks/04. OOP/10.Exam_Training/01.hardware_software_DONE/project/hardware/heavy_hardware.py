from project.hardware.hardware import Hardware


class HeavyHardware(Hardware):
    hardware_type = 'Heavy'

    def __init__(self,
                 name: str,
                 capacity: int,
                 memory: int):
        super().__init__(name,
                         self.hardware_type,
                         int(capacity * 2),
                         int(memory * 0.75))
