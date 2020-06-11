package com.gmail.monishmedhavi;

import javax.swing.JFrame;

public class AnimationScreen {

	public static void main(String[] args) {		// TODO Auto-generated method stub
		JFrame fs = new JFrame("Simulation");
		fs.setSize(900, 900);
		fs.setLocation(600, 100);
		fs.setVisible(true);
		AnimatedDisplay fw = new AnimatedDisplay();
		fs.add(fw);
		fs.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		int n = 50;
		for(int i=0; i<n ; i++) {
			while(!fw.lol()) {
				try {
					Thread.sleep(120);
				} catch (InterruptedException e) {
					// TODO Auto-generated catch block
					e.printStackTrace();
				}
			}
			fw.createNewGen(1);

		}
	}
}
