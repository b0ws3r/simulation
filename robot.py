from pyrosim.neuralNetwork import NEURAL_NETWORK
from sensor import SENSOR
from motor import MOTOR
import pyrosim.pyrosim as pyrosim
import pybullet as p
import os
import constants as c

class ROBOT:
		
	def __init__(self, solutionID):
		self.motors = {}
		self.sensors = {}
		self.solutionID = solutionID
		self.nn = NEURAL_NETWORK("brain" + str(solutionID) + ".nndf")
		self.robot = bodyId = p.loadURDF("body.urdf")
		pyrosim.Prepare_To_Simulate("body.urdf")
		self.Prepare_To_Sense()
		for jointName in pyrosim.jointNamesToIndices:
			self.motors[jointName] = MOTOR(jointName, self.nn)
		# only save the last runs for fast simulation
		if int(solutionID) < c.populationSize*(c.numberOfGenerations-1):
			os.system("rm brain" + str(solutionID) + ".nndf")

	def Prepare_To_Sense(self):
		for linkName in pyrosim.linkNamesToIndices:
			self.sensors[linkName] = SENSOR(linkName)

	def Sense(self, t):
		for sensor in self.sensors:
			self.sensors[sensor].Get_Value(t)

	def Think(self):
		self.nn.Update()
		# self.nn.Print()

	def Act(self):
		for motor in self.motors:
			self.motors[motor].Set_Value(self.robot)

	def Get_Fitness(self):
		stateOfLink0 = p.getLinkState(self.robot, 0)
		# print("Get_Fitness state of Link 0: " + str(stateOfLink0))
		positionOfLink0 = stateOfLink0[0]
		xCoordinateOfLink0 = positionOfLink0[0]
		solId = str(self.solutionID)
		tempFileName = "data.nosync/tmp" + solId + ".txt"
		f = open(tempFileName, "w")
		f.write(str(xCoordinateOfLink0))
		os.system("mv " + tempFileName + " data.nosync/fitness" + solId + ".txt")
		exit()
