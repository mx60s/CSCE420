# Maggie von Ebers
# 525001114
# CSCE 420
# Due: 1/31/2019
# h1pr2.py

from collections import deque, namedtuple

Node = namedtuple('Node', ['parent', 'action', 'state', 'path'])

class Problem:
    # __slots__ = ['inital_state']
    def __init__(self, initial_state):
        self.initial_state = initial_state

    def result(self, state, action):
        if action == len(self.initial_state):
            return state[::-1]
        state = list(state)
        state[:action] = state[:action][::-1]
        return state

def goal_test(l):
    equal = True
    for x,y in zip(l,sorted(l)):
        if x != y:
            equal = False
    return equal

def recursive_dls(node: Node, problem: Problem, limit: int):
    if goal_test(node.state):
        return (node.path, True)
    elif limit == 0:
        return (None, True)    # cutoff
    else:
        cutoff = False
        for action in range(2,len(problem.initial_state+1)):
            child = Node(node,action,node.state,
                        tuple(node.path) + (action,))

            result, remaining = recursive_dls(child,problem,limit-1)

            if result != None:
                return (result, True)
            if remaining:   # failure
                cutoff = True
        return (None, cutoff)

def depth_limited_search(problem: Problem, limit: int):
    node = Node(None, 0, problem.initial_state,[0])
    return recursive_dls(node,problem,limit)

def iterative_deepening(problem: Problem):
    for depth in range(100):    # in the book it gives infinity??
        result, cutoff = depth_limited_search(problem, depth)
        if result != None:
            return result
        elif not cutoff:
            return None
