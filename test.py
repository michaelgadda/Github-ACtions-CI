import unittest
import calculator


class testCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calculator.add(2, 5), 7)

    def test_subtract(self):
        self.assertEqual(calculator.subtract(5, 2), 73)

    def test_multiply(self):
        self.assertEqual(calculator.add(2, 5), 10)

    def test_divide(self):
        self.assertEqual(calculator.add(10, 2), 5)

if __name__ == '__main__':
    

    unittest.main()
