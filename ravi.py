def factorial_iterative(n):
    if n < 0:
        return "Factorial does not exist for negative numbers"
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

number = 5
print(f"Factorial of {number} is {factorial_iterative(number)}")
