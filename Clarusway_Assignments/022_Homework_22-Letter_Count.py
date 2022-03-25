
"""
Task : Count the number of each letter in a sentence.

The department you work for undertook a project construction that makes word / text analysis. You are asked to calculate the number of letters or any chars in the sentences entered under this project.
Write a Python program that;
1-takes a sentence from the user,
2-counts the number of each letter/chars of the sentence,
3-collects the letters/chars as a key and the counted numbers as a value in a dictionary.
"""

# First Method:
sentence = input("Please enter a sentence: ")
my_dict = {}
for letter in sentence:
    if letter not in my_dict:
        my_dict[letter] = 1
    else:
        my_dict[letter] += 1
print(my_dict)

# Second Method
sentence = input("Please enter a sentence: ")
my_dict = {}
for letter in sentence:
    my_dict[letter] = my_dict.get(letter, 1)
print(my_dict)
