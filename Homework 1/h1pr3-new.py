# Maggie von Ebers
# 525001114
# CSCE 420
# Due: 1/31/2019
# h1pr3.py

from collections import deque

class Node:
    __slots__ = ['parent', 'action', 'state', 'path', 'f_score', 'g_score']
    def __init__(self, parent, action, state, path, f_score, g_score):
        self.parent = parent
        self.action = action
        self.state = state
        self.path = path
        self.f_score = f_score
        self.g_score = g_score

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
    
    def path_cost_estimate(self, state) -> int:
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
        return abs(self.path_cost_estimate(node1.state) - self.path_cost_estimate(node2.state))

    def neighbors(self, node: Node):
        neighbors = []
        for action in range(2,len(self.initial_state)+1):
            n = Node(node,action,self.result(node.state,action),node.path + [action], 0, 0)
            neighbors.append(n)
        return neighbors


def goal_test(node):
    equal = True
    for x,y in zip(node.state,sorted(node.state)):
        if x != y:
            equal = False
    return equal


def a_star(p: Problem):
    n = Node(None,0,p.initial_state,[0], p.path_cost_estimate(p.initial_state),0)

    explored = set([])
    frontier = deque()
    frontier.append(n)
    g_score = dict()
    g_score[n] = 0

    f_score = dict()
    f_score[n] = p.path_cost_estimate(n.state)

    while frontier:
        current = p.find_lowest(frontier)
        if goal_test(current):
            return current.path
        
        frontier.remove(current)
        explored.add(current)

        for child in p.neighbors(current):
            if child in explored:
                continue
            
            temp_g_score = g_score[current] + p.dist_between(current,child)

            if child not in frontier:
                frontier.append(child)
            elif temp_g_score >= g_score[child]:
                continue
            
            g_score[child] = temp_g_score
            f_score[child] = g_score[child] + p.path_cost_estimate(child.state)

p = Problem([2,1,4,6,3,5])
a = a_star(p)
print(*a)