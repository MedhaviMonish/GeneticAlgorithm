package com.gmail.monishmedhavi;

import java.util.Random;

public class GOLPopulation {

	public GameOfLife[] gols;
	GameOfLife[] new_population;
	public int population_size;
	double[] prob;
	double[] fitness;
	double[] cummulative;
	int repeated=0;
	public boolean cross = false; 
	int gen =  1 ;
	public GOLPopulation() {
		// TODO Auto-generated constructor stub
		population_size  = 120;
		gols = new GameOfLife[population_size];
		new_population = new GameOfLife[population_size];
		prob = new double[population_size];
		fitness = new double[population_size];
		cummulative = new double[population_size];
		
		for(int i=0 ; i<population_size;i++) {
			gols[i] = new GameOfLife(); 
		}
	}
	public void newGen() {
		int c =0 ;
		for(int i=0 ; i<population_size;i++) {
			if(gols[i].createNewGen())
				c++;
		}
		if(c<=40 ) {
			repeated++;
		}
		if(repeated>=50 || c==0) {
			cross = true;
//			printAll();
			repeated=0;
		}
	}
	
	public void cummulative_probability() {
		double total = 0;		
		for(int i=0 ; i<population_size;i++) {
			fitness[i] = gols[i].fitness();
			total += fitness[i]; 			
		}		

		for(int i=0 ; i<population_size;i++) {
			prob[i] = fitness[i] / total;
		}
		
		total = 0;
		for(int i=0 ; i<population_size;i++) {
			total += prob[i];
			cummulative[i] = total;
		}
	}
	
	public void crossover(int show){
		cummulative_probability();
		printFit(show);
		Random rand = new Random();
		for(int i=0 ; i<population_size;i++) {
			GameOfLife p1 = selectParent();
			GameOfLife p2 = selectParent();
			if(p1 == null) {
				p1 = gols[Math.abs(rand.nextInt() % population_size)];
//				System.out.println("p1");
//				p1.population();
			}
			if(p2 == null) {
				p2 = gols[Math.abs(rand.nextInt() % population_size)];
//				System.out.println("p2");
//				p2.population();
			}
//			System.out.println(p1+"  "+p2);
			int[][] pop1 = p1.getStartingPopulation();
			int[][] pop2 = p2.getStartingPopulation();
//			System.out.println("p1 init");
//			p1.initPopulation();
//			System.out.println("p2 init");
//			p2.initPopulation();
			int[][] newpop = new int[10][10];
			for(int j=0;j<10;j++) 
				for(int k=0;k<10;k++)
					if(pop1[j][k] == 1 || pop2[j][k] == 1)
						if(rand.nextFloat()<0.5)
						newpop[j][k] = 1;				
			try {
			new_population[i] = new GameOfLife(newpop);
			}
			catch (Exception e) {
				// TODO: handle exception
				System.out.println("Error new pop");
				if(new_population[i]==null)
					System.out.println("Null");
				
			}
		}
		gen++;
		System.out.println("new gen "+gen);
		gols = new_population;
		cross = false;
	}

	public GameOfLife selectParent(){
		Random rand = new Random();
		double select  = rand.nextFloat();	
//		System.out.println(select);
		for(int i=0 ; i<population_size;i++) {
//			System.out.println(fitness[i]+" "+prob[i]+" "+cummulative[i]);
		}
		for(int i=0 ; i<population_size;i++) {
			if(cummulative[i]>=select) {
//				System.out.println("Parent ind "+i);
				return gols[i];
			}
		}
		return null;
	}	
	public void printAll() {
		for(int i=0 ; i<population_size;i++) {
			System.out.println("init "+i);
			System.out.println(gols[i].pop1+" "+gols[i].totalPop(gols[i].getPopulation()));
			System.out.println(fitness[i]+" "+prob[i]+" "+cummulative[i]);
			System.out.println();
/*			gols[i].initPopulation();
			System.out.println();
			gols[i].population();
	*/	}
	}
	
	public void printFit(int show) {
		int max = 0;
		for(int i=1 ; i<population_size;i++) {
			if(prob[max]<prob[i]) {
				max = i;
			}
		}
		int i = max;
		System.out.println("Index" +max);
		System.out.println(gols[i].pop1+" "+gols[i].pop2+" "+prob[i]);
		System.out.println(fitness[i]+" "+prob[i]+" "+cummulative[i]);
		if(show != 1)
			return;
		gols[max].initPopulation();
		System.out.println();
		gols[max].population();		
	}
}
