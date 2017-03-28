#!/bin/python
 
#Copyleft Arvind Ravichandran
#Sat Mar 25 00:41:41 CET 2017
#misc.py
#Description:

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import constants as sim
import time

# Returns the center of bins
def center(arr):
    return (arr[:-1]+arr[1:])/2.

# 2D histogram
def hist2D(x1t, x2t):
    counts, xbins, ybinx, image = plt.hist2d(x1t,x2t,bins=15)
    plt.axes().set_aspect('equal', 'datalim')
    plt.show()

# Plots the flux arrows
def flux_arrows(ax, flux, xc, yc):
    
    # Get center of cells in grid
    X,Y = np.meshgrid(xc,yc)

    # normalise flux with total flux in either direction
    flux_norm = np.divide(flux,np.abs(flux).sum(axis=(0,1)),dtype=float)*2.0
    ax.quiver( X, Y, flux_norm[:,:,1], flux_norm[:,:,0], scale=1, scale_units="inches", linewidths=(0.5,), headaxislength=5)

    plt.axis("equal")
    plt.xlim([-0.3,0.3])
    plt.ylim([-0.3,0.3])
    plt.show()

# helper function for pfa
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

    # loop over all the time steps except last one
    for ti in range(steps-1):
        i,j = digg[ti]
        d1,d2 = diff[ti]

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

    return ax, flux, center(xbins), center(ybins)

# plot the trajectory
def PlotXvsT(x1t, x2t):
    f, axarr = plt.subplots(2, sharex=True)

    axarr[0].set_title('Trajectory of beads')
    axarr[0].plot(x1t,c='b')
    axarr[0].set_ylabel(r'$x_1$')

    axarr[1].plot(x2t,c='g')
    axarr[1].set_ylabel(r'$x_2$')
    axarr[1].set_xlabel('time')

def HistXi(x1t, x2t, bins=30):
    f, axarr = plt.subplots(2, sharex=True)
    axarr[0].set_title('Histogram of '+ r'$x_i$')
    axarr[0].hist(x1t,bins=bins,color='b',normed=True)
    axarr[0].set_ylabel(r'$P(x_1)$')

    axarr[1].hist(x2t,bins=bins,color='g',normed=True)
    axarr[1].set_ylabel(r'$P(x_2)$')
    axarr[1].set_xlabel(r'$x _{i}$')

    print "Mean of x1: ", np.mean(x1t)
    print "Mean of x2: ", np.mean(x2t)

    print "Standard Deviation of x1: ", np.std(x1t)
    print "Standard Deviation of x2: ", np.std(x2t)

def HistCOM(x1t, x2t, bins=30):
    f, ax = plt.subplots(1,1)
    ax.set_title('Histogram of '+ r'$x_{com}$')

    xmean = (x1t+x2t)/2
    ax.hist(xmean,bins=bins,color='b',normed=True)
    ax.set_ylabel(r'$P(x_{com})$')
    ax.set_xlabel(r'$x _{com}$')

    print "Mean of COM: ", np.mean(xmean)
    print "Standard Deviation of COM: ", np.std(xmean)
