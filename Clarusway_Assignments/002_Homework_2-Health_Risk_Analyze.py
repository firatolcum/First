age = input("Are you a cigarette addict older than 75 years old? Enter yes or no: ")
age = age.capitalize()
chronic = input("Do you have a severe chronic disease?: ")
chronic = chronic.capitalize()
immune = input("Is your immune system too weak?: ")
immune = immune.capitalize()
if age=="Yes" or chronic=="Yes" or immune=="Yes":
    print("You are in risky group.")
else:
    print("You are not in risky group.")
