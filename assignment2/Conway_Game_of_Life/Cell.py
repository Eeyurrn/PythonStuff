class cell(object):
	"""Cell object representing the cell in conway's game of life, constructor takes argument of a tuple with two integers"""	
	def __init__(self, pos):
		super(cell, self).__init__()
		self.pos = pos
		self.alive = False
	def getNeighbours(self, grid):
		self.neighboursOffset = [(-1,-1),(0,-1),(1,-1),(-1,0),(0,1),(-1,1),(0,1),(1,1)]
		neighbours = []
		print "pos is "+str(self.pos)			
		for neighbour in self.neighboursOffset:
			coord = (self.pos[0]+neighbour[0],self.pos[1]+neighbour[1])
			if((coord[0] < 0) or (coord [1] < 0) or (coord [0] >= grid.x) or (coord [1] >= grid.y)):
				print "coord[0] = {} coord[1] = {}".format(coord[0],coord[1])
				print "rejecting coord"+str(coord)
				continue
			else:
				print "keeping {}".format(str(coord))
				neighbours.append(coord)
		return neighbours
