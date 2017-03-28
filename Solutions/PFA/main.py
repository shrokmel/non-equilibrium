#!/bin/python
 
#Copyleft Arvind Ravichandran
#Wed Mar 22 14:27:30 CET 2017
#main.py
#Description:

import matplotlib as mpl
mpl.use('Agg')

import matplotlib.pyplot as plt
import numpy as np
import constants as sim
import time
import misc3 as misc

def main():

    flux_total=[]
    fig, ax = plt.subplots()
    for i in range(sim.ensemble):
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
            x1 += sim.dt*(sim.k*(x2-2*x1)+noise1[ti])/sim.xi
            x2 += sim.dt*(sim.k*(x1-2*x2)+noise2[ti])/sim.xi

            x1t[ti]=x1
            x2t[ti]=x2
        ax, flux, xc, yc = misc.pfa(fig, ax, x1t,x2t)
        flux_total.append(flux)

    flux_average = np.zeros(flux.shape)
    
    for f in flux_total:
        flux_average += f

    flux_average = flux_average/sim.ensemble
    #misc.flux_arrows(ax,flux_average,xc,yc)

if __name__ == "__main__":
    main();

