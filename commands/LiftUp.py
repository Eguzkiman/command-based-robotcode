from wpilib.command import InstantCommand

class LiftUp (InstantCommand):

	def __init__ (self):
		super().__init__('Lift up')
		self.requires(self.robot.lift)

	def execute (self):
		self.robot.lift.up()

