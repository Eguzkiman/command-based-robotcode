from wpilib.command import CommandGroup
import commandbased.flowcontrol as fc

from commands.DriveFor import DriveFor
from commands.MoveClawFor import MoveClawFor
from commands.Observe import Observe

class Auto (CommandGroup):

	def __init__ (self):
		super().__init__('auto')

		self.addSequential(MoveClawFor(seconds=1, power=-0.5))
		self.addSequential(Observe())

		@fc.IF(lambda: self.robot.sd.getValue('autoDirection', 0) == 'left')
		def driveLeft (self):
			self.addSequential(DriveFor(seconds=2, direction=(0, -0.6)))

		@fc.ELIF(lambda: self.robot.sd.getValue('autoDirection', 0) == 'right')
		def driveRight (self):
			self.addSequential(DriveFor(seconds=2, direction=(0, 0.6)))

		@fc.ELSE
		def goForward(self):
			self.addSequential(DriveFor(seconds=3, direction=(0.7, 0)))
