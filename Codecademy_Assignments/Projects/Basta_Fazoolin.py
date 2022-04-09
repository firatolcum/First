"""
Basta Fazoolin'
You’ve started position as the lead programmer for the family-style Italian restaurant Basta Fazoolin’ with My Heart. The restaurant has been doing fantastically and seen a lot of growth lately. You’ve been hired to keep things organized.

If you get stuck during this project or would like to see an experienced developer work through it, click “Get Unstuck“ to see a project walkthrough video.
"""
"""
1. At Basta Fazoolin’ with my Heart our motto is simple: when you’re here with family, that’s great! We have four different menus: brunch, early-bird, dinner, and kids.Create a Menu class .
2. Give Menu a constructor with the five parameters self, name, items, start_time, and end_time.
"""


class Menu:
    def __init__(self, name, items, start_time, end_time):
        self.name = name
        self.items = items
        self.start_time = start_time
        self.end_time = end_time


"""
3. Let’s create our first menu: brunch. Brunch is served from 11am to 4pm. The following items are sold during brunch:
{
  'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50
}
"""
brunch_items = {
    'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50
}
brunch_menu = Menu("Brunch", brunch_items, 1100, 1600)

"""
4. Let’s create our second menu item early_bird. Early-bird Dinners are served from 3pm to 6pm. The following items are available during the early-bird menu:
{
  'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00,
}
"""
early_bird_items = {
    'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00,
}
early_bird_menu = Menu("Early bird", early_bird_items, 1300, 1800)

"""
5. Let’s create our third menu, dinner. Dinner is served from 5pm to 11pm. The following items are available for dinner:
{
  'crostini with eggplant caponata': 13.00, 'ceaser salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00,
}
"""
dinner_items = {
    'crostini with eggplant caponata': 13.00, 'ceaser salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00,
}
dinner_menu = Menu("Dinner", dinner_items, 1700, 2300)

"""
6. And let’s create our last menu, kids. The kids menu is available from 11am until 9pm. The following items are available on the kids menu.
{
  'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00
}
"""
kids_items = {
    'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00
}
kids_menu = Menu("Kids", kids_items, 1100, 1900)

"""
7. Give our Menu class a string representation method that will tell you the name of the menu. Also, indicate in this representation when the menu is available.
"""


class Menu:
    def __init__(self, name, items, start_time, end_time):
        self.name = name
        self.items = items
        self.start_time = start_time
        self.end_time = end_time

    def __repr__(self):
        return "{name} menu available from {start_time} to {end_time}".format(name=self.name, start_time=self.start_time, end_time=self.end_time)


"""
8. Try out our string representation. If you call print(brunch) it should print out something like the following:
brunch menu available from 11am to 4pm
"""
print(brunch_menu)
# output: Brunch menu available from 1100 to 1600

"""
9. Give Menu a method .calculate_bill() that has two parameters: self, and purchased_items, a list of the names of purchased items.
Have calculate_bill return the total price of a purchase consisting of all the items in purchased_items.
"""


def calculate_bill(self, purchased_items):
    total = 0
    for item in purchased_items:
        if item in self.items:
            total += self.items[item]
            return total


"""
10. Test out Menu.calculate_bill(). We have a breakfast order for one order of pancakes, one order of home fries, and one coffee. Pass that into brunch.calculate_bill() and print out the price.
"""
print(brunch_menu.calculate_bill(["pancakes", "home fries", "coffee"]))
# output: 7.5

"""
11. What about an early-bird purchase? Our last guests ordered the salumeria plate and the vegan mushroom ravioli. Calculate the bill with .calculate_bill().
"""
print(early_bird_menu.calculate_bill(
    ["salumeria plate", "mushroom ravioli (vegan)"]))
# output: 8.0

"""
12. Basta Fazoolin’ with my Heart has seen tremendous success with the family market, which is fantastic because when you’re at Basta Fazoolin’ with my Heart with family, that’s great!
We’ve decided to create more than one restaurant to offer our fantastic menus, services, and ambience around the country.
First, let’s create a Franchise class.
13. Give the Franchise class a constructor. Take in an address, and assign it to self.address. Also take in a list of menus and assign it to self.menus.
"""


class Franchise:
    def __init__(self, address, menus):
        self.address = address
        self.menus = menus


"""
14. Let’s create our first two franchises! Our flagship store is located at "1232 West End Road" and our new installment is located at "12 East Mulberry Street". Pass in all four menus along with these addresses to define flagship_store and new_installment.
"""
flagship_store.address
