"""
Challenge-1 : First Three Multiples
Let’s start by creating a function which both prints and returns values. For this function, we are going to print out the first three multiples of a number and return the third multiple. This means that we are going to print 1, 2, and 3 times the input number and then return the value of 3 times the input number. For this, we are going to need a few steps:

1-Define the function header to accept one input parameter called num
2-Print out 1 times num
3-Print out 2 times num
4-Print out 3 times num
5-Return the value of 3 times num
"""


def first_three_multiples(num):
    print(num * 1)
    print(num * 2)
    print(num * 3)
    return num * 3


first_three_multiples(10)
