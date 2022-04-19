"""
Challenge 3- Reverse

This one is similar to the last challenge. Instead of selecting every other letter, we want to reverse the entire string. This can be performed in a similar manner, but we will need to modify the range we are using. Here is what we need to do:

1. Define the function to accept one parameter for the string
2. Create a new empty string to hold the reversed string
3. Loop through the input string by starting at the end, and working towards the beginning
4. Inside the loop, append the character at the current location to the new string we initialized earlier
5. Return the result
"""


def reverse_string(word):
    new_word = ""
    for i in range((len(word)-1), -1, -1):
        new_word += word[i]
    return new_word


print(reverse_string("Codecademy"))
# should print ymedacedoC
print(reverse_string("Hello world!"))
# should print !dlrow olleH
