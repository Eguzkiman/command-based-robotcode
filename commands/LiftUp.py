from wpilib.command import Command

class LiftUp (Command):

	def __init__ (self):
		super().__init__('Follow Joystick')
		self.requires(self.robot.lift)

	def execute (self):

