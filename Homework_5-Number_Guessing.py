number = int(input("Guess my number: "))
my_number = 47
while number != my_number:
    if number < my_number:
        print("wrong! increase the number")
        number = int(input("Guess my number: "))
    
    elif number > my_number:
        print("wrong! decrease the number")
        number = int(input("Guess my number: "))
print("Correct! Well done.")
