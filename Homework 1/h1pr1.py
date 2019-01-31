# Maggie von Ebers
# 525001114
# CSCE 420
# Due: 1/31/2019
# h1pr1.py

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


def breadth_first(p: Problem):

    n = Node(None, 0, p.initial_state, [0])

    if goal_test(tuple(n.state)):
        return n.path 
    
    frontier = deque()
    frontier.append(n)

    explored = set([])
    
    while frontier:
        node = frontier.popleft()

        if goal_test(tuple(node.state)):
            return node.path

        for action in range(2, len(p.initial_state)+1):

            child = Node(node, action, p.result(node.state, action), 
                        tuple(node.path) + (action,))

            if tuple(child.state) in explored:
                continue

            if child not in frontier:
                frontier.append(child)

                if goal_test(tuple(child.state)):
                    return child.path
                    
        explored.add(tuple(node.state))
    return []



num = int(input())
a = []
for i in range(num):
    a.append(int(input()))

# a = list('214635')
p = Problem(a)
print(len(p.initial_state))
b = breadth_first(p)

print("Result:")
s = ""
for result in b:
    s = s + " " + str(result)
print(s)
