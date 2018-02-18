from wpilib.command import TimedCommand

class MoveArmFor (TimedCommand):
	def __init__ (self, seconds, power):
		super().__init__('Move Arm for', seconds)
		self.requires(self.robot.Arm)

		self.power = power


	def execute (self):

		self.robot.Arm.move_arm(self.power)

	def end(self):
		
		self.robot.Arm.move_arm(0)

