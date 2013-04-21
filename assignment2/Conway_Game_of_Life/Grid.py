class grid(object):
	"""docstring for grid"""
	def __init__(self, x,y):
		super(grid, self).__init__()
		self.x = x
		self.y = y
	def __str__(self):
		s = "X:{} Y:{}".format(self.x,self.y)
		return s