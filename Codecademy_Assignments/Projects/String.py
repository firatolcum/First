"""
Write a function called common_letters that takes two arguments, string_one and string_two and then returns a list with all of the letters they have in common.

The letters in the returned list should be unique. For example,
    common_letters("banana", "cream")
    should return ['a'].
"""


def common_letters(string_one, string_two):
    new_list = []
    for s in string_one:
        if s in string_two and not s in new_list:
            new_list.append(s)

    return new_list


print(common_letters("banana", "cream"))

"""
They sent over another list containing all the lines to the Audre Lorde poem, Love, Maybe. They want you to join together all of the lines into a single string that can be used to display the poem again, but this time, you’ve noticed that the list contains a ton of unnecessary whitespace that doesn’t appear in the actual poem.
    
First, use .strip() on each line in the list to remove the unnecessary whitespace and save it as a new list love_maybe_lines_stripped.
After, .join() the lines in love_maybe_lines_stripped together into one large multi-line string, love_maybe_full, that can be printed to display the poem.
Lastly, print love_maybe_full
Each line of the poem should show up on its own line.
"""
love_maybe_lines = ['Always    ', '     in the middle of our bloodiest battles  ',
                    'you lay down your arms', '           like flowering mines    ', '\n', '   to conquer me home.    ']

love_maybe_lines_stripped = []
for word in love_maybe_lines:
    new_word = word.strip()
    love_maybe_lines_stripped.append(new_word)

love_maybe_full = "\n".join(love_maybe_lines_stripped)
print(love_maybe_full)


"""
Write a function called poem_title_card that takes two inputs: the first input should be title and the second poet. The function should use .format() to return the following string:
    The poem "[TITLE]" is written by [POET].
    
For example, if the function is given the inputs
    poem_title_card("I Hear America Singing", "Walt Whitman")
    
It should return the string
    The poem "I Hear America Singing" is written by Walt Whitman.
"""


def poem_title_card(title, pet):
    return '''The poem "{}" is written by {}.'''.format(title, pet)


print(poem_title_card("I Hear America Singing", "Walt Whitman"))


"""
1.Preserve the Verse has one final task for you. They have delivered you a string that contains a list of poems, titled highlighted_poems, they want to highlight on the site, but they need your help to parse the string into something that can display the name, title, and publication date of the highlighted poems on the site.
First, start by printing highlighted_poems to the terminal and see how it displays.

2.The information for each poem is separated by commas, and within this information is the title of the poem, the author, and the date of publication.
Start by splitting highlighted_poems at the commas and saving it to highlighted_poems_list.

3.Print highlighted_poems_list, how does the structure of the data look now?

4.Notice that there is inconsistent whitespace in highlighted_poems_list. Let’s clean that up.
Start by creating a new empty list, highlighted_poems_stripped.
Then, iterate through highlighted_poems_list using a for loop and for each poem strip away the whitespace and append it to your new list, highlighted_poems_stripped.

5.Print highlighted_poems_stripped.
Looks good! All the whitespace is cleaned up.

6.Next we want to break up all the information for each poem into it’s own list, so we end up with a list of lists.
Create a new empty list called highlighted_poems_details.

7.Iterate through highlighted_poems_stripped and split each string around the : characters and append the new lists into highlighted_poems_details.

8.Great! Now we want to separate out all of the titles, the poets, and the publication dates into their own lists.
Create three new empty lists, titles, poets, and dates.

9.Iterate through highlighted_poems_details and for each list in the list append the appropriate elements into the lists titles, poets, and dates.
For example, for the poem The Shadow (1915) by William Carlos Williams your code should be adding "The Shadow" to titles, "William Carlos Williams" to poets, and "1915" to dates.

10.Finally, write a for loop that uses .format() to print out the following string for each poem:
The poem TITLE was published by POET in DATE.
"""

highlighted_poems = "Afterimages:Audre Lorde:1997,  The Shadow:William Carlos Williams:1915, Ecstasy:Gabriela Mistral:1925,   Georgia Dusk:Jean Toomer:1923,   Parting Before Daybreak:An Qi:2014, The Untold Want:Walt Whitman:1871, Mr. Grumpledump's Song:Shel Silverstein:2004, Angel Sound Mexico City:Carmen Boullosa:2013, In Love:Kamala Suraiyya:1965, Dream Variations:Langston Hughes:1994, Dreamwood:Adrienne Rich:1987"

# print(highlighted_poems)
highlighted_poems_list = highlighted_poems.split(",")
# print(highlighted_poems_list)

highlighted_poems_stripped = []
for char in highlighted_poems_list:
    highlighted_poems_stripped.append(char.strip())
# print(highlighted_poems_stripped)

highlighted_poems_details = []
for char in highlighted_poems_stripped:
    highlighted_poems_details.append(char.split(":"))

# print(highlighted_poems_details)
titles = []
poets = []
dates = []
for char in highlighted_poems_details:
    titles.append(char[0])
    poets.append(char[1])
    dates.append(char[2])

for x in range(len(titles)):
    print("The poem {} was published by {} in {}.".format(
        titles[x], poets[x], dates[x]))
