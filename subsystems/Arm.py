import wpilib
from wpilib.command.subsystem import Subsystem

class Arm(Subsystem):
	def __init__(self):
		super().__init__()

		self.arm_motor = wpilib.Jaguar(4)
		self.claw = wpilib.Jaguar(5)

		self.max_sensor = wpilib.DigitalInput(6)

	def move_claw(self, power):
		if self.max_sensor.get():
			power = max(0, power)
		self.claw.set(power)
		wpilib.DriverStation.reportWarning('Contact_sensor: ' + str(self.max_sensor.get()), False)

	def move_arm(self, power):
	 	self.arm_motor.set(power)
