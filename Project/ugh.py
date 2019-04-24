

import numpy as np
import random
import math
import re

class BackPropNet:

    def __init__(self, examples):
        self.examples = examples
        self.network = [[0] * len(examples[0][0]), [0] * 126, [0] * 26]
        self.weights = [[0] * (len(examples[0][0]) * 126), [0] * (126 * 26)]
        self.deltas = [[0] * len(examples[0][0]), [0] * 126, [0] * 26]
        self.sums = [[0] * len(examples[0][0]), [0] * 126, [0] * 26]

        self.eqs = [None, lambda x : np.tanh(x), lambda x : 1/(1+np.exp(-x))]
        self.deriv = [ None, 
                        lambda x : 1/(np.cosh(x)**2), 
                        lambda x : self.eqs[2](x) * (1 - self.eqs[2](x)) ]


    def learn(self):
        for i in range(len(self.weights)):
            for j in range(len(self.weights[i])):
                self.weights[i][j] = random.random()

        #print(self.weights)
        
        for e in range(2):  # epochs
            print("Epoch #", e)
            error = []
            for x, y in self.examples:
                self.network[0] = x
                print(len(x))

                for i in range(1, len(self.network)):   # for each layer
                    for j in range(len(self.network[i])):   # for each node
                        sum_w = 0
                        mult = len(self.network[i])
                        # ok I've decided that weights are different. Weights 0-125 are all for node 0, etc.
                        for k in range(len(self.network[i - 1])):   #for each of the previous nodes
                            sum_w = sum_w + (self.weights[i - 1][k*mult + j] * self.network[i - 1][k])

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

            print(*self.network[2])
            print("Avg error:", np.mean(error))
        


# startchar A to end (char z)
def import_bdf(filename):

    alphabet = []
    with open(filename) as f:
        lines = f.readlines()
        start = 0
        for i, line in enumerate(lines):
            if (line == "STARTCHAR A\n"):
                start = i
                break

        letter = 'A'
        i = start + 4
        count = 0
        while(count < 26):
            y = [0] * 26
            y[ord(letter) - 65] = 1
            digit = []
            width = int(re.search(r'\d+', lines[i]).group(0))
            height = int(re.search(r'\d+', lines[i][6:]).group(0))

            i += 2
            for h in range(height):
                bitline = [0] * 9
                currline = bin(int(lines[i + h], 16))[2:].zfill(8)
                for w in range(width):
                    bitline[w] = int(currline[w])
                #print(bitline)
                digit += bitline

            for _ in range(14 - height):
                digit += ([0] * 9)

            tup = (digit, y)
            print(tup)
            alphabet.append(tup)

            count += 1
            letter = lines[i + height + 1][10]
            i += height + 5

    return alphabet


training_set = import_bdf("bdf/ib8x8u.bdf")
net = BackPropNet(training_set)
net.learn()