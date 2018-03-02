from wpilib.command import TimedCommand

class DriveFor (TimedCommand):
	def __init__ (self, seconds, direction):
		super().__init__('Drive For', seconds)
		self.requires(self.robot.drivetrain)

		(x, y) = direction

		self.x = x
		self.y = y


	def execute (self):
		self.robot.drivetrain.driveManual(self.y, self.x)
		print('drivefor execute')

	def end (self):
		self.robot.drivetrain.driveManual(0, 0)
		print('drivefor end')
