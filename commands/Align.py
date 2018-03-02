import wpilib
from wpilib.command import Command

class Align (Command):

	def __init__ (self):
		super().__init__('Align') 
		self.requires(self.robot.drivetrain)
		self.max_distance = 650

	def execute (self):
		right = self.robot.drivetrain.left_ultra.getRangeMM()
		left = self.robot.drivetrain.right_ultra.getRangeMM()
		front = self.robot.drivetrain.front_ultra.getRangeMM()

		print('Align execute')
		
		wpilib.DriverStation.reportWarning('left: ' + str(left), False)
		wpilib.DriverStation.reportWarning('right: ' + str(right), False)
		wpilib.DriverStation.reportWarning('front: ' + str(front), False)

		if front >= 10 and front <= 500:
			self.cancel()
		elif left > 10 and left < self.max_distance:
			self.robot.drivetrain.driveManual(0.7, 0)
			self.max_distance = 630
		elif right > 10 and right < self.max_distance:
			self.robot.drivetrain.driveManual(-0.7, 0)
			self.max_distance = 630
		else:
			self.robot.drivetrain.driveManual (0, 0.6)
