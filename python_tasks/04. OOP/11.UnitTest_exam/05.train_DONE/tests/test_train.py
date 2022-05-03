from project.train.train import Train

from unittest import TestCase, main

class TrainTests(TestCase):
    def setUp(self) -> None:
        name = 'Foo'
        capacity = 3
        passengers = ['Bar', 'Barz']
        self.train = Train(name, capacity)
        self.train.passengers = passengers

    def test_init_with_default_values(self):
        name = 'Boo'
        capacity = 40
        train = Train(name, capacity)
        self.assertEqual(name, train.name)
        self.assertEqual(capacity, train.capacity)
        self.assertEqual([], train.passengers)


    def test_init_with_different_values(self):
        self.assertEqual('Foo', self.train.name)
        self.assertEqual(3, self.train.capacity)
        self.assertEqual(['Bar', 'Barz'], self.train.passengers)

    def test_add_method_with_full_capacity(self):
        self.train.passengers.append('Roo')
        with self.assertRaises(ValueError) as ex:
            self.train.add('Boo')

        expected_result = 'Train is full'
        self.assertEqual(expected_result, str(ex.exception))


    def test_add_method_with_existing_name_should_raise_error(self):
        passenger = 'Bar'
        with self.assertRaises(ValueError) as ex:
            self.train.add(passenger)

        expected_result = f"Passenger {passenger} Exists"

        self.assertEqual(expected_result, str(ex.exception))


    def test_add_method_with_proper_values(self):
        passenger = 'Boo'
        result = self.train.add(passenger)
        expected_str_result = f"Added passenger {passenger}"
        expected_values = ['Bar', 'Barz', 'Boo']
        self.assertEqual(expected_str_result, result)
        self.assertEqual(expected_values, self.train.passengers)

    def test_remove_method_with_non_existing_passenger_should_rise_error(self):
        passenger = 'Boo'
        with self.assertRaises(ValueError) as ex:
            self.train.remove(passenger)

        expected_result = "Passenger Not Found"
        self.assertEqual(expected_result, str(ex.exception))


    def test_remove_method_with_existing_passenger(self):
        passenger = 'Bar'
        result = self.train.remove(passenger)
        expected_str_result = f"Removed {passenger}"
        expected_value_result = ['Barz']
        self.assertEqual(expected_str_result, result)
        self.assertEqual(expected_value_result, self.train.passengers)


if __name__ == '__main__':
    main()