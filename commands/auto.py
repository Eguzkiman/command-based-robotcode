from wpilib.command import CommandGroup
import commandbased.flowcontrol as fc

from commands.DriveFor import DriveFor
from commands.MoveClawFor import MoveClawFor
from commands.MoveArmFor import MoveArmFor


def flipCoin ():
	pass


class Auto (CommandGroup):

	def __init__ (self):
		super().__init__('auto')


		self.addSequential(MoveArmFor(seconds=3, power=1))

		self.addSequential(MoveClawFor(seconds=2, power=-1))

		self.addSequential(MoveClawFor(seconds=4, power=1))

		self.addSequential(MoveArmFor(seconds=3, power=-1))

		self.addSequential(MoveClawFor(seconds=4, power=1))

		# @fc.IF(flipCoin)
		# def driveForward(self):
		# 	self.addSequential(DriveForwardFor(seconds=3))

		# bajar agarra sube

		# suelta

		# subir




		# @fc.ELSE
		# def driveBackwards(self):
		# 	self.addSequential(DriveBackwardsFor(seconds=3))
