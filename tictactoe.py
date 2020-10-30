#!/bin/python3
# Filename: tictactoe.py
# Course: Full Stack Developer Evening Bootcamps
# Author: Leon || Cleon || Peter, Students
# Assignment: Tic-Tac-Toe - Version 1
# Date: 10/28/2020
# Version 1.0



# PDX Fullstack: Tic Tac Toe 
# You will write a **Player** class and **Game** class to model Tic Tac Toe, and a function **main** that models gameplay taking in user inputs through REPL.

import pprint

# The Player class has the following properties: 
#* **name** = *player name*
#* **token** = *'X' or 'O'*


# class Player: Peter with take this part.



# Peter Entries Starts:
class Player:
    def __init__(self, type): # self = Players, type = X or O
        self.type = type

    def __str__(self):
        return "Player {}".format(self.type)


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

# class Game:

    def __init__(self, board):
        self.board = {'top-L': ' ',
                        'top-M': ' ',
                        'top-R': ' ',
                        'mid-L': ' ',
                        'mid-M': ' ',
                        'mid-R': ' ',
                        'low-L': ' ',
                        'low-M': ' ',
                        'low-R': ' '}
    def __repr__():
        # pretty print board

        print(str(self.board['top-L']) + '|' + str(self.board['top-M']) + '|' + str(self.board['top-R']))
        print('-+-+-')
        print(str(self.board['mid-L']) + '|' + str(self.board['mid-M']) + '|' + str(self.board['mid-R']))
        print('-+-+-')
        print(str(self.board['low-L']) + '|' + str(self.board['low-M']) + '|' + str(self.board['low-R']))
    def move(turn, player):
        print(self.board)
    def move(x, y, player):
        # player's token overwrites data for space in board
        # board(x, y) = player #either 'X' or 'O'
        
    def calc_winner():
        # check if winning condition met
        # horizontal_win_conditions = iterate 3 rows
        # vertical win condition = iterate 3 columns
        # l-diagonal
        # r-diagonal
    def is_full():
        # check if draw condition met
    def is_game_over():
        # check if either calc_wnner OR is_full are True

def main:
    board = Game()

main()

print("hello, world!")
print("Leon's portion of the game.")

game_on = Game()


print(game.board)

player_1 = Player('P1', 'X')
player_2 = Player('P2', 'O')

print(game_on.move('top-L', 'P1'))

print(game.board)


