import constants as c
import numpy

class SENSOR:
	def __init__(self, linkname):
		self.linkName=linkname
		self.values = numpy.zeros(c.simulationSteps)

	def Get_Value(self, t):
		self.values[t] = c.FL_amplitude * numpy.sin(c.FL_frequency * t + c.FL_phaseOffset)

	def Save_Values(self):  # Save vectors to file for use in analyze.py
		numpy.save("data/" + self.linkName + ".npy", self.values)
