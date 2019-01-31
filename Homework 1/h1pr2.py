# Maggie von Ebers
# 525001114
# CSCE 420
# Due: 1/31/2019
# h1pr2.py

from collections import namedtuple

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
    for x, y in zip(l, sorted(l)):
        if x != y:
            equal = False
    return equal


def recursive_dls(node: Node, p: Problem, limit: int, child_count: int):
    if limit == 0:
        if goal_test(node.state):
            return (node.path, True, child_count)
        else:
            return (None, True, child_count)    # cutoff
    elif limit > 0:
        any_remaining = False
        for action in range(2, len(node.state)+1):
            child = Node(node, action, p.result(node.state, action),
                         tuple(node.path) + (action,))
            child_count += 1

            found, remaining, child_count = recursive_dls(
                child, p, limit-1, child_count)

            if found != None:
                return (found, True, child_count)
            if remaining:   # remaining means we reached a cutoff
                any_remaining = True
        return (None, any_remaining, child_count)


def depth_limited_search(problem: Problem, limit: int):
    node = Node(None, 0, problem.initial_state, [0])
    return recursive_dls(node, problem, limit, 0)


def iterative_deepening(problem: Problem):
    for depth in range(10):
        found, remaining, child_count = depth_limited_search(problem, depth)
        if found != None:
            return (found, child_count)
        elif not remaining:
            return (None, 0)


num = int(input())
a = []
for i in range(num):
    a.append(input())

#a = list("214635")
p = Problem(a)
result, count = iterative_deepening(p)
if result == None:
    print("None.")
else:
    print("Result:", *result)
    print(count, "child nodes generated.")
