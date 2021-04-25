import numpy
import matplotlib.pyplot as pyplot

frontLegSensorValues = numpy.load('data.nosync/frontLegSensorValues.npy')
backLegSensorValues = numpy.load('data.nosync/backLegSensorValues.npy')
targetAngles = numpy.load('data.nosync/targetAngles.npy')
# generations
#(generation, fitness)
scatterplot = numpy.load('data.nosync/finalPerformance.npy')

pyplot.scatter(numpy.hsplit(scatterplot,2)[0], numpy.hsplit(scatterplot,2)[1], alpha=0.5)
pyplot.legend()
pyplot.show()