"""
Challenge 2 : Frequency Count

This next function is similar, but instead of counting the length of each string in the list of strings, we will be counting the frequency of each string. This function will also accept a list of strings as input and return a new dictionary. Here is what we need to do:

1. Define the function to accept one parameter for our list of strings
2. Create a new empty dictionary
3. Loop through every string in the list of strings
4. Inside the loop, if the string is not already in our dictionary, store the string as a key with a value of 0 in our dictionary. Then, increment the value by 1.
5. After the loop, return the new dictionary
"""


def frequency_dictionary(words):
    my_dict = {}
    count = 1
    for item in words:
        if item not in my_dict:
            my_dict[item] = count
        else:
            my_dict[item] += 1
    return my_dict


print(frequency_dictionary(["apple", "apple", "cat", 1]))
# should print {"apple":2, "cat":1, 1:1}
print(frequency_dictionary([0, 0, 0, 0, 0]))
# should print {0:5}
