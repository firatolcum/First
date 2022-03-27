"""
Challenge 3 : Bond, James Bond
It’s time to re-create a famous movie scene through code. Our function is going to concatenate strings together in order to replace James Bond’s name with whatever name we want. The input to our function will be two strings, one for a first name and another for a last name. The function will return a string consisting of the famous phrase but replaced with our inputs. To accomplish this, we need to:

1-Define the function to accept two parameters, first_name and last_name
2-Concatenate the string ', ' on to the last_name
3-Concatenate the first_name on to the result of the previous step
4-Concatenate a space on to the result
5-Concatenate the last_name again to the result
6-Return the final string
"""


def introduction(first_name, last_name):
    return (last_name + ", " + first_name + " " + last_name)


print(introduction("Maya", "Angelou"))
print(introduction("James", "Bond"))
