
def factorial(n):
    result = 1
    if n not in [0, 1]:
        for i in range(2, n + 1):
            result *= i

    return result