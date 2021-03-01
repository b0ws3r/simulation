import pyrosim.pyrosim as pyrosim


length = 1
width = 1
height = 1
x = 0
y = 0 
z = .5

def createWorld():
	pyrosim.Start_SDF("world.sdf")
	pyrosim.Send_Cube(name="Box", pos=[x-3,y-3,z] , size=[length,width,height])
	pyrosim.End()

def createRobot():
	pyrosim.Start_URDF("body.urdf")
	pyrosim.Send_Cube(name="Torso", pos=[x,y,z+1] , size=[length,width,height])
	pyrosim.Send_Joint( name = "Torso_backLeg" , parent= "Torso" , child = "backLeg" , type = "revolute", position = "-.5 0 1")
	pyrosim.Send_Cube(name="backLeg", pos=[-.5,0,-.5] , size=[length,width,height])
	pyrosim.Send_Joint( name = "Torso_frontLeg" , parent= "Torso" , child = "frontLeg" , type = "revolute", position = ".5 0 1")
	pyrosim.Send_Cube(name="frontLeg", pos=[.5,0,-.5] , size=[length,width,height])
	pyrosim.End()

createWorld()
createRobot()
