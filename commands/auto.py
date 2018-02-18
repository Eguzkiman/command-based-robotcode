from wpilib.command import CommandGroup
import commandbased.flowcontrol as fc

from commands.DriveFor import DriveFor
from commands.Observe import Observe
from networktables import NetworkTables

class Auto (CommandGroup):

	def __init__ (self):
		super().__init__('auto')
		self.addSequential(Observe())
		NetworkTables.initialize(server='roborio-5716-frc.local')
		self.sd = NetworkTables.getTable('SmartDashboard')

		@fc.IF(lambda: self.sd.getValue('autoDirection', 0) == 'left')
		def driveLeft (self):
			self.addSequential(DriveFor(seconds=6, direction=(0, -1)))

		@fc.ELIF(lambda: self.sd.getValue('autoDirection', 0) == 'right')
		def driveRight (self):
			self.addSequential(DriveFor(seconds=6, direction=(0, 1)))

		# @fc.IF(flipCoin)
		# def driveForward(self):
		# 	self.addSequential(DriveForwardFor(seconds=3))

		# @fc.ELSE
		# def driveBackwards(self):
		# 	self.addSequential(DriveBackwardsFor(seconds=3))
