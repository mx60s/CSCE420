# Maggie von Ebers
# 525001114
# CSCE 420
# Due: February 14, 2019
# hw2pr3.py

# so here, max is tom brady
# min is the rams (human player), but it might not need an algorithm cause it'll just be taking command line input
# so maybe nodes need to be mapped then

import numpy as np

class Node:
    def __init__(self):
        self.state = tuple()
        self.parent = None
        self.children = []

    def get_moves(self, board) -> list:
        moves = []
        if self.state[0] + 1 < 8 and self.state[1] + 1 < 8:
            if board[self.state[0] + 1][self.state[1] + 1] == 1:
                moves.append((self.state[0] + 1, self.state[1] + 1))
        if self.state[0] + 1 < 8 and self.state[1] - 1 >= 0:
            if board[self.state[0] + 1][self.state[1] - 1] == 1:
                moves.append((self.state[0] + 1, self.state[1] - 1))
        if self.state[0] - 1 >= 0 and self.state[1] - 1 >= 0:
            if board[self.state[0] - 1][self.state[1] - 1] == 1:
                moves.append((self.state[0] - 1, self.state[1] - 1))
        if self.state[0] - 1 >= 0 and self.state[1] + 1 < 8:
            if board[self.state[0] - 1][self.state[1] + 1] == 1:
                moves.append((self.state[0] - 1, self.state[1] + 1))

        return moves


    def result(self, action):
        return self.children[action]

    def test(self):
        return len(self.children) == 0

    def utility(self):
        return 1

class Game:
    def __init__(self):
        self.board = np.zeros((8,8))
        for i in range(8):
            for j in range(8):
                if (i + j) % 2 != 0:
                    self.board[i][j] = 1
        self.board[7][6] = 2
        self.board[0][1] = -1
        self.board[0][3] = -1
        self.board[0][5] = -1
        self.board[0][7] = -1
        print(self.board)
        self.rams_pos = [(0,1), (0,3), (0,5), (0,7)]
        self.tom_pos = (7,6)

    def move(self, pos: int, move: int) -> dict: # return the new board
        return


    def is_finished(self, tom: Node) -> bool:
        #if self.brady_pos in [29, 30, 31, 32]:
         #   return True
       
        if len(tom.get_moves(self.board)) == 0:
            return True

        return False
        
        

    def play(self, tom: Node) -> None:
        # don't forgot to update their positions
        while not self.is_finished(tom):
            play_rams()
            play_brady()


def max_value(n: Node, game: Game) -> Node:
    if n.test() or game.is_finished():
        return n.utility()

    v = Node()
    v.state = -10000

    for a in range(len(n.children)):
        temp = min_value(n.result(a), game)
        if v.state <= temp.state:
            v = temp

    return v


def min_value(n: Node, game: Game) -> Node:
    if n.test() or game.is_finished():
        return n.utility

    v = Node()
    v.state = 10000

    for a in range(len(n.children)):
        temp = max_value(n.result(a),game)
        if v.state >= temp.state:
            v = temp

    return v


def minimax_decision(n: Node, game: Game):
    val = min_value(n.result(0), game)

    for a in range(1, len(n.children)):
        temp = min_value(n.result(a), game)
        if temp.state > val.state:
            val = temp

    return val


def play_rams() -> None:
    ram = input("Which Ram do you want to move?")
    # validate input
    pos = input("To which square?")
    # validate input

def play_brady() -> None:
    return

g = Game()