from solution import SOLUTION
import constants as c
import copy
import numpy
import os

class PARALLEL_HILL_CLIMBER:
    def __init__(self):
        self.parents = {}
        self.nextAvailableID = 0
        self.synapseMode = c.synapseMode
        for i in range(0, c.populationSize):
            self.parents[i] = SOLUTION(self.nextAvailableID, synapseMode=self.synapseMode)
            self.nextAvailableID += 1
        self.data = numpy.zeros((c.numberOfGenerations*c.populationSize+1, 2))
        
    def Evolve(self):
        self.Evaluate(self.parents)
        for currentGeneration in range(0, c.numberOfGenerations):
            self.Evolve_For_OneGeneration(currentGeneration)

    def Evaluate(self, solutions):
        for solution in solutions:
            solutions[solution].Start_Simulation("DIRECT")
        for solution in solutions:
            solutions[solution].Wait_For_Simulation_To_End()

    def Evolve_For_OneGeneration(self, currentGeneration):
        self.Spawn()
        self.Mutate()
        self.Evaluate(self.children)
        self.Store_Data(currentGeneration)
        self.Select()
        self.Print()

    def Store_Data(self, currentGeneration):
        for parent in self.parents:
            self.data[currentGeneration + parent] = [currentGeneration, self.children[parent].fitness]

    def Print(self):
        for parent in self.parents:
            print("\r\nParent fitness: " + str(self.parents[parent].fitness) + " Child fitness: " + str(self.children[parent].fitness))
            print()

    def Spawn(self):
        self.children = {}
        for parent in self.parents:
            self.children[parent] = copy.deepcopy(self.parents[parent])
            self.children[parent].Set_ID(self.nextAvailableID)
            self.nextAvailableID += 1

    def Mutate(self):
        for child in self.children:
            self.children[child].Mutate()

    def Select(self):
        for parent in self.parents:
            if abs(self.children[parent].fitness) > abs(self.parents[parent].fitness):
                self.parents[parent] = self.children[parent]

    def Show_Best(self):
        maxValue = max(self.parents, key=(lambda k: self.parents[k].fitness))
        print(self.parents[maxValue].fitness)
        print(self.parents[maxValue].myID)
        winningId = self.parents[maxValue].myID
        self.Store_Data(c.numberOfGenerations)
        self.parents[maxValue].Start_Simulation("GUI")
        numpy.save("data.nosync/performancePlot_" + self.synapseMode + str(c.numHiddenNeurons)+"_"+ "_" + str(c.numberOfGenerations) + "x" + str(c.populationSize) + ".npy", self.data)
        os.system("mv  brain"+str(winningId) +".nndf data.nosync/brain_"+str(winningId) + "_" + self.synapseMode + str(c.numHiddenNeurons) + "_" + str(c.numberOfGenerations) + "x" + str(c.populationSize) +".nndf")
        os.system("mv world.sdf data.nosync/world_" + self.synapseMode + str(c.numHiddenNeurons) + "_" + str(c.numberOfGenerations) + "x" + str(c.populationSize) +".sdf")

        # pass
