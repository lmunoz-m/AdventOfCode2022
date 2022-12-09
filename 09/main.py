grid = [
['.','.','.','.','.','.',], # 00 01 02 03 04 05
['.','.','.','.','.','.',], # 10 11 12 13 14 15
['.','.','.','.','.','.',],	# 20 21 22 23 24 25
['.','.','.','.','.','.',], # 30 31 32 33 34 35
['H','.','.','.','.','.',]]	# 40 41 42 43 44 45

#print(grid)

gridT = [
['.','.','.','.','.','.',], # 00 01 02 03 04 05
['.','.','.','.','.','.',], # 10 11 12 13 14 15
['.','.','.','.','.','.',],	# 20 21 22 23 24 25
['.','.','.','.','.','.',], # 30 31 32 33 34 35
['.','.','.','.','.','.',]]

archivo = open("input2.txt")


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

# apply the instructions to the matrix and remove then once is done
print(instructions)
k = 1
while instructions:
	direcc, moves = instructions[0]
	instructions.pop(0)
	isChange = False
	for i in range(len(grid)):
	#start reading the grid from the left
		for j in range(len(grid[i])):
			#print('paso2')
			if (grid [i][j] == 'H' and isChange == False ):
				print('estoy pasando por ', k, ' vez')
				if direcc == 'U' and i-moves >= 0:
					grid[i-moves][j] = 'H'
					grid[i][j] = '.'
					isChange = True
				elif direcc == 'D' and i+moves < len(grid):
					grid[i+moves][j] = 'H'
					grid[i][j] = '.'
					isChange = True
				elif direcc == 'L' and j-moves >= 0:
					grid[i][j-moves] = 'H'
					grid[i][j] = '.'
					isChange = True
				elif direcc == 'R' and j+moves < len(grid[i]):
					grid[i][j+moves] = 'H'
					grid[i][j] = '.'
					isChange = True
				print('dirección: ', direcc, 'movimientos: ', moves)
				print(grid[0],'\n')
				print(grid[1],'\n')
				print(grid[2],'\n')
				print(grid[3],'\n')
				print(grid[4],'\n')
				k += 1
				print(instructions)
				break
			
		
					
print('tablero final\n')
grid[4][0] = 's'
print(grid[0],'\n')
print(grid[1],'\n')
print(grid[2],'\n')
print(grid[3],'\n')
print(grid[4],'\n') 