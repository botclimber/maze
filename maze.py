'''

 input: 2 matrix representing row walls( left wall and right wall) and col walls (up wall and down wall)
 robot = [] stack saves movment (d = down, u = up, r = right, l = left)
 cross = [] saves every cross

'''
import numpy

rowWall = numpy.array([[1,0,0,1,0,1,0,0,0,1,1],[1,0,1,1,1,0,1,0,1,1,1], [1,0,0,1,0,1,0,1,1,0,1], [1,0,0,0,1,0,1,0,1,0,1], [1,1,0,1,0,1,1,0,0,0,1], [1,0,1,1,0,1,0,0,0,0,1], [1,1,1,1,1,0,0,1,1,0,1], [1,1,1,1,0,0,1,0,1,0,1], [1,0,1,1,0,0,0,0,1,0,1], [1,0,0,1,0,0,0,0,0,0,1]])

colWall = numpy.array([[1,1,1,1,0,1,1,1,1,1], [1,0,0,0,1,0,1,1,0,0],[0,1,1,0,0,1,0,0,0,0],[1,1,0,1,1,0,1,0,0,1],[0,0,1,0,0,0,0,1,1,0],[0,1,0,0,0,0,1,1,1,1],[1,0,0,0,1,1,1,1,1,0],[0,0,0,0,1,0,0,0,0,1],[0,0,0,1,1,1,1,1,0,1],[1,1,0,0,1,1,1,0,1,0],[1,1,1,1,1,0,1,1,1,1]])

robot = ['d'] # assuming it wll always start at the top, even if dnt start at the top we can transpose the matrix
cross = {'turn': [], 'state':[]} # save all crosses

def getMazeIn():
	# considering just first and last line
	for x in range(len(colWall[0])):
		if colWall[0][x] == 0:
			return x

def getMazeOut():
	# considering just first and last line
	colsize = len(colWall)-1
	
	for x in range(len(colWall[colsize])):
		if colWall[colsize][x] == 0:
			return x 

mazeI = getMazeIn() # where it gonna start position
mazeO = getMazeOut() # where it gonna finish position

# actual state | begining state
aState = {'r': [0, mazeI+1], 'l': [0, mazeI], 'u': [0, mazeI], 'd': [1, mazeI]}




# change state
def chState():
	nr_turns = len(robot)-1	

	# checks if robot is in some loop	
	# loop = robot_in_loop()
	
	d = colWall[aState['d'][0]][aState['d'][1]]
	l = rowWall[aState['l'][0]][aState['l'][1]]
	r = rowWall[aState['r'][0]][aState['r'][1]]
	u = colWall[aState['u'][0]][aState['u'][1]]
	
	# verify if is a cross position
	if (d+l+r+u) < 2:
		cross['turn'].append(nr_turns+1)
		cross['state'].append([[aState['r'][0], aState['r'][1]], [aState['l'][0], aState['l'][1]], [aState['u'][0], aState['u'][1]], [aState['d'][0], aState['d'][1]]])	
	
	if robot[nr_turns] != 'u' and d == 0:
		robot.append('d')
		nState = {'r': [aState['r'][0]+1, aState['r'][1]], 'l': [aState['l'][0]+1, aState['l'][1]], 'u': [ aState['u'][0]+1 ,aState['u'][1] ], 'd': [ aState['d'][0]+1 ,aState['d'][1] ]}
	
	elif robot[nr_turns] != 'r' and l == 0:
		robot.append('l')
		nState = {'r': [aState['r'][0], aState['r'][1]-1], 'l': [aState['l'][0], aState['l'][1]-1], 'u': [ aState['u'][0] ,aState['u'][1]-1 ], 'd': [ aState['d'][0] ,aState['d'][1]-1 ]}

	elif robot[nr_turns] != 'l' and r == 0:
		robot.append('r')
		nState = {'r': [aState['r'][0], aState['r'][1]+1], 'l': [aState['l'][0], aState['l'][1]+1], 'u': [ aState['u'][0] ,aState['u'][1]+1 ], 'd': [ aState['d'][0] ,aState['d'][1]+1 ]}

	elif robot[nr_turns] != 'd' and u == 0:
		robot.append('u')
		nState = {'r': [aState['r'][0]-1, aState['r'][1]], 'l': [aState['l'][0]-1, aState['l'][1]], 'u': [ aState['u'][0]-1 ,aState['u'][1] ], 'd': [ aState['d'][0]-1 ,aState['d'][1] ]}

	else:
		# no way
		nState = show_me_the_way()

	return nState
'''
def robot_in_loop():
	
	count = 1
	if len(robot) >= 4:
		for x in range(len(robot)):
			if x >= len(robot)-5:
				for i in range(1, len(robot)-x-1):
					if robot[x] == robot[x+i]:
						count = 0
						break
	return count
'''


# if robot has no way out starts in a diff way from the last cross
def show_me_the_way():
	turn = cross['turn'][len(cross['turn'])-1]
	
	for x in range(len(robot)-turn):
		
		if len(robot) == turn+1:
			if robot[len(robot)-1] == 'd':
				colWall[cross['state'][len(cross['state'])-1][3][0]][cross['state'][len(cross['state'])-1][3][1]] = 1
			elif robot[len(robot)-1] == 'u':
				colWall[cross['state'][len(cross['state'])-1][2][0]][cross['state'][len(cross['state'])-1][2][1]] = 1
			elif robot[len(robot)-1] == 'l':
				rowWall[cross['state'][len(cross['state'])-1][1][0]][cross['state'][len(cross['state'])-1][1][1]] = 1
			elif robot[len(robot)-1] == 'r':
				rowWall[cross['state'][len(cross['state'])-1][0][0]][cross['state'][len(cross['state'])-1][0][1]] = 1
			
			robot.pop()		
		else:
			robot.pop()

	state = {'r':[cross['state'][len(cross['state'])-1][0][0], cross['state'][len(cross['state'])-1][0][1]], 'l': [cross['state'][len(cross['state'])-1][1][0], cross['state'][len(cross['state'])-1][1][1]], 'u': [cross['state'][len(cross['state'])-1][2][0], cross['state'][len(cross['state'])-1][2][1]], 'd': [cross['state'][len(cross['state'])-1][3][0], cross['state'][len(cross['state'])-1][3][1]]}
	
	cross['turn'].pop()
	cross['state'].pop()
	
	return state




# verify if robot reaches the end
def ver_finish():
	if aState['d'][0] == len(rowWall-1) and aState['d'][1] == mazeO:
		return True
	else:
		return False




# main program
move = {'l': 'left', 'r':'right', 'd': 'down', 'u': 'up'}

while ver_finish() is not True:
	aState = chState()

for x in range(len(robot)-1):
	print("turn {} move -> {}".format(x+1, move[robot[x]])) # print way that solves the maze

