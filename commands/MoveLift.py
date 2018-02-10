from wpilib.command import InstantCommand

class MoveLift (InstantCommand):

	def __init__ (self):
		super().__init__('Move Lift')
		self.requires(self.robot.lift)

	def execute (self):
		power = self.robot.joystick.getAxis(2)
		self.robot.lift.move(power)

