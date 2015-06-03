from random import randint

board = []
boardGridSize = 7
turns = 5

for x in range(boardGridSize):
	board.append(["O"] * boardGridSize)

def print_board(board):
	for row in board:
		print " ".join(row)

print "Let's play Battleship!"
print_board(board)

def random_row(board):
	return randint(0, len(board) - 1)

def random_col(board):
	return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)
print '(%s, %s)' % ship_row, ship_col

# Everything from here on should go in your for loop!
# Be sure to indent four spaces!
for turn in range(turns):
	guess_row = int(raw_input("Guess Row:"))
	guess_col = int(raw_input("Guess Col:"))
	
	if guess_row == ship_row and guess_col == ship_col:
		print "Congratulations! You sunk my battleship!"
		break
	else:
		if (guess_row < 0 or guess_row > boardGridSize - 1) or \
		(guess_col < 0 or guess_col > boardGridSize - 1):
			print "Oops, that's not even in the ocean."
		elif(board[guess_row][guess_col] == "X"):
			print "You guessed that one already."
		else:
			print "You missed my battleship!"
			board[guess_row][guess_col] = "X"
		if turn == turns - 1:
			print 'Game Over'
				
		print_board(board)
		# Print (turn + 1) here!
		print (turn + 1)