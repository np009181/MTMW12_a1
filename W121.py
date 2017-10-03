# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np 
#Assignment 1, Question 1#
N=int(1e7)
a=0
for i in range(N):
    a+=0.01

print(a)

#10e4 works, however 10e7 does not give the right answer as the mantissa#
#\is not long enough#

