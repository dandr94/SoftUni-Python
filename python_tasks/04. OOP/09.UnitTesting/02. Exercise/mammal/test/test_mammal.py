from project.mammal import Mammal
import unittest


class MammalTests(unittest.TestCase):
    def test_if_init_works(self):
        mammal = Mammal('Bob', 'Dog', 'Bauw')
        self.assertEqual(mammal.name, 'Bob')
        self.assertEqual(mammal.type, 'Dog')
        self.assertEqual(mammal.sound, 'Bauw')
        self.assertEqual(mammal._Mammal__kingdom, 'animals')

    def test_make_sound_method(self):
        mammal = Mammal('Bob', 'Dog', 'Bauw')
        result = mammal.make_sound()
        expected_result = 'Bob makes Bauw'
        self.assertEqual(result, expected_result)

    def test_get_kingdom_method(self):
        mammal = Mammal('Bob', 'Dog', 'Bauw')
        result = mammal.get_kingdom()

        self.assertEqual(result, 'animals')

    def test_info_method(self):
        mammal = Mammal('Bob', 'Dog', 'Bauw')
        result = mammal.info()
        expected_result = 'Bob is of type Dog'
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
