import wpilib
from wpilib.buttons import JoystickButton
from commands.TurboDrive import TurboDrive
from commands.FollowJoystick import FollowJoystick
from commands.LiftUp import LiftUp
from commands.LiftDrop import LiftDrop
from commands.LiftDown import LiftDown
from commands.LiftStop import LiftStop

class OI:
	def __init__ (self, robot):
		robot.joystick = wpilib.Joystick(0)

		A_button = JoystickButton(robot.joystick, 1)
		B_button = JoystickButton(robot.joystick, 2)
		LB_button = JoystickButton(robot.joystick, 5)
		RB_button = JoystickButton(robot.joystick, 6)

		A_button.whenPressed(TurboDrive())
		A_button.whenReleased(FollowJoystick())

		RB_button.whileHeld(LiftUp())
		B_button.whileHeld(LiftDrop())
		LB_button.whileHeld(LiftDown())