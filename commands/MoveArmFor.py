from wpilib.command import TimedCommand

class MoveArmFor (TimedCommand):
	def __init__ (self, seconds, power=0):
		super().__init__('Move Arm For', seconds)
		self.requires(self.robot.Arm)

		self.power = power

	def execute (self):
		self.robot.Arm.move_arm(self.power)

	def end (self):
		self.robot.Arm.move_arm(0)

