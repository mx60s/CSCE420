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
        self.board = np.zeros((8,8))
        self.board[7][6] = 2
        self.board[0][1] = -1
        self.board[0][3] = -1
        self.board[0][5] = -1
        self.board[0][7] = -1

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
        # This works!
        print("Possible moves for position", pos)
        new_pos = self.num_to_board[pos]
        moves = []
        if new_pos[0] + 1 < 8 and new_pos[1] + 1 < 8:
            if self.board[new_pos[0] + 1][new_pos[1] + 1] == 0:
                print(new_pos[0]+1, ",", new_pos[1]+ 1)
                moves.append((new_pos[0] + 1, new_pos[1] + 1))
        if new_pos[0] + 1 < 8 and new_pos[1] - 1 >= 0:
            if self.board[new_pos[0] + 1][new_pos[1] - 1] == 0:
                print(new_pos[0]+1, ",", new_pos[1]- 1)
                moves.append((new_pos[0] + 1, new_pos[1] - 1))
        if new_pos[0] - 1 >= 0 and new_pos[1] - 1 >= 0:
            if self.board[new_pos[0] - 1][new_pos[1] - 1] == 0:
                print(new_pos[0]-1, ",", new_pos[1]- 1)
                moves.append((new_pos[0] - 1, new_pos[1] - 1))
        if new_pos[0] - 1 >= 0 and new_pos[1] + 1 < 8:
            if self.board[new_pos[0] - 1][new_pos[1] + 1] == 0:
                print(new_pos[0]-1, ",", new_pos[1]+ 1)
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


class Node:
    def __init__(self, board: Board):
        self.state = board
        self.action = 1

    def result(self, action):
        if action in self.state.get_moves(self.action):
            n = Node(self.state.move(self.action,action))
            n.action = action
            return n

    def test(self):
        return len(self.state.get_moves(self.action)) == 0

    def utility(self):
        if len(self.state.get_moves(self.action)) == 0:
            return -1
        elif self.action in [29, 30, 31, 32]:
            return 1
        else:
            return self.action/32


class Game:
    def __init__(self):
        self.board = Board()
        self.tom = TomBrady(self)

    def is_finished(self) -> bool:
        if self.tom.pos in [29, 30, 31, 32]:
            print("Tom wins")
            return True
        if len(self.board.get_moves(self.tom.pos)) == 0:
            print("You win!")
            return True
        return False

    def rams_turn(self) -> None:
        while(True):
            ram = input("Which ram do you want to move?")
            ram_pos = self.board.num_to_board[ram]
            if self.board.board[ram_pos[0]][ram_pos[1]] == -1:
                break
            else:
                print("There's not a ram in that square.")
        while(True):
            move = input("Where do you want to move?")
            if move not in self.board.get_moves(ram):
                print("That's not a valid move.")
            else:
                break
        self.board.board[ram_pos[0]][ram_pos[1]] = 0
        move_pos = self.board.num_to_board[move]
        self.board.board[move_pos[0]][move_pos[1]] = -1

    def play(self) -> None:
        self.tom.start_position()
        while (True):
            self.board.move(self.tom.pos, self.tom.move(self.board))
            if self.is_finished():
                print("Game finished")
                return
            print(self.board.board)
            self.rams_turn()
            print(self.board.board)
            if self.is_finished():
                print("Game finished")
                return


class TomBrady:
    def __init__(self, game: Game):
        self.pos = 1
        self.board = game.board
        self.depth = 100

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
            temp = self.min_value(n.result(a), alpha, beta, d - 1)
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
        for a in range(len(n.children)):
            temp = self.max_value(n.result(a), alpha, beta, d - 1)
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