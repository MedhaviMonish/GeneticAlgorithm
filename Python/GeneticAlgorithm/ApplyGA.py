# -*- coding: utf-8 -*-



import numpy as np

class ApplyGa:
    
    def __init__(self, population, mutation=0 , percentile=0):
        self.fitnessVal   =  [None for i in range(len(population))]
        self.probability  =  [None for i in range(len(population))]
        self.cumulative   =  [None for i in range(len(population))]
        self.population   = population
        self.mutation  =  mutation
        self.preserve = percentile
        
    def mutate(self, rate):
        self.mutation = rate

    def preservePopulation(self, percentile):
        self.preserve = percentile

    def populationFitness(self):
		#Calculate fitness of all population
        self.totalFitness = 0
        for i in range(len(self.population)):
            self.fitnessVal[i] = self.population[i].fitness()
            self.totalFitness += self.fitnessVal[i]

    def populationProbability(self):
		#Calculate probability of all population
        for i in range(len(self.population)):
            self.probability[i] = self.fitnessVal[i]/self.totalFitness;



    def cumulativeProbabilty(self):
        temp = 0
        for i in range(len(self.population)):
            temp += self.probability[i]
            self.cumulative[i] = temp
        
    def newGen(self):
        self.populationFitness()
        self.populationProbability()
        self.cumulativeProbabilty()
        tempArr = [None for i in range(len(self.population))]
        newPop = int(len(self.population) * (1-self.preserve))
        for i in range(newPop):
            parent1 = self.randomSelect()
            parent2 = self.randomSelect()
            tempArr[i] = parent1.reproduce(parent2)
            tempArr[i].mutate(self.mutation)
        if self.preserve > 0:
            tempSorted = list(zip(self.fitnessVal, self.population))
            tempSorted.sort(key = lambda val : val[0] , reverse = True)
            for i in range(newPop,len(self.population)):
                tempArr[i] = tempSorted[i-newPop][1]
            
        return tempArr


    def randomSelect(self):
        randomValue = np.random.rand()
        for i in range(len(self.population)):
            if self.cumulative[i] >= randomValue:
                return self.population[i]
        return self.population[np.random.randint(len(self.population))]

