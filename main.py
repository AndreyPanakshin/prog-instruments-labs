from calculator import Calculator
from operations import Operations


def main():
    calc = Calculator()
    ops = Operations()

    # Демонстрация работы калькулятора
    print("Calculator Demo:")
    print(f"5 + 3 = {calc.add(5, 3)}")
    print(f"10 - 4 = {calc.subtract(10, 4)}")
    print(f"6 * 7 = {calc.multiply(6, 7)}")
    print(f"15 / 3 = {calc.divide(15, 3)}")
    print(f"2 ^ 8 = {calc.power(2, 8)}")
    print(f"sqrt(25) = {calc.sqrt(25)}")

    print("\nOperations Demo:")
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(f"Average of {numbers} = {ops.calculate_average(numbers)}")
    print(f"Max of {numbers} = {ops.find_max(numbers)}")
    print(f"Min of {numbers} = {ops.find_min(numbers)}")
    print(f"Factorial of 5 = {ops.calculate_factorial(5)}")

    # Обработка ошибок
    print("\nError Handling:")
    try:
        print(f"10 / 0 = {calc.divide(10, 0)}")
    except ValueError as e:
        print(f"Error: {e}")

    try:
        print(f"sqrt(-1) = {calc.sqrt(-1)}")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()