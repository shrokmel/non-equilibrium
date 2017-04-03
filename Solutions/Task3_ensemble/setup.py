#!/bin/python
 
#Copyleft Arvind Ravichandran
#Sun Mar 26 21:36:45 CEST 2017
#setup.py
#Description:
 
from distutils.core import setup
from Cython.Build import cythonize

setup(
    ext_modules=cythonize("loops.pyx"),
)
