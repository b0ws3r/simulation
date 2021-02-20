
import pybullet_data
import pybullet as p
import time
import pyrosim.pyrosim as pyrosim
import numpy

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

p.setGravity(0,0,-9.8)
planeId = p.loadURDF("plane.urdf")
bodyId = p.loadURDF("body.urdf")
p.loadSDF("world.sdf")

pyrosim.Prepare_To_Simulate("body.urdf")

frontLegSensorValues = numpy.zeros(1000)
backLegSensorValues = numpy.zeros(1000)

for x in range(0, 1000):
	time.sleep(0.0166667)
	p.stepSimulation()
	frontLegSensorValues[x] = pyrosim.Get_Touch_Sensor_Value_For_Link("frontLeg")
	backLegSensorValues[x] = pyrosim.Get_Touch_Sensor_Value_For_Link("backLeg")
	
numpy.save("data/frontLegSensorValues.npy", frontLegSensorValues)
numpy.save("data/backLegSensorValues.npy", backLegSensorValues)
p.disconnect()