import sys
while 1:
	print('Enter an option \n(a)calculate the square of a number\n(b)calculate the square root of a number\n(c)exit')
	print(':',end='')
	dec = input()
	
	if dec == "a":
		print('Enter a number: ', end='')
		
		try:
			data = float(input())
		except ValueError:
			print('The number entered was not valid')
		
		print(f'The square of {data} is : {data ** 2}')
		
	elif dec == "b":
		print('Enter a number: ', end='')
		try:
			data = float(input())
		except ValueError:
			print('The number entered was not valid')
			
		print(f'The square root of {data} is : {data ** 0.5}')
	elif dec == 'c':
		sys.exit(0)
	else:
		print("No options selected\n")
	
	
