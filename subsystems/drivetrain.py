import wpilib
import wpilib.drive
from wpilib.command.subsystem import Subsystem

from commands.FollowJoystick import FollowJoystick

class Drivetrain (Subsystem):
	def __init__ (self):
		super().__init__()

		self.frontLeft = wpilib.Spark(0)
		self.rearLeft = wpilib.Spark(1)
		self.left = wpilib.SpeedControllerGroup(self.frontLeft, self.rearLeft)

		self.frontRight = wpilib.Spark(2)
		self.rearRight = wpilib.Spark(3)
		self.right = wpilib.SpeedControllerGroup(self.frontRight, self.rearRight)

		self.drive = wpilib.drive.DifferentialDrive(self.left, self.right)

	def driveManual (self, x, y):
		powerX = 0 if x < 0.1 and x > -0.1 else x
		powerY = 0 if y < 0.1 and y > -0.1 else y
		self.drive.arcadeDrive(powerX, powerY)


	def initDefaultCommand (self):
		self.setDefaultCommand(FollowJoystick())