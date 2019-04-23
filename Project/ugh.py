

import numpy as np
import random
import math

class BackPropNet:

    def __init__(self, examples):
        self.examples = examples
        self.network = [[0] * len(examples[0][0]), [0] * 5, [0]]
        self.weights = [[0] * (len(examples[0][0]) * 5), [0] * 5]
        self.deltas = [[0] * len(examples[0][0]), [0] * 5, [0]]
        self.sums = [[0] * len(examples[0][0]), [0] * 5, [0]]
        self.eqs = [None, lambda x : np.tanh(x), lambda x : 1/(1+np.exp(-x))]
        self.deriv = [ None, 
                        lambda x : 1/(np.cosh(x)**2), 
                        lambda x : self.eqs[2](x) * (1 - self.eqs[2](x)) ]


    def learn(self):
        for i in range(len(self.weights)):
            for j in range(len(self.weights[i])):
                self.weights[i][j] = random.random()
        
        for e in range(7):  # epochs
            print("Epoch #", e)
            error = []
            for x, y in self.examples:

                self.network[0] = x

                for i in range(1, len(self.network)):   # for each layer
                    for j in range(len(self.network[i])):   # for each node
                        sum_w = 0
                        mult = len(self.network[i])
                        for k in range(len(self.network[i - 1])):   #for each of the previous nodes
                            sum_w = sum_w + (self.weights[i - 1][k * mult + j] * self.network[i - 1][k])

                        self.network[i][j] = self.eqs[i](sum_w)
                        self.sums[i][j] = sum_w
                
                """ Backpropagation """
                for i in range(len(self.network[2])):   # for each node in output layer
                    self.deltas[2][i] = self.deriv[2](self.sums[2][i]) * (y - self.network[2][i])

                for i in range(len(self.network) - 2, 1, -1):
                    for j in range(len(self.network[i])):
                        sums_d = 0
                        mult = len(self.network[i])
                        for k in range(len(self.network[i + 1])):
                            sum_d = sum_d + self.weights[i][k * mult + j] * self.deltas[i + 1][k]
                        self.deltas[i][j] = self.deriv[i](self.sums[i][j]) * sums_d   # could be an issue with the equation
                
                for i in range(len(self.weights)):
                    for j in range(len(self.weights[i])):
                        n = int(math.floor(j / len(self.network[i + 1])))
                        d = int(math.floor(j / len(self.network[i])))
                        self.weights[i][j] = self.weights[i][j] + (0.9 * self.network[i][n] * self.deltas[i+1][d])

                error.append(self.deltas[2])

            print("Avg error:", np.mean(error))
        


training_set = [([1,1,1,1,1], 1), ([1,1,1,1,0], 1), ([1,1,1,0,1], 1), ([1,1,0,1,1], 1), ([1,0,1,1,1], 1),
                ([0,0,0,0,1], 0), ([0,0,1,0,1], 0), ([0,1,0,0,1], 0), ([0,0,0,0,0], 0), ([0,0,0,0,1], 0),
                ([0,1,1,1,1], 1), ([1,1,1,0,0], 1), ([1,1,0,0,1], 1), ([1,0,0,1,1], 1), ([0,0,1,1,1], 1),
                ([0,1,1,1,0], 1), ([0,1,1,0,1], 1), ([0,1,0,1,1], 1), ([0,0,0,1,1], 0), ([0,0,1,1,0], 0),
                ([1,0,0,0,0], 0), ([1,0,1,1,0], 1)]

net = BackPropNet(training_set)
net.learn()