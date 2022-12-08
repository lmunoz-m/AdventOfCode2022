
	
# Read the input.txt file.
with open('input2.txt') as file:
  	grid = [list(line.strip()) for line in file]

#30373 00 01 02 03 04
#25512 10 11 12 13 14
#65332 20 21 22 23 24
#33549 30 31 32 33 34
#35390 40 41 42 43 44
""" max_i = max(grid[i])
  print('max_i = ', max_i) """

print(grid)
res = 0

for i in range(len(grid)): # i = filas
    for j in range(len(grid[i])): # j = columnas
      #print(' i = ', i, ' j = ', j, 'valor = ', grid[i][j])
      if i == 0 or i == len(grid) - 1:
        res += 1
      elif j == 0 or j == len(grid[i]) - 1:
        res += 1


max = 0
isVisible = False
#para abajo
for j in range(1,len(grid)-1):
  max = grid[0][j]
  for i in range(1,len(grid[j])-1)  :
    #print(' i = ', i, ' j = ', j, 'valor = ', grid[i][j], 'max = ', max)
    if grid[i][j] > max:
      max = grid[i][j]
      res += 1
      #print('cambio el max por = ', max)

#para derecha
for i in range(1,len(grid)-1):
  max = grid[i][0]
  for j in range(1,len(grid[j])-1)  :
    #print(' i = ', i, ' j = ', j, 'valor = ', grid[i][j], 'max = ', max)
    if grid[i][j] > max:
      max = grid[i][j]
      res += 1
      #print('cambio el max por = ', max)   

#para izquierda
for i in range(1,len(grid)-1):
  max = grid[i][len(grid[i])-1]
  for j in range(len(grid[j])-2,0,-1)  :
    #print(' i = ', i, ' j = ', j, 'valor = ', grid[i][j], 'max = ', max)
    if grid[i][j] > max:
      max = grid[i][j]
      res += 1
      #print('cambio el max por = ', max) 

#para arriba
for j in range(1,len(grid)-1):
  max = grid[len(grid)-1][j]
  for i in range(len(grid[j])-2,0,-1)  :
    #print(' i = ', i, ' j = ', j, 'valor = ', grid[i][j], 'max = ', max)
    if grid[i][j] > max:
      max = grid[i][j]
      res += 1
      #print('cambio el max por = ', max)



print(res)
            

