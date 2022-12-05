import numpy as np

archivo = open("input.txt")

array_bidimensional = np.array([[0,0,0,'J',0,0,0,'B','W'], [0,0,0,'T',0,'W','F','R','Z'], [0,0,'Q','M', 0, 'J','R','W','H'], [0,'F','L','P',0, 'R','N','Z','G'],
['F','M','S','Q', 0, 'M', 'P', 'S','C'], ['L','V','R', 'V', 'W', 'P', 'C', 'P', 'J'], ['M', 'Z', 'V','S','S','V','Q','H','M'], ['W', 'B', 'H', 'F', 'L', 'F','J','V','B']], dtype=str)


def move_pieces(numPieces, start, end):
	global array_bidimensional
	start = int(start) - 1
	end = int(end) - 1
	numPieces = int(numPieces)
	
	while(numPieces > 0):
		i = 0
		j = (np.shape(array_bidimensional)[0]) - 1
		#take the first piece from the start position which is not 0
		if(array_bidimensional[0][end] != '0'):
			array_bidimensional = np.insert(array_bidimensional, 0, [0,0,0,0,0,0,0,0,0], axis=0)
		while(array_bidimensional[i][start] == '0' and i < (np.shape(array_bidimensional)[0])-1):
			i += 1
		#make sure that the end position is not full		
		while(array_bidimensional[j][end] != '0' and j >= 0):
			j -= 1
		array_bidimensional[j][end] = array_bidimensional[i][start]
		array_bidimensional[i][start] = 0
		numPieces -= 1
	return array_bidimensional


#save just the numbers from line 11 to end of file
i = 0
for line in archivo:
	if i >= 10:
		line = line.split()
		line[1]
		line[3]
		line[5]
		star1 = move_pieces(line[1], line[3], line[5])
	i += 1
print("start1:\n",star1)


archivo.close()
archivo = open("input.txt")
array_bidimensional = np.array([[0,0,0,'J',0,0,0,'B','W'], [0,0,0,'T',0,'W','F','R','Z'], [0,0,'Q','M', 0, 'J','R','W','H'], [0,'F','L','P',0, 'R','N','Z','G'],
['F','M','S','Q', 0, 'M', 'P', 'S','C'], ['L','V','R', 'V', 'W', 'P', 'C', 'P', 'J'], ['M', 'Z', 'V','S','S','V','Q','H','M'], ['W', 'B', 'H', 'F', 'L', 'F','J','V','B']], dtype=str)


def move_pieces(numPieces, start, end):
	global array_bidimensional
	start = int(start) - 1
	end = int(end) - 1
	numPieces = int(numPieces)	
	while(numPieces > 0):
		i = 0
		j = (np.shape(array_bidimensional)[0]) - 1
		#take the first piece from the start position which is not 0
		if(array_bidimensional[0][end] != '0'):
			array_bidimensional = np.insert(array_bidimensional, 0, [0,0,0,0,0,0,0,0,0], axis=0)
		while(array_bidimensional[i][start] == '0' and i < (np.shape(array_bidimensional)[0])-1):
			i += 1
		#make sure that the end position is not full		
		while(array_bidimensional[j][end] != '0' and j >= 0):
			j -= 1
		i = i + numPieces-1
		array_bidimensional[j][end] = array_bidimensional[i][start]
		array_bidimensional[i][start] = 0
		numPieces -= 1
	return array_bidimensional

#save just the numbers from line 11 to end of file
i = 0
for line in archivo:
	if i >= 10:
		line = line.split()
		line[1]
		line[3]
		line[5]
		star2 = move_pieces(line[1], line[3], line[5])
	i += 1
print("start2:\n", star2)
