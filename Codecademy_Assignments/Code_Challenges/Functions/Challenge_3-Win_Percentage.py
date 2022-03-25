"""
Challenge-3 : Win Percentage
Next, we will create a function which calculates the percentage of games won. In order to do this, we will need to know how many total games there were and divide the number of wins by the total number of games. For this function, there will be two input parameters, the number of wins and the number of losses. We also need to make sure that we return the result as a percentage (in the range of 0 to 100). In order to create this method we need the following steps:

1-Define the function header with two parameters, wins and losses
2-Calculate the total number of games using the number of wins and losses
3-Get the ratio of winning using the number of wins out of the total number of games.
4-Convert the ratio to a percentage
5-Return the percentage
"""


def win_percentage(wins, losses):
    total_game = wins + losses
    win_ratio = wins / total_game
    win_percentage = win_ratio * 100
    return win_percentage


print(win_percentage(5, 5))  # 50
