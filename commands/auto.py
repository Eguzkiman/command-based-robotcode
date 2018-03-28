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
		self.chooser.addDefault('Dumb Auto', 1)
		self.chooser.addObject('Left Auto', 2)
		self.chooser.addObject('Right Auto', 3)

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
