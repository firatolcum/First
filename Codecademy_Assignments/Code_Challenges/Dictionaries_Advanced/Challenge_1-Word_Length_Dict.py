"""
Challenge 1 : Word Length Dict

Let’s start by writing a function that creates a new dictionary based on a list of strings. The keys of our dictionary will be every string in our list of strings, while the values will be the length of each of the words in the string list. Here are the steps:

1. Define the function to accept one parameter for our list of strings
2. Create a new empty dictionary
3. Loop through every string in the list of strings
4. Inside the loop, add the string as a key and the length of the string as the value to the dictionary
5. After the loop, return the new dictionary
"""


def word_length_dictionary(words):
    my_dict = {}
    for item in words:
        my_dict[item] = len(item)
    return my_dict


print(word_length_dictionary(["apple", "dog", "cat"]))
# should print {"apple":5, "dog": 3, "cat":3}
print(word_length_dictionary(["a", ""]))
# should print {"a": 1, "": 0}
