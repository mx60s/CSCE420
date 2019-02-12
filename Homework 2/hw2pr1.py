# Maggie von Ebers
# 525001114
# CSCE 420
# Due: February 14, 2019
# hw2pr1.py


class Node:
    def __init__(self):
        self.state = 0
        self.parent = None
        self.children = []

    def result(self, action):
        return self.children[action]

    def test(self):
        return len(self.children) == 0


def max_value(n: Node) -> Node:
    if n.test():
        return n

    v = Node()
    v.state = -10000

    for a in range(len(n.children)):
        temp = min_value(n.result(a))
        if v.state <= temp.state:
            v = temp

    return v


def min_value(n: Node) -> Node:
    if n.test():

        return n

    v = Node()
    v.state = 10000

    for a in range(len(n.children)):
        temp = max_value(n.result(a))
        if v.state >= temp.state:
            v = temp

    return v


def minimax_decision(n: Node):
    val = min_value(n.result(0))

    for a in range(1, len(n.children)):
        temp = min_value(n.result(a))
        if temp.state > val.state:
            val = temp

    return val


# ---------------------------------------------------------------------------
# Taking input

def build_tree(initial_state):
    tree = initial_state.split()
    n = Node()

    for c in tree:
        if str.isdigit(c):
            n.state = int(c)

        elif c == "(":
            temp = Node()
            temp.parent = n
            n.children.append(temp)
            n = temp

        elif c == ")":
            n = n.parent

        elif c == ",":
            temp = Node()
            temp.parent = n.parent
            n.parent.children.append(temp)
            n = temp
    return n


initial_state = "( ( 3 , 12 , 8 ) , ( 2 , 4 , 6 ) , ( 14 , 5 , 2 ) )"

n = build_tree(initial_state)

#print(minimax_decision(n).state)
