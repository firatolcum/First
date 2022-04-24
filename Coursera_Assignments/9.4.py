"""
9.4 Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.
"""

name = input("Enter file:")
handle = open(name)

senders = []
for line in handle:
    if line.startswith("From") and not line.startswith("From:"):
        line = line.split()
        senders.append(line[1])

counts = dict()
for word in senders:
   # counts[word] = counts.get(word, 0) + 1
    if word in counts:
        # Use this if-else block or get method.
        counts[word] = counts[word] + 1
    else:
        counts[word] = 1


bigcount = None
bigsender = None

for sender, count in counts.items():
    if bigcount is None or count > bigcount:
        bigsender = sender
        bigcount = count

print(bigsender, bigcount)
