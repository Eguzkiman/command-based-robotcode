import wpilib
from wpilib.buttons import JoystickButton
from commands.TurboDrive import TurboDrive
from commands.FollowJoystick import FollowJoystick
from commands.LiftUp import LiftUp

class OI:
	def __init__ (self, robot):
		robot.joystick = wpilib.Joystick(0)

		A_button = JoystickButton(robot.joystick, 1)
		A_button.whenPressed(TurboDrive())
		A_button.whenReleased(FollowJoystick())

		B_button.whenPressed(LiftUp())
		# B_button.whenReleased(FollowJoystick())

