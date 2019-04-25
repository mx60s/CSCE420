import numpy as np
import random
import math
import re
import os

class BackPropNet:

    def __init__(self, examples):
        self.examples = examples
        self.network = np.array([[0] * len(examples[0][0]), [0] * 126, [0] * 26])
        print(self.network.shape)
        self.weights = np.array([[0] * (len(examples[0][0]) * 126), [0] * (126 * 26)])
        self.deltas = np.array([[0] * len(examples[0][0]), [0] * 126, [0] * 26])
        self.sums = np.array([[0] * len(examples[0][0]), [0] * 126, [0] * 26])

        self.eqs = [None, lambda x : np.tanh(x), lambda x : 1/(1+np.exp(-x))]
        self.deriv = [ None, 
                        lambda x : 1/(np.cosh(x)**2), 
                        lambda x : self.eqs[2](x) * (1 - self.eqs[2](x)) ]


    def learn(self):
        for i in range(len(self.weights)):
            for j in range(len(self.weights[i])):
                self.weights[i][j] = random.uniform(-0.001, 0.001)
                #print(self.weights[i][j])

        #print(type(self.network[2]))
        
        for e in range(100):  # epochs
            print("Epoch #", e)
            error = []

            for x, y in self.examples:
                self.network[0] = x

                for i in range(1, len(self.network)):   # for each layer
                    for j in range(len(self.network[i])):   # for each node
                        sum_w = 0
                        np.matmul()
                        mult = len(self.network[i])
                        for k in range(len(self.network[i - 1])):   #for each of the previous nodes
                            if type(self.weights[i - 1][mult * j + k]) == type(np.array([0,0,0])):
                                self.weights[i - 1][mult * j + k] = self.weights[i - 1][mult * j + k][0]
                            #print("weight:", self.weights[i - 1][k])
                            #print("network:", self.network[i - 1][k])
                            sum_w = sum_w + (self.weights[i - 1][mult * j + k] * self.network[i - 1][k])
                        #print(sum_w)
                        self.network[i][j] = self.eqs[i](sum_w)
                        #print("i:", i, sum_w, self.network[i][j])
                        #print(self.network[i][j])
                        self.sums[i][j] = sum_w

                """ Backpropagation """
                for i in range(len(self.network[2])):   # for each node in output layer
                    self.deltas[2][i] = (y[i] - self.network[2][i]) * self.deriv[2](self.sums[2][i])
                    # print(self.deltas[2][i])


                for i in range(len(self.network) - 2, 1, -1):
                    for j in range(len(self.network[i])):
                        sums_d = 0
                        mult = len(self.network[i])
                        for k in range(len(self.network[i + 1])):
                            sums_d = sums_d + self.weights[i][j * mult + k] * self.deltas[i + 1][k]
                        self.deltas[i][j] = 100 * self.deriv[i](self.sums[i][j]) * sums_d
                #break
                # this is the slow part
                for i in range(len(self.weights)):
                    for j in range(len(self.weights[i])):
                        n = int(math.floor(j / len(self.network[i + 1])))
                        d = int(math.floor(j / (len(self.network[i]))))
                        self.weights[i][j] = self.weights[i][j] + (2 * self.network[i][n] * self.deltas[i+1][d])

                error.append(self.deltas[2])

            print(self.network[2])
            #print("Avg error:", np.me an(error))
        


# startchar A to end (char z)
def import_bdfs(directory):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    files = os.listdir(dir_path + directory)
    print(files)
    all_data = [[]] * 26
    for filename in files:
        with open(dir_path + directory + "/" + filename) as f:
            lines = f.readlines()
            start = 0
            for i, line in enumerate(lines):
                if (line == "STARTCHAR A\n"):
                    start = i
                    break
            #print(lines[i + 4])
            letter = 'A'
            i = start + 4
            count = 0
            while(count < 26):
                y = [0] * 26
                y[ord(letter) - 65] = 1
                digit = []
                width = int(re.search(r'\d+', lines[i]).group(0))
                height = int(re.search(r'\d+', lines[i][6:]).group(0))
                #print(lines[i+2])
                i += 2
                for h in range(height):
                    bitline = [0] * 9
                    currline = bin(int(lines[i + h], 16))[2:].zfill(8)
                    if len(currline) > 9:
                        currline = currline[:9]
                    #print(currline)
                    for w in range(len(currline)):
                        #print(w)
                        bitline[w] = int(currline[w])
                    #print(bitline)
                    digit += bitline

                for _ in range(14 - height):
                    digit += ([0] * 9)

                tup = (digit, y)
                #print(tup)
                all_data[count].append(tup)

                count += 1
                letter = lines[i + height + 1][10]
                i += height + 5

    return all_data

print("Done with file upload")

alphabet = import_bdfs("/bdf")
training_a = alphabet[0]
#print(training_a[0])

net = BackPropNet(training_a)
net.learn()