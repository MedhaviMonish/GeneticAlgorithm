# -*- coding: utf-8 -*-

from GeneticAlgorithm import GeneticAlgorithm
import random
import numpy as np

class Name(GeneticAlgorithm):
    def __init__(self, target , prediction=None):
        self.characters = "abcdefghijklmnopqrstuvwxyz "
        self.target = target
        self.prediction = prediction
        
        if self.prediction == None:
            self.prediction = ""
            for each in self.target:
                self.prediction += random.choice(self.characters)
        
    def fitness(self):
        self.fitness = 0
        for gs, gt in zip(self.prediction, self.target):
            if gs == gt: 
                self.fitness+= 1
        self.fitness = 2 ** self.fitness
        return self.fitness 

    def reproduce(self, obj):
        child = ""
        for gp1, gp2 in zip(self.prediction, obj.prediction):
            choice = random.choice([0,1])
            if choice ==  0:
                child += gp1 
            else:
                child += gp2
        tempObj = Name(self.target , prediction=child)
        return tempObj

    def mutate(self, rate):
        mutant = ""
        for i in range(len(self.prediction)):
            value = np.random.rand()
            if value <= rate:
                mutant += random.choice(self.characters)
            else:
                mutant += self.prediction[i]
        self.prediction = mutant
