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
from loops import integrate_loop

def main():

    flux_total=[]
    fig, ax = plt.subplots()

    # For each member in ensemble
    for i in range(sim.ensemble):
        # Setup generates empty (x1t, x2t), 
        # noise arrays (noise1, noise2), 
        # initial positions (x1=0,x2=0);
        x1t, x2t, x1, x2, noise1, noise2 = misc.setup()

        # Brownian motion integration loop
        x1t, x2t = integrate_loop(x1t, x2t, x1, x2, sim.steps, sim.dt, sim.k, sim.xi, noise1, noise2)

        # Calculate the probability flux
        ax, flux, xbins, ybins = misc.pfa(fig, ax, x1t,x2t)

        # append it to a list of fluxes
        flux_total.append(flux)

    # compute the average flux per cell 
    flux_average = np.zeros(flux.shape)         # initialise array
   
    for f in flux_total:                        # sum all elements in the list
        flux_average += f
    flux_average = flux_average/sim.ensemble    # compute the average

    # plotting
    #misc.hist2D( x1t, x2t, xbins, ybins)
    #misc.flux_arrows(ax,flux_average,misc.center(xbins),misc.center(ybins))

if __name__ == "__main__":
    main();

