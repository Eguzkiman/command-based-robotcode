from wpilib.command import Command

class Align (Command):

	def __init__ (self):
		super().__init__('Align')
		self.requires(self.robot.drivetrain)

	def execute (self):

		# left = self.robot.drivetrain.left_ultra.getRangeMM()
		# right = self.robot.drivetrain.right_ultra.getRangeMM()

		left = self.robot.drivetrain.left_analog.getVoltage()
		right = self.robot.drivetrain.right_analog.getVoltage()

		if left >= 2 and left <= 8 and right >= 2 and right <= 8:
			self.cancel()
		elif self.robot.drivetrain.left_sensor.get():
			self.robot.drivetrain.driveManual(0, 1)
		elif self.robot.drivetrain.right_sensor.get():
			self.robot.drivetrain.driveManual(0, -1)
		
		else:
			self.robot.drivetrain.driveManual(1, 0)
