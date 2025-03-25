import random

def format(text: str, fg="-1"):
	if fg == "-1":
		code = ""
	else:
		code = f";38;2;{int(fg[0:2], 16)};{int(fg[2:4], 16)};{int(fg[4:6], 16)}"

	return f"\033[1{code}m{text}\033[0m"


# pregame setup
choices = {"rock": 0, "paper": 0, "scissors": 0}
options = ["rock", "paper", "scissors"]

while True:
	# cpu's choice
	cpu = random.randint(0, 3)
	if cpu == 3:
		if choices["rock"] > choices["paper"] and choices["rock"] > choices["scissors"]:
			cpu = 1
		elif choices["paper"] > choices["rock"] and choices["paper"] > choices["scissors"]:
			cpu = 2
		else:
			cpu = 0

	# player's choice
	while True:
		player = input(f"{format("Rock, paper or scissors?")}\n\nPlayer: ").lower()
		if player in options:
			break
		print(format("\nYou have to pick 'Rock', 'Paper' or 'Scissors'.\n", "CC0000"))

	# displaying results
	print(f"CPU: \033[94m{options[cpu]}\n")
	p = options.index(player)
	if p == cpu:
		print(format("DRAW!", "6699FF"))
	elif p == cpu + 1 or p == cpu - 2:
		print(format("YOU WIN!", "77CC66"))
	else:
		print(format("CPU WINS!", "FF6666"))

	# replay
	if input("\nDo you want to play again? (y/n) ").lower() == "n":
		quit("\nThanks for playing!")
	print()
	choices[player] += 1