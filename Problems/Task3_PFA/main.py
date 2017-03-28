#!/bin/python
 
#Copyleft Arvind Ravichandran
#Wed Mar 22 14:27:30 CET 2017
#main.py
#Description: Problem version of main for Task 3 (PFA)

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import constants as sim
import time
from modules import PlotXvsT, HistXi, HistCOM
from modules import pfa, flux_arrows

def main():
        
    flux_total=[]

    # For analysis
    x1t = np.zeros(sim.steps)
    x2t = np.zeros(sim.steps)
    
    # initialise positions of beads
    x1, x2 = 0., 0.

    # Get random number between 0 and 1
    noise1=np.random.normal(loc=0.,scale=sim.nstd1,size=sim.steps)
    noise2=np.random.normal(loc=0.,scale=sim.nstd2,size=sim.steps)

    # Time loop
    for ti in xrange(sim.steps):

        ######## Fill in the integration steps here ########

        x1+= ???
        x2+= ???

        ######## %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% ########

        x1t[ti]=x1
        x2t[ti]=x2

    ### Uncomment following lines for Task 3: 1(a-d) and 2(a,b) ###
    # Task 1(a, c)
    PlotXvsT(x1t,x2t)

    # Task 1(b, d)
    #HistXi(x1t,x2t)
    #HistCOM(x1t,x2t)

    # Task 2(a) and 2(b)
    #fig, ax = plt.subplots()
    #ax, flux, xc, yc = pfa(fig, ax, x1t,x2t)           # Perform PFA
    #flux_arrows(ax,flux,xc,yc)

    plt.show()

if __name__ == "__main__":
    main();

