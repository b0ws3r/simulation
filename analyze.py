import numpy
import matplotlib.pyplot as pyplot

poopypath = '/Users/westlands/Documents/Missy/College/Complex Systems/CS206/assignment_1/data.nosync/PerformancePlots'
# SIMPLE DATA - 100 GENS
simpleRawPlot1 = numpy.load(poopypath + '/performancePlot_SIMPLE15__100x2.npy')
# ax[0] = \
pyplot.scatter(numpy.hsplit(simpleRawPlot1, 2)[0], numpy.hsplit(simpleRawPlot1, 2)[1], alpha=0.5)
pyplot.title("1 simple neuron")
# pyplot.legend()
pyplot.show()

# HIDDEN DATA - 100 GENS
hiddenRawPlot1 = numpy.load(poopypath + '/performancePlot_HIDDEN1__100x2.npy')
hiddenRawPlot5 = numpy.load(poopypath + '/performancePlot_HIDDEN5__100x2.npy')
hiddenRawPlot10 = numpy.load(poopypath + '/performancePlot_HIDDEN10__100x2.npy')
hiddenRawPlot15 = numpy.load(poopypath + '/performancePlot_HIDDEN15__100x2.npy')

pyplot.subplot(2, 2, 1)
# ax[0] = \
pyplot.scatter(numpy.hsplit(hiddenRawPlot1, 2)[0], numpy.hsplit(hiddenRawPlot1, 2)[1], alpha=0.5)
pyplot.title("1 hidden neuron")
pyplot.subplot(2, 2, 2)
# ax[1] = \
pyplot.scatter(numpy.hsplit(hiddenRawPlot5, 2)[0], numpy.hsplit(hiddenRawPlot5, 2)[1], alpha=0.5)
pyplot.title("5 hidden neurons")
pyplot.subplot(2, 2, 3)
# ax[2] =
pyplot.scatter(numpy.hsplit(hiddenRawPlot10, 2)[0], numpy.hsplit(hiddenRawPlot10, 2)[1], alpha=0.5)
pyplot.title("10 hidden neurons")
pyplot.subplot(2, 2, 4)
# ax[3] = \
pyplot.scatter(numpy.hsplit(hiddenRawPlot15, 2)[0], numpy.hsplit(hiddenRawPlot15, 2)[1], alpha=0.5)
pyplot.title("15 hidden neurons")

# pyplot.legend()
pyplot.show()

# RNN DATA - 100 GENS
rnnRawPlot1 = numpy.load(poopypath + '/performancePlot_RNN1__100x2.npy')
rnnRawPlot5 = numpy.load(poopypath + '/performancePlot_RNN5__100x2.npy')
rnnRawPlot10 = numpy.load(poopypath + '/performancePlot_RNN10__100x2.npy')
rnnRawPlot15 = numpy.load(poopypath + '/performancePlot_RNN15__100x2.npy')

pyplot.subplot(2, 2, 1)
# ax[0] = \
pyplot.scatter(numpy.hsplit(hiddenRawPlot1, 2)[0], numpy.hsplit(rnnRawPlot1, 2)[1], alpha=0.5)
pyplot.title("RNN: 1 hidden neuron")
pyplot.subplot(2, 2, 2)
# ax[1] = \
pyplot.scatter(numpy.hsplit(hiddenRawPlot5, 2)[0], numpy.hsplit(rnnRawPlot5, 2)[1], alpha=0.5)
pyplot.title("RNN: 5 hidden neurons")
pyplot.subplot(2, 2, 3)
# ax[2] =
pyplot.scatter(numpy.hsplit(hiddenRawPlot10, 2)[0], numpy.hsplit(rnnRawPlot10, 2)[1], alpha=0.5)
pyplot.title("RNN: 10 hidden neurons")
pyplot.subplot(2, 2, 4)
# ax[3] = \
pyplot.scatter(numpy.hsplit(hiddenRawPlot15, 2)[0], numpy.hsplit(rnnRawPlot15, 2)[1], alpha=0.5)
pyplot.title("RNN: 15 hidden neurons")

# pyplot.legend()
pyplot.show()


def split_data(param):
    return numpy.split(param[:, 1], numpy.unique(param[:, 0], return_index=True)[1][1:])
def get_max(arr):
    newguy = []
    for elem in arr:
        newguy.append(elem[0])
    poop = max(newguy)
    print(poop)
    return poop
# Now, stack the best simple run against the best HIDDEN and best RNN runs.
# TODO: Change this so that we are taking whatever run had the best performance
raw_simple = split_data(simpleRawPlot1)
raw_simple_avg = numpy.average(raw_simple)
get_max(raw_simple)

# TODO: Change this so that we are taking whatever run had the best performance
raw_hidden = split_data(hiddenRawPlot5)
raw_hidden_avg = numpy.average(raw_hidden)
get_max(raw_hidden)

# print(raw_hidden)
# print(raw_hidden_avg) # TODO: make sure that you get 4 arrays with one value each

# TODO: Change this so that we are taking whatever run had the best performance
raw_rnn = split_data(rnnRawPlot10)
raw_rnn_avg = numpy.average(raw_rnn)
get_max(raw_rnn)

# print(raw_rnn)

# Now plot averages on top of each other
