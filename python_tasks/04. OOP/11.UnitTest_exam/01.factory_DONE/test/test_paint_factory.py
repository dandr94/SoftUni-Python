from project.factory.paint_factory import PaintFactory
import unittest


class PaintFactoryTests(unittest.TestCase):
    def setUp(self):
        self.factory = PaintFactory('Blob', 50)

    def test_init(self):
        factory = PaintFactory('Glob', 30)
        self.assertEqual(factory.name, 'Glob')
        self.assertEqual(factory.capacity, 30)
        ingredients = ["white", "yellow", "blue", "green", "red"]
        self.assertEqual(factory.valid_ingredients, ingredients)
        self.assertEqual(factory.ingredients, {})

    def test_add_method(self):
        result = self.factory.can_add(5)
        self.assertEqual(result, True)

    def test_add_valid_ingredient(self):
        self.factory.add_ingredient('blue', 5)
        self.assertEqual(self.factory.ingredients['blue'], 5)

    def test_add_ingredient_with_too_much_capacity(self):
        with self.assertRaises(Exception) as ex:
            self.factory.add_ingredient('white', 55)

        self.assertEqual(str(ex.exception), 'Not enough space in factory')

    def test_add_invalid_ingredient(self):
        product = 'banana'
        with self.assertRaises(Exception) as ex:
            self.factory.add_ingredient(product, 5)
        expected_result = f"Ingredient of type {product} not allowed in {self.factory.__class__.__name__}"
        self.assertEqual(str(ex.exception), expected_result)

    def test_remove_valid_ingredient(self):
        self.factory.add_ingredient('white', 5)
        self.factory.remove_ingredient('white', 3)
        self.assertEqual(self.factory.ingredients['white'], 2)

    def test_remove_ingredient_with_more_quantity(self):
        self.factory.add_ingredient('white', 5)
        with self.assertRaises(Exception) as ex:
            self.factory.remove_ingredient('white', 50)

        self.assertEqual(str(ex.exception), 'Ingredients quantity cannot be less than zero')

    def test_remove_non_existing_ingredient(self):
        with self.assertRaises(Exception) as ex:
            self.factory.remove_ingredient('white', 50)

        self.assertEqual(str(ex.exception), "'No such ingredient in the factory'")

    def test_return_ingredients(self):
        self.factory.add_ingredient('white', 5)
        result = self.factory.products
        self.assertEqual(result, {'white': 5})


if __name__ == '__main__':
    unittest.main()
