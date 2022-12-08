
	
# Read the input.txt file.
with open('input.txt') as file:
  	grid = [list(line.strip()) for line in file]

res = 0

# Part 1

visitedNumbers = []

for i in range(len(grid)): # i = filas
    for j in range(len(grid[i])): # j = columnas
      #print(' i = ', i, ' j = ', j, 'valor = ', grid[i][j])
      if i == 0 or i == len(grid) - 1:
        res += 1
      elif j == 0 or j == len(grid[i]) - 1:
        res += 1


#make a bidimensional array of visited numbers with binary values
for i in range(len(grid)):
  visitedNumbers.append([])
  for j in range(len(grid[i])):
    visitedNumbers[i].append(0)


max = 0
isVisible = False
#para abajo
for j in range(1,len(grid)-1):
  max = grid[0][j]
  for i in range(1,len(grid[j])-1)  :
    #print(' i = ', i, ' j = ', j, 'valor = ', grid[i][j], 'max = ', max)
    if grid[i][j] > max:
      max = grid[i][j]
      if(visitedNumbers[i][j] == 0):
        visitedNumbers[i][j] = 1
        res += 1
      #print('cambio el max por = ', max)

#para derecha
for i in range(1,len(grid)-1):
  max = grid[i][0]
  for j in range(1,len(grid[j])-1)  :
    #print(' i = ', i, ' j = ', j, 'valor = ', grid[i][j], 'max = ', max)
    if grid[i][j] > max:
      max = grid[i][j]
      if(visitedNumbers[i][j] == 0):
        visitedNumbers[i][j] = 1
        res += 1
      #print('cambio el max por = ', max)   

#para izquierda
for i in range(1,len(grid)-1):
  max = grid[i][len(grid[i])-1]
  for j in range(len(grid[j])-2,0,-1)  :
    #print(' i = ', i, ' j = ', j, 'valor = ', grid[i][j], 'max = ', max)
    if grid[i][j] > max:
      max = grid[i][j]
      if(visitedNumbers[i][j] == 0):
        visitedNumbers[i][j] = 1
        res += 1
      #print('cambio el max por = ', max) 

#para arriba
for j in range(1,len(grid)-1):
  max = grid[len(grid)-1][j]
  for i in range(len(grid[j])-2,0,-1)  :
    #print(' i = ', i, ' j = ', j, 'valor = ', grid[i][j], 'max = ', max)
    if grid[i][j] > max:
      max = grid[i][j]
      if(visitedNumbers[i][j] == 0):
        visitedNumbers[i][j] = 1
        res += 1
      #print('cambio el max por = ', max)

print('star1: ', res)


# Part 2
#30373 00 01 02 03 04
#25512 10 11 12 13 14
#65332 20 21 22 23 24
#33549 30 31 32 33 34
#35390 40 41 42 43 44
res = 0
for i in range(1,len(grid)): # i = filas
    for j in range(1,len(grid[i])): # j = columnas
      act = 1
      #abajo
      k = 1
      while(i + k < len(grid)):   
        k += 1
        if (grid[i+k-1][j] >= grid[i][j]):
          break
      k -= 1
      act *= k
      #arriba
      k = 1;
      while(i - k >= 0):
          k += 1
          if(grid[i - (k - 1)][j] >= grid[i][j]):
              break;
      k -= 1;
      act *= k;
      #derecha
      k = 1;
      while(j + k < len(grid[i])):
        k += 1
        if(grid[i][j + k - 1] >= grid[i][j]):
            break;
      k -= 1;
      act *= k;
      #izquierda
      k = 1;
      while(j - k >= 0):
        k += 1
        if(grid[i][j - (k - 1)] >= grid[i][j]):
            break;
      k -= 1;
      act *= k;

      if(act > res):
        res = act
      
      

print(res)


            

