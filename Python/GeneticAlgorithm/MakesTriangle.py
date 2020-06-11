# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 21:53:51 2019

@author: Medhavi
"""

from GeneticAlgorithm import GeneticAlgorithm
import random
import numpy as np
import itertools
import queue

class MakeTriangle(GeneticAlgorithm):
    def __init__(self, nodes , edges=[]):
        self.edges = edges
        self.nodes = nodes
        if self.edges == []:
            self.edges = np.zeros((len(nodes),len(nodes)))
            for i in range(self.edges.shape[0]):
                for j in range(i+1, self.edges.shape[1]):
                    self.edges[i][j] = self.edges[j][i] = random.choice([0,1])
        
        
    def totalEdges(self):
        n = len(self.nodes)
        c = 0
        for i in range(n):
            for j in range(i+1,n):
               if(self.edges[i][j] == 1):
                   c += 1
        return c
                   
    def BFSUtil(self, u, visited, grp): 
        # Create a queue for BFS  
        q = queue.Queue() 
          
        # Mark the current node as visited 
        # and enqueue it  
        visited[u] = True
        grp.append(u)

        q.put(u)  
        # 'i' will be used to get all adjacent  
        # vertices 4 of a vertex list<int>::iterator i            
        while(not q.empty()):               
            # Dequeue a vertex from queue  
            # and print it  
            u = q.queue[0]

            q.get()  
          
            # Get all adjacent vertices of the  
            # dequeued vertex s. If an adjacent  
            # has not been visited, then mark  
            # it visited and enqueue it  
            for i in range(len(visited)): 
                if ((not visited[i]) and self.edges[u][i] == 1): 
                    visited[i] = True
                    q.put(i) 
      
        
    def BFS(self, adj): 
        visited = [False for i in range(len(adj))]
        grp = []
        for u in range(len(visited)): 
            if (visited[u] == False):  
                self.BFSUtil(u, visited, grp) 
        return len(grp)


    
    def tringles(self):
        node_ind = [i for i in range(len(self.nodes))]
        combos = itertools.combinations(node_ind, 3)
        combos = list(combos)
        count = 0
        
        for each in combos:
            if (self.edges[each[0]][each[1]] == 1 and self.edges[each[1]][each[2]] == 1 and self.edges[each[2]][each[0]] == 1):
                count += 1
        return [count, len(combos)]
        

    
    def fitness(self):
        self.fitnessVal = 0
        self.edge_count = self.totalEdges()
        n = len(self.nodes)
        ngrp = self.BFS(self.edges)


        c, n = self.tringles()
        self.count_triangle = c
        self.fitnessVal = 0 

        self.fitnessVal += (2**(n-c)) * self.edge_count
        
#        self.fitnessVal /= 2**ngrp

        return self.fitnessVal 


    def reproduce(self, obj):
        n = len(self.nodes)
        new_edges = np.zeros((n,n))
        for i in range(n):
            new_edges[i][i] = 0
            for j in range(i+1,n):
                choice = random.choice([0,1])
                if choice == 0 :
                    new_edges[i][j] = new_edges[j][i] = obj.edges[i][j]
                else :
                    new_edges[i][j] = new_edges[j][i] = self.edges[i][j]
        tempObj = MakeTriangle(self.nodes , edges=new_edges)
        return tempObj


    def mutate(self, rate):
        n = len(self.nodes)
        for i in range(n):
            for j in range(i+1,n):
                value = np.random.rand()
                if value <= rate:
                    self.edges[i][j] = self.edges[j][i] = (self.edges[j][i] + 1) % 2

