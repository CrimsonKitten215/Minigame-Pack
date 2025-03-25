import random

def format(text: str, fg="-1", underline=False, boxed=False):
	code = ""
	if underline:
		code += ";4"
	if boxed:
		code += ";51"
	if fg != "-1":
		code += f";38;2;{int(fg[0:2], 16)};{int(fg[2:4], 16)};{int(fg[4:6], 16)}"

	return f"\033[1{code}m{text}\033[0m"

def unlistify(listy: list):
	return str(listy).strip("[").strip("]").replace("'", "").replace(",", "")

def display_board(board):
	print(format(f"{format(unlistify(board[0:3]), "FF6666", boxed=True)}\n{format(unlistify(board[3:6]), "77CC66", boxed=True)}\n{format(unlistify(board[6:9]), "6699FF", boxed=True)}"))

def win_checker(board: list, symbol: str):
	win = f"[{symbol}] [{symbol}] [{symbol}]"
	if unlistify(board[0:3]) == win or unlistify(board[3:6]) == win or unlistify(board[6:9]) == win:
		return True
	if f"{board[0]} {board[3]} {board[6]}" == win or f"{board[1]} {board[4]} {board[7]}" == win or f"{board[2]} {board[5]} {board[8]}" == win:
		return True
	if f"{board[0]} {board[4]} {board[8]}" == win or f"{board[2]} {board[4]} {board[6]}" == win:
		return True
	return False

def game(board: list):
	for turn in range(0, 5):
		# player's turn
		valid = False
		while not valid:
			try:
				player_input = int(input("\n" + format("Player's Turn: ")))
				if board[player_input - 1] == "[ ]":
					board[player_input - 1] = "[X]"
					valid = True
				else:
					print("You have to pick a valid square.")
			except:
				print("You have to pick a valid square.")
		display_board(board)
		if win_checker(board, "X"):
			return 1

		# cpu's turn
		if turn < 5:
			valid = False
			while not valid:
				cpu_input = random.randint(0, 8)
				if board[cpu_input] == "[ ]":
					print(f"\n{format("CPU's Turn: ")}\033[94m{cpu_input + 1}")
					board[cpu_input] = "[O]"
					valid = True
			display_board(board)
			if win_checker(board, "X"):
				return 2
	return 0


board = ["[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]"]
print(f"{format("Naughts & Crosses:", underline=True)}\n\nPlayer is 'X'\nCPU is 'O'\nPlayer starts.\n\nPick a number from 1-9 to claim a square.\n")
display_board(board)
next = ""
while next == "":
	winner = game(board)
	if winner == 0:
		print(format("\nDRAW!", "6699FF"))
	elif winner == 1:
		print(format("\nYOU WIN!", "77CC66"))
	else:
		print(format("\nCPU WINS!", "FF6666"))
	next = input("\nPress 'Enter' to play again! ")
	board = ["[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]"]