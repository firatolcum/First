"""
Challenge 1 : Sum Values

For the first code challenge, we are going to look at only the values in a dictionary. This function should sum up all of the values from the key-value pairs in the dictionary. Here are the steps we need:

1. Define the function to accept one parameter for our dictionary
2. Create a variable to keep track of our sum
3. Loop through every value in the dictionary
4. Inside the loop, add each value to the sum
5. Return the sum
"""


def sum_values(my_dictionary):
    sum_value = 0
    for value in my_dictionary.values():
        sum_value += value
    return sum_value


print(sum_values({"milk": 5, "eggs": 2, "flour": 3}))
# should print 10
print(sum_values({10: 1, 100: 2, 1000: 3}))
# should print 6
