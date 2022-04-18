"""
Challenge 1 : Check Name

You are creating an app that allows users to interact and share their coding project ideas online. The first step is to provide your name in the application and a greeting for other people to see which contains your name. Let’s create a function that is able to check if a user’s name is located within their greeting. We need a function that accepts two parameters, a string for our sentence and a string for a name. The function should return True if the name exists within the string (ignoring any differences in capitalization). Here is what we need to do:

1. Define the function to accept two parameters, one string for the sentence and one string for the name
2. Convert all of the strings to the same case so we don’t have to worry about differences in capitalization
3. Check if the name is within the sentence. If so, then return True. Otherwise, return False
"""


def check_for_name(sentence, name):
    sentence = sentence.lower()
    name = name.lower()
    if name in sentence:
        return True
    return False


print(check_for_name("My name is Jamie", "Jamie"))
# should print True
print(check_for_name("My name is jamie", "Jamie"))
# should print True
print(check_for_name("My name is Samantha", "Jamie"))
# should print False
