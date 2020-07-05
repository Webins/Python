#creating sets
s = set({1,2,3,4,5,5,5}) #(1,2,3,4,5)

s2 = {'a','b','c'}

print('a' in s2) #True
print(6 in s) #False

#accessing all values

for number in s:
	print(number)
	

#methods
s.add(6)
s.remove(1)

s.discard(100) #remove an item but doesnt throw an error if the value doesnt exist

s3 = s.copy()
print(s3 == s)
print(s is s3)

s3.clear()


math_students = {"Matthew", "Helen", "Prashant", "James", "Aparna"}
biology_students = {"Jane", "Matthew", "Charlotte", "Mesut", "Oliver", "James"}

print(math_students | biology_students) #union
print(math_students & biology_students) #intersection


#set comprehesion
print({x**2 for x in range(10)}) # give me a set
print({x:x**2 for x in range(10)}) # give me a dictionary

print({char.upper() for char in 'Hellooooooooo'})


