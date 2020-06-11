package com.gmail.monishmedhavi;

public class RunLib {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int N = 50;
		ForSentence[] arr = new ForSentence[N];
		GeneticAlgorithm[] tmp = new GeneticAlgorithm[N];
		for(int i=0 ; i<N ; i++) {
			arr[i] = new ForSentence();
			tmp[i] = arr[i];
			System.out.print(arr[i].individual+" ");
		}		
		System.out.println();
		for(int i =0 ; i <1000;i++) {
			ApplyGA obj = new ApplyGA(tmp,0.01);
			tmp = obj.newGen();
			for(int j =0 ; j<arr.length; j++) {
				ForSentence temp = (ForSentence) tmp[j];
				System.out.print(temp.individual+" ");
				if(temp.individual.equals(ForSentence.target)) {
					System.out.println();
					System.out.println("Gen "+ i+ "  "+ j);
					return;
				}
			}
			System.out.println();
		}		
	}
}
