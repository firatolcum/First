"""
  
- Write a function/functions that checks whether the sentence you get from the user is a **palindrome**. 

input : "ey edip adana'da, pide ye!"

output : "ey edip adana'da, pide ye!" is a palindrome

input : "Was it a car or a cat I saw?"

output : "Was it a car or a cat I saw?" is a palindrome
"""

# Palindrome:  a word, phrase, or sequence that reads the same backwards as forwards.e.g madam

sentence = input("Enter a sentence: ")
sentence = sentence.lower()
list_1 = []
for i in sentence :
    if i in "qwertyuıopğüasdfgğhjklşizxcvbnmöç":
        list_1.append(i)

list_2 = list_1.copy()
list_2.reverse()
if list_1 == list_2:
    print(sentence, "is a palindrome")
else:
    print(sentence, "is not a palindrome")
        
