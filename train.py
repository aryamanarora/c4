import connectfour as c4
import random
import os
import numpy as np
import itertools

best = []

class Network(object):
    def __init__(self, sizes):
        self.num_layers = len(sizes)
        self.sizes = sizes
        self.biases = [np.random.randn(y, 1) for y in sizes[1:]]
        self.weights = [np.random.randn(y, x)
                        for x, y in zip(sizes[:-1], sizes[1:])]
    def feedforward(self, a):
        for b, w in zip(self.biases, self.weights):
            a = sigmoid(np.dot(w, a)+b).tolist()
        b = []
        for data in a:
            b.append(data[0])
        return b

def sigmoid(z):
    """The sigmoid function."""
    return 1.0/(1.0+np.exp(-z))

def sigmoid_prime(z):
    """Derivative of the sigmoid function."""
    return sigmoid(z)*(1-sigmoid(z))

def extract_board(board):
    data = board.board
    result = []
    for row in data:
        for col in row:
            result.append(1 if col == 1 else 0)
    for row in data:
        for col in row:
            result.append(1 if col == -1 else 0)
    for row in data:
        for col in row:
            result.append(1 if col == 0 else 0)
    return result

def player_vs_bot(bot):
    board = c4.Board()

    # the first move
    player = 1
    os.system('clear')
    board.move(player, int(input("Move (1-7): "))-1)
    board.view()

    while board.winner() not in (1, -1):
        player = -1
        input_layer = extract_board(board)
        output_layer = bot.feedforward(input_layer)
        move = np.argmax(output_layer)

        while move not in board.available_moves():
            output_layer[move] = 0
            move = np.argmax(output_layer)
        board.move(player, move)

        board.view()
        if board.draw():
            print("Draw!")
            break
        if board.winner() in (1, 2):
            print("The winner is " + "the bot" if board.winner() == -1 else "you")

        # player's turn
        player = 1
        move = int(input("Move: "))-1
        while move not in board.available_moves():
            move = int(input("Invalid move: "))-1
        board.move(player, move)

        board.view()
        if board.draw():
            print("Draw!")
            break
        if board.winner() in (1, 2):
            print("The winner is " + "the bot" if board.winner() == -1 else "you")

def competition(bots):
    """30 random neural networks fight each other. (900 games)
    The best goes on to the natural selection phase.
    """
    board = c4.Board()
    scores, games = [], []
    for i in range(30):
        scores.append(0)

    games = list(itertools.combinations(list(range(len(bots)))*2, 2))

    for (i, j) in games:
        print(i, j)
        bot_i = bots[i]
        bot_j = bots[j]
        board = c4.Board()
        no_moves = False

        while board.winner() not in (1, -1) or no_moves == True:
            # boti's turn
            player = 1
            input_layer = extract_board(board)
            output_layer = bot_i.feedforward(input_layer)
            move = np.argmax(output_layer)

            # print(board.available_moves())
            while move not in board.available_moves() and len(board.available_moves()) != 0:
                output_layer[move] = 0
                move = np.argmax(output_layer)
            if len(board.available_moves()) == 0:
                break

            board.move(player, move)

            if board.draw():
                board.view()
                print("Draw!")
                continue
            if board.winner() in (1, -1):
                board.view()
                print("The winner is " + str(i) if board.winner() == 1 else str(j))
                if board.winner == 1:
                    scores[i] += 1
                    scores[j] -= 1
                else:
                    scores[j] += 1
                    scores[i] -= 1
                continue

            # botj's turn
            player = -1
            input_layer = extract_board(board)
            output_layer = bot_j.feedforward(input_layer)
            move = np.argmax(output_layer)

            # print(board.available_moves())
            while move not in board.available_moves() and len(board.available_moves()) != 0:
                output_layer[move] = 0
                move = np.argmax(output_layer)
            if len(board.available_moves()) == 0:
                break
            board.move(player, move)

            if board.draw():
                board.view()
                print("Draw!")
                continue
            if board.winner() in (1, 2):
                board.view()
                print("The winner is " + str(i) if board.winner() == 1 else str(j))
                if board.winner == 1:
                    scores[i] += 1
                    scores[j] -= 1
                else:
                    scores[j] += 1
                    scores[i] -= 1
                continue
    print(scores)
    return bots[scores.index(max(scores))]

def select():
    best = []
    for i in range(15):
        bots = []
        bots.append(Network([126, 400, 7]))
        best.append(competition(bots))
    best = competition(best)
    with open('best.txt') as f:
        f.write(best.sizes)
        f.write(best.weights)
        f.write(best.biases)

if name == "__main__":
    select()
