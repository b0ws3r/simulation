import constants as c
import numpy
import pybullet as p
import pyrosim.pyrosim as pyrosim

class MOTOR:
    def __init__(self, jointName, frequency, amplitude, offset):
        self.jointName = jointName
        self.targetValues = numpy.zeros(c.simulationSteps)
        self.frequency = frequency
        self.amplitude = amplitude
        self.offset = offset

    def Set_Value(self, t, robot):
        self.targetValues[t] = self.amplitude * numpy.sin(self.frequency * t + self.offset)
        pyrosim.Set_Motor_For_Joint(
            bodyIndex=robot
            , jointName=self.jointName
            , controlMode=p.POSITION_CONTROL
            , targetPosition=self.targetValues[t]
            , maxForce=25)

    def Save_Values(self): #Save vectors to file for use in analyze.py
        numpy.save("data/" + self.jointName + ".npy", self.targetValues)
