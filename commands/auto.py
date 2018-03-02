from wpilib.command import CommandGroup
import commandbased.flowcontrol as fc

from commands.DriveFor import DriveFor
from commands.MoveClawFor import MoveClawFor
from commands.MoveArmFor import MoveArmFor
from commands.Observe import Observe
from commands.Align import Align

class Auto (CommandGroup):

	def __init__ (self):
		super().__init__('auto')

		self.addSequential(MoveClawFor(seconds=0.5, power=-0.5))
		self.addSequential(Observe())

		@fc.IF(lambda: self.robot.autoDirection == 'L')
		def driveLeft (self):
			self.addSequential(DriveFor(seconds=2, direction=(0, -0.6)))
			self.addSequential(Align())
			self.addSequential(MoveArmFor(seconds=1, power=1))
			self.addSequential(MoveClawFor(seconds=0.5, power=0.5))

		@fc.ELIF(lambda: self.robot.autoDirection == 'R')
		def driveRight (self):
			self.addSequential(DriveFor(seconds=2, direction=(0, 0.6)))
			self.addSequential(Align())
			self.addSequential(MoveArmFor(seconds=1, power=1))
			self.addSequential(MoveClawFor(seconds=0.5, power=0.5))

		@fc.ELSE
		def goForward(self):
			self.addSequential(DriveFor(seconds=3, direction=(0.7, 0)))
			self.addSequential(Align())
			self.addSequential(MoveArmFor(seconds=1, power=1))
			self.addSequential(MoveClawFor(seconds=0.5, power=0.5))
