from typing import List, Optional, Union

Number = Union[int, float]


class StatisticsOperations:
    
    @staticmethod
    def calculate_average(numbers: List[Number]) -> float:
        if not numbers:
            return 0.0
        return sum(numbers) / len(numbers)
    
    @staticmethod
    def find_max(numbers: List[Number]) -> Optional[Number]:
        if not numbers:
            return None
        max_num = numbers[0]
        for num in numbers:
            if num > max_num:
                max_num = num
        return max_num
    
    @staticmethod
    def find_min(numbers: List[Number]) -> Optional[Number]:
        if not numbers:
            return None
        min_num = numbers[0]
        for num in numbers:
            if num < min_num:
                min_num = num
        return min_num


class MathOperations:
    
    @staticmethod
    def calculate_factorial(n: int) -> int:
        if n < 0:
            raise ValueError("Factorial is not defined for negative numbers!")
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result


# Сохраняем старый класс для обратной совместимости
class Operations:
    @staticmethod
    def calculate_average(numbers: List[Number]) -> float:
        return StatisticsOperations.calculate_average(numbers)
    
    @staticmethod
    def find_max(numbers: List[Number]) -> Optional[Number]:
        return StatisticsOperations.find_max(numbers)
    
    @staticmethod
    def find_min(numbers: List[Number]) -> Optional[Number]:
        return StatisticsOperations.find_min(numbers)
    
    @staticmethod
    def calculate_factorial(n: int) -> int:
        return MathOperations.calculate_factorial(n)
