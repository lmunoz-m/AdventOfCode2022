archivo = open("input.txt")

lines = archivo.read()

# read all the input.txt and save and sum the numbers until blank line is found for all the file
sumTotal = []
sum = 0
for line in lines.splitlines():
	if line == "":
		sumTotal.append(sum)
		sum = 0
	else:
		sum += int(line)

#search for the bigger number in the list sumTotal	
def searchBiggestNumber(sumTotal):
	max = 0
	for sum in sumTotal:
		if sum > max:
			max = sum
	return max

print(sumTotal)
print('\n')
print("The biggest number is: %d", searchBiggestNumber(sumTotal))
print('\n')

#searh for the three max numbers in the list sumTotal
def searchThreeMaxNumbers(sumTotal):
	max1 = 0
	max2 = 0
	max3 = 0
	for sum in sumTotal:
		if sum > max1:
			max3 = max2
			max2 = max1
			max1 = sum
		elif sum > max2:
			max3 = max2
			max2 = sum
		elif sum > max3:
			max3 = sum
	return max1, max2, max3, (max1 + max2 + max3)


print("The three biggest numbers are:", searchThreeMaxNumbers(sumTotal))

archivo.close()