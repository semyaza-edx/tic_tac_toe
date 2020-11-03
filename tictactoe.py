#!/bin/python3
# Filename: tictactoe.py
# Course: Full Stack Developer Evening Bootcamps
# Author: Leon || Cleon || Peter, Students
# Assignment: Tic-Tac-Toe - Version 1
# Date: 10/28/2020
# Version 36.0.47b



# PDX Fullstack: Tic Tac Toe 
# You will write a **Player** class and **Game** class to model Tic Tac Toe, and a function **main** that models gameplay taking in user inputs through REPL.

# The Player class has the following properties: 
#* **name** = *player name*
#* **token** = *'X' or 'O'*
# Peter Entries Starts:
class Player:
    def __init__(self, name, token): 
        self.name = name
        self.token = token

# Peter Entries Ends:

# The Game class has the following properties:
# * **board** = *your representation of the board* <Cleon>
# You can represent the board however you like, such as a 2D list, tuples, or dictionary.
# The Game class has the following methods:
# <Leon> * `__repr__()` Returns a pretty string representation of the game board
# * 'move(x, y, player)' place a player's token character at a given coordinate 
# * 'calc_winner()' determines if a victory condition is met by a Player
# * 'is_full()' returns True if the game board is full and no victory condition met
# * 'is_game_over()' returns True if game board is full or a player has won

class Game:
    def __init__(self):
        self.board = {'top-L': ' ',
                        'top-M': ' ',
                        'top-R': ' ',
                        'mid-L': ' ',
                        'mid-M': ' ',
                        'mid-R': ' ',
                        'low-L': ' ',
                        'low-M': ' ',
                        'low-R': ' '}
    def __repr__(self):
        # pretty print board
        return f"{self.board['top-L']}|{self.board['top-M']}|{self.board['top-R']}\n-+-+-\n{self.board['mid-L']}|{self.board['mid-M']}|{self.board['mid-R']}\n-+-+-\n{self.board['low-L']}|{self.board['low-M']}|{self.board['low-R']}\n"
        
    def move(self, turn, player):
        # place tokens over the board
        if turn in self.board:
            self.board[turn] = player.token
            

    def calc_winner(self, p1, p2):
        # check if winning condition met
        vic = '' # fill with either p1 or p2
        players = [p1, p2]
        for player in players:
        # horizontal_win_conditions = iterate 3 rows
            if player.token == self.board['top-L'] == self.board['top-M'] == self.board['top-R']:
                vic = player
            if player.token == self.board['mid-L'] == self.board['mid-M'] == self.board['mid-R']:
                vic = player
            if player.token == self.board['low-L'] == self.board['low-M'] == self.board['low-R']:
                vic = player
        # vertical win condition = iterate 3 columns
            if player.token == self.board['top-L'] == self.board['mid-L'] == self.board['low-L']:
                vic = player
            if player.token == self.board['top-M'] == self.board['mid-M'] == self.board['low-M']:
                vic = player
            if player.token == self.board['top-R'] == self.board['mid-R'] == self.board['low-R']:
                vic = player
        # l-diagonal
            if player.token == self.board['top-L'] == self.board['mid-M'] == self.board['low-R']:
                vic = player
        # r-diagonal
            if player.token == self.board['top-R'] == self.board['mid-M'] == self.board['low-L']:
                vic = player
        return vic

    def is_full(self):
        # check if draw condition met
        empty = 0
        for i in self.board: 
            if self.board[i] == ' ':
                empty += 1
        if empty == 0:
            return True
        else:
            return False

    def is_game_over(self, p1, p2):
        # check if either calc_wnner OR is_full are True
        vic = self.calc_winner(p1, p2)
        draw = self.is_full()
        if draw == True:
            return True
        elif vic != '':
            return True
        else:
            return False

def main():
    game_on = Game()
    print("\tMoves are top-L, top-M, top-R,\n \
         \tmid-L, mid-M, mid-R, \n\
         \tlow-L, low-M, low-R.")
    print(repr(game_on))
    player1 = input("P1 will be 'X'. Enter name: ")
    player2 = input("P2 will be 'O'. Enter name: ")
    p1 = Player(player1, 'X')
    p2 = Player(player2, 'O')
    plist = [p1, p2]

    endgame  = False
    # add a loop layer to make replayable...
    while not endgame: 
        for player in plist:
            while True:
                try:
                    turn = input(f"Enter a square to take, {player.name}: ")
                    print("\n")
                    if ((turn in game_on.board) & (game_on.board[turn] == ' ')):
                        game_on.move(turn, player)
                        break
                    else: 
                        print("Try again.")
                except KeyError:
                    print("Try again.")

            print(repr(game_on))

            vic = game_on.calc_winner(p1, p2)

            end = game_on.is_game_over(p1, p2)

            if end == True:
                endgame = True
                break
    if vic == '':
        print("Draw")
    else:
        print(f"{vic.name} wins.")



main()










#print(game_on.move('top-L', 'P1'))




