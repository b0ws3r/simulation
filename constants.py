import numpy

#Constants
simulationSteps = 1000
pi = numpy.pi

numberOfGenerations = 50
populationSize = 4
numHiddenNeurons = 5

numMotorNeurons = 8
numSensorNeurons = 9
BL_amplitude = pi/6
BL_frequency = -10/(simulationSteps / (2*pi))
BL_phaseOffset = 0

FL_amplitude = pi/6
FL_frequency = -10/(simulationSteps / (2*pi))
FL_phaseOffset = 0

motorJointRange = .5
#Robot size/pos constants
length = 1
width = 1
height = 1
x = 0
y = 0
z = .5
zStart = 1.5
