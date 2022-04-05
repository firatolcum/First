"""
Define a function that returns the factorial of the number written and find the result of 8 factorials.
Note : take into account the case of entering a zero value in the function.
"""
#  Soultion 1 - for loop


def factorial_func(x):
    result = 1
    for i in range(1, x + 1):
        if x == 0:
            result = 1
        else:
            result = result * i
    return result


print(factorial_func(8))  # 40320

#  Solution 2 - recursive


def factorial_func(x):
    result = 1
    if x == 0:
        return result
    else:
        return x * factorial_func(x - 1)


print(factorial_func(5))
