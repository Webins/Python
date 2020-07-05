import sys
MILLES = 1.60934
print("How many kilometers did you run today?")

try:
	kilometers = float(input())
except ValueError:
	print('Enter a valid number')
	sys.exit(1)

milles = round(kilometers / MILLES, 2)
print(f"You've run {kilometers} kilometers that is equivalent to {milles} milles")
