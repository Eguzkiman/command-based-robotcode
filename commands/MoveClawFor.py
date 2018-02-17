from wpilib.command import TimedCommand

class MoveClawFor (TimedCommand):
	def __init__ (self, seconds ,power=0):
		super().__init__('Move Claw for', seconds)
		self.requires(self.robot.Arm)

		self.power = power


	def execute (self):

		self.robot.Arm.move_claw(seconds, self.power)

 