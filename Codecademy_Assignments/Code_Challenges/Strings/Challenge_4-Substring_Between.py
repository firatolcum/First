"""
Challenge 4 : Substring Between

Here is a challenging problem. We need a function that is able to extract a portion of a string between two characters. The function will take three parameters where the first parameter is the string we are going to extract the substring from, the second input is the starting character of our substring and the third character is the ending character of our substring. Here are the steps we can use:

1. Define the function to accept three parameters, one string and two characters
2. find the starting index of our substring using the second input parameter
3. find the ending index of our substring using the third input parameter
4. If neither of the indices are -1, return the portion of the first input parameter string between the starting and ending indices (not including the starting and ending index)
5. If either of the indices are -1, that means the start or end of the substring didn’t exist in our string. Return the original string in this case.
"""


def substring_between_letters(word, start, end):
    if word.find(start) != -1 and word.find(end) != -1:
        start_index = word.find(start)
        end_index = word.find(end)
        return word[start_index+1: end_index]
    else:
        return word


print(substring_between_letters("apple", "p", "c"))
# output : apple
print(substring_between_letters("apple", "p", "e"))
#output : pl
