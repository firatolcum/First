text = input()
space_amount = text.count(" ")
len_word = len(text) - space_amount
word_list = text.split()
word_amount = len(word_list)
avg_word_len = len_word / word_amount
print(avg_word_len)
