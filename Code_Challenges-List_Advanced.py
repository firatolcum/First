"""
Challenge-1 : Every Three Numbers
Let’s start our challenging problems with a function that creates a list of numbers up to 100 in increments of 3 starting from a number that is passed to the function as an input parameter. Here is what we need to do:

1-Define the function to accept one parameter for our starting number
2-Calculate the numbers between the starting number and 100 while incrementing by 3
3-Store the numbers in a list
4-Return the list
"""


def every_three_nums(start):
    number_list = []
    if start > 100:
        return []
    else:
        for number in range(start, 101, 3):
            number_list.append(number)
        return number_list


print(every_three_nums(101))

"""
Code Challenge-2 : Remove Middle
Our next function will remove all elements from a list with an index within a certain range. The function will accept a list, a starting index, and an ending index. All elements with an index between the starting and ending index should be removed from the list. Here are the steps:

1-Define the function to accept three parameters: the list, the starting index, and the ending index
2-Get all elements before the starting index
3-Get all elements after the ending index
4-Combine the two partial lists into the result
5-Return the result
"""


def remove_middle(lst, start, end):
    return lst[:start] + lst[end + 1:]


print(remove_middle([4, 8, 15, 16, 23, 42], 1, 3))
