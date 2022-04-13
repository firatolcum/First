"""
Challenge 2 : Even Keys

Next, we are going to do something similar, but we are going to use the keys in order to retrieve the values. Additionally, we are going to only look at every even key within the dictionary. Here are the steps:

1. Define the function to accept one parameter for our dictionary
2. Create a variable to keep track of our sum
3. Loop through every key in the dictionary
4. Inside the loop, if the key is even, add the value from the even key
5. After the loop, return the sum
"""


def sum_even_keys(my_dictionary):
    sum_value = 0
    for key in my_dictionary:
        if key % 2 == 0:
            sum_value += my_dictionary[key]
    return sum_value


print(sum_even_keys({1: 5, 2: 2, 3: 3}))
# should print 2
print(sum_even_keys({10: 1, 100: 2, 1000: 3}))
# should print 6
