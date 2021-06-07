import unittest
import calculator


class testCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calculator.add(2, 5), 7)

    def test_subtract(self):
        self.assertEqual(calculator.subtract(5, 2), 3)

    def test_multiply(self):
        self.assertEqual(calculator.multiply(2, 5), 10)

    def test_divide(self):
        self.assertEqual(calculator.divide(10, 2), 5)


if __name__ == '__main__':

    unittest.main()
