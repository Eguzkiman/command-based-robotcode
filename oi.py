import wpilib

class OI:
	def __init__ (self, robot):
		robot.joystick = wpilib.Joystick(0)