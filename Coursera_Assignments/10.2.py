"""
10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.
"""

fhand = open(input("Enter file:"))
times = []
for line in fhand:
    if line.startswith("From") and not line.startswith("From:"):
        line = line.split(":")
        line = str(line[0])
        times.append(line[-2:])

counts = dict()
for hour in times:
    if hour in counts:
        counts[hour] = counts[hour] + 1
    else:
        counts[hour] = 1

counts_list = []
for key, value in counts.items():
    counts_list.append((key, value))
sorted_counts_list = sorted(counts_list)
for key, value in sorted_counts_list:
    print(key, value)
