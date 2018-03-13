import wpilib
from wpilib.command import Command
from commands.DriveFor import DriveFor
from commands.MoveClawFor import MoveClawFor
from commands.MoveArmFor import MoveArmFor
from commands.Align import Align
from commands.rightauto import RightAuto
from commands.leftauto import LeftAuto
from commands.VeryDumbAuto import VeryDumbAuto
from commands.notlambotauto import NotLambotAuto

class Auto (Command):

	def __init__ (self):
		self.chooser = wpilib.SendableChooser()
		self.chooser.addDefault('Dumb auto', 1)
		self.chooser.addObject('Left auto', 2)
		self.chooser.addObject('Right auto', 3)
		self.chooser.addObject('Not Lambot Auto', 4)


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

		elif self.chooser.getSelected()== 4:
			self.NotLambotAuto = NotLambotAuto()
			self.NotLambotAuto.start()
		
