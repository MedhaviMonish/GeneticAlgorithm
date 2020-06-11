# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 01:12:43 2019

@author: Medhavi
"""


class GeneticAlgorithm:

    
    def __init__(self):
        pass
    
    def fitness(self):
        raise NotImplementedError 

    def reproduce(self, obj):
        raise NotImplementedError 

    def mutate(self, rate):
        raise NotImplementedError 




