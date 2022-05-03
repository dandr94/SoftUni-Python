from project.worker import Worker
import unittest


class WorkerTests(unittest.TestCase):

    def test_if_worker_is_properly_initialized(self):
        w = Worker('John', 5000, 200)
        self.assertEqual(w.name, 'John')
        self.assertEqual(w.salary, 5000)
        self.assertEqual(w.energy, 200)

    def test_worker_energy_properly_incremented_after_rest(self):
        w = Worker('John', 5000, 200)
        self.assertEqual(w.energy, 200)
        w.rest()
        self.assertEqual(w.energy, 201)

    def test_worker_error_if_energy_is_below_or_equal_to_zero(self):
        w = Worker('John', 5000, 0)

        with self.assertRaises(Exception) as ex:
            w.work()

        self.assertEqual(str(ex.exception), 'Not enough energy.')

    def test_if_worker_money_is_increase_after_working(self):
        w = Worker('John', 5000, 100)
        self.assertEqual(w.money, 0)

        w.work()
        self.assertEqual(w.money, 5000)

    def test_if_worker_energy_is_decreased_after_working(self):
        w = Worker('John', 5000, 100)
        self.assertEqual(w.energy, 100)

        w.work()
        self.assertEqual(w.energy, 99)

    def test_get_info_method(self):
        w = Worker('John', 5000, 100)

        result = w.get_info()
        expected_result = 'John has saved 0 money.'

        self.assertEqual(result, expected_result)


if __name__ == "__main__":
    unittest.main()
