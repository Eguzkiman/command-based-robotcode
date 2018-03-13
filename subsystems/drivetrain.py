import wpilib
import wpilib.drive
from wpilib.command.subsystem import Subsystem
from commands.FollowJoystick import FollowJoystick
from commands.Align import Align

class Drivetrain (Subsystem):
	def __init__ (self):
		super().__init__()

		self.frontLeft = wpilib.Spark(0)
		self.rearLeft = wpilib.Spark(3)

		self.frontRight = wpilib.Spark(1)
		self.rearRight = wpilib.Spark(2)

		self.drive = wpilib.drive.MecanumDrive(self.frontLeft, self.rearLeft, self.frontRight, self.rearRight)

		self.left_ultra = wpilib.Ultrasonic(5, 4)
		self.right_ultra = wpilib.Ultrasonic(3, 2)
		self.front_ultra = wpilib.Ultrasonic(1, 0)

		self.left_ultra.setAutomaticMode(True)
		self.right_ultra.setAutomaticMode(True)
		self.front_ultra.setAutomaticMode(True)

	def driveManual (self, x, y, z):

		powerX = 0 if x < 0.1 and x > -0.1 else x
		powerY = 0 if y < 0.1 and y > -0.1 else y
		powerZ = 0 if z < 0.1 and z > -0.1 else z

		self.drive.driveCartesian(powerY, powerX, powerZ)

	def initDefaultCommand (self):
		self.setDefaultCommand(FollowJoystick())
