from car_manager import Car
import unittest


class CarTest(unittest.TestCase):
    def test_if_init_works_properly(self):
        car = Car('Audi', 'A8', 50, 5000)
        result_make = car.make
        result_model = car.model
        result_fuel_consumption = car.fuel_consumption
        result_fuel_capacity = car.fuel_capacity
        self.assertEqual(result_make, 'Audi')
        self.assertEqual(result_model, 'A8')
        self.assertEqual(result_fuel_consumption, 50)
        self.assertEqual(result_fuel_capacity, 5000)

    def test_if_make_raises_error_if_input_is_empty_or_null(self):
        car = Car('Audi', 'A8', 50, 5000)

        with self.assertRaises(Exception) as ex:
            car.make = ''

        self.assertEqual(str(ex.exception), "Make cannot be null or empty!")

    def test_if_model_raises_error_if_input_is_empty_or_null(self):
        car = Car('Audi', 'A8', 50, 5000)

        with self.assertRaises(Exception) as ex:
            car.model = ''

        self.assertEqual(str(ex.exception), "Model cannot be null or empty!")

    def test_if_value_error_is_raised_if_negative_number_or_zero_is_inputted_on_fuel_consumption(self):
        car = Car('Audi', 'A8', 50, 5000)

        with self.assertRaises(Exception) as ex:
            car.fuel_consumption -= 50

        self.assertEqual(str(ex.exception), "Fuel consumption cannot be zero or negative!")

        with self.assertRaises(Exception) as ex:
            car.fuel_consumption -= 51

        self.assertEqual(str(ex.exception), "Fuel consumption cannot be zero or negative!")

    def test_if_value_error_is_raised_if_negative_or_zero_is_inputted_on_fuel_capacity(self):
        car = Car('Audi', 'A8', 50, 5000)

        with self.assertRaises(Exception) as ex:
            car.fuel_capacity -= 5000

        self.assertEqual(str(ex.exception), "Fuel capacity cannot be zero or negative!")

        with self.assertRaises(Exception) as ex:
            car.fuel_capacity -= 5001

        self.assertEqual(str(ex.exception), "Fuel capacity cannot be zero or negative!")

    def test_refuel_method(self):
        car = Car('Audi', 'A8', 50, 5000)

        car.refuel(50)

        self.assertEqual(car.fuel_amount, 50)

    def test_refuel_with_negative_number_or_zero(self):
        car = Car('Audi', 'A8', 50, 5000)

        with self.assertRaises(Exception) as ex:
            car.refuel(-5)

        self.assertEqual(str(ex.exception), "Fuel amount cannot be zero or negative!")

        with self.assertRaises(Exception) as ex:
            car.refuel(0)

        self.assertEqual(str(ex.exception), "Fuel amount cannot be zero or negative!")

    def test_if_fuel_amount_is_correct_if_exceeds_fuel_capacity(self):
        car = Car('Audi', 'A8', 50, 5000)

        car.refuel(6000)

        self.assertEqual(car.fuel_amount, 5000)

    def test_fuel_amount_after_drive(self):
        car = Car('Audi', 'A8', 50, 5000)
        car.refuel(50)
        self.assertEqual(car.fuel_amount, 50)
        car.drive(50)

        self.assertEqual(car.fuel_amount, 25)

    def test_drive_if_fuel_is_not_enough(self):
        car = Car('Audi', 'A8', 50, 5000)
        car.refuel(50)

        with self.assertRaises(Exception) as ex:
            car.drive(500)

        self.assertEqual(str(ex.exception), "You don't have enough fuel to drive!")


if __name__ == '__main__':
    unittest.main()
