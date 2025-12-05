from calculator import Calculator
from operations import StatisticsOperations, MathOperations, Operations

def main():
    # Теперь не нужно создавать экземпляры классов
    
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
    
    # Обработка ошибок
    print("\nError Handling:")
    try:
        print(f"10 / 0 = {Calculator.divide(10, 0)}")
    except ValueError as e:
        print(f"Error: {e}")
    
    try:
        print(f"sqrt(-1) = {Calculator.sqrt(-1)}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
