import unittest
from calculator import Calculator
from operations import Operations
from exceptions import DivisionByZeroError, NegativeFactorialError, EmptyListError

class TestCalculator(unittest.TestCase):
    
    def test_add(self):
        self.assertEqual(Calculator.add(2, 3), 5)
        self.assertEqual(Calculator.add(-1, 1), 0)
    
    def test_divide_by_zero(self):
        with self.assertRaises(DivisionByZeroError):
            Calculator.divide(10, 0)
    
    def test_average(self):
        self.assertEqual(Operations.calculate_average([1, 2, 3]), 2)
        self.assertEqual(Operations.calculate_average([]), 0)
    
    # Добавляем новые тесты для проверки новых исключений
    def test_negative_factorial(self):
        with self.assertRaises(NegativeFactorialError):
            Operations.calculate_factorial(-5)
    
    def test_empty_list_operations(self):
        # Operations класс должен обрабатывать пустые списки
        self.assertEqual(Operations.calculate_average([]), 0)
        self.assertIsNone(Operations.find_max([]))
        self.assertIsNone(Operations.find_min([]))
        
        # Но оригинальные классы должны выбрасывать исключения
        with self.assertRaises(EmptyListError):
            from operations import StatisticsOperations
            StatisticsOperations.calculate_average([])

if __name__ == "__main__":
    unittest.main()
