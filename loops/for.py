
#iterable objects
string = "String"
numbers = [1,2,4,6,11,22,11]
range1 = range(7) #from 0 to 6
range2 = range(1, 10 ,2) #skip two numbers
range3 = range(7, 0, -1) #reverse order
for number in range(1,10): #from 1 to 9
	print(number)
	
for letter in string:
	print(letter)

for item in numbers:
	print(item)

