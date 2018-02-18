from wpilib.command import TimedCommand

class Observe (TimedCommand):
	def __init__ (self, seconds = 2):
		super().__init__('Observe', seconds)
		self.requires(self.robot.drivetrain)

	def execute (self):
		direction = sd.getValue('autoDirection')

		if direction:
			self.robot.autoDirection = direction
			self.cancel()



