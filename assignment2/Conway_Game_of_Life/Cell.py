class cell(object):
	"""Cell object representing the cell in conway's game of life, constructor takes argument of a tuple with two integers"""
	def __init__(self, pos):
		super(cell, self).__init__()
		self.pos = (pos)
		self.alive = False;
	def getNeighbours(self):
		pass
		
