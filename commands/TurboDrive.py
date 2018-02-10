from wpilib.command import Command

class TurboDrive (Command):

	def __init__ (self):
		super().__init__('Follow Joystick')
		self.requires(self.robot.drivetrain)

	def execute (self):
		powerY = self.robot.joystick.getY()
		powerX = self.robot.joystick.getRawAxis(4)

		self.robot.drivetrain.driveManual(powerX, powerY)