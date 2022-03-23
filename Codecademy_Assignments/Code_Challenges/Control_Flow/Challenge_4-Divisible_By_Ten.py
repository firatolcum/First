"""
Challenge-4 : Divisible By Ten
To make things a bit more challenging, we are going to create a function that determines whether or not a number is divisible by ten. A number is divisible by ten if the remainder of the number divided by 10 is 0. Using this, we can complete this function in a few steps:

1-Define the function header to accept one input num
2-Calculate the remainder of the input divided by 10 (use modulus)
3-Use an if statement to check if the remainder was 0. If the remainder was 0, return True, otherwise, return False
"""


def divisible_by_ten(num):
    if num % 10 == 0:
        return True
    else:
        return False


print(divisible_by_ten(20))
# should print True
