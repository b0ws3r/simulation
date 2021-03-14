import pybullet_data
from world import WORLD
from robot import ROBOT
import pybullet as p
import constants as c
import time


class SIMULATION:
	def __init__(self):
		# Init pybullet simulation components (world, plane, robot, etc.)
		self.physicsClient = p.connect(p.GUI)
		p.setAdditionalSearchPath(pybullet_data.getDataPath())
		p.setGravity(0,0,-9.8)
		self.world = WORLD()
		self.robot = ROBOT()

	def Run(self):
		for t in range(0, c.simulationSteps):
			time.sleep(0.016667)
			p.stepSimulation()
			self.robot.Sense(t)
			self.robot.Act(t)

	def __del__(self):
		p.disconnect()