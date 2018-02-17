from wpilib.command import Command

class MoveClawTo (Command):
	def __init__ (self, power=0):
		super().__init__('Move Claw')
		self.requires(self.robot.Arm)

		self.power = power


	def execute (self):

		self.robot.Arm.move_claw(self.power)
