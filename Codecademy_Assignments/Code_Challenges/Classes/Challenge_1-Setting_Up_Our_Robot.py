"""
Challenge 1 : Setting Up Our Robot

Let’s begin by creating the class for our robot. We will begin by setting up the instance variables to keep track of important data related to the robot. Here are the steps we need to do:

1. Create a new class called DriveBot
2. Set up a basic constructor (no parameters needed)
3. Initialize three instance variables within our constructor which all default to 0: motor_speed, direction, and sensor_range
"""


class DriveBot:
    def __init__(self, motor_speed=0, direction=0, sensor_range=0):
        self.motor_speed = motor_speed
        self.direction = direction
        self.sensor_range = sensor_range


# Solution 1
robot_1 = DriveBot()
robot_1.motor_speed = 5
robot_1.direction = 90
robot_1.sensor_range = 10

print(robot_1.motor_speed)  # output: 5
print(robot_1.direction)  # output: 90
print(robot_1.sensor_range)  # output: 10

# Solution 2
robot_1 = DriveBot(5, 90, 10)
