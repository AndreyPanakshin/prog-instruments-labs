import unittest
from calculator import Calculator
from operations import Operations

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()
        self.ops = Operations()  # Используем совместимый класс
    
    def test_add(self):
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
    
    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            self.calc.divide(10, 0)
    
    def test_average(self):
        self.assertEqual(self.ops.calculate_average([1, 2, 3]), 2)
        self.assertEqual(self.ops.calculate_average([]), 0)

if __name__ == "__main__":
    unittest.main()
