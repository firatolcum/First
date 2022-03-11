"""Given a text as input, find and output the longest word.

Sample Input
this is an awesome text

Sample Output
awesome

Recall the split(' ') method, which returns a list of words of the string."""

txt = input()
word_list = txt.split(" ")
long = 0
for word in word_list:
    if len(word) > long:
        long = len(word)


for word in word_list:
    if long == len(word):
        print(word)
