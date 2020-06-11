package com.gmail.monishmedhavi;

import java.util.Random;

public class ApplyGA {

	private double[] fitnessVal;
	private double[] probability;
	private double[] cumulative;
	private double mutation, totalFitness;
	private GeneticAlgorithm[] population;
	Random rand ;
	
	public ApplyGA(GeneticAlgorithm[] population , double mutation) {
		// TODO Auto-generated constructor stub
		this.population = population;
		this.mutation = -1; 
		rand = new Random();
		fitnessVal = new double[population.length];
		probability = new double[population.length];
		cumulative = new double[population.length];
		this.mutation= mutation; 
	}
	
	
	
	public void popFitness() {
		// Calculate fitness of all population
		totalFitness = 0;
		for(int i=0 ; i<population.length;i++) {
			fitnessVal[i] = population[i].fitness();
			System.out.print(fitnessVal[i]+" ");
			totalFitness += fitnessVal[i];
		}
		System.out.println();
	}
	
	public void popProbability() {
		// Calculate probability
		for(int i=0 ; i<population.length;i++) {
			probability[i] = fitnessVal[i]/totalFitness;
			System.out.print(probability[i]+" ");
		}
		System.out.println();
	}

	public void cumulativeProb() {
		// Calculate Cumulative probability
		double tmp = 0;
		for(int i=0 ; i<population.length;i++) {
			tmp += probability[i];
			cumulative[i] = tmp;
			System.out.print(tmp+" ");
		}
		System.out.println();
	}
	
	public GeneticAlgorithm[] newGen() {
		popFitness();
		popProbability();
		cumulativeProb();
		GeneticAlgorithm[] tempaArr = new GeneticAlgorithm[population.length];
		for(int i=0 ; i<population.length;i++) {
			GeneticAlgorithm parent1 = randomSelect();
			GeneticAlgorithm parent2 = randomSelect();
			tempaArr[i] = parent1.reproduce(parent2);
			tempaArr[i] = tempaArr[i].mutate(mutation);
		}
		return tempaArr;
	}
	
	public GeneticAlgorithm randomSelect() {
		double select = rand.nextDouble();
		for(int i=0 ; i<population.length;i++) {
			if(cumulative[i]>=select) {
				return population[i];				
			}
		}

		return population[rand.nextInt(population.length)];
	}
	
}
