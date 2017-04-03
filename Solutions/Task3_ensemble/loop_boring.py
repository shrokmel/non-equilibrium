#!/bin/python
 
#Copyleft Arvind Ravichandran
#Sun Mar 26 21:20:20 CEST 2017
#loop.py
#Description:

import numpy as np

def integration_loop(x1t, x2t, x1, x2, steps, dt, k, xi, noise1, noise2):
    for ti in xrange(steps):
        x1 += dt*(k*(x2-2*x1) + noise1[ti])/xi
        x2 += dt*(k*(x1-2*x2) + noise2[ti])/xi

        x1t[ti] = x1
        x2t[ti] = x2
    return x1t, x2t

def flux_loop(flux,digg,diff,steps):
    for ti in range(steps-1):
        i = digg[ti,0]; 
        j = digg[ti,1];
        d1= diff[ti,0];
        d2= diff[ti,1]; 
        # up
        if d1==1 and d2==0:
            flux[i  , j, 0]+=1;
            flux[i+1, j, 0]+=1;

	# down
        elif d1==-1 and d2==0:
            flux[i  , j, 0]-=1;
            flux[i-1, j, 0]-=1;

        # right
        elif d1==0 and d2==1:
            flux[i, j, 1]  +=1;
            flux[i, j+1, 1]+=1;

        # left
        elif d1==0 and d2==-1:
            flux[i, j, 1]  -=1;
            flux[i, j-1, 1]-=1;

    return flux
