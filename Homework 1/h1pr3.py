# Maggie von Ebers
# 525001114
# CSCE 420
# Due: 1/31/2019
# h1pr3.py

from collections import deque, namedtuple

Node = namedtuple('Node', ['parent', 'action', 'state', 'path', 'f_score', 'g_score'])


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
    
    def path_cost(self, state) -> int:
        state = [0] + state
        h = 0
        less = True
        last = True
        for i in range(1,len(state)):
            if state[i-1] < state[i]:
                less = True
            else:
                less = False
            if less != last:
                h += 1
            last = less
        return h

    def find_lowest(self, nodes: deque) -> Node:
        min = nodes[0]
        for n in nodes:
            if n.f_score < min.f_score:
                min = n
        return min

    def dist_between(self,node1: Node, node2: Node) -> int:
        return abs(self.path_cost(node1.state) - self.path_cost(node2.state))


def goal_test(l):
    equal = True
    for x,y in zip(l,sorted(l)):
        if x != y:
            equal = False
    return equal

def a_star(p: Problem):
    n = Node(None,0,p.initial_state,[0], p.path_cost(p.initial_state),0)

    explored = set([])
    frontier = deque()
    frontier.append(n)
    # g_score = dict()
    # g_score[n] = 0

    # f_score = dict()
    # f_score[n] = p.path_cost(n.state)

    while frontier:
        current = p.find_lowest(frontier)
        if goal_test(current):
            return current.path
        
        frontier.remove(current)
        explored.add(tuple(current.state))

        for action in range(2,len(p.initial_state) + 1):
            child = Node(current, action, p.result(current.state,action),
                    tuple(current.path) + (action,),
                    p.path_cost(p.result(current.state,action)),
                    current.g_score + p.path_cost(p.result(current.state,action)))
            if tuple(child.state) in explored:
                continue
            
            g_score = child.g_score + p.dist_between(current,child)

            if child not in frontier:
                frontier.append(child)
            else if g_score >= child.g_score:
                continue
            
            child.g_score = g_score
            child.f_score
