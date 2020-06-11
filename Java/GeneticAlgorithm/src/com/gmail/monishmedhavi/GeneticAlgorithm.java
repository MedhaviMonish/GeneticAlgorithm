package com.gmail.monishmedhavi;

public interface GeneticAlgorithm {
	double fitness();
	GeneticAlgorithm reproduce(GeneticAlgorithm obj);
	GeneticAlgorithm mutate(double mutationRate);

}
