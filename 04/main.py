archivo = open("input.txt")


# verify that the numbers in n1 and n2 are in the range of m1 and m2
def verify(n1, n2, m1, m2):
	if (n1 <= m1 and n2 >= m2):
		return True
	elif (m1 <= n1 and m2 >= n2	):
		return True
	else:
		return False

# verify intersection between the numbers in n1 and n2 with the numbers in m1 and m2
def intersection(n1, n2, m1, m2):
	res = verify(n1, n2, m1, m2)
	if n1 >= m1 and n1 <= m2:
		res = True
	elif m1 >= n1 and m1 <= n2:
		res = True
	else:
		res = False
	return res

# repeat the process until the end of the file
sumStar = 0
sumStar2 = 0
i = 1
for line in archivo:
	line = line.split(',')
	n = line[0]
	m = line[1]
	#take the numbers separated by - from n and m and convert them to int
	n = n.split('-')
	n = [int(i) for i in n]
	m = m.split('-')
	m = [int(i) for i in m]
	n1 = n[0]
	n2 = n[1]
	m1 = m[0]
	m2 = m[1]
	#verify if the numbers in n1 and n2 are in the range of m1 and m2
	if (verify(n1, n2, m1, m2)):
		res = True
		sumStar += 1
	if (intersection(n1, n2, m1, m2)):
		res = True
		sumStar2 += 1
	else:
		res = False


#print(verify(2,8,3,7))
print("The first star is: ", sumStar)
print("The second star is: ", sumStar2)