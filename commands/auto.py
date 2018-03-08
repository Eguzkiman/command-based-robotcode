from wpilib.command import CommandGroup
import commandbased.flowcontrol as fc

from commands.DriveFor import DriveFor
from commands.MoveClawFor import MoveClawFor
from commands.MoveArmFor import MoveArmFor
from commands.Align import Align

class Auto (CommandGroup):

	def __init__ (self):
		super().__init__('auto')

		self.addSequential(MoveClawFor(seconds=0.5, power=-0.5))
		# self.addSequential(DriveFor(seconds=4.5, direction=(-0.45, 0)))

		@fc.IF(lambda: self.robot.autoDirection == 'L')
		def driveLeft (self):
			self.addSequential(DriveFor(seconds=1, direction=(-0.45, -0.9)))
			self.addSequential(DriveFor(seconds=3, direction=(-0.45, 0)))
			self.addSequential(DriveFor(seconds=1, direction=(-0.45, 0.9)))
			self.addSequential(Align())
			self.addSequential(MoveArmFor(seconds=2, power=1))
			self.addSequential(MoveClawFor(seconds=0.6, power=0.7))
			self.addSequential(MoveArmFor(seconds=2, power=-1))
			# self.addSequential(DriveFor(seconds=6, direction=(-0.45, 0)))
			# self.addSequential(Align())
			# self.addSequential(MoveArmFor(seconds=1, power=1))
			# self.addSequential(MoveClawFor(seconds=0.5, power=0.5))

		@fc.ELIF(lambda: self.robot.autoDirection == 'R')
		def driveRight (self):
			# self.addSequential(DriveFor(seconds=2.5, direction=(-5.0, 0)))
			self.addSequential(DriveFor(seconds=6, direction=(-0.45, 0)))
			# self.addSequential(Align())
			self.addSequential(MoveArmFor(seconds=2, power=1))
			self.addSequential(MoveClawFor(seconds=0.6, power=0.7))
			self.addSequential(MoveArmFor(seconds=2, power=-1))
		@fc.ELSE
		def goForward(self):
			self.addSequential(DriveFor(seconds=6, direction=(-0.45, 0)))
			# # self.addSequential(Align())
			# self.addSequential(MoveArmFor(seconds=2, power=1))
			# self.addSequential(MoveClawFor(seconds=1, power=0.7))
			# self.addSequential(MoveArmFor(seconds=2, power=-1))
			# self.addSequential(MoveArmFor(seconds=1, power=1))
			# self.addSequential(MoveClawFor(seconds=0.5, power=0.5))

