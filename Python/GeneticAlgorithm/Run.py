# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 10:59:08 2019

@author: Medhavi
"""
import Name
import ApplyGA
import ShortestPath
import itertools

def main():
    POPULATION_SIZE = 40
    generation = 1
    population = [None for i in range(POPULATION_SIZE)]
    for i in range(POPULATION_SIZE):
        population[i] = Name.Name("hello world")

    while True:        
        create = ApplyGA.ApplyGa(population,mutation=0.2)
        population = create.newGen()
        generation += 1
        for each in population:
            print(each.prediction)
            if "hello world" in each.prediction:
                print(generation)
                return
        print(generation)
	

if __name__ == '__main__': 
	pass#main() 



a = [1,2,3,4]
a = itertools.combinations(a,3)
a = list(a)
print(a)

3**(4/5)
3**(1/5)



