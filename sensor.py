import constants as c
import numpy
import pyrosim.pyrosim as pyrosim

class SENSOR:
	def __init__(self, linkname):
		self.linkName = linkname
		self.values = numpy.zeros(c.simulationSteps)

	def Get_Value(self, t):
		self.values[t] = pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)

	def Save_Values(self):  # Save vectors to file for use in analyze.py
		numpy.save("data.nosync/" + self.linkName + ".npy", self.values)
