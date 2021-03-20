from pyrosim.neuralNetwork import NEURAL_NETWORK
from sensor import SENSOR
from motor import MOTOR
import pyrosim.pyrosim as pyrosim
import pybullet as p
import constants as c

class ROBOT:
		
	def __init__(self):
		self.motors = {}
		self.sensors = {}
		self.nn = NEURAL_NETWORK("brain.nndf")
		self.robot = bodyId = p.loadURDF("body.urdf")
		pyrosim.Prepare_To_Simulate("body.urdf")
		self.Prepare_To_Sense()

	def Prepare_To_Sense(self):
		for linkName in pyrosim.linkNamesToIndices:
			self.sensors[linkName] = SENSOR(linkName)

	def Sense(self, t):
		for sensor in self.sensors:
			self.sensors[sensor].Get_Value(t)

	def Act(self, desiredAngle):
		for motor in self.motors:
			self.motors[motor].Set_Value(desiredAngle, self.robot)

	def Think(self, t):
		self.nn.Update()
		self.nn.Print()


