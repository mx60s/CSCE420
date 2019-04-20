

import numpy as np
import random

class BackPropNet:

    def __init__(self, examples):
        self.examples = examples
        self.network = [[0] * len(examples[0][0]), [0] * 30, [0] * 2]
        self.weights = [[0] * (len(examples[0][0]) * 30), [0] * 60]
        self.deltas = [[0] * len(examples[0][0]), [0] * 30, [0] * 2]
        self.sums = [[0] * len(examples[0][0]), [0] * 30, [0] * 2]
        self.eqs = [None, lambda x : np.tanh(x), lambda x : 1/(1+np.exp(-x))]


    def learn(self):
        for i in range(len(self.weights)):
            for j in range(len(self.weights[i])):
                self.weights[i][j] = random.random() / 5
        
        for _ in range(24):  # 3 epochs
            for x, y in self.examples:
                self.network[0] = x

                for i in range(1, len(self.network)):   # for each layer
                    for j in range(len(self.network[i])):   # for each node
                        sum_w = 0
                        mult = len(self.network[i])
                        for k in range(len(self.network[i - 1])):   #for each of the previous nodes
                            sum_w += self.weights[i-1][k*mult] * self.network[i-1][k]
                        self.network[i][j] = self.eqs[i](sum_w)
                        self.sums[i][j] = sum_w
                
                """ Backpropagation """
                for i in range(len(self.network[2])):   # for each node in output layer
                    self.deltas[2][i] = self.eqs[1](self.sums[2][i]) * (y - self.network[2][i])

                for i in range(len(self.network) - 2, 1, -1):
                    for j in range(len(self.network[i])):
                        sums_d = 0
                        mult = len(self.network[i])
                        for k in range(len(self.network[i + 1])):
                            sum_d += self.weights[i][k * mult] * self.deltas[i + 1][k]
                        self.deltas[i][j] = 0.5 * self.sums[i][j] * sums_d

                print(*self.network[2])
                    


training_set = [([1,1,1], 0), ([1,1,1], 1), ([1,1,0], 1), ([1,0,0], 0), ([0,1,1], 1), ([1,0,1], 1),
                ([0,1,0], 0), ([0,0,1], 0)]

net = BackPropNet(training_set)
net.learn()