"""
Challenge-5 : Combine Sort
Finally, let’s create a function that combines two different lists together and then sorts them. To do this we can combine the lists with an operation and then sort using a function call. Here are the steps we need to use:

1-Define the function to accept two parameters, one for each list.
2-Combine the two lists together
3-Sort the result
4-Return the sorted and combined list
"""


def combine_sort(lst1, lst2):
    combine = lst1 + lst2
    combine.sort()
    return combine


print(combine_sort([4, 10, 2, 5], [-10, 2, 5, 10]))
