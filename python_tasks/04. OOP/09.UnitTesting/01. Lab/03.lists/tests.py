from extended_list import IntegerList
import unittest


class IntegerListsTest(unittest.TestCase):

    def test_add_element_and_return_the_list(self):
        integer_list = IntegerList(5, 6, 7, 8)
        self.assertEqual(integer_list.get_data(), [5, 6, 7, 8])
        integer_list.add(5)
        self.assertEqual(integer_list.get_data(), [5, 6, 7, 8, 5])

    def test_if_adding_not_int_gets_value_error(self):
        integer_list = IntegerList(5, 6, 7, 8)
        self.assertEqual(integer_list.get_data(), [5, 6, 7, 8])

        with self.assertRaises(Exception) as ex:
            integer_list.add('hello')

        self.assertEqual(str(ex.exception), "Element is not Integer")

    def test_if_remove_method_works_properly(self):
        integer_list = IntegerList(5, 6, 7, 8)
        self.assertEqual(integer_list.get_data(), [5, 6, 7, 8])

        integer_list.remove_index(3)

        self.assertEqual(integer_list.get_data(), [5, 6, 7])

    def test_if_index_error_is_raised_if_given_incorrect_index(self):
        integer_list = IntegerList(5, 6, 7, 8)
        self.assertEqual(integer_list.get_data(), [5, 6, 7, 8])

        with self.assertRaises(Exception) as ex:
            integer_list.remove_index(5)

        self.assertEqual(str(ex.exception), "Index is out of range")

    def test_if_init_takes_only_integers(self):
        integer_list = IntegerList(5, 6, 7, 8, 'hello', True, [], 5.6)
        self.assertEqual(integer_list.get_data(), [5, 6, 7, 8])

    def test_if_get_method_returns_the_specific_element(self):
        integer_list = IntegerList(5, 6, 7, 8)

        result = integer_list.get(3)

        self.assertEqual(result, 8)

    def test_if_index_error_is_properly_working_if_input_is_out_of_range(self):
        integer_list = IntegerList(5, 6, 7, 8)

        with self.assertRaises(Exception) as ex:
            integer_list.get(7)

        self.assertEqual(str(ex.exception), "Index is out of range")

    def test_if_insert_works_properly(self):
        integer_list = IntegerList(5, 6, 7, 8)
        integer_list.insert(3, 10)

        self.assertEqual(integer_list.get_data(), [5, 6, 7, 10, 8])

    def test_if_index_error_is_raised_if_index_out_of_range_on_the_insert_method(self):
        integer_list = IntegerList(5, 6, 7, 8)

        with self.assertRaises(Exception) as ex:
            integer_list.insert(10, 10)

        self.assertEqual(str(ex.exception), "Index is out of range")

    def test_if_value_error_is_raised_if_not_int_is_passed_on_the_insert_method(self):
        integer_list = IntegerList(5, 6, 7, 8)

        with self.assertRaises(Exception) as ex:
            integer_list.insert(3, 'hello')

        self.assertEqual(str(ex.exception), "Element is not Integer")

    def test_if_biggest_method_works_properly(self):
        integer_list = IntegerList(5, 6, 7, 8)
        result = integer_list.get_biggest()

        self.assertEqual(result, 8)

    def test_if_get_index_method_works_properly(self):
        integer_list = IntegerList(5, 6, 7, 8)
        result = integer_list.get_index(8)

        self.assertEqual(result, 3)


if __name__ == '__main__':
    unittest.main()
