"""
Task : Print the Fizz Buzz numbers.

Fizz Buzz is a famous code challenge used in interviews to test basic programming skills. It's time to write your own implementation.
Print numbers from 1 to 100 inclusively following these instructions:
if a number is multiple of 3, print "Fizz" instead of this number,
if a number is multiple of 5, print "Buzz" instead of this number,
for numbers that are multiples of both 3 and 5, print "FizzBuzz",
print the rest of the numbers unchanged.
Output each value on a separate line.
Note that : This question is famous on the web, so to get more benefit from this assignment, try to complete this task on your own.
"""
    for number in range(1,101):
    if number % 3 == 0 and number % 5 != 0:
        print("Fizz")
    elif number % 3 != 0 and number % 5 == 0:
        print("Buzz")
    elif number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    else:
        print(number)


