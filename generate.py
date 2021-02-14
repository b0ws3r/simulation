import pyrosim.pyrosim as pyrosim

pyrosim.Start_SDF("boxes.sdf")

x = 0
y = 0 
z = .5
for xc	in range(0, 6):
	length = 1
	width = 1
	height = 1
	z=.5
	for yc in range(0,6):
		length = 1
		width = 1
		height = 1
		z=.5
		for i in range(0,10):
			pyrosim.Send_Cube(name="Box", pos=[x+xc,y,z] , size=[length,width,height])
			pyrosim.Send_Cube(name="Box", pos=[x,y+yc,z] , size=[length,width,height])
			pyrosim.Send_Cube(name="Box", pos=[x+xc,y+yc,z] , size=[length,width,height])
			z+=height
			length = .9 * length
			width = .9 * width
			height = .9 * height
	
pyrosim.End()

