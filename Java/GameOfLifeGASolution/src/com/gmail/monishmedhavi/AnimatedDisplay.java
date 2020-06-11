package com.gmail.monishmedhavi;
import java.awt.*;

import javax.swing.JComponent;

public class AnimatedDisplay extends JComponent{
	/**
	 * 
	 */
	private static final long serialVersionUID = 1L;
	/**
	 * 
	 */
	private GOLPopulation gol;
	public AnimatedDisplay() {
		// TODO Auto-generated constructor stub
		gol = new GOLPopulation();
	}
	
	public boolean  lol() {		
		gol.newGen();
		boolean tmp = gol.cross;
		repaint();
		return tmp;
	}
	
	public void createNewGen(int show) {
		gol.crossover(show);
//		gol.printAll();
	}
	
	public void printData(int show) {
		gol.printFit(show);
//		gol.printAll();
	}
	
	public void paintComponent(Graphics g){
		super.paintComponent(g);
		Graphics2D g2d = (Graphics2D) g;
		int x=10,y=10;
		g2d.translate(x, y);
		x = 100;
		y = 100;
		for(int pop=0; pop<gol.population_size;pop++) {
			int[][] arr=gol.gols[pop].getPopulation();	
			int box = 8;
			for(int i =0;i<10;i++) {
				for(int j=0;j<10;j++) {
					Rectangle rect = new Rectangle(i*box, j*box, box, box);
					g2d.setColor(Color.red); 
					if (arr[i][j]==1)
						g2d.fillRect(i*box, j*box, box, box);
					g2d.setColor(Color.blue); 
					g2d.draw(rect);
				}
			}
			g2d.translate(x, 0);
			if(pop%12 == 11)
				g2d.translate(-x*12, y);
		}
	}
}
