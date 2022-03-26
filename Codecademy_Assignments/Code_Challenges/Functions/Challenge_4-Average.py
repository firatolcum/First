"""
Challenge-4 : Average
Let’s create a function which takes the average of two numbers. These two numbers will be the input of the function and the output will be the average of the two. In order to do this, we need to do a few steps:

1-Define the function with two input parameters, num1 and num2
2-Calculate the sum of the two numbers
3-Divide the sum by the number of inputs to the function
4-Return the answer
"""


def average(num1, num2):
    return (num1 + num2) / 2


print(average(1, 100))  # 50.5
