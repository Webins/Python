from random import random

def flip_coin():
	""" A simple function that simulate the throws of a coin """
	return "Head" if (random() > 0.5) else "Tail"
	
print(flip_coin())
print(flip_coin.__doc__) #documentation
