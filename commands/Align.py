import wpilib
from wpilib.command import Command

class Align (Command):

	def __init__ (self):
		super().__init__('Align') 
		self.requires(self.robot.drivetrain)

	def execute (self):
		right = self.robot.drivetrain.left_ultra.getRangeMM()
		lefth = self.robot.drivetrain.right_ultra.getRangeMM()
		
		wpilib.DriverStation.reportWarning('left: ' + str(left), False)
		wpilib.DriverStation.reportWarning('right: ' + str(right), False)
		# left = self.robot.drivetrain.left_analog.getVoltage()
		# right = self.robot.drivetrain.right_analog.getVoltage()	  

		if left >= 10 and left <= 400 and right >= 10 and right <= 400:
			self.cancel()
		elif left > 400 and left < 700:
			self.robot.drivetrain.driveManual(-1, 0)
		elif right > 400 and right < 700:
			self.robot.drivetrain.driveManual(1, 0)
		
		else:
			self.robot.drivetrain.driveManual(0, 0.5) #02-0.200




#0, 400