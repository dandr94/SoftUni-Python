from project.pet_shop import PetShop

from unittest import TestCase, main


class PetShopTests(TestCase):
    def setUp(self) -> None:
        self.pet_shop = PetShop('Foo')
        self.pet_shop.food['Bar'] = 5
        self.pet_shop.pets.append('Barz')

    def test_init_with_default_values(self):
        name = 'Boo'
        pet_shop = PetShop(name)
        self.assertEqual(name, pet_shop.name)
        self.assertEqual({}, pet_shop.food)
        self.assertEqual([], pet_shop.pets)

    def test_init_with_non_default_values(self):
        expected_name = 'Foo'
        expected_food = {'Bar': 5}
        expected_pets = ['Barz']
        self.assertEqual(expected_name, self.pet_shop.name)
        self.assertEqual(expected_food, self.pet_shop.food)
        self.assertEqual(expected_pets, self.pet_shop.pets)

    def test_add_food_method_with_wrong_quantity_should_raise_error(self):
        with self.assertRaises(ValueError) as ex:
            self.pet_shop.add_food('Rbk', -1)

        self.assertEqual('Quantity cannot be equal to or less than 0', str(ex.exception))

    def test_add_food_method_with_right_values_with_new_food(self):
        food_name = 'Rbk'
        quantity = 5

        result = self.pet_shop.add_food(food_name, quantity)
        expected_result = {'Bar': 5, 'Rbk': 5}
        self.assertEqual(expected_result, self.pet_shop.food)
        str_result = f"Successfully added {quantity:.2f} grams of {food_name}."
        self.assertEqual(result, str_result)

    def test_add_food_method_with_existing_food(self):
        food_name = 'Bar'
        quantity = 5
        result = self.pet_shop.add_food(food_name, quantity)
        expected_result = {'Bar': 10}
        self.assertEqual(expected_result, self.pet_shop.food)
        str_expected_result = f"Successfully added {quantity:.2f} grams of {food_name}."
        self.assertEqual(result, str_expected_result)

    def test_add_pet_method_with_right_values(self):
        name = 'Barki'
        result = self.pet_shop.add_pet(name)
        expected_result = ['Barz', 'Barki']
        self.assertEqual(expected_result, self.pet_shop.pets)
        str_expected_result = f"Successfully added {name}."
        self.assertEqual(str_expected_result, result)

    def test_add_pet_method_with_same_name_should_rise_error(self):
        name = 'Barz'
        with self.assertRaises(Exception) as ex:
            self.pet_shop.add_pet(name)

        self.assertEqual("Cannot add a pet with the same name", str(ex.exception))

    def test_feed_pet_method_with_invalid_pet_name(self):
        pet_name = 'Gorko'
        pet_food = 'Bar'
        expected_result = f"Please insert a valid pet name"
        with self.assertRaises(Exception) as ex:
            self.pet_shop.feed_pet(pet_food, pet_name)

        self.assertEqual(expected_result, str(ex.exception))

    def test_feed_pet_method_with_invalid_food_name(self):
        pet_name = 'Barz'
        food_name = 'Arggg'
        expected_result = f'You do not have {food_name}'
        result = self.pet_shop.feed_pet(food_name, pet_name)

        self.assertEqual(expected_result, result)

    def test_feed_pet_method_with_less_quantity_should_increase_food(self):
        pet_name = 'Barz'
        food_name = 'Bar'
        expected_str_result = "Adding food..."
        expected_value_result = {food_name: 1005}
        result = self.pet_shop.feed_pet(food_name, pet_name)
        self.assertEqual(expected_str_result, result)
        self.assertEqual(expected_value_result, self.pet_shop.food)

    def test_feed_pet_method_with_right_values(self):
        pet_name = 'Barz'
        food_name = 'Bar'
        self.pet_shop.food[food_name] += 1000
        result = self.pet_shop.feed_pet(food_name, pet_name)
        expected_str_result = f"{pet_name} was successfully fed"
        expected_value_result = {'Bar': 905}

        self.assertEqual(expected_value_result, self.pet_shop.food)
        self.assertEqual(expected_str_result, result)

    def test_repr_method(self):
        shop_name = 'Foo'
        self.pet_shop.pets.append('Roshko')
        expected_result = f'Shop {shop_name}:\n' \
                        f'Pets: Barz, Roshko'

        self.assertEqual(expected_result, str(self.pet_shop))
if __name__ == '__main__':
    main()
