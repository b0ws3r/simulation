import catch as catch

import pyrosim.pyrosim as pyrosim
import constants as c
import numpy
import random
import os
import time

class SOLUTION:

    def __init__(self, nextAvailableID, synapseMode):
        self.myID = nextAvailableID
        self.synapseMode = synapseMode

        # Matrices to hold synaptic weights
        self.weights = numpy.zeros((c.numSensorNeurons, c.numMotorNeurons))
        self.sensorToHiddenWeights = numpy.zeros((c.numSensorNeurons*c.numHiddenNeurons))
        self.hiddenToMotorWeights = numpy.zeros((c.numMotorNeurons*c.numHiddenNeurons))
        self.recurrentWeights = numpy.zeros((c.numHiddenNeurons, 2))
        # Set them, depending whether we are using hidden neurons or not.
        self.Set_Synaptic_Weights()

    def Set_Synaptic_Weights(self):
        if self.synapseMode == "HIDDEN" or self.synapseMode == "RNN":
            for i in range(0, len(self.sensorToHiddenWeights)):
                self.sensorToHiddenWeights[i] = numpy.random.rand()
            for i in range(0, len(self.hiddenToMotorWeights)):
                self.hiddenToMotorWeights[i] = numpy.random.rand()
            for i in range(0, c.numHiddenNeurons):
                self.recurrentWeights[i, 0] = numpy.random.rand()
                self.recurrentWeights[i, 1] = numpy.random.rand()

            self.sensorToHiddenWeights = self.sensorToHiddenWeights * 2 - 1
            self.hiddenToMotorWeights = self.hiddenToMotorWeights * 2 - 1
            self.recurrentWeights = self.recurrentWeights *2-1
        else:
            for i in range(0, len(self.weights)):
                for j in range(0, len(self.weights[i])):
                    self.weights[i][j] = numpy.random.rand()
            self.weights = self.weights * 2 - 1

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
        sqr = 5
        for i in range(-1 * sqr, sqr):
            for j in range(-1*sqr, sqr):
                height = numpy.random.rand()/2
                pyrosim.Send_Cube(name="Box" + str(i) + "_" + str(j), pos=[c.x - i, c.y - j, height/2], size=[c.length, c.width, height])
        pyrosim.End()


    def Create_Cruel_World(self):
        pyrosim.Start_SDF("world.sdf")
        sqr = 5
        for i in range(-1 * sqr, sqr):
            for j in range(-1*sqr, sqr):
                height = numpy.random.rand()/2
                pyrosim.Send_Cube(name="Box" + str(i) + "_" + str(j), pos=[c.x - i, c.y - j, height/2], size=[c.length, c.width, height])
        pyrosim.End()

    def Create_Body(self):
        pyrosim.Start_URDF("body.urdf")
        pyrosim.Send_Cube(name="Torso", pos=[c.x, c.y,  c.zStart], size=[c.length, c.width, c.height])

        # joint from front torso to back leg
        pyrosim.Send_Joint(name="Torso_backLeg", parent="Torso", child="backLeg", type="revolute", position="0 -0.5 "+str(c.zStart),
                           jointAxis="1 0 0")
        pyrosim.Send_Cube(name="backLeg", pos=[0, -.5, 0], size=[c.length/5, c.width, c.height/5])

        # joint from front torso to front leg
        pyrosim.Send_Joint(name="Torso_frontLeg", parent="Torso", child="frontLeg", type="revolute", position="0 .5 "+str(c.zStart),
                           jointAxis="1 0 0")
        pyrosim.Send_Cube(name="frontLeg", pos=[0, 0.5, 0], size=[c.length / 5, c.width, c.height / 5])

        # left leg
        pyrosim.Send_Joint(name="Torso_leftLeg", parent="Torso", child="leftLeg", type="revolute", position="-.5 0 "+str(c.zStart),
                           jointAxis="0 1 0")
        pyrosim.Send_Cube(name="leftLeg", pos=[-.5, 0, 0], size=[c.length, c.width/5, c.height / 5])

        # right leg
        pyrosim.Send_Joint(name="Torso_rightLeg", parent="Torso", child="rightLeg", type="revolute", position=".5 0 "+str(c.zStart),
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

    def Build_Neurons(self):
        nameIndex = 0
        for linkName in pyrosim.linkNamesToIndices:
            pyrosim.Send_Sensor_Neuron(name=nameIndex, linkName=linkName)
            nameIndex += 1
        for jointName in pyrosim.jointNamesToIndices:
            pyrosim.Send_Motor_Neuron(name=nameIndex, jointName=jointName)
            nameIndex += 1

    def Create_Brain(self):
        if self.synapseMode == "SIMPLE":
            self.Create_Simple_Brain()
        if self.synapseMode == "HIDDEN":
            self.Create_Hidden_Brain()
        if self.synapseMode == "RNN":
            self.Create_RNN_Brain()

    def Create_Simple_Brain(self):
        pyrosim.Start_NeuralNetwork("brain" + str(self.myID) + ".nndf")
        self.Build_Neurons()

        for i in range(0, c.numSensorNeurons):
            for j in range(0, len(self.weights[i])):
                pyrosim.Send_Synapse(sourceNeuronName=i, targetNeuronName=j + c.numSensorNeurons,
                                     weight=self.weights[i][j])
        pyrosim.End()

    def Create_Hidden_Brain(self):
        pyrosim.Start_NeuralNetwork("brain" + str(self.myID) + ".nndf")
        self.Build_Neurons()

        nameIndex = c.numSensorNeurons + c.numMotorNeurons
        hiddenNeuronNames = {}

        for i in range(0, c.numHiddenNeurons):
            pyrosim.Send_Hidden_Neuron(name=nameIndex)
            hiddenNeuronNames[i] = nameIndex
            nameIndex += 1

        for hiddenNeuron in hiddenNeuronNames:
             for i in range(0, c.numSensorNeurons):
                weight_index = i + hiddenNeuron * c.numSensorNeurons
                pyrosim.Send_Synapse(sourceNeuronName=i, targetNeuronName=hiddenNeuronNames[hiddenNeuron], weight=self.sensorToHiddenWeights[weight_index])
             for i in range(0, c.numMotorNeurons):
                 weight_index = i + hiddenNeuron * c.numMotorNeurons
                 pyrosim.Send_Synapse(sourceNeuronName=hiddenNeuronNames[hiddenNeuron], targetNeuronName=i+c.numSensorNeurons, weight=self.hiddenToMotorWeights[weight_index])

        pyrosim.End()

    def Create_RNN_Brain(self):
        pyrosim.Start_NeuralNetwork("brain" + str(self.myID) + ".nndf")
        self.Build_Neurons()
        nameIndex = c.numSensorNeurons + c.numMotorNeurons

        hiddenNeuronNames = {}

        for i in range(0, c.numHiddenNeurons):
            pyrosim.Send_Hidden_Neuron(name=nameIndex)
            hiddenNeuronNames[i] = nameIndex
            nameIndex += 1

        for hiddenNeuron in hiddenNeuronNames:
            for i in range(0, c.numSensorNeurons):
                weight_index = i + hiddenNeuron * c.numSensorNeurons
                pyrosim.Send_Synapse(sourceNeuronName=i, targetNeuronName=hiddenNeuronNames[hiddenNeuron], weight=self.sensorToHiddenWeights[weight_index])
            for i in range(0, c.numMotorNeurons):
                weight_index = i + hiddenNeuron * c.numMotorNeurons
                pyrosim.Send_Synapse(sourceNeuronName=hiddenNeuronNames[hiddenNeuron], targetNeuronName=i+c.numSensorNeurons, weight=self.hiddenToMotorWeights[weight_index])

        for i in range(0, c.numHiddenNeurons):
            pyrosim.Send_Hidden_Neuron(name=nameIndex)
            pyrosim.Send_Synapse(sourceNeuronName=i, targetNeuronName=nameIndex, weight=self.recurrentWeights[i][0])
            pyrosim.Send_Synapse(sourceNeuronName=nameIndex, targetNeuronName=i, weight=self.recurrentWeights[i][1])
            nameIndex += 1

        pyrosim.End()

    def Mutate(self):
        # TODO: Mutate method does not appear to be mutating the right weights in "original" mode
        synapseToMutate = random.randint(0, c.numSensorNeurons-1)
        preOrPostSynapticNeuron = random.randint(0, c.numMotorNeurons-1)
        inputOrOutput = random.randint(0, 1)
        if self.synapseMode == "HIDDEN":
            synapseToMutate = random.randint(0, len(self.sensorToHiddenWeights)-1)
            self.sensorToHiddenWeights[synapseToMutate] = random.random() * 2 - 1
            synapseToMutate = random.randint(0,len(self.hiddenToMotorWeights)-1)
            self.hiddenToMotorWeights[synapseToMutate] = random.random() * 2 - 1
        if self.synapseMode == "RNN":
            synapseToMutate = random.randint(0, len(self.recurrentWeights) - 1)
            self.recurrentWeights[synapseToMutate][inputOrOutput]= random.random() * 2 - 1
        if self.synapseMode == "SIMPLE":
            self.weights[synapseToMutate][preOrPostSynapticNeuron] = random.random() * 2 - 1

    def Set_ID(self, nextAvailableID):
        self.myID = nextAvailableID
