import constants as c
import numpy
import pybullet as p
import pyrosim.pyrosim as pyrosim


class MOTOR:
    def __init__(self, jointName, nn):
        self.nn = nn
        self.jointName = jointName

    def Set_Value(self, robot):
        for neuronName in self.nn.Get_Neuron_Names():
            if self.nn.Is_Motor_Neuron(neuronName):
                jointName = self.nn.Get_Motor_Neurons_Joint(neuronName)
                desiredAngle = self.nn.Get_Value_Of(neuronName)
                # print("jointName: " + jointName)
                # print("neuronName: " + neuronName)
                # print("desiredAngle: " + str(desiredAngle))

                pyrosim.Set_Motor_For_Joint(
                    bodyIndex=robot
                    , jointName=jointName
                    , controlMode=p.POSITION_CONTROL
                    , targetPosition=desiredAngle
                    , maxForce=25)
