# pregame setup
import random
player_choices = []
ROCK = 0
PAPER = 1
SCISSORS = 2

while True:
	# answers
	retry = True
	player_choices_rock = player_choices.count("rock")
	player_choices_paper = player_choices.count("paper")
	player_choices_scissors = player_choices.count("scissors")
	if player_choices_rock > player_choices_paper and player_choices_rock > player_choices_scissors:
		cpu = random.randint(0, 3)
		if cpu == 3:
			cpu = PAPER
	elif player_choices_paper > player_choices_rock and player_choices_paper > player_choices_scissors:
		cpu = random.randint(0, 3)
		if cpu == 3:
			cpu = SCISSORS
	else:
		cpu = random.randint(0, 3)
		if cpu == 3:
			cpu = ROCK
		
	while retry:
		retry = False
		player = input("Rock paper or scissors?\n\nPlayer: ")
  		# win, loss, or draw
		if player.lower() == "rock":
			if cpu == PAPER:
				result = "Loss"
			elif cpu == SCISSORS:
				result = "Win"
			else:
				result = "Draw"
		elif player.lower() == "paper":
			if cpu == ROCK:
				result = "Win"
			elif cpu == SCISSORS:
				result = "Loss"
			else:
				result = "Draw"
		elif player.lower() == "scissors":
			if cpu == ROCK:
				result = "Loss"
			elif cpu == PAPER:
				result = "Win"
			else:
				result = "Draw"
		else:
			retry = True
			print("\nYou have to pick 'Rock', 'Paper' or 'Scissors'.\n")
	
	if cpu == ROCK:
		print("CPU: Rock")
	elif cpu == PAPER:
		print("CPU: Paper")
	else:
		print("CPU: Scissors")
	if result == "Win":
	  	print("\n\033[1;31;48mYOU WIN!\033[0;20;48m\n")
	elif result == "Loss":
	  	print("\n\033[1;35;48mYOU LOSE!\033[0;20;48m\n")
	else:
	  	print("\n\033[1;32;48mA DRAW!\033[0;29;48m\n")
	retry = True
	
	while retry == True:
		repeat = input("Do you want to play again? (y/n) ")
		if repeat.lower() == "y":
			retry = False
		elif repeat.lower() == "n":
			quit("\nThanks for playing!")
		else:
			print("Say 'Yes' or 'No'.")
			retry = True
	player_choices.append(player.lower())