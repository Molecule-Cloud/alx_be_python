import unittest
from simple_calculator import SimpleCalculator


class TestSimpleCalculator(unitest.TestCase):
    def setUp(self):
        self.calc = SimpleCalculator()

    def test_addition(self):
        self.assertEqual(self.calc.add(5, 3), 8)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(-1, -1), -2)

    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(10, 4), 6)
        self.assertEqual(self.calc.subtract(-1, -1), 0)
        self.assertEqual(self.calc.subtract(-1, 1), -2)

    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(7, 6), 42)
        self.assertEqual(self.calc.multiply(-1, 1), -1)
        self.assertEqual(self.calc.multiply(-2, -3), 6)

    def test_division(self):
        self.assertEqual(self.calc.divide(8, 2), 4)
        self.assertEqual(self.calc.divide(5, 0), None)
        self.assertEqual(self.calc.divide(-6, -2), 3)