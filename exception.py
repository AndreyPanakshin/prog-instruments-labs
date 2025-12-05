class CalculatorError(Exception):
    pass


class DivisionByZeroError(CalculatorError):

    def __init__(self, message: str = "Cannot divide by zero!"):
        super().__init__(message)


class NegativeSquareRootError(CalculatorError):

    def __init__(self, message: str = "Cannot calculate square root of negative number!"):
        super().__init__(message)


class NegativeFactorialError(CalculatorError):

    def __init__(self, message: str = "Factorial is not defined for negative numbers!"):
        super().__init__(message)


class EmptyListError(CalculatorError):

    def __init__(self, operation: str):
        super().__init__(f"Cannot perform {operation} on empty list!")