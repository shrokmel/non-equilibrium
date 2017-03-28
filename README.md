# non-equilibrium

README file for Random walks and probability flux in non-equilibrium systems prepared for Spring School 2017 

Author
------
  Arvind Ravichandran

Contact
-------
  a.ravichandran@fz-juelich.de

Affiliation
-----------
  Graduate Student in Theoretical Soft Matter and Biophysics
  Institute of Complex Systems and Institute for Advanced Simulation, 
  Forschungszentrum Juelich, Germany

What is it?
-----------
  
  This contains Python scripts to simulate illustrate concepts of non-equilibrium
  for the Spring School 2017 course at ICS II. In this course, conducted as
  a workshop, there are three instances of equilibrium and non-equilibrium 
  systems. 
  
Tasks
-----
  - Task 1 (Unbiased Random Walk):
    Simulation and analysis of an unbiased random walk using numpy.random.uniform 
    (step length is varied between -0.5 and 0.5)  
    Parts of the code are adapted from:
    http://pages.physics.cornell.edu/~sethna/StatMech/ComputerExercises/PythonSoftware/RandomWalk.py
    
  - Task 2 (Biased Random Walk):
    Simulation and analysis of a biased random walk using numpy.random.choice (uniform step length).
		A neat pythonic implementation of Mean Squared Displacement (MSD), and an extemporary approach to
		compute its standard deviation is given here. 
  
  - Task 3 (PFA for Harmonic Oscillators):
    Probability flux analysis in a coarse grained phase space for a pair of connected harmonic oscillators
    coupled to independent temperature baths. The flux of energy, and the non-equilibrium signature is seen
		in the probability flux in phase space.
		The idea is based on the example from Battle et al.
		Science. 2016 Apr 29;352(6285):604-7. doi: 10.1126/science.aac8167.

  Directories
  -----------
  - Problems
		This contains the problems, with comments for students to complete to get the systems up and running.
  - Solutions
		Contains the solutions to the problems, with the completed code running. There are Cython optimizations,
		which students are not required to learn. They are implemented for quickly running an ensemble of coupled
		oscillators serially for Task 3. 
  - docs
		Contains the pdf document for the teaching of random walk, diffusion, non-equilibrium, 
		probability flux analysis, and an in-depth perspective on introductory Python.

This project was conducted under the guidance of my PhD advisors, Gerrit Vliegenthart, Thorsten Auth, and with helpful discussions with Ewan Henry. In case of questions, comments, please contact me (Arvind).

