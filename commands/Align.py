import wpilib
from wpilib.command import Command

class Align (Command):

	def __init__ (self):
		super().__init__('Align') 
		self.requires(self.robot.drivetrain)
		# self.max_distance = 700

	def execute (self):
		right = self.robot.drivetrain.left_ultra.getRangeMM()
		left = self.robot.drivetrain.right_ultra.getRangeMM()
		front = self.robot.drivetrain.front_ultra.getRangeMM()
		
		wpilib.DriverStation.reportWarning('left: ' + str(left), False)
		wpilib.DriverStation.reportWarning('right: ' + str(right), False)
		wpilib.DriverStation.reportWarning('front: ' + str(front), False)



		# left = self.robot.drivetrain.left_analog.getVoltage()
		# right = self.robot.drivetrain.right_analog.getVoltage()	  

		# if left >= 10 and left <= 400 and right >= 10 and right <= 400 and front >= 10 and front <= 400:
		# 	self.cancel()
		# elif left > 400 and left < self.max_distance:
		# 	self.robot.drivetrain.driveManual(-1, 0)
		# 	self.max_distance = 800
		# elif right > 400 and right < self.max_distance:
		# 	self.robot.drivetrain.driveManual(1, 0)
		# 		self.max_distance = 800
		# elif front > 400 and front < self.max_distance:
		# 	self.robot.drivetrain.driveManual(0,0.5)
		
		# else:
		# 	pass



#0, 400