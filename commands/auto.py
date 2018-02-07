from wpilib.command import CommandGroup
import commandbased.flowcontrol as fc

from commands.DriveFor import DriveFor

def flipCoin ():
	return False


class Auto (CommandGroup):

	def __init__ (self):
		super().__init__('auto')

		self.addSequential(DriveFor(seconds=6, direction=(1,0)))

		# @fc.IF(flipCoin)
		# def driveForward(self):
		# 	self.addSequential(DriveForwardFor(seconds=3))

		# @fc.ELSE
		# def driveBackwards(self):
		# 	self.addSequential(DriveBackwardsFor(seconds=3))
