"""
Password Generator
Generate a password that contains three uppercase letters, three lowercase letters, three numbers and two special characters.
"""
import random
# The ASCII list has between 65 and 90 capital letters.
uppers = [chr(random.randint(65, 90)) for i in range(3)]
# The ASCII list has between 97 and 122 lowercase letter.
lowers = [chr(random.randint(97, 122)) for i in range(3)]
# The ASCII list has between 48 and 57 number.
numbers = [chr(random.randint(48, 57)) for i in range(3)]
# The ASCII list has between 33-47 and 58-64 special character
chars = chr(random.randint(33, 47)) + chr(random.randint(58, 64))
password = "".join(uppers) + "".join(lowers) + \
    "".join(numbers) + chars  # join list and convert string


def shuffle_pass(password):
    temp_lst = list(password)
    random.shuffle(temp_lst)  # Shuffle list
    return "".join(temp_lst)


print(shuffle_pass(password))
