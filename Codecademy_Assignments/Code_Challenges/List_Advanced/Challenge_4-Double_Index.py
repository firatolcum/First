"""
Challenge-4 : Double Index
Our next function will double a value at a given position. We will provide a list and an index to double. This will create a new list by replacing the value at the index provided with double the original value. If the index is invalid then we should return the original list. Here is what we need to do:

1-efine the function to accept two parameters, one for the list and another for the index of the value we are going to double
2-Test if the index is invalid. If its invalid then return the original list
3-If the list is valid then get all values up to the index and store it as a new list
4-Append the value at the index times 2 to the new list
5-Add the rest of the list from the index onto the new list
6-Return the new list
"""


def double_index(lst, index):
    if index + 1 > len(lst):
        return lst
    else:
        new_list = lst[:index]
        new_list.append(lst[index] * 2)
    return new_list + lst[index + 1:]


print(double_index([3, 8, -10, 12], 2))
