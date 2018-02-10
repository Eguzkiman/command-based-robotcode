from wpilib.command import Command

class Align (Command):

	def __init__ (self):
		super().__init__('Align')
		self.requires(self.robot.drivetrain)

	def execute (self):

		if self.robot.drivetrain.right_sensor.get() & self.robot.drivetrain.left_sensor.get():
			self.cancel()
		elif self.robot.drivetrain.left_sensor.get():
			self.robot.drivetrain.driveManual(0, 1)
		elif self.robot.drivetrain.right_sensor.get():
			self.robot.drivetrain.driveManual(0, -1)
		
		else:
			self.robot.drivetrain.driveManual(1, 0)
