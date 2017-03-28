#!/bin/python
 
#Copyleft Arvind Ravichandran
#Mon Mar 27 10:34:43 CEST 2017
#main.py
#Description: main file for Simple and Biased Random Walks
 
import numpy as np
from modules import MSD, PlotRandomWalk2D
import matplotlib.pyplot as plt

def task2():
    """ Task 2: Biassed Random Walk """

    # (1A): MSD of 2D Random Walk
    #MSD(N=10000, d=2, p=0.55)

    # (1B): Plot biased 2D Random Walk 
    #PlotRandomWalk2D(N=10000,p=0.55) 

    # (1C): Compute MSD of biassed 2-D random walk 

    # try p=0.55
    #MSD(N=10000, d=2, p=0.55)

    # try p=0.60
    #MSD(N=10000, d=2, p=0.60)

    # try p=0.90
    #MSD(N=10000, d=2, p=0.90)

    plt.show()


if __name__=="__main__":
    task2()
