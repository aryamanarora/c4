import numpy as np
from termcolor import colored

class Board:
    """ It's a connect four board.

    None of the methods have error handling btw.
    """
    def __init__(self):
        self.board = [
                        [0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0]
        ]

    def winner(self):
        """Find if anyone has one yet.

        Returns 1 if player1 has won, -1 if player2 has won, 0 if no one has won.
        """
        for row in self.board: # horizontal
            for col in range(4):
                if row[col] == row[col+1] == row[col+2] == row[col+3] != 0:
                    return row[col]
        for col in range(7): # vertical
            for row in range(3):
                if self.board[row][col] == self.board[row+1][col] == self.board[row+2][col] == self.board[row+3][col]:
                    return self.board[row][col]
        for row in range(3): # diagonal right
            for col in range(4):
                if self.board[row][col] == self.board[row+1][col+1] == self.board[row+2][col+2] == self.board[row+3][col+3] != 0:
                    return self.board[row][col]
        for row in range(3): # diagonal left
            for col in range(3, 7):
                if self.board[row][col] == self.board[row+1][col-1] == self.board[row+2][col-2] == self.board[row+3][col-3] != 0:
                    return self.board[row][col]
        return 0 # no winners

    def valid(self, col):
        """Checks if move is valid"""
        valid = False
        for row in reversed(range(6)):
            if self.board[row][col] == 0:
                valid = True
        return valid

    def move(self, col):
        """Places a piece in the connect four board. It figures out whose move it is (1 always goes first)

        Returns False if it's an invalid move/somebody."""
        if not self.valid(col):
            return False
        player = -2 * sum(map(sum, self.board)) + 1 # black magic, don't worry about it
        for row in reversed(range(6)):
            if self.board[row][col] == 0:
                self.board[row][col] = player
                break
        return True

    def view(self):
        """Prettyprints the board; red is 1 yellow is -1"""
        for row in self.board:
            for col in row:
                if col == 1:
                    print(colored('●', 'red'), end=' ')
                elif col == -1:
                    print(colored('●', 'yellow'), end=' ')
                else: print("☐", end=' ')
            print()
