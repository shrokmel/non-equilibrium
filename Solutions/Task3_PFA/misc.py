#!/bin/python
 
#Copyleft Arvind Ravichandran
#Sat Mar 25 00:41:41 CET 2017
#misc.py
#Description: Contains miscellaneous and modular functions for Task 3

import matplotlib as mpl
#mpl.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import constants as sim
from itertools import izip

# Returns the center of bins
def center(arr):
    return (arr[:-1]+arr[1:])/2.

def hist2D(x1t, x2t):
    counts, xbins, ybinx, image = plt.hist2d(x1t,x2t,bins=15)
    plt.axes().set_aspect('equal', 'datalim')
    plt.show()

def flux_arrows(ax, flux, xc, yc):
    
    # Get center of cells in grid
    X,Y = np.meshgrid(xc,yc)

    # normalise flux with total flux in either direction
    flux_norm = np.divide(flux,np.abs(flux).sum(axis=(0,1)),dtype=float)*2.0
    #flux_norm = flux

    ax.quiver( X, Y, flux_norm[:,:,1], flux_norm[:,:,0], scale=1, scale_units="inches", linewidths=(0.5,), headaxislength=5)

    #plt.axes().set_aspect('equal', 'datalim')
    plt.axis("equal")
    plt.xlim([-0.3,0.3])
    plt.ylim([-0.3,0.3])
    plt.show()

def determine_case(d1,d2):
    if d1==1 and d2==0:
        return 'up'
    elif d1==-1 and d2==0:
        return 'down'
    elif d1==0 and d2==1:
        return 'right'
    elif d1==0 and d2==-1:
        return 'left'

# Probability Flux Analysis
def pfa(fig,ax, x1t, x2t):

    binnum= sim.binnum
    xbins = ybins = np.linspace(-0.5,0.5,binnum+1)
    
    # Discritize (x1,x2) positions into 2D bins
    # First index refers to x1t (xbins)
    counts, xbins, ybins, image = ax.hist2d(x1t,x2t,bins=[xbins,ybins])

    plt.hist2d(x1t,x2t,bins=[xbins,ybins],cmap=mpl.cm.jet)
    plt.colorbar()

    # initialize fluxes
    flux = np.zeros((counts.shape[0],counts.shape[1],2))
    fluxt = np.zeros((counts.shape[0],counts.shape[1],2))

    # digitize positions in phase space (0=<digg<15)
    # -1 to convert to array indices as per counts
    x1dig = np.digitize(x1t, xbins[:-1])-1
    x2dig = np.digitize(x2t, ybins[:-1])-1

    digg = np.vstack((x1dig,x2dig)).T

    # calculate flux (last time step has no flux)
    diff = np.diff(digg,axis=0)

    # This is just a fancy loop over all the time steps
    for (i,j),(d1,d2) in izip(digg[:-1],diff):

        # up
        if d1==1 and d2==0:
            flux[ i  , j, 0]+=1;
            flux[ i+1, j, 0]+=1;

        # down
        elif d1==-1 and d2==0:
            flux[ i  , j, 0]-=1;
            flux[ i-1, j, 0]-=1;

        # right
        elif d1==0 and d2==1:
            flux[ i, j, 1]  +=1;
            flux[ i, j+1, 1]+=1;

        # left
        elif d1==0 and d2==-1:
            flux[ i, j, 1]  -=1;
            flux[ i, j-1, 1]-=1;

    # plot the flux arrows appropriately
    #flux_arrows(ax,flux,center(xbins),center(ybins))

    return ax, flux, center(xbins), center(ybins)

def plot_traj(x1t, x2t):
    plt.plot(x1t)
    plt.plot(x2t)
    plt.show()
