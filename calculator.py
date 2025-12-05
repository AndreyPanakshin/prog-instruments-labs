from typing import Union

Number = Union[int, float]


class Calculator:
    
    @staticmethod
    def add(a: Number, b: Number) -> Number:
        return a + b
    
    @staticmethod
    def subtract(a: Number, b: Number) -> Number:
        return a - b
    
    @staticmethod
    def multiply(a: Number, b: Number) -> Number:
        return a * b
    
    @staticmethod
    def divide(a: Number, b: Number) -> float:
        if b == 0:
            raise ValueError("Cannot divide by zero!")
        return a / b
    
    @staticmethod
    def power(a: Number, b: Number) -> Number:
        return a ** b
    
    @staticmethod
    def sqrt(a: Number) -> float:
        if a < 0:
            raise ValueError("Cannot calculate square root of negative number!")
        return a ** 0.5
