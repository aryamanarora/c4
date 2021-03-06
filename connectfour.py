import numpy as np
from termcolor import colored
import os


class Board(object):
    """ It's a connect four board.

    None of the methods have error handling btw.
    """

    # the board itself
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
        """Find if anyone has won yet.

        Returns 1 if player1 has won, -1 if player2 has won, 0 if no one has won.
        """

        # horizontal
        for row in self.board:
            for col in range(4):
                if row[col] == row[col + 1] == row[col + 2] == row[col + 3] != 0:
                    return row[col]
        # vertical
        for col in range(7):
            for row in range(3):
                if self.board[row][col] == self.board[row + 1][col] == self.board[row + 2][col] == self.board[row + 3][col] != 0:
                    return self.board[row][col]
        # diag right
        for row in range(3):
            for col in range(4):
                if self.board[row][col] == self.board[row + 1][col + 1] == self.board[row + 2][col + 2] == self.board[row + 3][col + 3] != 0:
                    return self.board[row][col]
        # diag left
        for row in range(3):
            for col in range(3, 7):
                if self.board[row][col] == self.board[row + 1][col - 1] == self.board[row + 2][col - 2] == self.board[row + 3][col - 3] != 0:
                    return self.board[row][col]
        return 0

    def draw(self):
        return (self.winner() is None and self.complete())

    def complete(self):
        for row in self.board:
            if 0 in row:
                return False
        return True

    def available_moves(self):
        """Gives array of valid moves"""
        cols = []
        for col in range(7):
            for row in reversed(range(6)):
                if self.board[row][col] == 0:
                    cols.append(col)
                    continue
        return set(cols) or []

    def move(self, player, col):
        """Places a piece in the connect four board. It figures out whose move it is (1 always goes first)

        Returns False if it can't be done."""
        if player != 0:
            if col not in self.available_moves():
                return False
            for row in reversed(range(6)):
                if self.board[row][col] == 0:
                    self.board[row][col] = player
                    break
        else:
            for row in range(6):
                if self.board[row][col] != 0:
                    self.board[row][col] = player
                    break

        self.last_move = player
        return True

    def view(self):
        """Prettyprints the board; red is 1 yellow is -1"""
        os.system('clear')
        for row in self.board:
            for col in row:
                if col == 1:
                    print(colored('●', 'red'), end=' ')
                elif col == -1:
                    print(colored('●', 'yellow'), end=' ')
                else:
                    print("☐", end=' ')
            print()
