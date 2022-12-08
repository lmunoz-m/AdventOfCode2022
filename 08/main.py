""" # A function to count the number of visible trees in a grid.
def count_visible_trees(grid):
  # Get the dimensions of the grid.
  rows = len(grid)
  cols = len(grid[0])

  # Initialize a counter for the number of visible trees.
  count = 0

  # Loop through each tree in the grid.
  for row in range(rows):
    for col in range(cols):
      # If this tree is on the edge of the grid, it is visible.
      if row == 0 or row == rows-1 or col == 0 or col == cols-1 or (grid[row-1][col] == 0 or grid[row+1][col] == 0 or grid[row][col-1] == 0 or grid[row][col+1] == 0):
        count += 1
        continue

      # Otherwise, we need to check if it is visible from any edge.
      # Check if it is visible from the top or bottom.
      if max(grid[row-1][col], grid[row+1][col]) < grid[row][col]:
        count += 1
        continue

      # Check if it is visible from the left or right.
      if max(grid[row][col-1], grid[row][col+1]) < grid[row][col]:
        count += 1
        continue

  # Return the total number of visible trees.
  return count """

""" def count_visible_trees(grid):
  num_visible_trees = 0
  for row in range(len(grid)):
    for col in range(len(grid[row])):
      # Check if tree is on the edge of the grid
      if col == 0 or col == len(grid[row]) - 1 or row == 0 or row == len(grid) - 1:
        # Tree is on the edge and is only visible from the edge
        num_visible_trees += 1
      else:
        # Tree is an interior tree
        # Check if tree is blocked in all directions
        blocked = False
        # Check left direction
        for i in range(col-1, -1, -1):
          # Check all of the trees between the tree and the edge of the grid
          for j in range(len(grid)):
            if grid[j][i] >= grid[row][col]:
              blocked = True
              break
          if blocked:
            break
        # Check top direction
        for i in range(row-1, -1, -1):
          # Check all of the trees between the tree and the edge of the grid
          for j in range(len(grid[row])):
            if grid[i][j] >= grid[row][col]:
              blocked = True
              break
          if blocked:
            break
        # Check right direction
        for i in range(col+1, len(grid[row])):
          # Check all of the trees between the tree and the edge of the grid
          for j in range(len(grid)):
            if grid[j][i] >= grid[row][col]:
              blocked = True
              break
          if blocked:
            break
        # Check bottom direction
        for i in range(row+1, len(grid)):
          # Check all of the trees between the tree and the edge of the grid
          for j in range(len(grid[row])):
            if grid[i][j] >= grid[row][col]:
              blocked = True
              break
          if blocked:
            break
        # Check if tree is visible from any direction
        if not blocked:
          num_visible_trees += 1
  return num_visible_trees

 """

def count_visible_trees(grid):
  num_visible_trees = 0
  for row in range(len(grid)):
    for col in range(len(grid[row])):
      # Check if tree is on the edge of the grid
      if col == 0 or col == len(grid[row]) - 1 or row == 0 or row == len(grid) - 1:
        # Tree is on the edge and is only visible from the edge
        num_visible_trees += 1
      else:
        # Tree is an interior tree
        # Check if tree is blocked in all directions
        if is_blocked(grid, row, col, 'left') or is_blocked(grid, row, col, 'top') or is_blocked(grid, row, col, 'right') or is_blocked(grid, row, col, 'bottom'):
           continue
        # Tree is visible from at least one direction
        num_visible_trees += 1
  return num_visible_trees

# Returns True if the tree at the given row and column is blocked in the given direction,
# False otherwise.
def is_blocked(grid, row, col, direction):
  if direction == 'left':
    return all(grid[j][col-1] >= grid[row][col] for j in range(len(grid)))
  elif direction == 'top':
    return all(grid[row-1][j] >= grid[row][col] for j in range(len(grid[row])))
  elif direction == 'right':
    return all(grid[j][col+1] >= grid[row][col] for j in range(len(grid)))
  elif direction == 'bottom':
    return all(grid[row+1][j] >= grid[row][col] for j in range(len(grid[row])))
	
# Read the input.txt file.
with open('input.txt') as file:
  	grid = [list(line.strip()) for line in file]

# Convert the strings in the grid to integers
grid = [[int(num) for num in row] for row in grid]

print(grid)
# Print the number of visible trees in the grid.
print(count_visible_trees(grid))
# This should print 21.

