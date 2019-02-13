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
    def __init__(self, board):
        self.state = board
        self.parent = None
        self.children = []

    def result(self, pos, action):
        if action in self.state.get_moves(pos):
            return 1

    def test(self):
        return len(self.children) == 0

    def utility(self):
        return 1

class Game:
    def __init__(self):
        self.board = np.zeros((8,8))

        self.board[7][6] = 2
        self.board[0][1] = -1
        self.board[0][3] = -1
        self.board[0][5] = -1
        self.board[0][7] = -1
        print(self.board)
        self.tom_pos = (7,6)
        self.num_to_board = {}
        ind1 = 7
        ind2 = 6
        #for i in range(1,33):
         #   if ind1 % 2 == 0:
          #      ind2

        self.num_to_board = {
            1 : (7,6),
            2 : (7,4),
            3 : (7,2),
            4 : (7,0),
            5 : (6,7),
            6 : (6,5),
            7 : (6,3),
            8 : (6,1),
            9 : (5,6),
            10 : (5,4),
            11 : (5,2),
            12 : (5,0),
            13 : (4,7),
            14 : (4,5),
            15 : (4,3),
            16 : (4,1),
            17 : (3,6),
            18 : (3,4),
            19 : (3,2),
            20 : (3,0),
            21 : (2,7),
            22 : (2,5),
            23 : (2,3),
            24 : (2,1),
            25 : (1,6),
            26 : (1,4),
            27 : (1,2),
            28 : (1,0),
            29 : (0,7),
            30 : (0,5),
            31 : (0,3),
            32 : (0,1)
        }


    def get_moves(self, pos: int) -> list:
        new_pos = self.num_to_board[pos]
        moves = []
        if new_pos[0] + 1 < 8 and new_pos[1] + 1 < 8:
            if self.board[new_pos[0] + 1][new_pos[1] + 1] != -1:
                moves.append((new_pos[0] + 1, new_pos[1] + 1))
        if new_pos[0] + 1 < 8 and new_pos[1] - 1 >= 0:
            if self.board[new_pos[0] + 1][new_pos[1] - 1] != -1:
                moves.append((new_pos[0] + 1, new_pos[1] - 1))
        if new_pos[0] - 1 >= 0 and new_pos[1] - 1 >= 0:
            if self.board[new_pos[0] - 1][new_pos[1] - 1] != -1:
                moves.append((new_pos[0] - 1, new_pos[1] - 1))
        if new_pos[0] - 1 >= 0 and new_pos[1] + 1 < 8:
            if self.board[new_pos[0] - 1][new_pos[1] + 1] != -1:
                moves.append((new_pos[0] - 1, new_pos[1] + 1))

        return moves


    def move(self, pos: int, move: int) -> dict: # return the new board
        if self.num_to_board[move] in self.get_moves(pos):
            m1 = self.num_to_board[move][0]
            m2 = self.num_to_board[move][1]
            p1 = self.num_to_board[pos][0]
            p2 = self.num_to_board[pos][1]
            self.board[m1][m2] = self.board[p1][p2]
            self.board[p1][p2] = 0
        return self.board


    def is_finished(self, tom: int) -> bool:
        if tom in [29, 30, 31, 32]:
            return True
       
        if len(self.get_moves(tom)) == 0:
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

    v = Node(game.board)
    v.state = -10000

    for a in range(len(n.children)):
        temp = min_value(n.result(a), game)
        if v.state <= temp.state:
            v = temp

    return v


def min_value(n: Node, game: Game) -> Node:
    if n.test() or game.is_finished():
        return n.utility

    v = Node(game.board)
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