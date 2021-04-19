
import numpy

#Constants
simulationSteps = 1000
pi = numpy.pi

numberOfGenerations = 15
populationSize = 15

numMotorNeurons = 8
numSensorNeurons = 9

BL_amplitude = pi/6
BL_frequency = -10/(simulationSteps / (2*pi))
BL_phaseOffset = 0

FL_amplitude = pi/6
FL_frequency = -10/(simulationSteps / (2*pi))
FL_phaseOffset = 0

motorJointRange = 0.2
#Robot size/pos constants
length = 1
width = 1
height = 1
x = 0
y = 0
z = .5
