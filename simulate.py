
import pybullet_data
import pybullet as p
import time
import pyrosim.pyrosim as pyrosim
import numpy
import random

# Init pybullet simulation components (world, plane, robot, etc.)
physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0,0,-9.8)
planeId = p.loadURDF("plane.urdf")
robot = bodyId = p.loadURDF("body.urdf")
p.loadSDF("world.sdf")
pyrosim.Prepare_To_Simulate("body.urdf")

#Constants
simulationSteps = 1000
pi = numpy.pi


BL_amplitude = pi/4
BL_frequency = 100/(simulationSteps / (2*pi))
BL_phaseOffset = 0

FL_amplitude = pi/4
FL_frequency = 10/(simulationSteps / (2*pi))
FL_phaseOffset = 0

#Arrays for storing data
frontLegSensorValues = numpy.zeros(simulationSteps)
backLegSensorValues = numpy.zeros(simulationSteps)
frontLegTargetAngles = numpy.zeros(simulationSteps)
backLegTargetAngles = numpy.zeros(simulationSteps)

#Populate target values for motors
for x in range(0, simulationSteps):
	frontLegTargetAngles[x] = FL_amplitude * numpy.sin(FL_frequency * x + FL_phaseOffset)
	backLegTargetAngles[x] = BL_amplitude * numpy.sin(BL_frequency * x + BL_phaseOffset)

for x in range(0, simulationSteps):
	time.sleep(0.0166667)
	p.stepSimulation()
	frontLegSensorValues[x] = pyrosim.Get_Touch_Sensor_Value_For_Link("frontLeg")
	backLegSensorValues[x] = pyrosim.Get_Touch_Sensor_Value_For_Link("backLeg")
	pyrosim.Set_Motor_For_Joint(
		bodyIndex = robot
		,jointName = "Torso_backLeg"
		,controlMode = p.POSITION_CONTROL
		,targetPosition = backLegTargetAngles[x]
		,maxForce = 30)
	pyrosim.Set_Motor_For_Joint(
		bodyIndex = robot
		,jointName = "Torso_frontLeg"
		,controlMode = p.POSITION_CONTROL
		,targetPosition = frontLegTargetAngles[x]
		,maxForce = 30)
	
#Save vectors to file for use in analyze.py
numpy.save("data/frontLegTargetAngles.npy", frontLegTargetAngles)
numpy.save("data/backLegTargetAngles.npy", backLegTargetAngles)

# numpy.save("data/frontLegSensorValues.npy", frontLegSensorValues)
# numpy.save("data/backLegSensorValues.npy", backLegSensorValues)
p.disconnect()