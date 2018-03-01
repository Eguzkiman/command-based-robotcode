import wpilib
from wpilib.command import TimedCommand

class Observe (TimedCommand):
	def __init__ (self, seconds = 0.5):
		super().__init__('Observe', seconds)
		self.requires(self.robot.drivetrain)
		self.direction = None

	def execute (self):
		blueDirection = self.robot.sd.getValue('blueDirection', 0)

		if not blueDirection:
			return

		allianceNumber = wpilib.DriverStation.getInstance().getAlliance()

		isRedAlliance = allianceNumber == 0
		isBlueAlliance = allianceNumber == 1
		isInvalidAlliance = allianceNumber == 2

		if isInvalidAlliance:
			pass
		elif isBlueAlliance:
			self.direction = blueDirection
		else:
			self.direction = 'left' if blueDirection == 'right' else 'right'

		self.robot.sd.putValue('autoDirection', self.direction)


	def isFinished (self):
		return bool(self.direction) or self.isTimedOut()