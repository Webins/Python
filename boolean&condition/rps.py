import sys
import random
import time
print('Rock, Paper And Scissor Game!')

wins = 0
loses = 0
ties = 0
CHOICES = ['rock', 'paper', 'scissor']

start = time.time()
while True:
	
	print('Player 1 make you move: ', end='')
	
	move = input().lower()
	
	computer_move = CHOICES[random.randint(0,2)]
	
	if move != CHOICES[0] and move != CHOICES[1] and move != CHOICES[2]:
		print('You\'ve Selected an invalid option\n')
	elif move == CHOICES[0] and computer_move == CHOICES[0]:
		print(f'Computer\'s move: {computer_move}')
		print('It\'s a tie! \n')
		ties += 1
	elif move == CHOICES[0] and computer_move == CHOICES[1]:
		print(f'Computer\'s move: {computer_move}')
		print('You\'ve lost \n')
		loses += 1
	elif move == CHOICES[0] and computer_move == CHOICES[2]:
		print(f'Computer\'s move: {computer_move}')
		print('You\'ve won \n')
		wins += 1
	elif move == CHOICES[1] and computer_move == CHOICES[0]:
		print(f'Computer\'s move: {computer_move}')
		print('You\'ve won \n')
		wins += 1
	elif move == CHOICES[1] and computer_move == CHOICES[1]:
		print(f'Computer\'s move: {computer_move}')
		print('It\'s a tie! \n')
		ties += 1
	elif move == CHOICES[1] and computer_move == CHOICES[2]:
		print(f'Computer\'s move: {computer_move}')
		print('You\'ve lost \n')
		loses += 1
	elif move == CHOICES[2] and computer_move == CHOICES[0]:
		print(f'Computer\'s move: {computer_move}')
		print('You\'ve lost \n')
		loses += 1
	elif move == CHOICES[2] and computer_move == CHOICES[1]:
		print(f'Computer\'s move: {computer_move}')
		print('You\'ve won \n')
		wins += 1
	elif move == CHOICES[2] and computer_move == CHOICES[2]:
		print(f'Computer\'s move: {computer_move}')
		print('It\'s a tie! \n')
		ties += 1	
	
	print('Do you want to play again? (y/n): ', end='')
	dec = input().lower()
	if(dec == 'n'):
		print("==========Summary==========")
		print(f"Wins: {wins}")
		print(f"Loses: {loses}")
		print(f"Ties: {ties}")
		print(f'Time played: {round(time.time() - start ,2)} Seconds')
		sys.exit(0)
		
	
	


