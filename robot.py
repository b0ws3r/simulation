from sensor import SENSOR
from motor import MOTOR
import pyrosim.pyrosim as pyrosim
import pybullet as p
import constants as c

class ROBOT:
		
	def __init__(self):
		self.motors = {}
		self.sensors = {}
		self.robot = bodyId = p.loadURDF("body.urdf")
		pyrosim.Prepare_To_Simulate("body.urdf")
		self.Prepare_To_Sense()
		self.Prepare_To_Act()

	def Prepare_To_Sense(self):
		for linkName in pyrosim.linkNamesToIndices:
			self.sensors[linkName] = SENSOR(linkName)

	def Sense(self, t):
		for sensor in self.sensors:
			self.sensors[sensor].Get_Value(t)

	def Prepare_To_Act(self):
		for jointName in pyrosim.jointNamesToIndices:
			if jointName == "Torso_backLeg":
				self.motors[jointName] = MOTOR(jointName, c.FL_frequency, c.FL_amplitude, c.FL_phaseOffset)
			else:
				self.motors[jointName] = MOTOR(jointName, c.FL_frequency/2, c.FL_amplitude, c.FL_phaseOffset)

	def Act(self, t):
		for motor in self.motors:
			self.motors[motor].Set_Value(t, self.robot)
