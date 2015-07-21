"""
Lattice paths

Starting in the top left corner of a 2x2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.

https://projecteuler.net/project/images/p015.gif

How many such routes are there through a 20x20 grid?


"""

import time
start_time = time.time()


grid_size = 3
grid_sizeX = grid_size
grid_sizeY = grid_size

if grid_sizeX < grid_sizeY:
	num_of_digits = len(str(grid_sizeY))+1
else:
	num_of_digits = len(str(grid_sizeX))+1



grid_graph = {}
for nodeX in xrange(grid_sizeX+1):
	x = "%0*d" % (num_of_digits, nodeX)
	for nodeY in xrange(grid_sizeY+1):
		y = "%0*d" % (num_of_digits, nodeY)
		grid_graph[x+","+y] = []
		# if x is not at end of graph, add arc to right
		if nodeX < grid_sizeX:
			grid_graph[x+","+y].append(str("%0*d" % (num_of_digits, nodeX+1))+","+y)
		
		# if y is not at end of graph, add arc to down
		if nodeY < grid_sizeY:
			grid_graph[x+","+y].append(x+","+str("%0*d" % (num_of_digits, nodeY+1)))

print grid_graph, "    len is:", len(grid_graph)

for node in grid_graph:
	x, y = node[:num_of_digits], node[-num_of_digits:]
	print x,y



print "Time elapsed: %5.3f" % (time.time() - start_time)

"""
answer is 

"""