

from robot import Robot

class Fleet:
    def __init__(self):
        self.robot = []
        

    def create_fleet(self):
        robo_one = Robot('Nokia')
        robo_two = Robot('Samsung')
        robo_three = Robot('Asus')
        self.robot.append(robo_one)
        self.robot.append(robo_two)
        self.robot.append(robo_three)
        pass