#!/bin/python
 
#Copyleft Arvind Ravichandran
#Fri Mar 24 23:14:32 CET 2017
#constants.py
#Description: All constants for the simulation must be written down here

import numpy as np

# General Simulation Parameters
steps = int(1e7)                    # length of simulation
ensemble = 1                       # size of ensemble

# System Parameters
dt    = 0.1                         # size of time step
kB    = 1.0                         # Boltzmann constant
xi    = 18.849                      # Drag coeff
T1    = 1.0                         # Temperature of bead 1
T2    = 1.0                         # Temperature of bead 2
k     = 1.0                         # Spring constant
nstd1 = np.sqrt(2.*xi*kB*T1*dt)     # standard deviation of noise for bead 1
nstd2 = np.sqrt(2.*xi*kB*T2*dt)     # standard deviation of noise bead 2
x1,x2 = 0, 0                        # initial position of bead 1 & 2

# Probability Flux Analysis Parameters
binnum = 15                         # number of bins for PFA
