import wpilib
from commandbased import CommandBasedRobot
from wpilib.command import Command

from oi import OI

from subsystems.drivetrain import Drivetrain

class MyRobot (CommandBasedRobot):
	def robotInit (self):
		Command.robot = self

		# Init subsystems
		self.drivetrain = Drivetrain()

		# Init oi
		self.oi = OI(self)

		# Init commands

if __name__ == '__main__':
	wpilib.run(MyRobot)