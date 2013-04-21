import Cell
import os
from time import sleep
import Grid
#Test script for Conway's Game of Life
allcells=[]


x = 10
y = 10

g = Grid.grid(0,0)
print g

for i in range(0,y):
	column = []
	for j in range(0,x):
		column.append(Cell.cell((i,j)))
	allcells.append(column)

for column in allcells:
	for c in column:
		print c.pos
	print
sleep(0.5)
os.system("cls")