from wpilib.command import TimedCommand

class Observe (TimedCommand):
	def __init__ (self, seconds = 3):
		super().__init__('Observe', seconds)
		self.requires(self.robot.drivetrain)

	def execute (self):
		self.direction = self.robot.sd.getValue('autoDirection', 0)
		# self.direction = 'right'
		# self.robot.sd.putValue('autoDirection', self.direction)

	def isFinished (self):
		return bool(self.direction)




