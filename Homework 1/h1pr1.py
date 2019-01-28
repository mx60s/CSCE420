class Problem:
    def __init__(self, initial_state, path_cost):
        self.state = initial_state
        self.path_cost = path_cost
    
    def goal_test(self, node):
        return true

    def actions(self,node_state):
        return []

class Node:
    def __init__(self, state):
        self.state = state

class ChildNode:
    def __init__(self, problem, node, action):
        self.problem = problem
        self.node = node
        self.action = action
        self.state = node.state


def breadth_first(p):
    node = p.initial_state()
    if node.goal_test():
        # return solution(node)
    frontier = []   # queue
    frontier.append(node)
    explored = set()
    while True:
        if len(frontier) == 0:
            # return failure
        node = frontier.popleft()
        explored.append(node)
        for action in p.actions(node.state):
            child = ChildNode(p, node, action)
            if frontier.count(child) == 0 & explored.count(child) == 0:
                if p.goal_test(child.state):
                    # return solution
                frontier.append(child)



num = int(input())
a = []
for i in range(num):
    a.append(int(input()))

p = Problem(a,0)
b = breadth_first(p)

for result in b:
    print(result)