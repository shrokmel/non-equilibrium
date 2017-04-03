#!/bin/python
 
#Copyleft Arvind Ravichandran
#Mon Mar 27 10:34:43 CEST 2017
#main.py
#Description: main file for Task 1: Simple Random Walk
 
import numpy as np
from modules import PlotRandomWalk1D, HistogramAllSteps, HistogramEndPoints
from modules import PlotRandomWalk2D, PlotEndPoints
import matplotlib.pyplot as plt

if __name__=="__main__":
    """ Task1: Simple Random Walk """

    # (1A): 1-D Random Walk X vs.t
    #PlotRandomWalk1D(10000)

    # (1B): Histogram the positions of single SRW
    #HistogramAllSteps(N=10000)

    # (2A): Edit the function called EndPoints

    # (2B): Histogram the end points of many SRW (What is sigma?)
    #HistogramEndPoints()

    # (3A): 2-D Random Walk X vs. Y
    #PlotRandomWalk2D(1000)

    # (3B): Spread of end points in 2D
    #PlotEndPoints()

    # (3C): Demonstration of Central Limit Theorem
    #HistogramEndPoints(N=1)
    #HistogramEndPoints(N=2)
    #HistogramEndPoints(N=10)

    plt.show()
