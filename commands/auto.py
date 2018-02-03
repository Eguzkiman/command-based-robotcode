from wpilib.command import CommandGroup

from commands.DriveForwardFor import DriveForwardFor
from commands.DriveBackwardsFor import DriveBackwardsFor

class Auto (CommandGroup):

	def __init__ (self):
		super().__init__('auto')
		self.addSequential(DriveForwardFor(seconds=3))
		self.addSequential(DriveBackwardsFor(seconds=3))
