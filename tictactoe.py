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
# class Game:




    def __init__(self, board):
        self.board = board
    def __repr__():
        # pretty print board
        print(self.board)
    def move(x, y, player):
        # player's token overwrites data for space in board

# def main:

# main()

print("hello, world!")





##############
class game:
    

