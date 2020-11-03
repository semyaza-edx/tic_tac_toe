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
    def __init__(self, name, typex): # self = Players, typex = X or O
        self.name = name
        self.typex = typexx
        self.boom = False

    def __str__(self):
        return "Player {}".format(self.typexx)


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

    board = {'top-L': ' ',
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

        print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
        print('-+-+-')
        print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
        print('-+-+-')
        print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])
    '''    
    def move(turn, player):
        print(self.board)
    '''
    #maybe move function inside a for loop so it will go back and for between two players. 
    def move(position, Player_name):
        if board[position]  == "X" and board[position] == "O":
            print("Already taken! Try another ")
            continue
        elif board[position] != "X" and board[position] != "O":
            place_holder = Player_name.typexx # Player_name.typex is "X" or "O"
            board[position] =  place_holder 
        # player's token overwrites data for space in board
        # board(x, y) = player #either 'X' or 'O'
        
    def calc_winner(player_obj): # Parameter will be current player, so we can compare inside function.
        #Use some kind of loop to rotate player turns 
        # check if winning condition met
        # horizontal_win_conditions = iterate 3 rows
        # vertical win condition = iterate 3 columns
        # l-diagonal
        # r-diagonal
        # Thinking about highlighting the rows winning the game 
        if board[top-L] == player_obj.typex and board[top-M] == player_obj.typex and board[top-R] == player_obj.typex: # Top
            return player_obj.type 
        elif board[mid-L] == player_obj.typex and board[mid-M] == player_obj.typex and board[mid-R] == player_obj.typex: # Mid
            return player_obj.type 
        elif board[low-L] == player_obj.typex and board[low-M] == player_obj.typex and board[low-R] == player_obj.typex: #Bottom
            return player_obj.type 
        elif board[top-R] == player_obj.typex and board[mid-R] == player_obj.typex and board[low-R] == player_obj.typex: # Right side
            return player_obj.type 
        elif board[top-M] == player_obj.typex and board[mid-M] == player_obj.typex and board[low-M] == player_obj.typex: # Down middle
            return player_obj.type 
        elif board[top-L] == player_obj.typex and board[mid-L] == player_obj.typex and board[low-L] == player_obj.typex: # Left side
            return player_obj.type 
        elif board[top-R] == player_obj.typex and board[mid-M] == player_obj.typex and board[low-L] == player_obj.typex: #Diagonal start top Right
            return player_obj.type 
        elif board[top-L] == player_obj.typex and board[mid-M] == player_obj.typex and board[low-R] == player_obj.typex: #Diagonal start top left
            return player_obj.type 
        else:
            return ""

        
        
    def is_full():
        # check if draw condition met
        i = all(value == "X" or value == "0"  for value in board.values()): # Checks if all the values in dictionary are "X" or "O". Returns True or False
        return i
        
        # May need to place in a return statement if error occurs
            

    def is_game_over():
        # check if either calc_winner OR is_full are True

def main():
    game_1 = Game()
    player_1 = Player('P1', 'X')
    player_2 = Player('P2', 'O')

    list_of_Players = [player_1,player_2]
    count = 1
    while True:
        for Player_name in list_of_Players:# All function  Player argument function inputs should be handled by for loop
            game_1.board.__repr__() # Display board
            p_move = input("Where would you like to move?")
            game_1.board.move(p_move,Player_name)
            # if count less than 5 continue 
            game_1.board.__repr__() # Display board
            x = game_1.board.calc_winner()
            if x == "X" or x == "O":
                print(f"{Player_name.name} is the winner!")
            
            
            
            
            #maybe place calc_winner function next --- maybe add a bool attribute to Player class __init__ function. We can use
            # that to check which player won and return winner using player_name in for loop. 
            game_1.board.calc_winner()











            #place is_full function here

            
            








main()

print("hello, world!")
print("Leon's portion of the game.")

game_on = Game()


print(game.board)



print(game_on.move('top-L', 'P1'))

print(game.board)




