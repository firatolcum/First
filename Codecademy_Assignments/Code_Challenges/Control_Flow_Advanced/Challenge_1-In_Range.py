

"""
Challenge-1 : In Range
Let’s start the advanced challenge problems by testing if a number falls within a certain range. We will accept three parameters where the first parameter is the number we are testing, the second parameter is the lower bound and the third parameter is the upper bound of our range. These are the steps required:

1-Define the function to accept three numbers as parameters
2-Test if the number is greater than or equal to the lower bound and less than or equal to the upper bound
3-If this is true, return True, otherwise, return False
"""


def in_range(num, lower, upper):
    if lower <= num <= upper:
        return True
    else:
        return False


print(in_range(10, 10, 10))
# should print True
print(in_range(5, 10, 20))
# should print False
