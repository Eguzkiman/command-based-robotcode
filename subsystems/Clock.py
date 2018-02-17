import wpilib
from wpilib.command.subsystem import Subsystem
from commands.LiftStop import LiftStop

class Arm(Subsystem):
	def __init__(self):
		super().__init__()

		self.arm_motor = wpilib.Jaguar(4)
		self.claw = wpilib.Jaguar(5)

	def grab(self):
		self.arm_motor.set(1)

	def release(self):
		self.arm_motor.set(-1)

	def initDefaultCommand (self):
		self.setDefaultCommand(LiftStop())




