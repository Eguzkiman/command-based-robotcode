from wpilib.command import CommandGroup
import commandbased.flowcontrol as fc

from commands.DriveFor import DriveFor
from commands.Observe import Observe

class Auto (CommandGroup):

	def __init__ (self):
		super().__init__('auto')

		self.addSequential(Observe())

		@fc.IF(lambda: self.robot.sd.getValue('autoDirection', 0) == 'left')
		def driveLeft (self):
			self.addSequential(DriveFor(seconds=6, direction=(0, -1)))

		@fc.ELIF(lambda: self.robot.sd.getValue('autoDirection', 0) == 'right')
		def driveRight (self):
			self.addSequential(DriveFor(seconds=6, direction=(0, 1)))