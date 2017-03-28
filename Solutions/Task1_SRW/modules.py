#!/bin/python
 
#Copyleft Arvind Ravichandran
#Thu Mar 23 12:29:58 CET 2017
#random.py
#Description:

import numpy as np
import matplotlib.pyplot as plt

def RandomWalk(N=100, d=2):
    """
    Use np.cumsum and np.random.uniform to generate
    a 2D random walk of length N.  You might want to generate an array of
    shape (N,d), using (for example), random.uniform(min, max, shape).
    """
    return np.cumsum(np.random.uniform(-0.5,0.5,(N,d)),axis=0)

def PlotRandomWalk1D(N=100):
    """
    Plot X(t) for one-dimensional random walk
    """

    X = RandomWalk(N,d=1)

    plt.plot(X)
    plt.title('1-D Random Walker Trajectory')
    plt.xlabel('steps')
    plt.ylabel('X (position)')

def PlotRandomWalk2D(N=1000):
    """
    Plot X,Y two-dimensional random walk
    """
    walk = RandomWalk(N,2)                  # conduct the walk

    plt.figure(figsize=(8,8))
    X, Y = walk.T

    plt.plot(X,Y)                           # plot the trajectory
    plt.scatter(X[0],Y[0],c='g',s=100)      # starting position
    plt.scatter(X[-1],Y[-1],c='r',s=100)    # ending position
    plt.axis('equal')

def EndPoints(W=10000, N=10, d=2):
    """
    Returns a list of endpoints of W random walks of step length N.
    One can generate the random walks and then peel off the final positions,
    or one can generate the steps and sum them directly, for example:
    sum(numpy.random.uniform(-0.5,0.5,(10,100,2))
    """

    return sum(np.random.uniform(-0.5,0.5,(N,W,d)))

def PlotEndPoints(W=10000, N=10, d=2):
    """
    Plot endpoints of random walks.
    """

    X, Y = np.transpose(EndPoints(W, N, d))
    plt.figure(figsize=(8,8))
    plt.scatter(X,Y,c='k',s=5)
    plt.axis('equal')

def plotGaussian(N, bins):
    '''
    Plots rho = (1/(sqrt(2 pi) sigma)) exp(-x**2/(2 sigma**2))
    for -3 sigma < x < 3 sigma 
    '''

    sigma = np.sqrt(N/12.)
    x = np.arange(-3*sigma,3*sigma,sigma/bins)
    rho = (1/(np.sqrt(2*np.pi)*sigma))*np.exp(-x**2/(2*sigma**2))
    plt.plot(x, rho, "k-")

def HistogramAllSteps(N=10, d=1, bins=50):
    """
    Histograms all positions explored by one random walker 
    """    
    X = RandomWalk(N,d)
    plt.hist(X, bins=bins, normed=1)
   
def HistogramEndPoints(W=10000, N=10, d=1, bins=50):
    """
    Compares the histogram of end points of random walks with the 
    Gaussian distribution predicted by the central limit theorem.

    (1) Plots a histogram P(X): the probability that a random walk
    of N steps has endpoint x-coordinate at position X.
    Uses plt.hist(X, bins=bins, normed=1) to produce the histogram
    #
    (2) Calculates the RMS stepsize sigma for a random walk of length N
    (with each step uniform in [-1/2,1/2]
    Plots rho = (1/(sqrt(2 pi) sigma)) exp(-x**2/(2 sigma**2))
    """

    X = EndPoints(W, N, d)

    plt.hist(X, bins=bins, normed=1)
    plotGaussian(N,bins)
