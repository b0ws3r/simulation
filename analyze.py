import numpy
import matplotlib.pyplot as pyplot

frontLegSensorValues = numpy.load('data.nosync/frontLegSensorValues.npy')
backLegSensorValues = numpy.load('data.nosync/backLegSensorValues.npy')
targetAngles = numpy.load('data.nosync/targetAngles.npy')


# pyplot.plot(backLegSensorValues, linewidth=1, label="Back leg sensor values")
# pyplot.plot(frontLegSensorValues, linewidth=.5,label="Front leg sensor values")
pyplot.plot(targetAngles)
pyplot.legend()
pyplot.show()