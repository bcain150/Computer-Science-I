# File: proj2.py
# Author: Brendan Cain
# Date: 12/8/16
# Section: 22
# E-mail: bcain1@umbc.edu
# Description: recursively solves a maze using a search algorithm
# Collaboration: I did not collaborate with anyone on this assignment

#GLOBAL CONSTANTS
#wall indexes
RIGHT = 0
BOTTOM = 1
LEFT = 2
TOP = 3
#Maze Tuple indexes
D = 0 #dimensions
F = 1 #finish 
M = 2 #maze

#readMaze() Reads in the maze file and makes it into a 3D list
#input: The name of the maze file.
#output: a tuple with the dimensions of the maze at i=0,
#		 the coords of the finish at i=1, and a 3D List at i=2
def readMaze(file_name):
	#opens file for reading and reads in as a list of lines
	mazeFile = open(file_name, 'r')
	#gets the size of the file
	size_ = mazeFile.readline().split()
	height = int(size_[0])
	width = int(size_[1])
	size = (height, width)
	#gets the finish coordinates
	end_ = mazeFile.readline().split()
	end = (int(end_[0]), int(end_[1]))
	#creats 3D maze list using a 3D for loop but uses split() to split lines
	maze = []
	for h in range(height):
		row = []
		temp = ""
		for w in range(width):
			temp = mazeFile.readline().split()
			#casts all i to ints
			for i in range(len(temp)):
				temp[i] = int(temp[i])
			#end for
			row.append(temp)
		#end for width
		maze.append(row)
	#end for height
	return (size, end, maze)
#END def readMaze():

#searchMaze() a recursive function that solves the maze.
#input: the maze tuple and the current path (list of coordinate tuples)
#		*NOTE* if this is the first call then the list is only one tuple long (the start)
#output: the final path to the finish or NONE if there is no path
def searchMaze(mazeTupe, path):
	
	#unpackage maze
	# ***NOTE*** c index for end(both are lists) is always 0 and r is always 1
	end = mazeTupe[F]
	maze = mazeTupe[M]
	#gets path length and current location in maze
	pathLength = len(path)
	loc = path[pathLength-1]
	r = loc[0]
	c = loc[1]

	#checks for finish
	if loc == end:
		return path
	#Checks for every direction for a new open space:
	#checks squares to the Right, Below, to the Left, and above in that order
	#appends the new open spot to the path as long as it hasn't already been there
	#uses recursion to check the squares around the new spot.
	#deletes the step from the path if it was a dead end.

	#OPEN RIGHT
	stepRight = (r, c+1)
	if maze[r][c][RIGHT] == 0 and stepRight not in path:
		path.append(stepRight)
		solution = searchMaze(mazeTupe, path)
		if solution != None:
			return solution
		path.remove(stepRight)
	#END RIGHT CHECK

	#OPEN BOTTOM
	stepBottom = (r+1, c)
	if maze[r][c][BOTTOM] == 0 and stepBottom not in path:
		path.append(stepBottom)
		solution = searchMaze(mazeTupe, path)
		if solution != None:
			return solution
		path.remove(stepBottom)
	#END BOTTOM CHECK

	#OPEN LEFT
	stepLeft = (r, c-1)
	if maze[r][c][LEFT] == 0 and stepLeft not in path:
		path.append(stepLeft)
		solution = searchMaze(mazeTupe, path)
		if solution != None:
			return solution
		path.remove(stepLeft)
	#END LEFT CHECK

	#OPEN TOP
	stepTop = (r-1, c)
	if maze[r][c][TOP] == 0 and stepTop not in path:
		path.append(stepTop)
		solution = searchMaze(mazeTupe, path)
		if solution != None:
			return solution
		path.remove(stepTop)
	#END TOP CHECK

	#if you come to a dead end or there is no solution, return None
	return None
#END def searchMaze():

#checkInput() checks that input is valid and reprompts otherwise
#input: the input message string, the max bound (inclusive)
#output: the valid input
def checkInput(msg, maxx):
	#get input
	i = int(input(msg))
	#check input and loop if invalid
	while i < 0 or i > maxx:
		invalid = "Invalid, enter a number between 0 and " + str(maxx) + " (inclusive): "
		i = int(input(invalid))
	#break out of loop and return input
	return i
#END def checkInput():

def main():
	#start program and get string of file name
	print("Welcome to the Maze Solver!")
	mazeName = input("Please enter the filename of the maze: ")
	#reads in maze from file and gets dimensions
	maze = readMaze(mazeName)
	size = maze[D]
	#gets valid starting point from user
	rMsg = "Please enter the starting row: "
	cMsg = "Please enter the starting column: "
	row = checkInput(rMsg, size[0]-1)
	column = checkInput(cMsg, size[1]-1)
	start = (row, column)
	#call recursive function
	solution = searchMaze(maze, [start])
	#print solution if there is one.
	if solution == None:
		print("No solution found!")
	else:
		#print the path coordinates
		print("Solution found!")
		for p in solution:
			print(p)
#END def main():
main()