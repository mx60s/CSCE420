# Maggie von Ebers 
# 525001114 
# CSCE 420
# Due: February 14, 2019
# hw2pr2.py

from hw2pr1 import Node, build_tree     # The node and build_tree information works fine for this problem

# Maximize my values, while also pruning the beta values.
def max_value(n: Node, alpha: int, beta: int) -> Node:
    if n.test():
        return n

    v = Node()
    v.state = -10000

    for a in range(len(n.children)):
        temp = min_value(n.result(a), alpha, beta)
        if v.state <= temp.state:
            v = temp
        alpha = max(alpha, v.state)
        if beta <= alpha:
            print("Beta pruning")
            break

    return v


def min_value(n: Node, alpha: int, beta: int) -> Node:
    if n.test():
        return n

    v = Node()
    v.state = 10000

    for a in range(len(n.children)):
        temp = max_value(n.result(a), alpha, beta)
        if v.state >= temp.state:
            v = temp
        beta = min(beta, v.state)
        if beta <= alpha:
            print("Alpha pruning")
            break
    
    return v


def alpha_beta_search(n: Node) -> Node:
    v = max_value(n, -10000, 10000)
    return v    # idk
    


# ---------------------------------------------------------------------------
# Taking input


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

print(alpha_beta_search(n).state)