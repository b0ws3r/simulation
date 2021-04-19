import catch as catch

import pyrosim.pyrosim as pyrosim
import constants as c
import numpy
import random
import os
import time

class SOLUTION:

    def __init__(self, nextAvailableID):
        self.myID = nextAvailableID
        self.weights = numpy.zeros((c.numMotorNeurons, c.numSensorNeurons))
        for i in range(0, len(self.weights)):
            for j in range(0, len(self.weights[i])):
                self.weights[i][j] = numpy.random.rand()
        self.weights = self.weights*2-1

    def Evaluate(self, directOrGui):
        # self.Create_World()
        # self.Create_Body()
        self.Create_Brain()
        os.system("python3 simulate.py " + directOrGui + " " + str(self.myID) + "  2&>1 &")

    def Start_Simulation(self, directOrGui):
        self.Create_World()
        self.Create_Body()
        self.Create_Brain()
        os.system("python3 simulate.py " + directOrGui + " " + str(self.myID) + " 2&>1 &")


    def Wait_For_Simulation_To_End(self):
        fitnessFileName = "data.nosync/fitness" + str(self.myID) + ".txt"
        while not os.path.exists(fitnessFileName):
            time.sleep(0.1)
        f = open(fitnessFileName)
        try:
            xcoord_Link0 = float(f.read())
            self.fitness = xcoord_Link0

        except:
            print(fitnessFileName + " could not be read")
        finally:
            os.system("rm " + fitnessFileName)


    def Create_World(self):
        pyrosim.Start_SDF("world.sdf")
        pyrosim.Send_Cube(name="Box", pos=[c.x - 3, c.y - 3, c.z], size=[c.length, c.width, c.height])
        pyrosim.End()

    def Create_Body(self):
        pyrosim.Start_URDF("body.urdf")
        pyrosim.Send_Cube(name="Torso", pos=[c.x, c.y,  1], size=[c.length, c.width, c.height])

        # joint from front torso to back leg
        pyrosim.Send_Joint(name="Torso_backLeg", parent="Torso", child="backLeg", type="revolute", position="0 -0.5 1",
                           jointAxis="1 0 0")
        pyrosim.Send_Cube(name="backLeg", pos=[0, -.5, 0], size=[c.length/5, c.width, c.height/5])

        # joint from front torso to front leg
        pyrosim.Send_Joint(name="Torso_frontLeg", parent="Torso", child="frontLeg", type="revolute", position="0 .5 1",
                           jointAxis="1 0 0")
        pyrosim.Send_Cube(name="frontLeg", pos=[0, 0.5, 0], size=[c.length / 5, c.width, c.height / 5])

        # left leg
        pyrosim.Send_Joint(name="Torso_leftLeg", parent="Torso", child="leftLeg", type="revolute", position="-.5 0 1",
                           jointAxis="0 1 0")
        pyrosim.Send_Cube(name="leftLeg", pos=[-.5, 0, 0], size=[c.length, c.width/5, c.height / 5])

        # right leg
        pyrosim.Send_Joint(name="Torso_rightLeg", parent="Torso", child="rightLeg", type="revolute", position=".5 0 1",
                           jointAxis="0 1 0")
        pyrosim.Send_Cube(name="rightLeg", pos=[.5, 0, 0], size=[c.length, c.width / 5, c.height / 5])

        # joint to back foot and foot
        ##############################
        pyrosim.Send_Joint(name="backLeg_backFoot", parent="backLeg", child="backFoot", type="revolute", position="0 -1 0",
                           jointAxis="1 0 0")
        pyrosim.Send_Cube(name="backFoot", pos=[0, 0, -.5], size=[c.length/5, c.width/5, c.height])
        ##############################

        # joint to front foot and foot
        pyrosim.Send_Joint(name="frontLeg_frontFoot", parent="frontLeg", child="frontFoot", type="revolute", position="0 1 0",
                           jointAxis="1 0 0")
        pyrosim.Send_Cube(name="frontFoot", pos=[0, 0, -.5], size=[c.length/5, c.width/5, c.height])

        # joint to left foot and foot
        pyrosim.Send_Joint(name="leftLeg_leftFoot", parent="leftLeg", child="leftFoot", type="revolute", position="-1 0 0",
                           jointAxis="0 1 0")
        pyrosim.Send_Cube(name="leftFoot", pos=[0, 0, -.5], size=[c.length/5, c.width/5, c.height])

        # joint to right foot and foot
        pyrosim.Send_Joint(name="rightLeg_rightFoot", parent="rightLeg", child="rightFoot", type="revolute", position="1 0 0",
                           jointAxis="0 1 0")
        pyrosim.Send_Cube(name="rightFoot", pos=[0, 0, -.5], size=[c.length/5, c.width/5, c.height])

        pyrosim.End()

    def Create_Brain(self):
        pyrosim.Start_NeuralNetwork("brain" + str(self.myID) + ".nndf")
        pyrosim.Send_Sensor_Neuron(name=0, linkName="Torso")
        pyrosim.Send_Sensor_Neuron(name=1, linkName="backLeg")
        pyrosim.Send_Sensor_Neuron(name=2, linkName="frontLeg")
        pyrosim.Send_Sensor_Neuron(name=3, linkName="rightLeg")
        pyrosim.Send_Sensor_Neuron(name=4, linkName="leftLeg")
        pyrosim.Send_Sensor_Neuron(name=5, linkName="frontFoot")
        pyrosim.Send_Sensor_Neuron(name=6, linkName="backFoot")
        pyrosim.Send_Sensor_Neuron(name=6, linkName="leftFoot")
        pyrosim.Send_Sensor_Neuron(name=7, linkName="rightFoot")

        pyrosim.Send_Motor_Neuron(name=3, jointName="Torso_backLeg")
        pyrosim.Send_Motor_Neuron(name=4, jointName="Torso_frontLeg")
        pyrosim.Send_Motor_Neuron(name=5, jointName="Torso_leftLeg")
        pyrosim.Send_Motor_Neuron(name=6, jointName="Torso_rightLeg")
        pyrosim.Send_Motor_Neuron(name=7, jointName="frontLeg_frontFoot")
        pyrosim.Send_Motor_Neuron(name=8, jointName="backLeg_backFoot")
        pyrosim.Send_Motor_Neuron(name=9, jointName="leftLeg_leftFoot")
        pyrosim.Send_Motor_Neuron(name=10, jointName="rightLeg_rightFoot")

        for i in range(0, len(self.weights)):
            for j in range(0, len(self.weights[i])):
                pyrosim.Send_Synapse(sourceNeuronName=i, targetNeuronName=j+3, weight=self.weights[i][j])

        pyrosim.End()

    def Mutate(self):
        synapseToMutate = random.randint(-1, 1)
        preOrPostSynapticNeuron = random.randint(0, 1)
        self.weights[synapseToMutate][preOrPostSynapticNeuron] = random.random() * 2 - 1
    
    def Set_ID(self, nextAvailableID):
        self.myID = nextAvailableID
