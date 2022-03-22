"""
Your computer is the doorman at a bar in a country where the drinking age is 21.

Loop through the ages list. If an entry is less than 21, skip it and move to the next entry. Otherwise, print() the age.
ages = [12, 38, 34, 26, 21, 19, 67, 41, 17]

"""
ages = [12, 38, 34, 26, 21, 19, 67, 41, 17]
for i in ages:
    if i < 21:
        continue
    print(i)
