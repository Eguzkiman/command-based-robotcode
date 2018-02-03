from wpilib.command import Command

class FollowJoystick (Command):

	def __init__ (self):
		super().__init__('Follow Joystick')
		self.requires(self.robot.drivetrain)

	def execute (self):
		powerY = self.robot.joystick.getY() * 0.7
		powerX = self.robot.joystick.getX() * 0.7

		self.robot.drivetrain.driveManual(powerY, powerX)