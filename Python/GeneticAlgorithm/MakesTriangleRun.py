# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 22:14:44 2019

@author: Medhavi
"""

import MakesTriangle
import ApplyGA
from tkinter import *
import numpy as np
import time



#------------- Define Class --------------------

class SimulationOfPath:

    def __init__(self, root):        
#------------- Dividing window in node Creating Area and Simulation Area -------------
        self.root = root
        self.creation = Frame(self.root)
        self.creation.pack(expand=True, fill=BOTH, side=LEFT)
        self.M = 2
        self.N = 500
        self.C = 30
        h = w = 40
        self.nodes = []

#--------------Click on this to create nodes at different locations-----------------
        self.creating_area = Canvas(self.creation, bd=4, bg="white", width=w*self.M, height=h*self.M, relief=RAISED)
        self.creating_area.grid()
        self.creating_area.bind("<Button-1>", self.click)

#---------Button to start all----------------------
        self.start_sim = Button(self.creation, text="Start", fg="black", width=20)
        self.start_sim.bind("<ButtonPress-1>",self.start)
        self.start_sim.grid()
#--------To show best-----------------------
        self.best = Canvas(self.creation, bd=4, bg="white", width=w*self.M, height=h*self.M, relief=RAISED)
        self.best.grid()
        
        self.value = Button(self.creation, text="Edges ", fg="black", width=20)
        self.value.grid()

#--------------This will show simulations------------------------
        self.population = Frame(root)
        self.population.pack(expand=FALSE, fill=BOTH, side=RIGHT)

#-------------These show individual population-----------------        
        c = 0
        r = 0
        self.sims = [None for i in range(self.N)]
        for i in range(self.N):
            self.sims[i] = Canvas(self.population, bd=4, bg="white", width=w, height=h, relief=RAISED)
            if(c == self.C):
                c = 0
                r += 1
            c += 1 
            self.sims[i].grid(column = c , row = r)


#-------------- Catch Mouse Click-------------------
    def click(self, event=None):
        self.nodes.append([event.x, event.y])
        self.drawNode(self.creating_area,[[event.x, event.y]])
        
    def drawNode(self, canvas , nodes):
        s = 3
        for i in range(len(nodes)):
            canvas.create_oval(nodes[i][0]-s, nodes[i][1] -s ,nodes[i][0] +s, nodes[i][1] +s)

    def drawEdge(self, canvas , nodes , edges):
        n = len(nodes)
        canvas.delete("all")
        self.drawNode(canvas, nodes)
        for i in range(n):
            for j in range(i+1,n):
                if(edges[i][j] == 1):
                    canvas.create_line(nodes[i][0] , nodes[i][1] , nodes[j][0] , nodes[j][1], smooth=True)

    def start(self, event):
        POPULATION_SIZE = self.N
        generation = 1
        population = [None for i in range(POPULATION_SIZE)]
        nodes = np.array(self.nodes)#[[0,0],[12,0],[12,5]])
        nodes = nodes / self.M
        print(nodes)
        for i in range(POPULATION_SIZE):
            population[i] = MakesTriangle.MakeTriangle(nodes)

        for i in range(1000):        
            
            prev = population

            create = ApplyGA.ApplyGa(population,mutation=0.2,percentile=0.1 )
            population = create.newGen()

            tempf = create.fitnessVal.copy()
            tempSorted = list(zip(tempf, prev))
            first = lambda val : val[0]
            tempSorted.sort(key = first , reverse = True)
            print("GEN",generation,tempSorted[0][0],tempSorted[0][1].edge_count)

            for j in range(POPULATION_SIZE):
                self.drawEdge(self.sims[j] ,nodes, tempSorted[j][1].edges)            
#                print("AS",tempSorted[j][1].edges,tempSorted[j][0])
            showNode = nodes.copy()
            showNode = showNode * self.M
            self.drawNode(self.best, showNode)            
            self.drawEdge(self.best, showNode , tempSorted[0][1].edges)
            self.value.config(text="E "+str(tempSorted[0][1].edge_count)+" T "+ str(tempSorted[0][1].count_triangle ))
            self.root.update()
            time.sleep(0.1)
            generation += 1
	



root = Tk()
paint_app = SimulationOfPath(root)
root.mainloop()




