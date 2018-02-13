from wpilib.command import Command

class Align (Command):

	def __init__ (self):
		super().__init__('Align')
		self.requires(self.robot.drivetrain)

	def execute (self):
		left = self.robot.drivetrain.left_ultra.getRangeMM()
		right = self.robot.drivetrain.right_ultra.getRangeMM()
		
		#left = self.robot.drivetrain.left_analog.getVoltage()
		#right = self.robot.drivetrain.right_analog.getVoltage()

		if (left >= 30 and left <= 200) & (right >= 30 and right <= 200):
			self.cancel()
		elif left >= 30 and left <= 200:
			self.robot.drivetrain.driveManual(1, 0)
		elif right >= 30 and right <= 200:
			self.robot.drivetrain.driveManual(-1, 0)
		
		else:
			self.robot.drivetrain.driveManual(0, 1) #02-0.200
