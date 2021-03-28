import pyrosim.pyrosim as pyrosim
import constants as c
import numpy
import random
import os


class SOLUTION:

    def __init__(self):
        c = numpy.zeros(2)
        self.weights = numpy.array([c, c, c])
        for i in range(0, len(self.weights)):
            for j in range(0, len(c)):
                self.weights[i][j] = numpy.random.rand()
        self.weights = self.weights*2-1

    def Evaluate(self, directOrGui):
        self.Create_World()
        self.Create_Body()
        self.Create_Brain()
        os.system("python3 simulate.py " + directOrGui)
        f = open("fitness.txt")
        xcoord_Link0 = float(f.read())
        self.fitness = xcoord_Link0

    def Create_World(self):
        pyrosim.Start_SDF("world.sdf")
        pyrosim.Send_Cube(name="Boc.x", pos=[c.x - 3, c.y - 3, c.z], size=[c.length, c.width, c.height])
        pyrosim.End()

    def Create_Body(self):
        pyrosim.Start_URDF("body.urdf")
        pyrosim.Send_Cube(name="Torso", pos=[c.x, c.y, c.z + 1], size=[c.length, c.width, c.height])
        pyrosim.Send_Joint(name="Torso_backLeg", parent="Torso", child="backLeg", type="revolute", position="-.5 0 1")
        pyrosim.Send_Cube(name="backLeg", pos=[-.5, 0, -.5], size=[c.length, c.width, c.height])
        pyrosim.Send_Joint(name="Torso_frontLeg", parent="Torso", child="frontLeg", type="revolute", position=".5 0 1")
        pyrosim.Send_Cube(name="frontLeg", pos=[.5, 0, -.5], size=[c.length, c.width, c.height])
        pyrosim.End()

    def Create_Brain(self):
        pyrosim.Start_NeuralNetwork("brain.nndf")
        pyrosim.Send_Sensor_Neuron(name=0, linkName="Torso")
        pyrosim.Send_Sensor_Neuron(name=1, linkName="backLeg")
        pyrosim.Send_Sensor_Neuron(name=2, linkName="frontLeg")
        pyrosim.Send_Motor_Neuron(name=3, jointName="Torso_backLeg")
        pyrosim.Send_Motor_Neuron(name=4, jointName="Torso_frontLeg")
        for i in range(0, len(self.weights)):
            for j in range(0, len(self.weights[i])):
                pyrosim.Send_Synapse(sourceNeuronName=i, targetNeuronName=j+3, weight=self.weights[i][j])
        pyrosim.End()

    def Mutate(self):
        synapseToMutate = random.randint(-1, 1)
        preOrPostSynapticNeuron = random.randint(0, 1)
        self.weights[synapseToMutate][preOrPostSynapticNeuron] = random.random() * 2 - 1
