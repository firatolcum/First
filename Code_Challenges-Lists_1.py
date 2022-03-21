"""
Challenge-1 : Append Size
For the first code challenge, we are going to calculate the length of a list and then append the value to the end of the list. Here is what we need to do:

Define the function to accept one parameter for our list
Get the length of the list
Append the length of the list to the end of the list
Return the modified list
"""


def append_size(lst):
    length = len(lst)
    lst.append(length)
    return lst


print(append_size([23, 42, 108]))
