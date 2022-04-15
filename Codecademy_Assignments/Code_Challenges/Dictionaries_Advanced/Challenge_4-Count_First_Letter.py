"""
Challenge 4 : Count First Letter

This function accepts a dictionary where the keys are last names and the values are lists of first names of people who have that last name. We need to calculate the number of people who have the same first letter in their last name. Here are the steps we need:

1. Define the function to accept one parameter for our dictionary
2. Create a new empty dictionary called letters
3. Loop through every key in our names dictionary
4. Inside the loop, get the first letter of the last name we are looking at. If the first letter is not in our letter dictionary, add it as a key with a value of 0. Then, increment that key by the number of people that have that last name
5. After the loop, return the letters dictionary
"""


def count_first_letter(names):
    my_dict = {}
    for key, value in names.items():
        if key[0] not in my_dict.keys():
            my_dict[key[0]] = len(value)
        else:
            my_dict[key[0]] += len(value)
    return my_dict


print(count_first_letter({"Stark": ["Ned", "Robb", "Sansa"], "Snow": [
      "Jon"], "Lannister": ["Jaime", "Cersei", "Tywin"]}))
# should print {"S": 4, "L": 3}
print(count_first_letter({"Stark": ["Ned", "Robb", "Sansa"], "Snow": [
      "Jon"], "Sannister": ["Jaime", "Cersei", "Tywin"]}))
# should print {"S": 7}
