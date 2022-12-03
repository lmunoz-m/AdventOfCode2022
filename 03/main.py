archivo = open("input.txt")

#take the letter wich reppeats in n1 and n2
def rep(n1,n2):
	for i in n1:
		if i in n2:
			return i
	return 0

# Lowercase item types a through z have priorities 1 through 26.
# Uppercase item types A through Z have priorities 27 through 52.

# wich priority is the letter i 
def priority(i):
	if i.islower():
		return ord(i)-96
	else:
		return ord(i)-38


#repeat for all the file
sum = 0
for line in archivo:
	line = line.split()
	n = line[0]
	n1 = n[0:int(len(n)/2)]
	n2 = n[int(len(n)/2):len(n)]
	sum += priority(rep(n1,n2));
	#print('la letra repetida es ',  rep(n1,n2), 'y su num ',  priority(rep(n1,n2)))
	
print('La suma para la primera parte es: ', sum)


#close the file
archivo.close()

archivo = open("input.txt")

#find the letter that repeats in the three lines line1, line2 and line3
def rep(n1,n2,n3):
	for i in n1:
		if i in n2 and i in n3:
			return i
	return 0


# wich priority is the letter i
def priority(i):
	if i.islower():
		return ord(i)-96
	else:
		return ord(i)-38


#repeat for all the file
sum = 0
i = 0
for line in archivo:
	line = line.split()
	line2 = archivo.readline()
	line2 = line2.split()
	line3 = archivo.readline()
	line3 = line3.split()
	n1 = line[0]
	n2 = line2[0]
	n3 = line3[0]
	sum += priority(rep(n1,n2,n3));
	#print('la letra repetida es ',  rep(n1,n2,n3), 'y su num ',  priority(rep(n1,n2,n3)))

print('La suma para la segunda parte es: ', sum)
#close the file
archivo.close()
