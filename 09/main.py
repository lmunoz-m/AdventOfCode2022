import numpy as np

global grid
global gridT
grid = np.array([['.','.','.','.','.','.'], ['.','.','.','.','.','.'], ['.','.','.','.','.','.'],['.','.','.','.','.','.'], ['H','.','.','.','.','.']], dtype=str)


gridT = np.array([['.','.','.','.','.','.'], ['.','.','.','.','.','.'], ['.','.','.','.','.','.'],['.','.','.','.','.','.'], ['.','.','.','.','.','.']], dtype=str)


archivo = open("input2.txt")

#make grid and gridT global variables





# create an empty list to store the instructions from the file
instructions = []

# read the lines from the file and add them to the list of instructions
while True:
    line = archivo.readline()

    # if there are no more lines to read, break out of the loop
    if not line:
        break

    line = line.split()
	# add the instruction to the list of instructions
    instructions.append((line[0], int(line[1])))

# hacer una funcion que devuelva true o false si hay un T al lado de un H, mirar tambien las diagonales
def findT(grid):
	res = False
	for i in range(len(grid)):
		for j in range(len(grid[i])):
			if grid[i][j] == 'H':
				if grid[i][j] == 'T':
					res = True
				elif i-1 >= 0 and grid[i-1][j] == 'T':
					res = True
				elif i+1 < len(grid) and grid[i+1][j] == 'T':
					res = True
				elif j-1 >= 0 and grid[i][j-1] == 'T':
					res = True
				elif j+1 < len(grid[i]) and grid[i][j+1] == 'T':
					res = True
				elif i-1 >= 0 and j-1 >= 0 and grid[i-1][j-1] == 'T':
					res = True
				elif i-1 >= 0 and j+1 < len(grid[i]) and grid[i-1][j+1] == 'T':
					res = True
				elif i+1 < len(grid) and j-1 >= 0 and grid[i+1][j-1] == 'T':
					res = True
				elif i+1 < len(grid) and j+1 < len(grid[i]) and grid[i+1][j+1] == 'T':
					res = True



	if (res == False):
		#find the pos where 'T' is and change it to '.'
		for i in range(len(grid)):
			for j in range(len(grid[i])):
				if grid[i][j] == 'T':
					grid[i][j] = '.'

	return res

def printGrid(grid):
	for i in range(len(grid)):
		for j in range(len(grid[i])):
			print(grid[i][j], end = ' ')
		
		print('\n')

# apply the instructions to the matrix and remove then once is done
print(instructions)
k = 1

while instructions:
	direcc, moves = instructions[0]
	instructions.pop(0)
	isChange = False
	print(direcc, moves)
	for i in range(len(grid)) :
	#start reading the grid from the left
		for j in range(len(grid[i])):
			if (grid [i][j] == 'H' and isChange == False ):
				if direcc == 'U':
					q = 0
					while q < moves:
						a = moves
						while(i-a < 0):
							grid = np.insert(grid, 0, '.', axis=0)
							gridT = np.insert(gridT, 0, '.', axis=0)
							i += 1
						if i-q-1 >= 0:
							if grid[i-q-1][j] == 'T':
								grid[i-q-1][j] = 'H'
								grid[i-q][j] = '.'
							else:
								grid[i-q-1][j] = 'H'
								grid[i-q][j] = '.'
								if findT(grid) == False:
									grid[i-q][j] = 'T'
									gridT[i-q][j] = '#'
							isChange = True
							q += 1

				elif direcc == 'D':
					q = 0
					while q < moves:
						a = moves
						while(i+a >= len(grid)):
							num_cols = len(grid[i])
							print(num_cols)
							grid = np.insert(grid, len(grid)-1, '.', axis=0)
							gridT = np.insert(gridT, len(grid)-1, '.', axis=0)
						if i+q+1 < len(grid):
							if grid[i+q+1][j] == 'T':
								grid[i+q+1][j] = 'H'
								grid[i+q][j] = '.'
							else:
								grid[i+q+1][j] = 'H'
								grid[i+q][j] = '.'
								if findT(grid) == False:
									grid[i+q][j] = 'T'
									gridT[i+q][j] = '#'
							isChange = True
						q += 1

				elif direcc == 'L':
					q = 0
					if (i == 4 and j == 0 and k == 1) :
						grid[i][j] = 'H'
						q += 1
					while q < moves:
						a = moves
						while(j-a < 0):
							num_filas = len(grid)
							grid = np.insert(grid, 0, ['.']*num_filas, axis = 1)
							gridT = np.insert(gridT, 0, ['.']*num_filas, axis = 1)
							j += 1
						if j-q-1 >= 0:
							if grid[i][j-q-1] == 'T':
								grid[i][j-q-1] = 'H'
								grid[i][j-q] = '.'
							else:
								grid[i][j-q-1] = 'H'
								grid[i][j-q] = '.'
								if findT(grid) == False:
									grid[i][j-q] = 'T'
									gridT[i][j-q] = '#'
							isChange = True
						q += 1

				elif direcc == 'R' :
					q = 0
					if (i == 4 and j == 0 and k == 1) :
						grid[i][j+q+1] = 'H'
						grid[i][j+q] = '.'
						q += 1
					while q < moves:
						if j+q+1 < len(grid[i]):
							if grid[i][j+q+1] == 'T':
								grid[i][j+q+1] = 'H'
								grid[i][j+q] = '.'
							else:
								grid[i][j+q+1] = 'H'
								grid[i][j+q] = '.'
								if findT(grid) == False:
									grid[i][j+q] = 'T'
									gridT[i][j+q] = '#'
							isChange = True
						else:
							v = moves - 1
							while( j+v+1 >= len(grid[i]) ):
								num_filas = len(grid)
								grid = np.insert(grid, len(grid[i]), ['.']*	num_filas, axis = 1)
								gridT = np.insert(gridT, len(gridT[i]), ['.']*num_filas, axis = 1)
								v -= 1
							
							if grid[i][j+q+1] == 'T':
								grid[i][j+q+1] = 'H'
								grid[i][j+q] = '.'
							else:
								grid[i][j+q+1] = 'H'
								grid[i][j+q] = '.'
								if findT(grid) == False:
									grid[i][j+q] = 'T'
									gridT[i][j+q] = '#'
							isChange = True
						q += 1
				
				printGrid(grid);
				print('\n')
				printGrid(gridT);
				print('\n') 
				k += 1
				break
			
		
printGrid(grid);

print('\n')

printGrid(gridT);

#count the number of # in gridT
r = 0
for i in range(len(gridT)):
	for j in range(len(gridT[i])):
		if gridT[i][j] == '#':
			r += 1


print('Star1: ', r)

archivo.close()