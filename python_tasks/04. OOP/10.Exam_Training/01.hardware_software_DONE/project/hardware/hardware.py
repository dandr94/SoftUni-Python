from project.software.software import Software


class Hardware:
    INSTALL_ERROR_MESSAGE = 'Software cannot be installed'

    def __init__(self, name: str, hardware_type: str, capacity: int, memory: int):
        self.name = name
        self.hardware_type = hardware_type
        self.capacity = capacity
        self.memory = memory
        self.software_components = []

    def install(self, software: Software):
        if self.memory < software.memory_consumption or self.capacity < software.capacity_consumption:
            raise Exception(self.INSTALL_ERROR_MESSAGE)

        self.software_components.append(software)

    def uninstall(self, software: Software):
        # TODO: maybe check for validation
        self.software_components.remove(software)

    def total_software_memory_consumption(self):
        result = 0
        for software in self.software_components:
            result += software.memory_consumption

        return result

    def total_software_capacity_consumption(self):
        result = 0
        for software in self.software_components:
            result += software.capacity_consumption

        return result

    def __str__(self):
        result = f'Hardware Component - {self.name}\n'
        result += f'Express Software Components: ' \
                  f'{len([x for x in self.software_components if x.software_type == "Express"])}\n'
        result += f'Light Software Components: ' \
                  f'{len([x for x in self.software_components if x.software_type == "Light"])}\n'
        result += f'Memory Usage: {self.total_software_memory_consumption()} / {self.memory}\n'
        result += f'Capacity Usage: {self.total_software_capacity_consumption()} / {self.capacity}\n'
        result += f'Type: {self.hardware_type}\n'
        result += f'Software Components: {", ".join(x.name for x in self.software_components) if self.software_components else "None"}\n'

        return result