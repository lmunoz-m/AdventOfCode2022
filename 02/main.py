archivo = open("input.txt")


#compare n with m A>C X>C A>Z X>Z B>X B>A Y>A Y>X C>B C>Y Z>B Z>Y 
	
def compare1(n, m):
	sum2 = 0;
	if m == "X":
		sum2 += 1
		if n == "C":
			sum2 += 6
		elif n == "A":
			sum2 += 3
	elif m == "Y":
		sum2 += 2
		if n == "A":
			sum2 += 6
		elif n == "B":
			sum2 += 3
	elif  m == "Z":
		sum2 += 3
		if n == "B":
			sum2 += 6
		elif n == "C":
			sum2 += 3
	return sum2

# make the function compare for all the lines of the file and sum each result 

sum = 0
count = 0
for line in archivo:
	count += 1
	line = line.split()
	n = line[0]
	m = line[1]
	print(n, m)
	sum += compare1(n, m)
	print("la suma es: ", sum)



print(count)
print(sum)

archivo.close()
archivo = open("input.txt")

#Change the method compare to give the next results  if line[0] == "A": line[1] == "Y"	# 4 if line[0] == "B": line[1] == "X"	# if line[0] == "C": line[1] == "Z"	# 7
def compare2(n, m):
	sum2 = 0;
	if m == "X":
		if n == "C":
			sum2 += 2
		elif n == "A":
			sum2 += 3
		elif n == "B":
			sum2 += 1
	elif m == "Y":
		if n == "A":
			sum2 += 4
		elif n == "B":
			sum2 += 5
		elif n == "C":
			sum2 += 6
	elif  m == "Z":
		if n == "B":
			sum2 += 9
		elif n == "C":
			sum2 += 7
		elif n == "A":
			sum2 += 8
	return sum2





print(compare2('A','Y')) # 4
print(compare2('B','X')) # 1
print(compare2('C','Z')) # 7

print('\n')

sum3 = 0
count = 0
for line in archivo:
	count += 1
	line = line.split()
	n = line[0]
	m = line[1]
	print(n, m)
	sum3 += compare2(n, m)
	print("la suma es: ", sum3)



print(count)

print("la suma total es: ", sum3)

archivo.close()
