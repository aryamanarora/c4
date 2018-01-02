# a very helpful resource: https://cwoebker.com/posts/tic-tac-toe

import connectfour as c4

def minmax(board):
    # assumes 1 is the player and -1 is the opponent
    # type(board) == c4.Board
    if board.complete():
        if board.winner():
            return board.winner():
        elif board.draw():
            return 0
        best = None
    for move in board.available_moves():
        board.move(move)
        val = self.m
