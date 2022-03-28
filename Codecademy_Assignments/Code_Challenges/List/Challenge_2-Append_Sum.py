"""
Challenge-2 : Append Sum
Let’s create a function that calculates the sum of the last two elements of a list and appends it to the end. After doing so, it will repeat this process two more times and return the resulting list. You can choose to use a loop or manually use three lines. Here are the steps we need:

1-Define the function to accept one parameter for our list of numbers
2-Add the last and second to last elements from our list together
3-Append the calculated value to the end of our list.
4-Repeat steps 2 and 3 two more times
5-Return the modified list
"""


def append_sum(lst):
    count = 0
    while count < 3:
        lst.append(lst[-1] + lst[-2])
        count += 1
    return lst


print(append_sum([1, 1, 2]))
