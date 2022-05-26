from simple_calc import SimpleCalc
from unittest import TestCase

class CalcTest(TestCase):
    calc = SimpleCalc()

    def test_add(self):
        actual = self.calc.add(2, 4)
        expected = 6
        self.assertEqual(actual, expected)