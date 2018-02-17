import wpilib
from wpilib.command.subsystem import Subsystem

class Arm(Subsystem):
	def __init__(self):
		super().__init__()

		self.arm_motor = wpilib.Jaguar(4)
		self.claw = wpilib.Jaguar(5)

	def move_claw(self, power):
	 	self.claw.set(power)

	def move_arm(self, power):
	 	self.arm_motor.set(power) 	
