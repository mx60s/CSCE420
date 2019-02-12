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
        # print("Max val:",n.result(a).state)
        temp = min_value(n.result(a), alpha, beta)
        if v.state <= temp.state:
            v = temp
            # print("v is now", v.state)
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
        # print("Min val:",n.result(a).state)
        temp = max_value(n.result(a), alpha, beta)
        if v.state >= temp.state:
            v = temp
            # print("v is now", v.state)
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


initial_state = "( ( 3 , 8 , ( 7 , ( 3 , 0 , 7 ) , ( 8 , 8 , 2 ) ) ) , ( 4 , ( 7 , 9 , 8 ) , 8 ) , ( ( ( 3 , 6 , 4 ) , 2 , 6 ) , ( ( 9 , 2 , 9 ) , 4 , 7 , ( 6 , 4 , 5 ) ) , 4 , ( 6 , 4 , 5 ) ) ) "
n = build_tree(initial_state)

print(alpha_beta_search(n).state)