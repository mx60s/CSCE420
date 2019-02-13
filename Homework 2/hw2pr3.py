# Maggie von Ebers
# 525001114
# CSCE 420
# Due: February 14, 2019
# hw2pr3.py

# so here, max is tom brady
# min is the rams (human player), but it might not need an algorithm cause it'll just be taking command line input
# so maybe nodes need to be mapped then

import numpy as np

class Board:
    def __init__(self):
        self.b = np.zeros((8,8))
        self.b[7][6] = 2
        self.b[0][1] = -1
        self.b[0][3] = -1
        self.b[0][5] = -1
        self.b[0][7] = -1

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
            32 : (0,1),
        }

        self.board_to_num = {
            (7,6) : 1,
            (7,4) : 2,
            (7,2) : 3,
            (7,0) : 4,
            (6,7) : 5, 
            (6,5) : 6,
            (6,3) : 7,
            (6,1) : 8,
            (5,6) : 9,
            (5,4) : 10,
            (5,2) : 11,
            (5,0) : 12,
            (4,7) : 13,
            (4,5) : 14,
            (4,3) : 15,
            (4,1) : 16,
            (3,6) : 17,
            (3,4) : 18,
            (3,2) : 19,
            (3,0) : 20,
            (2,7) : 21,
            (2,5) : 22,
            (2,3) : 23,
            (2,1) : 24,
            (1,6) : 25,
            (1,4) : 26,
            (1,2) : 27,
            (1,0) : 28,
            (0,7) : 29,
            (0,5) : 30,
            (0,3) : 31,
            (0,1) : 32
        }

    def get_moves(self, pos: tuple) -> list:
        print("Possible moves for position", pos)
        moves = []
        if type(pos) != tuple:
            pos = self.num_to_board[int(pos)]
            # print(pos)
        if self.b[pos[0]][pos[1]] == 2:
            if pos[0] + 1 < 8 and pos[1] + 1 < 8:
                if self.b[pos[0] + 1][pos[1] + 1] == 0:
                    #print(pos[0]+1, ",", pos[1]+ 1)
                    moves.append((pos[0] + 1, pos[1] + 1))
            if pos[0] + 1 < 8 and pos[1] - 1 >= 0:
                if self.b[pos[0] + 1][pos[1] - 1] == 0:
                    #print(pos[0]+1, ",", pos[1]- 1)
                    moves.append((pos[0] + 1, pos[1] - 1))
        if pos[0] - 1 >= 0 and pos[1] - 1 >= 0:
            if self.b[pos[0] - 1][pos[1] - 1] == 0:
                #print(pos[0]-1, ",", pos[1]- 1)
                moves.append((pos[0] - 1, pos[1] - 1))
        if pos[0] - 1 >= 0 and pos[1] + 1 < 8:
            if self.b[pos[0] - 1][pos[1] + 1] == 0:
                #print(pos[0]-1, ",", pos[1]+ 1)
                moves.append((pos[0] - 1, pos[1] + 1))

        print(*moves)
        return moves


    def move(self, pos: tuple, move: tuple) -> dict: # return the new board
        if move in self.get_moves(pos):
            self.b[move[0]][move[1]] = self.b[pos[0]][pos[1]]
            self.b[pos[0]][pos[1]] = 0
        return self


class Node:
    def __init__(self, b: Board):
        self.state = b
        self.action = (7,6)

    def result(self, action):
        if action in self.state.get_moves(self.action):
            n = Node(self.state.move(self.action,action))
            n.action = action
            return n

    def test(self):
        return (len(self.state.get_moves(self.action)) == 0) or (self.action in [(0,1), (0,3), (0,5), (0,7)])

    def utility(self):
        if len(self.state.get_moves(self.action)) == 0:
            return -1
        elif self.action in [29, 30, 31, 32]:
            return 1
        else:
            return self.state.board_to_num[self.action]/32


class Game:
    def __init__(self):
        self.gameboard = Board()
        self.tom = TomBrady(self)

    def is_finished(self) -> bool:
        if self.tom.pos in [29, 30, 31, 32]:
            print("Tom wins")
            return True
        if len(self.gameboard.get_moves(self.tom.pos)) == 0:
            print("You win!")
            return True
        return False

    def rams_turn(self) -> None:
        while(True):
            ram = input("Which ram do you want to move? ")
            ram_pos = self.gameboard.num_to_board[int(ram)]
            if self.gameboard.b[ram_pos[0]][ram_pos[1]] == -1:
                break
            else:
                print("There's not a ram in that square.")
        while(True):
            move = input("Where do you want to move? ")
            print(move, "maps to", self.gameboard.num_to_board[int(move)])
            if self.gameboard.num_to_board[int(move)] not in self.gameboard.get_moves(ram):
                print("That's not a valid move.")
            else:
                break
        self.gameboard.b[ram_pos[0]][ram_pos[1]] = 0
        move_pos = self.gameboard.num_to_board[int(move)]
        self.gameboard.b[move_pos[0]][move_pos[1]] = -1

    def play(self) -> None:
        self.tom.start_position()
        while (True):
            self.gameboard.move(self.tom.pos, self.tom.move(self.gameboard))
            if self.is_finished():
                print("Game finished")
                return
            print(self.gameboard.b)
            self.rams_turn()
            print(self.gameboard.b)
            if self.is_finished():
                print("Game finished")
                return


class TomBrady:
    def __init__(self, game: Game):
        self.pos = 1
        self.board = game.gameboard
        self.depth = 2

    def start_position(self) -> None:
        return
    
    def move(self, state: Board):
        action = self.alpha_beta_search()
        print("Tom moved to space", action)
        return action


    def max_value(self, n: Node, alpha: int, beta: int, d: int) -> Node:
        print("Max value")
        if n.test() or d == self.depth:
            print("Test returned true in max")
            return n

        v = Node(n.state)
        util = -10000

        for a in n.state.get_moves(n.action):
            print("Action",a)
            temp = self.min_value(n.result(a), alpha, beta, d + 1)
            if util <= temp.utility():
                v = temp
                util = v.utility()
            alpha = max(alpha, util)
            if beta <= alpha:
                print("Beta pruning")
                break

        return v


    def min_value(self, n: Node, alpha: int, beta: int, d: int) -> Node:
        print("Min value")
        if n.test() or d == self.depth:
            print("Test returned true in min")
            return n

        print("v")
        v = Node(n.state)
        util = 10000
        print("children")
        for a in n.state.get_moves(n.action):
            temp = self.max_value(n.result(a), alpha, beta, d + 1)
            if util >= temp.utility():
                v = temp
                util = v.utility()
            beta = min(beta, v.utility())
            if beta <= alpha:
                print("Alpha pruning")
                break
    
        return v


    def alpha_beta_search(self) -> Node:
        n = Node(self.board)
        v = self.max_value(n, -10000, 10000, 0)
        return v.action   # idk


g = Game()
g.play()