# -*- coding: utf-8 -*-

import numpy as np

class neuralNet(object):
    def __init__(self):
        
        #   Parameters
        self.inputSize  = len(inputData[1,:])
        self.outputSize = 1
        self.hiddenSize = 4
        
        #   Weights
        self.weight1 = np.random.rand(self.inputSize, self.hiddenSize)
        self.weight2 = np.random.rand(self.hiddenSize, self.outputSize)
        
    def forward(self, inputData):
        #   Forward propagation through network
        self.z1     = np.dot(inputData, self.weight1)
        self.z2     = self.sigmoid(self.z1)
        self.z3     = np.dot(self.z2, self.weight2)
        output      = self.sigmoid(self.z3)
        return output
    
    def backward(self, inputData, trainData, output):
        #   backwards propagation through network
        self.outputError     = trainData - output
        self.outputDelta     = self.outputError * self.sigmoidPrime(output)
        
        self.z2Error    = self.outputDelta.dot(self.weight2.T)
        self.z2Delta    = self.z2Error * self.sigmoidPrime(self.z2)
        
        self.weight1    += inputData.T.dot(self.z2Delta)
        self.weight2    += self.z2.T.dot(self.outputDelta)
        
    def sigmoid(self, x):
        #   Sigmoid transfer function
        transferFunction = 1/(1+np.exp(-x))
        return transferFunction
    
    def sigmoidPrime(self, x):
        #   First derivative of sigmoid function
        sigmoidPrime = x*(1-x)
        return sigmoidPrime
    
    def train(self, inputSize, trainData, iterations):
        for j in range(iterations):
            output = self.forward(inputSize)
            self.backward(inputData, trainData, output)

if __name__ == "__main__":
    
    inputDataFile = "input.csv"
    trainDataFile = "train.csv"
    
    inputData = np.genfromtxt(inputDataFile, delimiter = ',')
    trainData = np.genfromtxt(trainDataFile, delimiter = ',')
    trainData = np.transpose([trainData])
    
    #   Create neural network with above data
    nn = neuralNet()
    
    #   Number of iterations over which to train network
    iMax = 1000
    
    nn.train(inputData, trainData, iMax)
    
    print("Input: \n", inputData)
    print("Actual Output: \n", trainData)
    print("Predicted Output: \n", nn.forward(inputData))
    print("Loss: ", np.mean(np.square(trainData - nn.forward(inputData))))
    print()
