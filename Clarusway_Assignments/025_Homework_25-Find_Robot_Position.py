"""
Below is a list of the directions a robot will move. Find the final position of the robot.
"""
command = ["right 20", "right 30", "left 50", "up 10",
           "down 20", "right 50", "up 30", "down 10", "down 20"]

right = 0
left = 0
up = 0
down = 0
for i in command:
    if i.startswith("r"):
        i = i.split()
        right = right + int(i[1])
    elif i.startswith("l"):
        i = i.split()
        left = left + int(i[1])
    elif i.startswith("u"):
        i = i.split()
        up = up + int(i[1])
    elif i.startswith("d"):
        i = i.split()
        down = down + int(i[1])

x_line = right - left
y_line = up - down
print("position on the x-axis:", x_line)
print("position on the y-axis:", y_line)
