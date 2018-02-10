import wpilib
from wpilib.command.subsystem import Subsystem
from commands.MoveLift import MoveLift

class Lift(Subsystem):
	def __init__(self):
		super().__init__()

		self.lift1 = wpilib.Jaguar(4)
		self.lift2 = wpilib.Jaguar(5)
		self.drop1 = wpilib.Jaguar(6)

	def up(self):
		self.lift1.set(.8)
		self.lift2.set(.8)
		self.drop1.set(0)

	def down(self):
		self.lift1.set(-.8)
		self.lift2.set(-.8)
		self.drop1.set(0)

	def drop(self):
		self.lift1.set(0)
		self.lift2.set(0)
		self.drop1.set(1)

	def stop(self):
		self.lift1.set(0)
		self.lift2.set(0)
		self.drop1.set(0)

	def move(self, power=0):
		self.lift1.set(power)
		self.lift2.set(power)

	def initDefaultCommand (self):
		self.setDefaultCommand(MoveLift())

