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

		L3_button = JoystickButton(robot.joystick, 9)
		RT_button = JoystickButton(robot.joystick, 2)
		LT_button = JoystickButton(robot.joystick, 3)
		B_button = JoystickButton(robot.joystick, 4)
		LB_button = JoystickButton(robot.joystick, 5)

		L3_button.whenPressed(TurboDrive())
		L3_button.whenReleased(FollowJoystick())
		LB_button.whenPressed(Align())
		#LR_button.whenReleased(FollowJoystick())

		RT_button.whileHeld(LiftUp())
		B_button.whileHeld(LiftDrop())
		LT_button.whileHeld(LiftDown())

