# Maggie von Ebers
# 525001114
# CSCE 420
# Due: February 14, 2019
# hw2pr3.py

# so here, max is tom brady
# min is the rams (human player), but it might not need an algorithm cause it'll just be taking command line input
# so maybe nodes need to be mapped then

from hw2pr1 import Node, build_tree

class Game:
    def __init__(self):
        self.board = {}
        for i in range(1,33):
            print(i)
            self.board[i] = "N"
        self.board[1] = "T"
        for i in range(29,33):
            self.board[i] = "R"
        for d in self.board.values():
            print(d)
    def move(self, pos: int, move: int) -> None:
        return

    def isFinished(self) -> bool:
        return True

    def play(self) -> None:
        while not self.isFinished():
            play_rams()
            play_brady()


def play_rams() -> None:
    ram = input("Which Ram do you want to move?")
    # validate input
    pos = input("To which square?")
    # validate input

def play_brady() -> None:
    return

g = Game()