#! /usr/bin/python
import os


class tik_tak_toe:
	def __init__(self, player, first, second, third) -> None:
		self.board = [' ']*9
		self.current_player = player	
		self.first_player = first
		self.second_player = second	
		self.choice = third
		
	def print_board(self):
		print("The current boad state is:")
		print('-------------')
		for i in range(3):
			print(f'| {i*3} | {i*3+1} | {i*3+2} |')
			print(f'| {self.board[i*3]} | {self.board[i*3+1]} | {self.board[i*3+2]} |')
			print('-------------')
		
		print("")
		print("######################")
		if self.choice == self.current_player:
			print(f"It's {self.first_player}'s turn")
		else:
			print(f"It's {self.second_player}'s turn")
		print("######################")
		print("Enter the number for the box you would like to play: ")
		
	def make_move(self, position):
		if self.board[position] == ' ':
			self.board[position] = self.current_player
			if self.current_player == 'X':
				self.current_player = 'O'
			else:
				self.current_player = 'X'
			return True
		else:
			return False

	def play(self):
		while True:
			self.print_board()
			val = input("The space entered is: " )
			game.make_move(int(val))
			if self.check_win() or self.check_tie():
				self.print_board()
				break


	def check_win(self):
		win_positions = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
		for pos in win_positions:
			if self.board[pos[0]] == self.board[pos[1]] == self.board[pos[2]] != ' ':
				return True
		return False

	def check_tie(self):
		if ' ' not in self.board:
			return True
		else:
			return False

print("Hello! Welcome to tic tac toe")
print("This game requires two players")

print("Please enter the name of player 1: ")
player_1 = input()
print("Please enter the name of player 2: ")
player_2 = input()

players_choice = ''
which_player = ''
while True:
	print(f"Who will be X and who will be O? Let's let {player_1} choose") 
	which_player = input("Please enter 'X' for player X or 'O' for player O: ")	
	if which_player == 'X' or which_player == 'O':
		players_choice = which_player
		print("players_choise: " + players_choice)
		print("which_player: " + which_player)
		break



game = tik_tak_toe(which_player,player_1,player_2,players_choice)
game.play()	
if game.check_win():
	print(f"Player {game.current_player} wins!")
elif game.check_tie():
	print("The game ends in a tie!")



