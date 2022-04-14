"""
Challenge 5 : Largest Value

For the last challenge, we are going to create a function that is able to find the maximum value in the dictionary and return the associated key. This is a twist on the max algorithm since it is using a dictionary rather than a list. These are the steps:

1. Define the function to accept one parameter for our dictionary
2. Initialize the starting key to a very low number
3. Initialize the starting value to a very low number
4. Iterate through the dictionary’s key/value pairs.
5. Inside the loop, if the current value is larger than the current largest value, replace the largest key and largest value with the current ones you are looking at
6. Once you are done iterating through all key/value pairs, return the key which has the largest value
"""
# Solution 1


def max_key(my_dictionary):
    max_value = 0
    for key, value in my_dictionary.items():
        if value > max_value:
            max_value = value
    for key in my_dictionary:
        if my_dictionary[key] == max_value:
            return key


print(max_key({1: 100, 2: 1, 3: 4, 4: 10}))
# should print 1
print(max_key({"a": 100, "b": 10, "c": 1000}))
# should print "c"


# Solution 2
def max_key(my_dictionary):
    # float values can be used to represent an infinite integer.
    largest_key = float("-inf")
    # One can use float('inf') as an integer to represent it as infinity.
    largest_value = float("-inf")
    for key, value in my_dictionary.items():
        if value > largest_value:
            largest_value = value
            largest_key = key
    return largest_key
