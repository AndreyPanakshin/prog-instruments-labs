from calculator import Calculator
from operations import StatisticsOperations, MathOperations, Operations
from exceptions import CalculatorError

def main():
    # Демонстрация работы калькулятора
    print("Calculator Demo:")
    print(f"5 + 3 = {Calculator.add(5, 3)}")
    print(f"10 - 4 = {Calculator.subtract(10, 4)}")
    print(f"6 * 7 = {Calculator.multiply(6, 7)}")
    print(f"15 / 3 = {Calculator.divide(15, 3)}")
    print(f"2 ^ 8 = {Calculator.power(2, 8)}")
    print(f"sqrt(25) = {Calculator.sqrt(25)}")
    
    print("\nOperations Demo:")
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(f"Average of {numbers} = {StatisticsOperations.calculate_average(numbers)}")
    print(f"Max of {numbers} = {StatisticsOperations.find_max(numbers)}")
    print(f"Min of {numbers} = {StatisticsOperations.find_min(numbers)}")
    print(f"Factorial of 5 = {MathOperations.calculate_factorial(5)}")
    
    # Проверка обратной совместимости
    print(f"\nBackward compatibility - Average: {Operations.calculate_average(numbers)}")
    print(f"Backward compatibility - Factorial of 5: {Operations.calculate_factorial(5)}")
    print(f"Backward compatibility - Average of empty list: {Operations.calculate_average([])}")
    
    # Обработка ошибок с унифицированными исключениями
    print("\nError Handling (unified exceptions):")
    
    test_cases = [
        (Calculator.divide, (10, 0), "Division by zero"),
        (Calculator.sqrt, (-1,), "Square root of negative"),
        (MathOperations.calculate_factorial, (-5,), "Negative factorial"),
        (StatisticsOperations.calculate_average, ([],), "Average of empty list"),
        (StatisticsOperations.find_max, ([],), "Max of empty list"),
    ]
    
    for func, args, description in test_cases:
        try:
            result = func(*args)
            print(f"{description}: {result}")
        except CalculatorError as e:
            print(f"{description}: {type(e).__name__} - {e}")
        except Exception as e:
            print(f"{description}: Unexpected error - {type(e).__name__}: {e}")

if __name__ == "__main__":
    main()
