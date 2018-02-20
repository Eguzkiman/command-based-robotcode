from wpilib.command import TimedCommand
from networktables.util import ntproperty

class Observe (TimedCommand):
	target = ntproperty('/target', 0)

	def __init__ (self, seconds = 3):
		super().__init__('Observe', seconds)
		self.requires(self.robot.drivetrain)

	def execute (self):
		if self.target:
			# self.robot.autoDirection = direction
			self.cancel()



