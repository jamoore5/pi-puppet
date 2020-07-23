from gpiozero import AngularServo

class Servo:
    def __init__(self, pin, inital_angle=0, reverse=False):
        self.servo = None
        self.current_angle = inital_angle
        angle = self.current_angle - 90
        if reverse:
            self.servo = AngularServo(pin, angle, min_angle=90, max_angle=-90)
        else:
            self.servo = AngularServo(pin, angle)
    def __set_angle(self, value):
        if value is None:
            angle = None
        else:
            self.current_angle = value
            angle = self.current_angle - 90
        self.servo.angle = angle
    def __get_angle(self):
        return self.current_angle
    angle = property(__get_angle, __set_angle)
    def close(self):
        self.servo.close()
