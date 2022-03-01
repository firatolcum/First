word_list = ["eat", "tea", "tan", "ate", "nat", "bat", "cat", "tac"]
anagram = {}

for i in word_list:
    element = "".join(sorted(i))              # The join() method takes all items in an iterable and joins them into one string.
                                              # A string must be specified as the separator.
    if element in anagram:                    
              anagram[element].append(i)      # Sorted() sorts any sequence (list, tuple) and always returns a list with the elements in a sorted manner, without modifying the original sequence.
    else:
        anagram[element] = [i]
print(list(anagram["aet"]), list(anagram["ant"]), list(anagram["abt"]), sep="\n")
