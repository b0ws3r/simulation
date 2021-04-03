import pybullet_data
from world import WORLD
from robot import ROBOT
import pybullet as p
import constants as c
import time


class SIMULATION:
	def __init__(self, directOrGUI):
		# Init pybullet simulation components (world, plane, robot, etc.)
		mode = p.DIRECT if directOrGUI == "DIRECT" else p.GUI
		self.physicsClient = p.connect(mode)
		p.setAdditionalSearchPath(pybullet_data.getDataPath())
		p.setGravity(0, 0, -9.8)
		self.world = WORLD()
		self.robot = ROBOT()
		self.directOrGui = directOrGUI

	def Run(self):
		for t in range(0, c.simulationSteps):
			if self.directOrGui == 'GUI':
				time.sleep(0.016667)
			p.stepSimulation()
			self.robot.Sense(t)
			self.robot.Think()
			self.robot.Act()

	def Get_Fitness(self):
		self.robot.Get_Fitness()

	def __del__(self):
		p.disconnect()