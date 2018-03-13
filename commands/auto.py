import wpilib
from wpilib.command import Command
from commands.DriveFor import DriveFor
from commands.MoveClawFor import MoveClawFor
from commands.MoveArmFor import MoveArmFor
from commands.Align import Align
from commands.rightauto import RightAuto
from commands.leftauto import LeftAuto
from commands.VeryDumbAuto import VeryDumbAuto

class Auto (Command):

	def __init__ (self):
		self.chooser = wpilib.SendableChooser()
		self.chooser.addDefault('Dumb auto', 1)
		self.chooser.addObject('Left auto', 2)
		self.chooser.addObject('Right auto', 3)

		wpilib.SmartDashboard.putData('Autonomous Mode', self.chooser)

	def start (self):
		if  self.chooser.getSelected()== 1:
			self.VeryDumbAuto = VeryDumbAuto()
			self.VeryDumbAuto.start()

		elif self.chooser.getSelected()== 2:
			self.LeftAuto = LeftAuto()
			self.LeftAuto.start()

		elif self.chooser.getSelected()== 3:
			self.RightAuto = RightAuto()
			self.RightAuto.start()
		


		# self.addSequential(MoveClawFor(seconds=0.5, power=-0.5))
		# self.addSequential(Observe())

		"""@fc.IF(lambda: self.robot.autoDirection == 'L')
		def driveLeft (self):
			self.addSequential(DriveFor(seconds=2, direction=(0, -0.6)))
			# self.addSequential(Align())
			# self.addSequential(MoveArmFor(seconds=1, power=1))
			# self.addSequential(MoveClawFor(seconds=0.5, power=0.5))

		@fc.ELIF(lambda: self.robot.autoDirection == 'R')
		def driveRight (self):
			self.addSequential(DriveFor(seconds=2, direction=(0, 0.6)))
			self.addSequential(Align())
			self.addSequential(MoveArmFor(seconds=1, power=1))
			self.addSequential(MoveClawFor(seconds=0.5, power=0.5))

		@fc.ELSE
		def goForward(self):
			self.addSequential(DriveFor(seconds=3, direction=(0.7, 0)))
			# self.addSequential(Align())
			# self.addSequential(MoveArmFor(seconds=1, power=1))
			# self.addSequential(MoveClawFor(seconds=0.5, power=0.5))"""

