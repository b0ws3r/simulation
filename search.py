import os as os

from parallelHillClimber import PARALLEL_HILL_CLIMBER
# from hillclimber import HILL_CLIMBER

# hc = HILL_CLIMBER()
phc = PARALLEL_HILL_CLIMBER()

phc.Evolve()
phc.Show_Best()

