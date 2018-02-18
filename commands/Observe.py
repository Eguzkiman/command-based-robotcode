from wpilib.command import TimedCommand
from networktables import NetworkTables

class Observe (TimedCommand):
	def __init__ (self, seconds = 5):
		super().__init__('Observe', seconds)
		self.requires(self.robot.drivetrain)
		NetworkTables.initialize(server='roborio-5716-frc.local')
		self.sd = NetworkTables.getTable('SmartDashboard')


	def execute (self):
		direction = self.sd.getValue('autoDirection', 0)

		if direction:
			# self.robot.autoDirection = direction
			self.cancel()



