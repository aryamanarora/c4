import connectfour as c4
import random

class Network(object):

    def __init__(self, sizes):
        self.num_layers = len(sizes)
        self.sizes = sizes
        self.biases = [np.random.randn(y, 1) for y in sizes[1:]]
        self.weights = [np.random.randn(y, x)
                        for x, y in zip(sizes[:-1], sizes[1:])]

    def feedforward(self, a):
        for b, w in zip(self.biases, self.weights):
            a = sigmoid(np.dot(w, a)+b)
        return a

def sigmoid(z):
    """The sigmoid function."""
    return 1.0/(1.0+np.exp(-z))

def sigmoid_prime(z):
    """Derivative of the sigmoid function."""
    return sigmoid(z)*(1-sigmoid(z))

def extract_board(board):
    data = board.board
    result = []
    for row in board:
        for col in row:
            result.append([1 if col == 1 else 0])
    for row in board:
        for col in row:
            result.append([-1 if col == -1 else 0])

board = c4.Board()
bot = Network([84, random.randint(200, 500), 7])

# the first move
player = 1
board.move(player, int(input("Move (1-7): "))-1)

while board.winner() == None and board.draw() == False:
    input_layer = extract_board(board)
