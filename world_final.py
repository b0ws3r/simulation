import pybullet as p

class WORLD_FINAL:
	def __init__(self, worldyname):
		self.planeId = p.loadURDF("plane.urdf")
		self.worldId = p.loadSDF(worldyname)
		# for j in range(1,len(self.worldId)+1):
		# 	posor = p.getBasePositionAndOrientation(j)
		# 	cid = p.createConstraint(j, -1, -1, -1, p.JOINT_FIXED, [0, 0, 0], [0, 0, 0], posor[0])
		# p.changeConstraint()
