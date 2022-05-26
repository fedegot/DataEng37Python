from simple_calc import SimpleCalc
from unittest import TestCase

class CalcTest(TestCase):
    calc = SimpleCalc()

    def test_add(self):
        actual = self.calc.add(2, 4)
        expected = 6
        self.assertEqual(actual, expected)

    def test_subtract(self):
        actual = self.calc.subtract(6, 3)
        expected = 3
        self.assertEqual(actual, expected)

    def test_multiply(self):
        actual  = self.calc.mult(2, 3)
        expected = 6
        self.assertEqual(actual, expected)

    def test_division(self):
        actual = self.calc.div(6, 2)
        expected = 3
        self.assertEqual(actual, expected)
