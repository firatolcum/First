"""Task : Create a list consisting of Fibonacci numbers from 1 to 55 using control flow statements and range() function."""

fibonacci = [1, 1]
n = 0
while fibonacci[n] in list(range(1, 56)):
    fibonacci.append(fibonacci[n] + fibonacci[n+1])
    n += 1
    if fibonacci[-1] == 55:
        break
    
print(fibonacci)
