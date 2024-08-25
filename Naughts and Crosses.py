import random
board = ["[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]"]
print("\n\n\033[1;20;48mNaughts and Crosses:\n\nPlayer is 'X'\nCPU is 'O'\nPlayer starts.\n\nPick a number from 1-9 to claim a square.\n\n\033[1;36;48m"+board[0]+board[1]+board[2]+"\n\033[1;31;48m"+board[3]+board[4]+board[5]+"\n\033[1;32;48m"+board[6]+board[7]+board[8]+"\033[0;20;48m")
def Game(board):
		global winner
		board = ["[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]"]
		for turn in range(1, 10):
				valid = False
				while valid == False:
						try:
								if turn % 2 == 0:
										cpu_input = random.randint(0, 8)
										if board[cpu_input] == "[ ]":
												print("\nCPU's Turn:\033[3;32;48m",str(cpu_input + 1)+"\033[0;30;48m")
												board[cpu_input] = "[O]"
												valid = True
								else:
										player_input = int(input("\nPlayer's Turn: "))
										if board[player_input - 1] == "[ ]":
												board[player_input - 1] = "[X]"
												valid = True
										else:
												print("You have to pick a valid square.")
						except:
								print("You have to pick a valid square.")
				print(f"\033[1;36;48m{board[0]+board[1]+board[2]}\n\033[1;31;48m{board[3]+board[4]+board[5]}\n\033[1;32;48m{board[6]+board[7]+board[8]}\033[0;20;48m")
				#win/loss
				if board[0] == "[O]" and board[1] == "[O]" and board[2] == "[O]":
						winner = 2
				elif board[3] == "[O]" and board[4] == "[O]" and board[5] == "[O]":
						winner = 2
				elif board[6] == "[O]" and board[7] == "[O]" and board[8] == "[O]":
						winner = 2
				elif board[0] == "[O]" and board[3] == "[O]" and board[6] == "[O]":
						winner = 2
				elif board[1] == "[O]" and board[4] == "[O]" and board[7] == "[O]":
						winner = 2
				elif board[2] == "[O]" and board[5] == "[O]" and board[8] == "[O]":
						winner = 2
				elif board[0] == "[O]" and board[4] == "[O]" and board[8] == "[O]":
						winner = 2
				elif board[2] == "[O]" and board[4] == "[O]" and board[6] == "[O]":
						winner = 2
				elif board[0] == "[X]" and board[1] == "[X]" and board[2] == "[X]":
						winner = 1
				elif board[3] == "[X]" and board[4] == "[X]" and board[5] == "[X]":
						winner = 1
				elif board[6] == "[X]" and board[7] == "[X]" and board[8] == "[X]":
						winner = 1
				elif board[0] == "[X]" and board[3] == "[X]" and board[6] == "[X]":
						winner = 1
				elif board[1] == "[X]" and board[4] == "[X]" and board[7] == "[X]":
						winner = 1
				elif board[2] == "[X]" and board[5] == "[X]" and board[8] == "[X]":
						winner = 1
				elif board[0] == "[X]" and board[4] == "[X]" and board[8] == "[X]":
						winner = 1
				elif board[2] == "[X]" and board[4] == "[X]" and board[6] == "[X]":
						winner = 1
				if winner != 0:
						break
#loop
while True:
		winner = 0
		Game(board)
		if winner == 0:
				print("\n\nDRAW!")
		elif winner == 2:
				print("\n\nCPU WINS!")
		elif winner == 1:
				print("\n\nYOU WIN!")
		skippy_variable = input("\n\nPress 'Enter' to play again! ")