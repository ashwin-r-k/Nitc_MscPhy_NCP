#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 10 13:27:30 2022

Purpose : To find the root of the given function using th bisection method.     
@author: Ashwin
Roll no : M220590PH
"""
 
#importing the needed packages
import numpy as np
from matplotlib import pyplot as plt

#Defining the Function which we want to find root for.
def fn(x):
    y=2*np.sin(x)+3*np.e**(-x)+4*x**3-4
    return y

#defining the bisection method
def bisection(a,b,esp):
    
    #for counting the number of times we run loop
    itter=0
    
    while abs(a-b)>=esp:
        m=(a+b)/2
        #incresing the value of counter as we run the loop
        itter=itter+1
        
        #first we asume that m is on the sie of b if this is tru then 
        #we replace b with m and if our assumption is false we replace m with a.
        if fn(a)*fn(m)<0:
            b=m
        else:
            a=m
            
    return m,itter
    #return gives back the value to the place where thefunction was called.
    
#defining the range and values
a=-1
b=2
esp=0.0001

#ploting the given function
#here 1000 is number of points to take in between a and b
x=np.linspace(a,b,1000)
plt.plot(x,fn(x))

#ploting the axis.
plt.axhline(color="red")
plt.axvline(color="red")


# solving the bisection method
root,itter=bisection(a,b,esp)

print("The root of given function is =",root)
print("Number of iteration is = ",itter)