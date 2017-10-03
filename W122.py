# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 14:58:33 2017

@author: np009181
"""
#Question 2#

def intef(f, a, b, n):
    #integrate function f by Gaussian quadrature#
    #here n is the number of intervals#
#Define function f#
    f = 3*x - 2
#Set integration limits and number of integrals#
a = 0
b = 10
n = 3
#Calculate the integral length#
dx = (b-a)/n
#Initialise the integral#
I = 0.0

for i in xrange(0,n): #use this to find the sum up to n#
    
    I += (a + (i+0.5)*dx)
    
I* = dx
return I
