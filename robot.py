import wpilib
from commandbased import CommandBasedRobot
from wpilib.command import Command
from oi import OI
from subsystems.drivetrain import Drivetrain
from subsystems.Lift import Lift

from commands.auto import Auto


class MyRobot (CommandBasedRobot):
	def robotInit (self):

		wpilib.CameraServer.launch('vision.py:main')
		Command.robot = self

		# Init subsystems
		self.drivetrain = Drivetrain()
		self.lift = Lift()

		# Init oi
		self.oi = OI(self)

		# Init commands
		self.auto = Auto()


	def autonomousInit (self):
		self.auto.start()


if __name__ == '__main__':
	wpilib.run(MyRobot)