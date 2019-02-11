# Maggie von Ebers 
# 525001114 
# CSCE 420
# Due: February 14, 2019
# hw2pr2.py

from hw2pr1 import Node, build_tree


def max_value(n: Node, alpha: int, beta: int) -> Node:
    if n.test():
        return n

    v = Node()
    v.state = -10000

    for a in range(len(n.children)):
        temp = min_value(n.result(a), alpha, beta)
        if v.state <= temp.state:
            v = temp
        if v.state >= beta:
            return v
        alpha = max(alpha, v.state)
        print("Alpha pruning")

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
        if v.state <= alpha:
            return v
        beta = min(beta, v.state) 
        print("Beta pruning")
    
    return v


def alpha_beta_search(n: Node) -> Node:
    v = max_value(n, -10000, 10000)
    return v    # idk
    


# ---------------------------------------------------------------------------
# Taking input


initial_state = "( ( 3 , 12 , 8 ) , ( 2 , 4 , 6 ) , ( 14 , 5 , 2 ) )"
n = build_tree(initial_state)

print(alpha_beta_search(n).state)