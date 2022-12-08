with open('input2.txt', 'r') as file:
	trees = tuple([tuple(map(int, list(row.strip())))
					for row in file.read().strip().split()])

visibles = 0

for i, row in enumerate(trees):
	for j, col in enumerate(row):
		element = trees[i][j]
		print(element)
		top = tuple([element > row[j] for row in trees[:i]])
		print(top)
		left = tuple([element > col for col in trees[i][:j]])
		right = tuple([element > col for col in trees[i][j + 1:]])
		bottom = tuple([element > row[j] for row in trees[i + 1:]])

		if any([all(top), all(left), all(right), all(bottom)]):
			visibles += 1

print(visibles)