from servo import Servo
from time import sleep

class Puppet:
    def __init__(self, inital_angle=0):
        self.__left_leg = Servo(17, inital_angle)
        self.__left_arm = Servo(18, inital_angle, reverse=True)
        self.__right_arm = Servo(27, inital_angle)
        self.__right_leg = Servo(22, inital_angle, reverse=True)
        sleep(0.5)
        self.__left_leg.angle = None
        self.__left_arm.angle = None
        self.__right_arm.angle = None
        self.__right_leg.angle = None


    def close(self):
        self.clear()
        self.__left_leg.close()
        self.__left_arm.close()
        self.__right_arm.close()
        self.__right_leg.close()

    def clear(self):
        angle = 90
        self.left_leg = angle
        self.left_arm = angle
        self.right_arm = angle
        self.right_leg = angle
        sleep(0.5)
    
    def sleep(self):
        self.__left_leg.angle = None
        self.__left_arm.angle = None
        self.__right_arm.angle = None
        self.__right_leg.angle = None

    def move(self, move, delay=0.05):
        self.left_leg = move[0]
        self.left_arm = move[1]
        self.right_arm = move[2]
        self.right_leg = move[3]
        sleep(delay)
    
    def __get_left_leg(self):
        return self.__left_leg.angle

    def __set_left_leg(self, angle):
        self.__left_leg.angle = angle 

    def __get_left_arm(self):
        return self.__left_arm.angle

    def __set_left_arm(self, angle):
        self.__left_arm.angle = angle

    def __get_right_leg(self):
        return self.__right_leg.angle

    def __set_right_leg(self, angle):
        self.__right_leg.angle = angle

    def __get_right_arm(self):
        return self.__right_arm.angle

    def __set_right_arm(self, angle):
        self.__right_arm.angle = angle

    left_leg = property(__get_left_leg, __set_left_leg)
    left_arm = property(__get_left_arm, __set_left_arm)
    right_leg = property(__get_right_leg, __set_right_leg)
    right_arm = property(__get_right_arm, __set_right_arm)



