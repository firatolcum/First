amount = int(input("Enter total second amount: "))
hour = amount // 60
minute = (amount % 60) // 60
second = (amount % 60) % 60
print(amount, "second is", hour, "hours,", minute, "minutes and", second, "seconds.")
