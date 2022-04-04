"""
Exception Handling:

1-Using while loop and full try-except block,
2-Give the user three chances to enter an input, and whenever the user raises an exception, decrease the counter by 1 displaying that "<warning message>, you have n right left.Try again!"
3-If no eception raise, display a message: "Congrats! You've entered a valid input."
4-In all circumstances, diplay a message: "Our fruits are always fresh!
"""

fruits = ["banana", "mango", "pear", "apple", "kiwi", "grape"]
num = 3
while num > 0:
    try:
        print("You have {} right.".format(num))
        index = int(input("Please enter index number :"))
        print("My favorite fruit is", fruits[index])

    except IndexError:
        num -= 1
        print("Index Error raised.You have {} right left. Try again!".format(num))

    except ValueError:
        num -= 1
        print("Value Error raised.You have {} right left. Try again!".format(num))

    else:
        print("Congrats! You've entered a valid input")
        break

    finally:
        print("Our fruits are always fresh!")
