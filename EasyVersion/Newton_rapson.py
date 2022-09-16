#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 10 14:06:20 2022

Purpose : To find the root of the given function using the Newton rapson method.     
@author: Ashwin
Roll no : M220590PH
"""

#importing the required definations
import numpy as np

#creating the defination for given function
def fn(x):
    y=2*np.sin(x)+3*np.e**(-x)+4*x**3-4
    return y

#This the the derivative of the given function
def fn_p(x):
    y=2*np.cos(x)-3*np.e**(-x)+12*x**2
    return y

#Defining the newton raphson method function
#taking only x0 and esp as input.
def newton_rapshon(x0,esp):
    itter=0
    #assuming thexip1 as x0
    xip1=x0
    xi=xip1+10*esp
    #just taking xi as a higher value
    
    #having while loop until needed accuracy is achived. 
    while abs(xip1-xi)>=esp:
        
        #this incress value of itter by 1 on each loop
        itter+=1
        
        xi=xip1
        xip1=xi-fn(xi)/fn_p(xi)
        #this above is the formula for newton raphson.
    return xip1,itter

#initial values
x0=0.5
esp=0.0001

#solving by calling newton raphson
root,itter=newton_rapshon(x0, esp)
print("Root is at ",root)
print("Number of iteration is = ",itter)

#Method 2 for finding nth root of givenn number
#dfining the newton rapshon method for finidng the value
def nr_bthroot(xi,a,b,esp):
    xip1=x0
    xi=xip1+10*esp
    #just taking xi as a higher value
    
    while abs(xip1-xi)>=esp:
        xi=xip1
        xip1=1/b*((b-1)*xi + a/pow(xi,b-1))
        #newtonrapshon formula
    return xip1

#initial values
a=12
b=3
x0=2.5
esp=0.0001

#solving by calling newton raphson bth root
root=nr_bthroot(x0, a, b, esp)
print("{0} th root of {1} is {2}".format(b,a,root))
    