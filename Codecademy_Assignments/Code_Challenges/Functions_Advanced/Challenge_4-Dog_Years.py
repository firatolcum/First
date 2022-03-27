"""
Challenge 4 : Dog Years
Let’s create a function which calculates a dog’s age in dog years! This function will accept the name of the dog and the age in human years. It will calculate the age of the dog in dog years and return a string describing the dog’s age. This will require a few steps:

1-Define the function called dog_years to accept two parameters: name and age
2-Calculate the age of the dog in dog years
3-Concatenate the string with the dog’s name and age in dog years : "{name}, you are {age} years old in dog years"
4-Return the resulting string
"""

# the age in dog years =  age * 7


def dog_years(name, age):
    return name + ", you are " + str(age * 7) + " years old in dog years"


print(dog_years("Lola", 16))
