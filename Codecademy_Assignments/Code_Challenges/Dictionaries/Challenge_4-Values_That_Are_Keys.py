"""
Challenge 4 : Values That Are Keys

We are making a program that will create a family tree. Using a dictionary, we want to return a list of all the children who are also parents of other children. Using dictionaries we can consider those people to be values which are also keys in our dictionary of family data. Here is what we need to do:

1. Define the function to accept one parameter for our dictionary
2. Create an empty list to hold the values we find
3. Loop through every value in the dictionary
4. Inside the loop, test if the current value is a key in the dictionary. If it is then append it to the list of values we found
5. After the loop, return the list of values which are also keys
"""


def values_that_are_keys(my_dictionary):
    my_list = []
    for value in my_dictionary.values():
        if value in my_dictionary:
            my_list.append(value)
    return my_list


print(values_that_are_keys({1: 100, 2: 1, 3: 4, 4: 10}))
# should print [1, 4]
print(values_that_are_keys({"a": "apple", "b": "a", "c": 100}))
# should print ["a"]
