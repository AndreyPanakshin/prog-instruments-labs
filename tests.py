import unittest
from calculator import Calculator
from operations import Operations

class TestCalculator(unittest.TestCase):
    # Убираем setUp, так как теперь используем статические методы
    
    def test_add(self):
        self.assertEqual(Calculator.add(2, 3), 5)
        self.assertEqual(Calculator.add(-1, 1), 0)
    
    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            Calculator.divide(10, 0)
    
    def test_average(self):
        self.assertEqual(Operations.calculate_average([1, 2, 3]), 2)
        self.assertEqual(Operations.calculate_average([]), 0)

if __name__ == "__main__":
    unittest.main()
