from wpilib.command import Command

class FollowJoystick (Command):

	def __init__ (self):
		super().__init__('Follow Joystick')
		self.requires(self.robot.drivetrain)

	def execute (self):
		self.robot.drivetrain.driveManual(self.robot.joystick.getY(), self.robot.joystick.getX())