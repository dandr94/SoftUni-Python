from project.cat import Cat
import unittest


class CatTests(unittest.TestCase):
    def test_if_cat_size_is_increased_after_eating(self):
        cat = Cat('Tom')
        self.assertEqual(cat.size, 0)

        cat.eat()
        self.assertEqual(cat.size, 1)

    def test_if_boolean_is_true_after_feed_method(self):
        cat = Cat('Tom')
        self.assertFalse(cat.fed)

        cat.eat()
        self.assertTrue(cat.fed)

    def test_if_cat_is_already_fed_raise_error(self):
        cat = Cat('Tom')
        self.assertFalse(cat.fed)
        cat.eat()
        self.assertTrue(cat.fed)

        with self.assertRaises(Exception) as ex:
            cat.eat()

        self.assertEqual(str(ex.exception), 'Already fed.')

    def test_if_cat_cannot_fall_asleep_if_not_fed(self):
        cat = Cat('Tom')
        self.assertFalse(cat.fed)
        self.assertFalse(cat.sleepy)

        with self.assertRaises(Exception) as ex:
            cat.sleep()

        self.assertEqual(str(ex.exception), 'Cannot sleep while hungry')

    def test_if_cat_is_not_sleepy_after_sleeping(self):
        cat = Cat('Tom')
        cat.eat()
        self.assertTrue(cat.sleepy)
        cat.sleep()
        self.assertFalse(cat.sleepy)


if __name__ == '__main__':
    unittest.main()
