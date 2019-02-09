# Maggie von Ebers 
# 525001114 
# CSCE 420
# Due: February 14, 2019
# hw2pr1.py

# from anytree import Node


class Node:
    def __init__(self):
        self.state = 0
        self.parent = None
        self.children = []
        self.siblings = []

    def result(self, action):
        return self.children[action]

    def utility(self):
        return 1

    def test(self):
        return len(self.children) == 0


def max_value(n: Node) -> Node:
    if n.test():
        return n.utility()

    v = Node()
    v.state = -10000

    for a in range(len(n.children)):
        if v.state <= n.result(a).state:
            v = n

    n = v
    return n


def min_value(n: Node) -> Node:
    if n.test():
        return n.utility()

    v = Node()
    v.state = 10000

    for a in range(len(n.children)): # fix later
        if v.state >= n.result(a).state:
            v = n
    n = v
    
    return n


def minimax_decision(n: Node):
    val = min_value(n.result(0))
    for a in range(1,len(n.children)):
        if n.result(a).state > val.state:
            val = n.result(a)
    return val


initial_state = "( ( 3 , 12 , 8 ) , ( 2 , 4 , 6 ) , ( 14 , 5 , 2 ) )"
n = Node()
tree = initial_state.split()

for c in initial_state.split():
    #print(c)
    if str.isdigit(c):
        n.state = int(c)
        #print("Setting node to",c)
    elif c == "(":
        #print("Making a child")
        temp = Node()
        temp.parent = n
        n.children.append(temp)
        n = temp
    elif c == ")":
        #print("Moving to parent")
        n = n.parent
    elif c == ",":
        #print("Making a sibling")
        temp = Node()
        temp.parent = n.parent
        n.parent.children.append(temp)
        n.siblings.append(temp)
        n = temp
    # print("state:",n.state)

print(minimax_decision(n).state)