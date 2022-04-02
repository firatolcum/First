"""
Challenge-5 : Exponents
In this challenge, we will be using nested loops in order to raise a list of numbers to the power of a list of other numbers. What this means is that for every number in the first list, we will raise that number to the power of every number in the second list. If you provide the first list with 2 elements and the second list with 3 numbers, then there will be 6 final answers. Let’s look at the steps we need:

1-Define the function to accept two lists of numbers, bases and powers
2-Create a new list that will contain our answers
3-Create a loop that iterates through every base in bases
4-Within that loop, create another loop that iterates through every power in power
5-Within that nested loop, append the result of the current base raised to the current power.
6-After all iterations of both loops are complete, return the list of answers
"""


def exponents(bases, powers):
    new_list = []
    for base in bases:
        for power in powers:
            new_list.append(base**power)
    return new_list


print(exponents([2, 3, 4], [1, 2, 3]))
