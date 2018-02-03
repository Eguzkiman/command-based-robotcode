from wpilib.command import TimedCommand

class DriveBackwardsFor (TimedCommand):

	def __init__(self, seconds):
		super().__init__('Drive Forward', seconds)
		self.requires(self.robot.drivetrain)

	def execute (self):
		self.robot.drivetrain.driveManual(-1,-1)
	
	def end (self):
		self.robot.drivetrain.driveManual(0,0)

