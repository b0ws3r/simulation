import numpy
import matplotlib.pyplot as pyplot

frontLegSensorValues = numpy.load('data/frontLegSensorValues.npy')
backLegSensorValues = numpy.load('data/backLegSensorValues.npy')



pyplot.plot(backLegSensorValues, linewidth=1, label="Back leg sensor values")
pyplot.plot(frontLegSensorValues, linewidth=.5,label="Front leg sensor values")
pyplot.legend()
pyplot.show()