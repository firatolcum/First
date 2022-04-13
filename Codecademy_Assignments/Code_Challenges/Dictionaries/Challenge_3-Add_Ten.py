"""
Challenge 3 : Add Ten

Let’s loop through the keys again, but this time let’s modify the values within the dictionary. Our function should add 10 to every value in the dictionary and return the modified dictionary. Here is what we need to do:

1. Define the function to accept one parameter for our dictionary
2. Loop through every key in the dictionary
3. Retrieve the value using the key and add 10 to it. Make sure to re-save the new value to the original key.
4. After the loop, return the modified dictionary
"""


def add_ten(my_dictionary):
    for key in my_dictionary:
        my_dictionary[key] += 10
    return my_dictionary


print(add_ten({1: 5, 2: 2, 3: 3}))
# should print {1:15, 2:12, 3:13}
print(add_ten({10: 1, 100: 2, 1000: 3}))
# should print {10:11, 100:12, 1000:13}
