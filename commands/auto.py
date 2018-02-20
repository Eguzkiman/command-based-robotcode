from wpilib.command import CommandGroup
import commandbased.flowcontrol as fc

from commands.DriveFor import DriveFor
from commands.Observe import Observe
from networktables.util import ntproperty

class Auto (CommandGroup):
	target = ntproperty('/target', 0)

	def __init__ (self):
		super().__init__('auto')

		self.addSequential(Observe())

		@fc.IF(lambda: self.target == 'left')
		def driveLeft (self):
			self.addSequential(DriveFor(seconds=6, direction=(0, -1)))

		@fc.ELIF(lambda: self.target == 'right')
		def driveRight (self):
			self.addSequential(DriveFor(seconds=6, direction=(0, 1)))