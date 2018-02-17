import wpilib
from wpilib.buttons import JoystickButton
from commands.TurboDrive import TurboDrive
from commands.FollowJoystick import FollowJoystick
from commands.Align import Align

class OI:
	def __init__ (self, robot):
		robot.joystick = wpilib.Joystick(0)

		L3_button = JoystickButton(robot.joystick, 9)
		LB_button = JoystickButton(robot.joystick, 5)

		L3_button.whenPressed(TurboDrive())
		L3_button.whenReleased(FollowJoystick())
		LB_button.whenPressed(Align())
		LB_button.whenReleased(FollowJoystick())

	

