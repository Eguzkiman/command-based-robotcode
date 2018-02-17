import wpilib
import wpilib.drive
from wpilib.command.subsystem import Subsystem
from commands.FollowJoystick import FollowJoystick
from commands.Align import Align

class Drivetrain (Subsystem):
	def __init__ (self):
		super().__init__()

		self.frontLeft = wpilib.Spark(0)
		self.rearLeft = wpilib.Spark(1)
		self.left = wpilib.SpeedControllerGroup(self.frontLeft, self.rearLeft)

		self.frontRight = wpilib.Spark(2)
		self.rearRight = wpilib.Spark(3)
		self.right = wpilib.SpeedControllerGroup(self.frontRight, self.rearRight)

		self.drive = wpilib.drive.DifferentialDrive(self.right, self.left)

		self.left_ultra = wpilib.Ultrasonic(1, 0)
		self.right_ultra = wpilib.Ultrasonic(3, 2)

		self.left_ultra.setAutomaticMode(True)
		self.right_ultra.setAutomaticMode(True)

		self.left_analog = wpilib.AnalogInput(0)
		self.left_analog = wpilib.AnalogInput(2)

		self.left_sensor = wpilib.DigitalInput(4)
		self.right_sensor = wpilib.DigitalInput(5)


	def driveManual (self, x, y):	
		
		self.left_ultra = wpilib.Ultrasonic(5, 4)
		self.right_ultra = wpilib.Ultrasonic(3, 2)
		self.front_ultra = wpilib.Ultrasonic(1, 0)

		
		self.left_ultra.setAutomaticMode(True)
		self.right_ultra.setAutomaticMode(True)
		self.front_ultra.setAutomaticMode(True)

		# self.left_analog = wpilib.AnalogInput(0)
		# self.right_analog = wpilib.AnalogInput(2)
		# sself.left_sensor = wpilib.DigitalInput(4)
		# self.right_sensor = wpilib.DigitalInput(5)

	def driveManual (self, x, y):
		
		#self.left_ultra.getRangeMM()
		#self.right_ultra.getRangeMM()

		powerX = 0 if x < 0.1 and x > -0.1 else x
		powerY = 0 if y < 0.1 and y > -0.1 else y
		
		self.drive.arcadeDrive(powerY, powerX)

	def initDefaultCommand (self):
		self.setDefaultCommand(FollowJoystick())
