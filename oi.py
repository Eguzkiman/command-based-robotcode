import wpilib
from wpilib.buttons import JoystickButton
from commands.TurboDrive import TurboDrive
from commands.FollowJoystick import FollowJoystick
from commands.LiftUp import LiftUp
from commands.LiftDrop import LiftDrop
from commands.LiftDown import LiftDown
from commands.LiftStop import LiftStop
from commands.Align import Align

class OI:
	def __init__ (self, robot):
		robot.joystick = wpilib.Joystick(0)

		A_button = JoystickButton(robot.joystick, 1)
		B_button = JoystickButton(robot.joystick, 2)
		X_button = JoystickButton(robot.joystick, 3)
		Y_button = JoystickButton(robot.joystick, 4)
		LR_button = JoystickButton(robot.joystick, 5)

		A_button.whenPressed(TurboDrive())
		A_button.whenReleased(FollowJoystick())
		LR_button.whenPressed(Align())
		LR_button.whenReleased(FollowJoystick())

		B_button.whileHeld(LiftUp())
		Y_button.whileHeld(LiftDrop())
		X_button.whileHeld(LiftDown())

