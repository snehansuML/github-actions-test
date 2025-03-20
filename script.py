def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

number = 5  # Change this number to calculate a different factorial
result = factorial(number)

print(f"✅ Factorial of {number} is {result}")
