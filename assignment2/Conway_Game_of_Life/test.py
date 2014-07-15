import Cell
import os
from time import sleep
import Grid
#Test script for Conway's Game of Life
def test_1():
	allcells=[]


	x = 10
	y = 10

	g = Grid.grid(10,10)
	print g

	for i in range(0,y):
		column = []
		for j in range(0,x):
			column.append(Cell.cell((i,j)))
		allcells.append(column)

	c = Cell.cell((0,0))
	c.getNeighbours()

def test_grid_line():
	length = 10
	Grid.print_horizontal_line(length)
	Grid.print_bars(length)
	Grid.print_horizontal_line(length)

test_grid_line()
