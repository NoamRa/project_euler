"""
Lattice paths

Starting in the top left corner of a 2x2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.

https://projecteuler.net/project/images/p015.gif

How many such routes are there through a 20x20 grid?


"""

import time
start_time = time.time()


grid_size = 20
grid_sizex = grid_size
grid_sizey = grid_size


grid_graph = []
for x in xrange(grid_sizex+1):
	grid_graph.append([])
	for y in xrange(grid_sizey+1):
		grid_graph[x].append(0)
		if x == 0:
			grid_graph[0][y] = 1


# algorithem
for x in xrange(grid_sizex+1):
	if x > 0:
		for y in xrange(grid_sizey+1):
			if x == y:
				grid_graph[x][y] = grid_graph[x-1][y]*2
			else:
				grid_graph[x][y] = grid_graph[x-1][y]+grid_graph[x][y-1]


# pretty print
num_of_digits = len(str(grid_graph[x][y]))

for x in xrange(grid_sizex+1):
	for y in xrange(grid_sizey+1):
		grid_graph[x][y] = "%0*d" % (num_of_digits, grid_graph[x][y])

for i in grid_graph:
	print i
print 

print "answer is:", grid_graph[x][y]


print "Time elapsed: %5.3f" % (time.time() - start_time)

"""
answer is 137846528820

"""