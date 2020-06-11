package com.gmail.monishmedhavi;
import java.util.Random;

public class GameOfLife {

	private int[][] initial;
	public int pop1,pop2;
	private int[][] arr;
	private int[][] newarr;
	private boolean tmp = true;
	public GameOfLife() {
		// TODO Auto-generated constructor stub
		arr = new int[10][10];
		createPopulation();
		pop1 = totalPop(arr);
	}
	
	public GameOfLife(int[][] population) {
		// TODO Auto-generated constructor stub
		arr = population;
		mutate();
		pop1 = totalPop(arr);
		initial = arr;
//		System.out.println("New pop arr");
//		population();
	}
	
	private void createPopulation() {
		Random rand = new Random();
		for(int i=0;i<10;i++) 
			for(int j=0;j<10;j++)
				if (rand.nextFloat()<0.2)
					arr[i][j] = 1;
			
		initial = arr;
	}
	
	
	public boolean createNewGen() {
		if(tmp) {
			newarr = new int[10][10];
			survives();
			newborn();
			tmp = differs();
			pop2 = totalPop(newarr);
			arr = newarr;
//			System.out.println("the new");
		}
		if(!tmp) {
//			System.out.println("the end");
		}
		return tmp;
	}
	
	
	private void survives() {
		for(int i=0;i<10;i++) 
			for(int j=0;j<10;j++) {
				if(arr[i][j] == 1)
					if ((around(i, j)-1)>=2) {
						newarr[i][j] = 1;
					}
			}		
	}
	
	private void newborn() {
		for(int i=0;i<10;i++) 
			for(int j=0;j<10;j++) {
				if(arr[i][j] == 0)
					if (around(i, j)==3) {
//						System.out.print(" "+i+"  "+j);
						newarr[i][j] = 1;
					}
			}		
	}
	
	
	
	public int around(int i, int j) {
		int startx,starty,endx,endy,temp;
		int surround = 0;
		if (i-1<0)
			startx = 0;
		else
			startx = i-1;
		if (j-1<0)
			starty = 0;
		else
			starty = j-1;
		if (i+1>9)
			endx = 9;
		else
			endx = i+1;
		if (j+1>9)
			endy = 9;
		else
			endy = j+1;
//		System.out.println("box"+i+" "+j +" "+startx+" "+starty+" "+endx+" "+endy);
		for(;startx<=endx;startx++) {
			for(temp = starty;starty<=endy;starty++) {
				if(arr[startx][starty]==1) 
					surround++;
			}
			starty = temp;
		}		
		return surround;
	}
	
	public void population() {
		for(int i=0;i<10;i++) {
			for(int j=0;j<10;j++)
				System.out.print(arr[i][j]+" ");
			System.out.println();			
		}
	}
	public int[][] getPopulation() {
		return arr;
	}

	public int[][] getStartingPopulation() {
		return initial;
	}
	
	public void initPopulation() {
		System.out.println("{");
		for(int i=0;i<10;i++) {
			System.out.print("{");
			for(int j=0;j<10;j++) {
				System.out.print(initial[i][j]+"");
				if(j<9)
					System.out.print(",");
			}
			System.out.print("}\n");
		}
		System.out.println("}");
	}
	
	public boolean differs() {
		for(int i=0;i<10;i++) 
			for(int j=0;j<10;j++)
				if(arr[i][j] != newarr[i][j])
					return true;
		return false;
	}
	
	public double fitness() {
		double fit;
		int count =0;
		int started =0;
		for(int i=0;i<10;i++) 
			for(int j=0;j<10;j++)
				if(arr[i][j] == 1)
					count++;
		for(int i=0;i<10;i++) 
			for(int j=0;j<10;j++)
				if(initial[i][j] == 1)
					started++;
		try{
			fit = Math.pow(2, count/started);
		}catch (Exception e) {
			// TODO: handle exception
			return 0;
		}
//		System.out.println(started+"   "+ count +"  "+fit);
		return fit;
	}
	public void mutate() {
		Random rand = new Random();
		for(int i=0;i<10;i++) 
			for(int j=0;j<10;j++)
				if(rand.nextFloat()<0.01) {
					arr[i][j] = rand.nextInt(2) ;
				}		
	}
	
	public int totalPop(int[][] tmp) {
		int c=0;
		for(int i=0;i<10;i++) 
			for(int j=0;j<10;j++)
				if(tmp[i][j] == 1) {
					c++;
				}
		return c;
	}

}
