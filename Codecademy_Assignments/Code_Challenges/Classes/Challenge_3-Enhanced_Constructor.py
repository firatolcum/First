"""
Challenge 3 : Enhanced Constructor

It can be tedious manually setting the values for each instance variable after we have created an object from the DriveBot class. We can enhance our constructor to automatically assign the values we provide to the instance variables. Instead of taking zero parameters, we are going to make the constructor take three parameters. Here is what we need to do:

1. Modify the constructor to take three parameters (in addition to self): one for motor_speed, one for direction, and one for sensor_range
2. For the first parameter, make the default value 0
3. For the second parameter, make the default value 180
4. For the third parameter, make the default value 10
5. Within the constructor, replace the instance variables with the variables from the input parameters
"""


class DriveBot:
    def __init__(self, motor_speed=0, direction=180, sensor_range=10):
        self.motor_speed = motor_speed
        self.direction = direction
        self.sensor_range = sensor_range

    def control_bot(self, speed, direction):
        self.speed = speed
        self.direction = direction

    def adjust_sensor(self, new_sensor_range):
        self.sensor_range = new_sensor_range


# sensor_range defaults to 10
test_bot_1 = DriveBot(10, 270)

# direction defaults to 180
test_bot_2 = DriveBot(sensor_range=20, motor_speed=45)

# direction defaults to 180 and sensor_range defaults to 10
test_bot_3 = DriveBot(50)

# all default values are used
test_bot_4 = DriveBot()

# no default values are used
test_bot_5 = DriveBot(18, 95, 30)

robot_1 = DriveBot()
