from solution import SOLUTION
import constants as c
import copy
import numpy
import os

class PARALLEL_HILL_CLIMBER:
    def __init__(self):
        self.parents = {}
        self.nextAvailableID = 0
        self.useHiddenNeurons = True
        for i in range(0, c.populationSize):
            self.parents[i] = SOLUTION(self.nextAvailableID, useHiddenNeurons=self.useHiddenNeurons)
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
            if self.parents[parent].fitness > self.children[parent].fitness:
                self.parents[parent] = self.children[parent]

    def Show_Best(self):
        minValue = min(self.parents, key=(lambda k: self.parents[k].fitness))
        print(self.parents[minValue].fitness)
        print(self.parents[minValue].myID)
        winningId = self.parents[minValue].myID
        self.Store_Data(c.numberOfGenerations)
        self.parents[minValue].Start_Simulation("GUI")
        synapseMode = "hidden" + str(c.numHiddenNeurons) if self.useHiddenNeurons is True else "original"
        numpy.save("data.nosync/performancePlot_" + synapseMode + "_" + str(c.numberOfGenerations) + "x" + str(c.populationSize) + ".npy", self.data)
        os.system("mv  brain_"+str(winningId) +" data.nosync/brain_"+str(winningId) +"_" + synapseMode + "_" + str(c.numberOfGenerations) + "x" + str(c.populationSize) +".nndf")

        pass
