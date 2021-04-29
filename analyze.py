import numpy
import matplotlib.pyplot as pyplot

frontLegSensorValues = numpy.load('data.nosync/frontLegSensorValues.npy')
backLegSensorValues = numpy.load('data.nosync/backLegSensorValues.npy')
targetAngles = numpy.load('data.nosync/targetAngles.npy')
# generations
#(generation, fitness)


# fig, ax = pyplot.subplots(4, figsize=(10, 6))

scatterplot1 = numpy.load('data.nosync/performancePlot_hidden1_20x4.npy')
scatterplot2 = numpy.load('data.nosync/performancePlot_hidden5_20x4.npy')
scatterplot3 = numpy.load('data.nosync/performancePlot_hidden10_20x4.npy')
scatterplot4 = numpy.load('data.nosync/performancePlot_hidden15_20x4.npy')

pyplot.subplot(2, 2, 1)
# ax[0] = \
pyplot.scatter(numpy.hsplit(scatterplot1,2)[0], numpy.hsplit(scatterplot1,2)[1], alpha=0.5)
pyplot.title("1 hidden neuron")
pyplot.subplot(2, 2, 2)
# ax[1] = \
pyplot.scatter(numpy.hsplit(scatterplot2,2)[0], numpy.hsplit(scatterplot2,2)[1], alpha=0.5)
pyplot.title("5 hidden neurons")
pyplot.subplot(2, 2, 3)
# ax[2] =
pyplot.scatter(numpy.hsplit(scatterplot3,2)[0], numpy.hsplit(scatterplot3,2)[1], alpha=0.5)
pyplot.title("10 hidden neurons")
pyplot.subplot(2, 2, 4)
# ax[3] = \
pyplot.scatter(numpy.hsplit(scatterplot4,2)[0], numpy.hsplit(scatterplot4,2)[1], alpha=0.5)
pyplot.title("15 hidden neurons")


# pyplot.legend()
pyplot.show()