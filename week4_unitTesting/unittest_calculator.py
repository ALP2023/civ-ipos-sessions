''' Write simple calc Class with + - * /'''

import unittest
from calculator import Calculator

# Pascal naming convention for class
class TestCalculator(unittest.TestCase):

    # universal condition  calculator = Calculator is independent
    def setUp(self):
        self.calculator = Calculator()

  #  camel case for methods as per C#
    def test_sum_positive_ints(self):
        self.assertEqual(self.calculator.add(3, 4), 7)
    def test_sum_positive_floats(self):
        self.assertEqual(self.calculator.add(3.5, 4.5), 8)
    def test_sum_one_negative_ints(self):
        self.assertEqual(self.calculator.add(3, -4), -1)
    def test_sum_two_negative_ints(self):
        self.assertEqual(self.calculator.add(-3, -4), -7)
    def test_sum_int_to_string_throws_exception(self):
        with self.assertRaises(TypeError):
            self.calculator.add(3, "abc")
    def test_multiply_two_negative_ints(self):
        self.assertEqual(self.calculator.multiply(-3, -4), 12)

    def test_multiply_int_to_string_throws_exception(self):
        with self.assertRaises(TypeError):
            self.calculator.multiply(3, "abc")