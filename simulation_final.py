import pybullet_data
from world_final import WORLD_FINAL
from robot_finalsim import ROBOT_FINAL
import pybullet as p
import constants as c
import time


class SIMULATION_FINAL:
	def __init__(self, directOrGUI, brainFileName, worldyfilename):
		# Init pybullet simulation components (world, plane, robot, etc.)
		mode = p.DIRECT if directOrGUI == "DIRECT" else p.GUI
		self.physicsClient = p.connect(mode)
		p.setAdditionalSearchPath(pybullet_data.getDataPath())
		p.setGravity(0, 0, -9.8)
		self.world = WORLD_FINAL(worldyfilename)
		self.robot = ROBOT_FINAL(brainFileName)
		self.directOrGui = directOrGUI
		

	def Run(self):
		for t in range(0, c.simulationSteps):
			if self.directOrGui == 'GUI':
				time.sleep(0.0000167)
			p.stepSimulation()
			self.robot.Sense(t)
			self.robot.Think()
			self.robot.Act()

	def Get_Fitness(self):
		self.robot.Get_Fitness()

	def __del__(self):
		p.disconnect()
