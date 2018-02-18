
import wpilib
from wpilib.buttons import JoystickButton
from commands.TurboDrive import TurboDrive
from commands.FollowJoystick import FollowJoystick
from commands.Align import Align
from commands.MoveArmTo import MoveArmTo
from commands.MoveClawTo import MoveClawTo


class OI:
	def __init__ (self, robot):
		robot.joystick = wpilib.Joystick(0)

		L3_button = JoystickButton(robot.joystick, 9)
		LB_button = JoystickButton(robot.joystick, 5)
		A_button = JoystickButton(robot.joystick, 1)
		B_button = JoystickButton(robot.joystick, 2)
		X_button = JoystickButton(robot.joystick, 3)
		Y_button = JoystickButton(robot.joystick, 4)


		L3_button.whenPressed(TurboDrive())
		L3_button.whenReleased(FollowJoystick())

		LB_button.whenPressed(Align())
		LB_button.whenReleased(FollowJoystick())


		X_button.whenPressed(MoveClawTo(power=.3))
		X_button.whenReleased(MoveClawTo(power=0))

		B_button.whenPressed(MoveClawTo(power=-.3))
		B_button.whenReleased(MoveClawTo(power=0))

		Y_button.whenPressed(MoveArmTo(power=1))
		Y_button.whenReleased(MoveArmTo(power=0))

		A_button.whenPressed(MoveArmTo(power=-1))
		A_button.whenReleased(MoveArmTo(power=0))



