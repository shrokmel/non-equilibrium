#!/bin/python
 
#Copyleft Arvind Ravichandran
#Sat Mar 25 00:41:41 CET 2017
#misc.py
#Description: Contains functions not defined in main

import matplotlib.pyplot as plt
import numpy as np
import constants as sim
from loops import flux_loop     # cython

def setup():
    # Arrays storing all positions
    x1t = np.zeros(sim.steps)
    x2t = np.zeros(sim.steps)

    # Initialise positions of beads
    x1, x2 = 0., 0.
  
    # Get gaussian distributed random number between 0 and 1
    noise1=np.random.normal(loc=0.,scale=sim.nstd1,size=sim.steps)
    noise2=np.random.normal(loc=0.,scale=sim.nstd2,size=sim.steps)

    return x1t,x2t,x1,x2,noise1,noise2

# Returns the center of bins
def center(arr):
    return (arr[:-1]+arr[1:])/2.

def hist2D(x1t, x2t, xbins, ybins):
    plt.hist2d(x1t,x2t,bins=[xbins,ybins])

def flux_arrows(ax, flux, xc, yc):
    
    # Get center of cells in grid
    X,Y = np.meshgrid(xc,yc)

    # normalise flux with total flux in either direction
    flux_norm = np.divide(flux,np.abs(flux).sum(axis=(0,1)),\
            dtype=float)*5.0
    #flux_norm = flux

    ax.quiver( X, Y, flux_norm[:,:,1], flux_norm[:,:,0], \
            scale=1, scale_units="inches", linewidths=(0.5,), \
            headaxislength=5)

    plt.axis("equal")
    plt.xlim([-0.3,0.3])
    plt.ylim([-0.3,0.3])
    plt.show()

# Probability Flux Analysis
def pfa(fig,ax, x1t, x2t):

    # Initialise bins for histogramming
    binnum= sim.binnum
    xbins = ybins = np.linspace(-0.5,0.5,binnum+1)
    
    # Discritize (x1,x2) positions into 2D bins
    # First index refers to x1t (xbins)
    counts, xbins, ybins  = np.histogram2d(x1t,x2t,bins=[xbins,ybins])

    # initialize fluxes
    flux  = np.zeros((counts.shape[0],counts.shape[1],2))

    # digitize positions in phase space (0=<digg<15)
    # -1 to convert to array indices as per counts
    x1dig = np.digitize(x1t, xbins[:-1])-1
    x2dig = np.digitize(x2t, ybins[:-1])-1
    digg = np.vstack((x1dig,x2dig)).T

    # calculate flux (last time step has no flux)
    diff = np.diff(digg,axis=0)

    # Determine which process goes which way
    flux = flux_loop(flux, digg, diff, sim.steps)   #cython wrapped

    return ax, flux, xbins, ybins

def plot_traj(x1t, x2t):
    plt.plot(x1t)
    plt.plot(x2t)
    plt.show()
