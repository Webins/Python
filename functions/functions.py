def say_hello(s='nobody'):
	print('hello ' + s)

def square(n):
	return n ** 2;

def division(divisor, dividendo):
	return divisor / dividendo

say_hello('User')
print(square(2))

#keyword argument
print(division(dividendo=5, divisor=8))
