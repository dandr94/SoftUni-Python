from project.hardware.heavy_hardware import HeavyHardware
from project.hardware.power_hardware import PowerHardware
from project.software.express_software import ExpressSoftware
from project.software.light_software import LightSoftware


class System:
    _hardware = []
    _software = []

    @staticmethod
    def register_power_hardware(name: str, capacity: int, memory: int):
        power_hardware = PowerHardware(name, capacity, memory)
        System._hardware.append(power_hardware)

    @staticmethod
    def register_heavy_hardware(name: str, capacity: int, memory: int):
        heavy_hardware = HeavyHardware(name, capacity, memory)
        System._hardware.append(heavy_hardware)

    @staticmethod
    def register_express_software(hardware_name: str,
                                  name: str,
                                  capacity_consumption: int,
                                  memory_consumption: int):
        express_software = ExpressSoftware(name, capacity_consumption, memory_consumption)
        hardware = System.find_hardware(hardware_name)
        if hardware is None:
            return 'Hardware does not exist'

        hardware.install(express_software)
        System._software.append(express_software)


    @staticmethod
    def register_light_software(hardware_name: str,
                                name: str,
                                capacity_consumption: int,
                                memory_consumption: int):
        light_software = LightSoftware(name, capacity_consumption, memory_consumption)
        hardware = System.find_hardware(hardware_name)
        if hardware is None:
            return 'Hardware does not exist'

        hardware.install(light_software)
        System._software.append(light_software)

    @staticmethod
    def release_software_component(hardware_name: str, software_name: str):
        hardware = System.find_hardware(hardware_name)
        software = System.find_software(software_name)

        if hardware is None or software is None:
            return 'Some of the components do not exist'

        hardware.uninstall(software)
        System._software.remove(software)

    @staticmethod
    def analyze():
        hardware_components = len(System._hardware)
        software_components = len(System._software)
        software_total_memory_consumption = sum([x.total_software_memory_consumption() for x in System._hardware])
        hardware_total_memory = sum([x.memory for x in System._hardware])
        total_capacity_consumption_for_all_software = sum([x.total_software_capacity_consumption() for x in System._hardware])
        total_capacity_for_all_hardware = sum([x.capacity for x in System._hardware])
        result = 'System Analysis\n' \
                 f'Hardware Components: {hardware_components}\n' \
                 f'Software Components: {software_components}\n' \
                 f'Total Operational Memory: {software_total_memory_consumption} / {hardware_total_memory}\n' \
                 f'Total Capacity Taken: {total_capacity_consumption_for_all_software} / {total_capacity_for_all_hardware}'

        return result

    @staticmethod
    def system_split():
        result = ''
        for hardware in System._hardware:
            result += str(hardware)

        return result.strip()

    @staticmethod
    def find_hardware(hardware_name):
        for hardware in System._hardware:
            if hardware.name == hardware_name:
                return hardware

        return None

    @staticmethod
    def find_software(software_name):
        for software in System._software:
            if software.name == software_name:
                return software

        return None
