from wpilib.command import Command

class MoveArmTo (Command):
	def __init__ (self, power=0):
		super().__init__('Move Arm')
		self.requires(self.robot.Arm)

		self.power = power

	def execute (self):

		self.robot.Arm.move_arm(self.power)

	def end (self):

		self.robot.Arm.move_arm(0)

