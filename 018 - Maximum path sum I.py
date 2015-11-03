"""
Maximum path sum I
Problem 18

By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.

   3 
  7 4 
 2 4 6  
8 5 9 3 

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom of the triangle below:

               75
              95 64
             17 47 82
            18 35 87 10
           20 04 82 47 65
          19 01 23 75 03 34
         88 02 77 73 07 63 67
        99 65 04 28 06 16 70 92
       41 41 26 56 83 40 80 70 33
      41 48 72 33 47 32 37 16 94 29
     53 71 44 65 25 43 91 52 97 51 14
    70 11 33 28 77 73 17 78 39 68 17 57
   91 71 52 38 17 14 91 43 58 50 27 29 48
  63 66 04 68 89 53 67 30 73 16 69 87 40 31
 04 62 98 27 23 09 70 98 73 93 38 53 60 04 23



NOTE: As there are only 16384 routes, it is possible to solve this problem by trying every route. 
However, Problem 67, is the same challenge with a triangle containing one-hundred rows; it cannot be solved by brute force, and requires a clever method! ;o)

"""

import time
start_time = time.time()


# note to selfe - number of paths is 2^ (triangle lines-1)

raw_triangle = "\
75\n\
95 64\n\
17 47 82\n\
18 35 87 10\n\
20 04 82 47 65\n\
19 01 23 75 03 34\n\
88 02 77 73 07 63 67\n\
99 65 04 28 06 16 70 92\n\
41 41 26 56 83 40 80 70 33\n\
41 48 72 33 47 32 37 16 94 29\n\
53 71 44 65 25 43 91 52 97 51 14\n\
70 11 33 28 77 73 17 78 39 68 17 57\n\
91 71 52 38 17 14 91 43 58 50 27 29 48\n\
63 66 04 68 89 53 67 30 73 16 69 87 40 31\n\
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"



def format_triangle(raw_triangle):
	lined_triangle = raw_triangle.split('\n')
	str_triangle = []
	for line in lined_triangle:
		str_triangle.append(line.split(" "))
	
	triangle = []
	for line in str_triangle:
		int_line = []
		for num in line:
			int_line.append(int(num))
		triangle.append(int_line)

	#print triangle
	return triangle



def best_group_in_line(line):
	group_sums = []

	if len(line) / float(2) <= 1:
		best_group = None

	elif (len(line) % 2) == 0:
		for i in xrange(0, (len(line) / 2)):
			group_sums.append(line[i*2] + line[i*2+1])
		best_group = group_sums.index(max(group_sums))

	elif (len(line) % 2) == 1:
		for i in xrange(0, (len(line) / 2)):
			group_sums.append(line[i*2] + line[i*2+1])
		group_sums.append(line[i*2] + line[i*2-1])
		best_group = group_sums.index(max(group_sums))

	# normalize to 0.0-1.0
	if best_group != None:
		best_group_norm = float(best_group*2)/len(line)
	else:
		best_group_norm = None

	print best_group_norm, best_group, group_sums
	return best_group_norm




def lines_over_avg(triangle):
	# returns a list with lines whose avg is higher than the triangle avg.
	s,c, = 0.0, 0.0
	line_avg = []
	lines_over_avg = [False]*len(triangle)
	for line in triangle:
		line_sum, line_len = sum(line), len(line)
		line_avg.append(line_sum / line_len)
		s = s + line_sum
		c = c + line_len
	
	overall_avg = s/c
	for i in xrange(len(line_avg)):
		if line_avg[i] > overall_avg + (overall_avg/15): # strength factor. experiment!
			lines_over_avg[i] = True

	return lines_over_avg


def triangle_weight(raw_triangle):
	triangle = format_triangle(raw_triangle)
	lines_over_avg_res = lines_over_avg(triangle)

	group_score = [0]*(len(triangle[-1])/2) # init a list to keep score

	important_lines_score = []

	for i in xrange(len(triangle)):
		best_group = best_group_in_line(triangle[i])
		#print best_group
		if best_group:
			important_lines_score.append(best_group * lines_over_avg_res[i])
		else:
			important_lines_score.append(0.0)
	

	return important_lines_score


#print triangle_weight(raw_triangle)



"""
Dynamic Programming
http://www.mathblog.dk/project-euler-18/

a + max(b,c)
"""
"""
raw_triangle = "\
3\n\
7 4\n\
2 4 6\n\
8 5 9 3"
"""

triangle = format_triangle(raw_triangle)[::-1]

first = True
for i in xrange(0, len(triangle)-2):
	print "line", i, "content:", triangle[0]
	summed_line = []
	for j in xrange(len(triangle[0])-1):
		b = triangle[0][j]
		c = triangle[0][j+1]
		a = triangle[1][j]
		tot = max(b, c) + a
		print b, c, a, "=", tot
		summed_line.append(tot)
	triangle = triangle[2:]
	triangle = [summed_line] + triangle
	#print triangle
	print

print "result:", max(triangle[0])+triangle[1][0]

# Fuck me I was so far away from target. This solution could be more elegant but I'm a lazy ass...
# Keeping the line weight method. Maybe it'll be usful sometime.


print "Time elapsed: %5.3f" % (time.time() - start_time)

"""
answer is 1074
"""



