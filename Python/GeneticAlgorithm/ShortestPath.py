# -*- coding: utf-8 -*-

import queue
from GeneticAlgorithm import GeneticAlgorithm
import random
import numpy as np

class ShortestPath(GeneticAlgorithm):
    def __init__(self, nodes , edges=[]):
        self.edges = edges
        self.nodes = nodes
        if self.edges == []:
            self.edges = np.zeros((len(nodes),len(nodes)))
            for i in range(self.edges.shape[0]):
                for j in range(i+1, self.edges.shape[1]):
                    self.edges[i][j] = self.edges[j][i] = random.choice([0,1])
        
        
    def distance(self):
        n = len(self.nodes)
        dist = 0
        for i in range(n):
            for j in range(i+1,n):
                if(self.edges[i][j] == 1):
                    x1 = self.nodes[i][0]
                    y1 = self.nodes[i][1]
                    x2 = self.nodes[j][0]
                    y2 = self.nodes[j][1]
                    d = ((x1-x2)**2 + (y1-y2)**2)**0.5
                    dist += d
        return dist

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



    def forTwo(self):
        n = len(self.nodes)
        c = 0
        for i in range(n):
            istwo = 0
            for j in range(i+1,n):
                if(self.edges[i][j] == 1):
                    istwo += 1 
            if istwo <= 2:
                c+=1
        return c
        
    def fitness(self):
        self.fitnessVal = 0
        self.dist = self.distance()
        ngrp = self.BFS(self.edges)
        c = self.totalEdges()
        n = len(self.nodes)
        twos = self.forTwo()
        
        
        self.fitnessVal = 0 
#        print(self.edges, ngrp)
#        self.fitnessVal = 2 ** twos
        self.fitnessVal += 2**((n-1)/( (abs(c-n-0.2))))
        self.fitnessVal += 2**(1/(1+self.dist))
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
        tempObj = ShortestPath(self.nodes , edges=new_edges)
        return tempObj

    def mutate(self, rate):
        n = len(self.nodes)
        for i in range(n):
            for j in range(i+1,n):
                value = np.random.rand()
                if value <= rate:
                    self.edges[i][j] = self.edges[j][i] = (self.edges[j][i] + 1) % 2

