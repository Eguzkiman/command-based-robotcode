import wpilib
from wpilib.command import CommandGroup
import commandbased.flowcontrol as fc
from commands.DriveFor import DriveFor
from commands.MoveClawFor import MoveClawFor
from commands.MoveArmFor import MoveArmFor
from commands.Align import Align
from commands.Observe import Observe

class LeftNotMonarchEAuto (CommandGroup):

	def __init__ (self):
		super().__init__('MonarchE Auto') 
		self.requires(self.robot.drivetrain)

		self.addSequential(Observe())

		@fc.IF(lambda: self.robot.autoDirection == 'L')
		def driveAndDrop (self):

			self.addSequential(MoveClawFor(seconds=0.5, power=-0.5))
			self.addSequential(DriveFor(seconds=3, direction=(-0.6, 0, 0)))     
			self.addSequential(MoveArmFor(seconds=1, power=1))
			self.addSequential(MoveClawFor(seconds=0.5, power=0.5))
			self.addSequential(MoveArmFor(seconds=1, power=-1))


		@fc.ELIF(lambda: self.robot.autoDirection == 'R')
		def driveAndDrop (self):

			self.addSequential(MoveClawFor(seconds=0.5, power=-0.5))
			self.addSequential(DriveFor(seconds=3, direction=(-0.6, 0, 0))) 

