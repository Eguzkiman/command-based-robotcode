from wpilib.command import InstantCommand

class LiftDown (InstantCommand):

	def __init__ (self):
		super().__init__('Follow Joystick')
		self.requires(self.robot.lift)

	def execute (self):
		self.robot.lift.down()