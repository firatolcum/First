"""
Using datetime module, write a program to calculate the following.
Mary was born on 12th June 1935 and died on 8th September 2021.
How many days have he lived in her life? 
"""
from datetime import date
birth = date(1935, 6, 12)
death = date(2021, 9, 8)
life_day = death - birth
print(life_day)
