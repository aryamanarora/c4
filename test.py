# supposed to be a method of connectfour.board() but it's too slow

def alphabeta(self, node, player, alpha, beta):
    # assumes 1 is the player and -1 is the opponent
    # type(board) == c4.Board
    previous_state = node
    if node.winner():
        return node.winner()
    elif node.draw():
        return 0
        bes
    for move in node.available_moves():
        print()
        print(move, end=" ")
        node.move(player, move)
        val = self.alphabeta(node, -1*player, alpha, beta)
        node.move(0, move)
        if player == 1:
            if val > alpha:
                alpha = val
            if alpha >= beta:
                return beta
        else:
            if val < beta:
                beta = val
            if beta <= alpha:
                return alpha
    if player == 1:
        return alpha
    else:
        return beta
