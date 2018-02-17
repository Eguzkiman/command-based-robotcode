import wpilib
from wpilib.command.subsystem import Subsystem
from commands.LiftStop import LiftStop

class Clock(Subsystem):
	def __init__(self):
		super().__init__()

		self.clock_motor = wpilib.Jaguar(4)
		self.claw = wpilib.Jaguar(5)

	def grab(self):
		self.clock_motor.set(1)

	def release(self):
		self.clock_motor.set(-1)

	def initDefaultCommand (self):
		self.setDefaultCommand(LiftStop())




