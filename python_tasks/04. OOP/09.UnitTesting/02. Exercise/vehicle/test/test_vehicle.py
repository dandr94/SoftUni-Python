from project.vehicle import Vehicle
import unittest


class VehicleTests(unittest.TestCase):
    def test_init(self):
        veh = Vehicle(50.5, 30)
        self.assertEqual(veh.fuel, 50.5)
        self.assertEqual(veh.capacity, 50.5)
        self.assertEqual(veh.horse_power, 30)
        self.assertEqual(veh.fuel_consumption, 1.25)

    def test_drive_successful(self):
        veh = Vehicle(50.5, 30)

        veh.drive(5)

        self.assertEqual(veh.fuel, 44.25)

    def test_drive_raises_error_if_fuel_not_enough(self):
        veh = Vehicle(50.5, 30)

        with self.assertRaises(Exception) as ex:
            veh.drive(500)

        self.assertEqual(str(ex.exception), "Not enough fuel")

    def test_successful_refuel(self):
        veh = Vehicle(50.5, 30)
        veh.fuel = 25

        veh.refuel(25)

        self.assertEqual(veh.fuel, 50)

    def test_refuel_capacity(self):
        veh = Vehicle(50.5, 30)

        with self.assertRaises(Exception) as ex:
            veh.refuel(50)

        self.assertEqual(str(ex.exception), 'Too much fuel')

    def test_if_str_returns_right_value(self):
        veh = Vehicle(50.5, 30)
        result = str(veh)
        self.assertEqual(result, f"The vehicle has {30} horse power with {50.5} fuel left and {1.25} fuel consumption")


if __name__ == '__main__':
    unittest.main()
