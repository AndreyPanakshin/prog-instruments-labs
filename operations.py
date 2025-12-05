from typing import List, Optional, Union
from exceptions import NegativeFactorialError, EmptyListError

Number = Union[int, float]


class StatisticsOperations:
    
    @staticmethod
    def calculate_average(numbers: List[Number]) -> float:
        if not numbers:
            raise EmptyListError("average calculation")
        return sum(numbers) / len(numbers)
    
    @staticmethod
    def find_max(numbers: List[Number]) -> Number:
        if not numbers:
            raise EmptyListError("maximum finding")
        max_num = numbers[0]
        for num in numbers:
            if num > max_num:
                max_num = num
        return max_num
    
    @staticmethod
    def find_min(numbers: List[Number]) -> Number:
        if not numbers:
            raise EmptyListError("minimum finding")
        min_num = numbers[0]
        for num in numbers:
            if num < min_num:
                min_num = num
        return min_num


class MathOperations:

    @staticmethod
    def calculate_factorial(n: int) -> int:
        if n < 0:
            raise NegativeFactorialError()
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result


# Сохраняем старый класс для обратной совместимости
class Operations:
    
    @staticmethod
    def calculate_average(numbers: List[Number]) -> float:
        try:
            return StatisticsOperations.calculate_average(numbers)
        except EmptyListError:
            return 0.0
    
    @staticmethod
    def find_max(numbers: List[Number]) -> Optional[Number]:
        try:
            return StatisticsOperations.find_max(numbers)
        except EmptyListError:
            return None
    
    @staticmethod
    def find_min(numbers: List[Number]) -> Optional[Number]:
        try:
            return StatisticsOperations.find_min(numbers)
        except EmptyListError:
            return None
    
    @staticmethod
    def calculate_factorial(n: int) -> int:
        return MathOperations.calculate_factorial(n)
