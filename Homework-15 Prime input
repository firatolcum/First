"""Task : Print the prime numbers which are between 1 to entered limit number (n).

You can use a nested for loop.
Collect all these numbers into a list
The desired output for n=100 :"""





n = int(input("Enter an end number : "))
list_prime = []
for i in range(2, n+1):
    divider = 0
    for x in range(2, i):
        if i % x == 0:
            divider += 1
            break
    if divider == 0:
        list_prime.append(i)

print(list_prime)
