# Maggie von Ebers
# 525001114
# CSCE 420
# Due: February 14, 2019
# hw2pr1.py


# Each node makes up the minimax tree
class Node:
    def __init__(self):
        self.state = 0
        self.parent = None
        self.children = []

    def result(self, action):
        return self.children[action]

    # This method checks if a node is a leaf
    def test(self):
        return len(self.children) == 0

    def utility(self):
        return 1


# Maximize my values
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

# Minimize the values for the opponent
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

# Calculates the best possible decision for the top node.
def minimax_decision(n: Node) -> Node:
    val = min_value(n.result(0))

    for a in range(1, len(n.children)):
        temp = min_value(n.result(a))
        if temp.state > val.state:
            val = temp

    return val


# ---------------------------------------------------------------------------
# Taking input

def build_tree(initial_state) -> Node:
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



i = input("Please input your tree, one character at a time: >")
initial = ""
parens = 1
while(parens > 0):
    i = input("> ")
    if i == "(":
        parens += 1
    elif i == ")":
        parens += 1
    initial += " "
    initial += i

n = build_tree(initial)

print(minimax_decision(n).state)
