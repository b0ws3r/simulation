
import pybullet_data
import pybullet as p
import time

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

p.setGravity(0,0,-9.8)
planeId = p.loadURDF("plane.urdf")
p.loadSDF("boxes.sdf")

for x in range(0, 1000):
	time.sleep(0.0166667)
	p.stepSimulation()


p.disconnect()