from wpilib.command import CommandGroup
import commandbased.flowcontrol as fc

from commands.DriveFor import DriveFor
from commands.MoveClawFor import MoveClawFor
from commands.Align import Align

class Auto (CommandGroup):

	def __init__ (self):
		super().__init__('auto')

		self.addSequential(MoveClawFor(seconds=0.5, power=-0.5))

		@fc.IF(lambda: self.robot.sd.getValue('autoDirection', 0) == 'left')
		def driveLeft (self):
			self.addSequential(DriveFor(seconds=2, direction=(0, -0.6)))
			# self.addSequential(Align())

		@fc.ELIF(lambda: self.robot.sd.getValue('autoDirection', 0) == 'right')
		def driveRight (self):
			self.addSequential(DriveFor(seconds=2, direction=(0, 0.6)))
			# self.addSequential(Align())

		@fc.ELSE
		def goForward(self):
			self.addSequential(DriveFor(seconds=3, direction=(0.7, 0)))
