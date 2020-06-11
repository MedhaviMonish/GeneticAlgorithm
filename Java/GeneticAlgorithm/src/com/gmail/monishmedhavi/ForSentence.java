package com.gmail.monishmedhavi;

import java.util.Random;

public class ForSentence implements GeneticAlgorithm{

	static String target = "created this sentence";
	private String GENES = "abcdefghijklmnopqrstuvwxyz ";
	String individual; 
	public ForSentence() {
		// TODO Auto-generated constructor stub
		individual = "";
		Random rand = new Random();
		for(int i =0 ; i<target.length(); i++) {
			individual += GENES.charAt(rand.nextInt(GENES.length()));
		}
	}
	

	public ForSentence(String individual) {
		super();
		this.individual = individual;
	}


	@Override
	public double fitness() {
		// TODO Auto-generated method stub
		double tmp=0;
		for(int i =0 ; i<target.length(); i++) {
			if(target.charAt(i) == individual.charAt(i))
				tmp++;
		}
		return Math.pow(2,tmp);
	}

	@Override
	public GeneticAlgorithm reproduce(GeneticAlgorithm obj) {
		// TODO Auto-generated method stub		
		ForSentence ref = (ForSentence) obj;
		String cross="";
		Random rand = new Random();
		for(int i=0 ; i<target.length(); i++) {
			if(rand.nextBoolean()) {
				cross += individual.charAt(i);
			}
			else {
				cross += ref.individual.charAt(i);
			}
		}
		ForSentence tmp = new ForSentence(cross);

		return tmp;
	}

	@Override
	public GeneticAlgorithm mutate(double mutationRate) {
		// TODO Auto-generated method stub
		ForSentence tmp = new ForSentence();
		Random rand = new Random();
		String str="";
		for(int i=0 ; i<target.length(); i++) {
			if(rand.nextDouble()<=mutationRate)
				str += GENES.charAt(rand.nextInt(GENES.length()));
			else
				str += individual.charAt(i);
		}
		tmp.individual = str;
		return tmp;
	}
}
