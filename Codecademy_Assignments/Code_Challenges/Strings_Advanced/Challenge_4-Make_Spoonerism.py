"""
Challenge 4 : Make Spoonerism

A Spoonerism is an error in speech when the first syllables of two words are switched. For example, a Spoonerism is made when someone says “Belly Jeans” instead of “Jelly Beans”. We are going to make a function that is similar, but instead of using the first syllable, we are going to switch the first character of two words. Here is what we need to do:

1. Define the function to accept two parameters for our two words
2. Get the first character of the first word and the first character of the second word
3. Get the remaining characters of the first word and the remaining characters of the second word.
4. Append the first character of the second word to the remaining character of the first word
5. Append a space character
6. Append the first character of the first word to the remaining characters of the second word.
7. Return the result
"""

# Solution 1:


def make_spoonerism(word1, word2):
    new_word1 = word1.replace(word1[0], word2[0])
    new_word2 = word2.replace(word2[0], word1[0])
    return new_word1 + " " + new_word2


print(make_spoonerism("Hello", "world!"))
# should print wello Horld!
print(make_spoonerism("Codecademy", "Learn"))
# should print Lodecademy Cearn

# Solution 2:


def make_spoonerism(word1, word2):
    return word2[0] + word1[1:] + " " + word1[0] + word2[1:]
