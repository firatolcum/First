"""
Challenge 3 : Unique Values

Now let’s try reading a dictionary as input and finding how many values are unique. The function should return a number which is the count of all values from the dictionary without including duplicates. These are the steps:

1. Define the function to accept one parameter for our dictionary
2. Create a new empty list
3. Loop through every value in our dictionary
4. Inside the loop, if the value is not already in our list, append the value to our list
5. After the loop, return the length of our list
"""

# Solution 1 :


def unique_values(my_dictionary):
    my_dict = {}
    for key, value in my_dictionary.items():
        if value not in my_dict.values():
            my_dict[key] = value
    return len(my_dict)


print(unique_values({0: 3, 1: 1, 4: 1, 5: 3}))
# should print 2
print(unique_values({0: 3, 1: 3, 4: 3, 5: 3}))
# should print 1

# Solution 2 :


def unique_values(my_dictionary):
    seen_values = []
    for value in my_dictionary.values():
        if value not in seen_values:
            seen_values.append(value)
    return len(seen_values)
