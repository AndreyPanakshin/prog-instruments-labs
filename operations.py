class Operations:
    def calculate_average(self, numbers):
        if not numbers:
            return 0
        return sum(numbers) / len(numbers)

    def find_max(self, numbers):
        if not numbers:
            return None
        max_num = numbers[0]
        for num in numbers:
            if num > max_num:
                max_num = num
        return max_num

    def find_min(self, numbers):
        if not numbers:
            return None
        min_num = numbers[0]
        for num in numbers:
            if num < min_num:
                min_num = num
        return min_num

    def calculate_factorial(self, n):
        if n < 0:
            raise ValueError("Factorial is not defined for negative numbers!")
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result