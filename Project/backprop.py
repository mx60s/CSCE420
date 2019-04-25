import os
import numpy as np
import re

def import_bdfs(directory):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    files = os.listdir(dir_path + directory)
    all_data = []
    digits = []

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

                #print(tup)
                all_data.append(digit)
                digits.append(y)

                count += 1
                letter = lines[i + height + 1][10]
                i += height + 5

    return all_data, digits


def tanh(x):
    return np.tanh(x)

def derivative_tanh(x):
    return 1 - tanh(x)**2

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def derivative_sigmoid(x):
    return np.multiply( (1 / (1 + np.exp(-x))), (1 - (1 / (1 + np.exp(-x)))) )


class BackPropNet:
    def __init__(self):
        #self.training = training
        self.weights1 = np.random.uniform(-0.01, 0.01, (126, 126))
        self.weights2 = np.random.uniform(-0.01, 0.01, (126, 26))

    def tanh(self, x):
        return np.tanh(x)

    def derivative_tanh(self, x):
        return 1 - tanh(x)**2

    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    def derivative_sigmoid(self, x):
        return np.multiply( (1 / (1 + np.exp(-x))), (1 - (1 / (1 + np.exp(-x)))) )

    def train(self, all_data, digits, epochs):
        for e in range(epochs):  # epochs
            print("Epoch:", e)
            for x, y in zip(all_data, digits):

                input_layer = np.matrix([x])

                """ Feed-forward """
                layer1 = sigmoid(np.dot(input_layer, self.weights1))
                output = sigmoid(np.dot(layer1, self.weights2))


                """ Backpropagation """
                d_weights2 = np.dot(layer1.T, np.multiply(2 * np.subtract(y, output), derivative_sigmoid(output)) )

                d_weights1 = np.dot(input_layer.T, np.multiply( np.dot( np.multiply( 2 * np.subtract(y, output), derivative_sigmoid(output) ), self.weights2.T), derivative_sigmoid(layer1) ) )

                self.weights1 += d_weights1
                self.weights2 += d_weights2

                #m = max(output.T)
                #maxiter = [i for i, j in enumerate(output.T) if j == m]

                #ym = max(y)
                #maxitery = [i for i, j in enumerate(y) if j == 1]
                #print("Actual pos:", maxitery)
                #print("Output pos:", maxiter)
                #if (maxitery == maxiter):
                 #   print("Correct!")
                #else:
                 #   print("Nope")


    def predict(self, example, correct):
        input_layer = np.matrix( [example] )

        layer1 = sigmoid(np.dot(input_layer, self.weights1))
        output = sigmoid(np.dot(layer1, self.weights2))

        m = max(output.T)
        maxiter = [i for i, j in enumerate(output.T) if j == m]
        letter_guessed = chr(65 + maxiter[0])

        ym = max(correct)
        maxitery = [i for i, j in enumerate(correct) if j == 1]
        letter_actual = chr(65 + maxitery[0])

        print("Predicted = ", letter_guessed)
        print("Actual = " , letter_actual)

        


all_data, digits = import_bdfs("/bdf")
print("Done with file upload")

net = BackPropNet()
net.train(all_data, digits, 10)
net.predict(all_data[100], digits[100])