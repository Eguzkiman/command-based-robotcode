import wpilib
from commandbased import CommandBasedRobot
from wpilib.command import Command
from oi import OI
from subsystems.drivetrain import Drivetrain
from commands.auto import Auto
from commands.MoveArmTo import MoveArmTo
from commands.MoveClawTo import MoveClawTo
from subsystems.Arm import Arm


class MyRobot (CommandBasedRobot):
	def robotInit (self):

		wpilib.CameraServer.launch('vision.py:main')
		Command.robot = self

		# Init subsystems
		self.drivetrain = Drivetrain()

		self.Arm = Arm()

		# Init oi
		self.oi = OI(self)

		# Init commands
		self.auto = Auto()



	def autonomousInit (self):
		self.auto.start()


if __name__ == '__main__':
	wpilib.run(MyRobot)