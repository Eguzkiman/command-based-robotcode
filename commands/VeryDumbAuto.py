from wpilib.command import CommandGroup
import commandbased.flowcontrol as fc
from commands.DriveFor import DriveFor
from commands.MoveClawFor import MoveClawFor
from commands.Align import Align

class VeryDumbAuto (CommandGroup):

	def __init__ (self):
		super().__init__('auto')

		self.addSequential(MoveClawFor(seconds=0.5, power=-0.5))
		self.addSequential(DriveFor(seconds=3, direction=(0.7, 0, 0)))
