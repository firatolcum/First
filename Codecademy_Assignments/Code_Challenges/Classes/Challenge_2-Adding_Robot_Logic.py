"""
Challenge 2 : Adding Robot Logic

Now we want to add some logic to our robot. It would be very useful to be able to control our robot, so we are going to create a control_bot method which changes the speed and direction. We are also going to create a method called adjust_sensor. This method is used to change the range of our robot’s sensors which are used to detect obstacles. Here are the steps:

1. Define a function within the DriveBot class which accepts two additional parameters: one for a new speed and one for a new direction
2. Replace the instance variables for speed and direction with the input parameters
3. Define another function called adjust_sensor which accepts one additional parameter
4. Replace the instance variable sensor_range with the input parameter
"""


class DriveBot:
    def __init__(self, motor_speed=0, direction=0, sensor_range=0):
        self.motor_speed = motor_speed
        self.direction = direction
        self.sensor_range = sensor_range

    def control_bot(self, speed, direction):
        self.speed = speed
        self.direction = direction

    def adjust_sensor(self, new_sensor_range):
        self.sensor_range = new_sensor_range


robot_1 = DriveBot()
