import unittest
from calculator import add, subtract, multiply, divide, validate_input


class TestCalculator(unittest.TestCase):
    
    def test_add_positive_numbers(self):
        self.assertEqual(add(5, 3), 8)
        self.assertEqual(add(10, 20), 30)
    
    def test_add_negative_numbers(self):
        self.assertEqual(add(-5, -3), -8)
        self.assertEqual(add(-5, 3), -2)
        self.assertEqual(add(5, -3), 2)
    
    def test_add_floats(self):
        self.assertAlmostEqual(add(2.5, 3.5), 6.0)
        self.assertAlmostEqual(add(-1.5, 2.5), 1.0)
    
    def test_add_invalid_input(self):
        with self.assertRaises(TypeError):
            add("5", 3)
        with self.assertRaises(TypeError):
            add(5, "three")
    
    def test_subtract_positive_numbers(self):
        self.assertEqual(subtract(10, 3), 7)
        self.assertEqual(subtract(5, 5), 0)
    
    def test_subtract_negative_numbers(self):
        self.assertEqual(subtract(-5, -3), -2)
        self.assertEqual(subtract(5, -3), 8)
        self.assertEqual(subtract(-5, 3), -8)
    
    def test_subtract_floats(self):
        self.assertAlmostEqual(subtract(5.5, 2.5), 3.0)
    
    def test_subtract_invalid_input(self):
        with self.assertRaises(TypeError):
            subtract("10", 3)
    
    def test_multiply_positive_numbers(self):
        self.assertEqual(multiply(5, 3), 15)
        self.assertEqual(multiply(0, 100), 0)
    
    def test_multiply_negative_numbers(self):
        self.assertEqual(multiply(-5, 3), -15)
        self.assertEqual(multiply(-5, -3), 15)
    
    def test_multiply_floats(self):
        self.assertAlmostEqual(multiply(2.5, 4), 10.0)
    
    def test_multiply_invalid_input(self):
        with self.assertRaises(TypeError):
            multiply(5, "three")
    
    def test_divide_positive_numbers(self):
        self.assertEqual(divide(10, 2), 5.0)
        self.assertAlmostEqual(divide(7, 2), 3.5)
    
    def test_divide_negative_numbers(self):
        self.assertEqual(divide(-10, 2), -5.0)
        self.assertEqual(divide(10, -2), -5.0)
        self.assertEqual(divide(-10, -2), 5.0)
    
    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            divide(10, 0)
        with self.assertRaises(ZeroDivisionError):
            divide(0, 0)
    
    def test_divide_floats(self):
        self.assertAlmostEqual(divide(5.0, 2.0), 2.5)
    
    def test_divide_invalid_input(self):
        with self.assertRaises(TypeError):
            divide("10", 2)
    
    def test_validate_input_integer(self):
        self.assertEqual(validate_input("42"), 42)
        self.assertEqual(validate_input("0"), 0)
        self.assertEqual(validate_input("-10"), -10)
    
    def test_validate_input_float(self):
        self.assertEqual(validate_input("3.14"), 3.14)
        self.assertEqual(validate_input("-2.5"), -2.5)
    
    def test_validate_input_invalid(self):
        with self.assertRaises(ValueError):
            validate_input("abc")
        with self.assertRaises(ValueError):
            validate_input("12a34")


if __name__ == "__main__":
    unittest.main()
