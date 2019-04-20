# Maggie von Ebers

from collections import namedtuple
import numpy as np
import random


class BackPropNet :
    def __init__(self, examples):

        self.examples = examples
        # layer consists of weights, values, deltas, and sums, respectively
        self.inner_layer = [[0] * len(examples[0][0]), [0] * 126, [0] * 126, [0] * 126]
        self.output_layer = [[0] * 126, [0] * 26, [0] * 26, [0] * 26]
        self.inner_activation = lambda x : np.tanh(x)
        self.outer_activation = lambda x : 1 / (1 + np.exp(-x))

        self.layers = [[self.inner_layer, self.inner_activation], 
                        [self.output_layer, self.outer_activation]]

    # activation function in layers[x][1]
    # layer in layers[x][0]
    # weights in layers[x][0][0]
    # nodes in layers[x][0][1]

    def learn(self):

        for layer in self.layers:
           for i in range(len(layer[0][0])):   # correct
               layer[0][0][i] = random.random

        for _ in range(3):      # sub in some metric to stop at
            for x, y in self.examples:
                for layer, activation in self.layers:
                    for i in range(len(layer[1])):    # correct
                        sum_in = 0
                        for j in range(len(x)): # transform into list comprehension
                            sum_in += layer[0][j] * x[j]
                        layer[3][i] = sum_in
                        layer[1][i] = activation(sum_in)
                
                for i in range(len(self.output_layer[1])):
                    self.output_layer[2][i] = self.outer_activation(self.output_layer[3][i]) * (y - x[i])
                
                for i in range(len(self.layers) - 1, 1, -1):
                    for j in range(len(self.layers[i][0][1])):
                        sum_in = 0
                        for k in range(len(self.layers[i][0][0])):
                            sum_in += self.layers[i][0][0][k] * self.layers[i][0][2][k]
                        self.layers[i][0][2][j] = self.layers[i][1](self.layers[i][0][3][j]) * sum_in

                for i in range(len(self.layers)):
                    for j in range(len(self.layers[i][0][1])):
                        for k in range(len(self.layers[i][0][0])):
                            self.layers[i][0][0][k] += 0.01 * self.layers[i][0][1][j] * self.layers[i][0][2][j]
                    
        return self.layers



# train to pick up a majority function
training_set = [([0,0,0], 0), ([1,1,1], 1), ([1,1,0], 1), ([1,0,0], 0), ([0,1,1], 1), ([1,0,1], 1),
                ([0,1,0], 0), ([0,0,1], 0)]

net = BackPropNet(training_set)

l = net.learn()
print(l)