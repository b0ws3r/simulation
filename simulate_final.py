from simulation_final import SIMULATION_FINAL
import sys
import os
import shutil
import time

filepath = '/Users/westlands/Documents/Missy/College/Complex Systems/CS206/assignment_1/data.nosync'

def getWorldPathFromBrainPath(brainPath):
    j=0
    leftIndex = -1
    types = ['SIMPLE', 'RNN', 'HIDDEN']
    while leftIndex < 0:
        leftIndex = brainPath.find(types[j])
        j+=1
    rightIndex = brainPath.rindex("_")
    brainyname = brainPath[leftIndex:rightIndex]
    print(brainyname)
    for worldyname in worldFileNames:
        if(worldyname.find(brainyname+'_')>0):
            associatedWorldy = worldyname
            print(associatedWorldy)
    return associatedWorldy


directOrGUI = sys.argv[1]
solutionID = sys.argv[2]

worldFileNames = []
# put world file names in an array
for filename in os.listdir(filepath + '/Worlds'):
    worldFileNames.append(filename)
    # print(filename)

# for filename in os.listdir(filepath + '/Brains'):
    # get corresponding world
# associatedWorldy = getWorldPathFromBrainPath(filename)
    # print(filename)
# SIMPLE15
# worldName = "world_SIMPLE15_100x2.sdf"
# brainName = "brain_66_SIMPLE15_100x2.nndf" #1.5873116204306146

# SIMPLE15
# worldName = "world_SIMPLE15_100x2.sdf"
# brainName = "brain_167_SIMPLE15_100x2.nndf" 1.3263676179805906
#     # HIDDEN1
# worldName = "world_HIDDEN1_100x2.sdf"
# brainName = "brain_69_HIDDEN1_100x2.nndf"
#     # HIDDEN1
# worldName = "world_HIDDEN1_100x2.sdf"
# brainName = "brain_103_HIDDEN1_100x2.nndf"
#     # HIDDEN2
# worldName = "world_HIDDEN2_100x2.sdf"
# brainName = "brain_124_HIDDEN2_100x2.nndf"
#     # HIDDEN3
# worldName = "world_HIDDEN3_100x2.sdf"
# brainName = "brain_99_HIDDEN3_100x2.nndf"
#     # HIDDEN4
# worldName = "world_HIDDEN4_100x2.sdf"
# brainName = "brain_165_HIDDEN4_100x2.nndf"
#     # HIDDEN5
# worldName = "world_HIDDEN5_100x2.sdf"
# brainName = "brain_62_HIDDEN5_100x2.nndf"
#     # HIDDEN5
# 1.3678991326406311
# worldName = "world_HIDDEN5_100x2.sdf"
# brainName = "brain_108_HIDDEN5_100x2.nndf"
#     # HIDDEN6
# worldName = "world_HIDDEN6_100x2.sdf"
# brainName = "brain_179_HIDDEN6_100x2.nndf"
#     # HIDDEN10
# worldName = "world_HIDDEN10_100x2.sdf"
# brainName = "brain_31_HIDDEN10_100x2.nndf"
#     # HIDDEN15
# worldName = "world_HIDDEN15_100x2.sdf"
# brainName = "brain_86_HIDDEN15_100x2.nndf"
#     # RNN1
# worldName = "world_RNN1_100x2.sdf"
# brainName = "brain_94_RNN1_100x2.nndf"
#     # RNN1
# worldName = "world_RNN1_100x2.sdf"
# brainName = "brain_38_RNN1_100x2.nndf"
#     # RNN2
# worldName = "world_RNN2_100x2.sdf"
# brainName = "brain_179_RNN2_100x2.nndf"
#     # RNN3
# worldName = "world_RNN3_100x2.sdf"
# brainName = "brain_103_RNN3_100x2.nndf"
#     # RNN4
# worldName = "world_RNN4_100x2.sdf"
# brainName = "brain_160_RNN4_100x2.nndf"
#     # RNN5
# worldName = "world_RNN5_100x2.sdf"
# brainName = "brain_62_RNN5_100x2.nndf"
#     # RNN5
# worldName = "world_RNN5_100x2.sdf"
# brainName = "brain_45_RNN5_100x2.nndf"
#     # RNN6
# worldName = "world_RNN6_100x2.sdf"
# brainName = "brain_172_RNN6_100x2.nndf"
#     # RNN10
# worldName = "world_RNN10_100x2.sdf"
# brainName = "brain_189_RNN10_100x2.nndf"
#     # RNN10
# worldName = "world_RNN10_100x2.sdf"
# brainName = "brain_104_RNN10_100x2.nndf"
#     # RNN15
worldName = "world_RNN15_100x2.sdf"
brainName = "brain_64_RNN15_100x2.nndf"
#     # RNN15
# worldName = "world_RNN15_100x2.sdf"
# brainName = "brain_130_RNN15_100x2.nndf"

    # simulate the stuff
simulation = SIMULATION_FINAL(directOrGUI, '/Users/westlands/Documents/Missy/College/Complex Systems/CS206/assignment_1/data.nosync/brain_33_HIDDEN5_100x2.nndf', '/Users/westlands/Documents/Missy/College/Complex Systems/CS206/assignment_1/data.nosync/world_HIDDEN5_100x2.sdf')

# simulation = SIMULATION_FINAL(directOrGUI, filepath + '/Brains/' + brainName, filepath + '/Worlds/' + worldName)
simulation.Run()
# print(brainName)
simulation.Get_Fitness()


# brain_31_HIDDEN10_100x2.nndf

