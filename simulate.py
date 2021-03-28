from simulation import SIMULATION
import sys

derectOrGUI = sys.argv[1]
simulation = SIMULATION(derectOrGUI)
simulation.Run()
simulation.Get_Fitness()
