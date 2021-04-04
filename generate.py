import pyrosim.pyrosim as pyrosim
import random as random

# def createWorld():
# 	pyrosim.Start_SDF("world.sdf")
# 	pyrosim.Send_Cube(name="Box", pos=[x-3,y-3,z] , size=[length,width,height])
# 	pyrosim.End()

def createRobot():
	# Generate_Body()
	# Generate_Brain()
	pass

# def Generate_Body():
# 	pyrosim.Start_URDF("body.urdf")
# 	pyrosim.Send_Cube(name="Torso", pos=[x, y, z + 1], size=[length, width, height])
# 	pyrosim.Send_Joint(name="Torso_backLeg", parent="Torso", child="backLeg", type="revolute", position="-.5 0 1")
# 	pyrosim.Send_Cube(name="backLeg", pos=[-.5, 0, -.5], size=[length, width, height])
# 	pyrosim.Send_Joint(name="Torso_frontLeg", parent="Torso", child="frontLeg", type="revolute", position=".5 0 1")
# 	pyrosim.Send_Cube(name="frontLeg", pos=[.5, 0, -.5], size=[length, width, height])
# 	pyrosim.End()

def Generate_Brain(solutionID):
	pyrosim.Start_NeuralNetwork("brain" + str(solutionID) + ".nndf")
	pyrosim.Send_Sensor_Neuron(name=0, linkName="Torso")
	pyrosim.Send_Sensor_Neuron(name=1, linkName="backLeg")
	pyrosim.Send_Sensor_Neuron(name=2, linkName="frontLeg")
	pyrosim.Send_Motor_Neuron(name=3, jointName="Torso_backLeg")
	pyrosim.Send_Motor_Neuron(name=4, jointName="Torso_frontLeg")
	for i in pyrosim.sensorNeurons:
		for j in pyrosim.motorNeurons:
			weight = 2*random.random()-1
			pyrosim.Send_Synapse(sourceNeuronName=i, targetNeuronName=j, weight=weight)
	pyrosim.End()


# createWorld()
createRobot()
