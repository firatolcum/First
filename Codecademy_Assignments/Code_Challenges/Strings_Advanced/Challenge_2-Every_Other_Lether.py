"""
Challenge 2 : Every Other Letter

For this next function, we are going to create a function that extract every other letter from a string and returns the resulting string. There are a few different ways you can solve this problem Here are the steps needed for one of the ways:

1. Define the function to accept one parameter for the string
2. Create a new empty string to hold every other letter from the input string
3. Loop through the input string while incrementing by two every time
4. Inside the loop, append the character at the current location to the new string we initialized earlier
5. Return the new string
"""

# Solution 1:


def every_other_letter(word):
    every_other = ""
    for i in range(0, len(word), 2):
        every_other += word[i]
    return every_other

# Solution 2:


def every_other_letter(word):
    new_word = ""
    for i in range(len(word)):
        if i % 2 == 0:
            new_word += word[i]
    return new_word


print(every_other_letter("Codecademy"))
# should print Cdcdm
print(every_other_letter("Hello world!"))
# should print Hlowrd
